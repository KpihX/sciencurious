# 🌫️ Blur: From Scalar Scores to Spatial Fields

> 🧠 **Making blur inspectable** — why global scalar metrics fail to distinguish bokeh from motion, the dataset trap of CNNs, the mathematics of reblurring, and how modeling blur as a continuous vector field bridges the gap between deep learning and physics.
>
> 📅 Date: 2026-09-05
> 👤 Author: KpihX
> 📚 Code & Repo: [GitHub](https://github.com/KpihX/culling-presentation) · [GitLab](https://gitlab.com/kpihx/culling-presentation)

> 🔗 **Prequel:** [Eye Status: Geometry vs Deep Learning](eye-status.md)

---

## 📋 Table of Contents

1. [The Preoccupation: Is this picture sharp?](#-1-the-preoccupation-is-this-picture-sharp)
2. [II.A: The Classical Bank (Global Metrics)](#-2-iia-the-classical-bank-global-metrics)
3. [II.B & II.C: The Corpus Trap and The Learned Judge](#-3-iib--iic-the-corpus-trap-and-the-learned-judge)
4. [II.D: The Window-Based Approach (Physics)](#-4-iid-the-window-based-approach-physics)
5. [Diffusion & The Final Fields](#-5-diffusion--the-final-fields)
6. [References](#references)

---

## 🧩 1. The Preoccupation: Is this picture sharp? <span id="preoccupation"></span>

Unlike eye status, which has a discrete, nameable answer, blur does not. 

A photograph can have global motion blur (camera shake), global defocus (missed focus), local motion (subject moving), or bokeh (background defocus). A culling system must distinguish a ruined photo from artistic intent. 

---

## 📉 2. II.A: The Classical Bank (Global Metrics) <span id="classical"></span>

Everything starts with the log-luminance frame. Why log rather than color? Two hues of equal luminance return the same derivative, making the kernels blind to color by construction (color repeatedly failed in this project as a blur cue). Furthermore, the gradient of $ \log I $ is $ \frac{\nabla I}{I} $, which is invariant to exposure. A dark night scene should not be penalized simply for being dark.

![Classical Kernels](assets/blur_01_kernels.png)

1. **Laplacian Variance and Tenengrad:** Both metrics measure high-frequency energy. They fall from sharp to motion to defocus by a factor of about 25. They answer *"how much?"* perfectly.
2. **The Structure Tensor ($ T $):** The magnitude of a gradient says *how much*; the asymmetry between the $ G_x $ and $ G_y $ gradients says *which way*.

![Structure Tensor](assets/blur_03_tensor.png)

A gradient is a vector $ g = [G_x, G_y]^T $. To find the direction with the most gradient energy, we maximize the squared projection $ (g^T u)^2 $ over a unit vector $ u $. This leads directly to the eigenvalue problem for $ T $, the mean of $ g g^T $:

$$
T = \overline{g g^T} = \begin{bmatrix} \overline{G_x^2} & \overline{G_x G_y} \\ \overline{G_x G_y} & \overline{G_y^2} \end{bmatrix}
$$

The eigenvalues $ \lambda_1, \lambda_2 $ are not proxies for the directional energies; they *are* them.

3. **Coherence ($ \rho $):** The normalized difference of the two eigenvalues.

$$
\rho = \frac{(\lambda_1 - \lambda_2)^2}{(\lambda_1 + \lambda_2)^2}
$$

Coherence is 0 when the two directions carry the same energy — a disc, which is what a defocus and a sharp frame both look like. It is 1 when everything is in a single direction — a smear. This is the categorical axis, and no single ordering of "how blurred" can carry it.

Two magnitudes and one axis. The classical bank carries a real signal.

---

## 🏗️ 3. II.B & II.C: The Corpus Trap and The Learned Judge <span id="cnn"></span>

Since the classical bank carries a signal, the next obvious step is to feed it to a classifier. We define 5 classes: `sharp`, `global_motion`, `global_defocus`, `local_motion`, and `bokeh`.

But here lies the trap. We combined two datasets: **Kwentar** (which has the global states and neither local one) and **CUHK** (a blur-detection set with only local states). 

![Corpus Trap](assets/corpus.png)

Look at what the classifier sees: two disjoint blocks. `local_motion` means CUHK and `global_defocus` means Kwentar. The class and the archive are the exact same fact. A tower has a way of being right that has nothing at all to do with blur: it learns the sensor noise, color profile, and lens characteristics of the cameras used.

You cannot solve a dataset problem with an architecture. We had to aggressively audit and curate 8 different archives to ensure no single source dominated, with at least three sources per class.

### The CNN Classifier (Hybrid Lite)

![CNN Architecture](assets/blur_cnn.png)

We trained a network called `hybrid_lite`. The map tower is gone. The RGB tower is rebuilt for one input channel (the three color kernels averaged into one, taking a pre-trained color backbone to gray without throwing priors away). 

We also provided 6 classical scalars (Structure tensor coherence and Alpha-structure, computed on the whole frame, the subject, and the outside) as extra features. But the result was striking: every removal of extra features either kept the score or improved it. The classical maps, handed to a network as extra channels, bought nothing at all — the tower recovers whatever they carried from the gray frame by itself.

### The Fusion Judge

When predicting if a local blur ruins the shot (e.g., subject vs background), we use a salient-object mask (S3OD) to split the frame into **Subject** and **Outside**.

![Judges](assets/judges.png)

We use 3 probes: Laplacian Variance, Tenengrad, and the CNN Embedding gap. Each computes a normalized differential:

$$
\text{Score} = \frac{\text{Subject} - \text{Outside}}{|\text{Subject}| + |\text{Outside}| + \epsilon}
$$

The CNN probe alone is actually the *weakest* of the three (0.908 accuracy). But the weighted fusion of all three reaches 0.951. The fusion is not a hedge; it is the result. The three probes fail on different frames, and averaging them makes the judge usable.

![Blur Rule](assets/blur_rule.png)

Finally, we ship an abstention band $ \tau $. If the frame is too close to call, the module refuses to decide, passing the map to the photographer.

---

## 📐 4. II.D: The Window-Based Approach (Physics) <span id="window"></span>

Everything so far produced a global score. But blur is spatial. A network that outputs `local_motion` tells you what the picture is, but it doesn't tell you *where* the motion is or *why* it decided that.

![Why Windows?](assets/deep_why.png)

We need a map. We cut the image into overlapping windows. The side of a window is a fraction of the frame's short edge (e.g., 2% of a 24-megapixel file). Local vs. global is precisely a question about shares, so the measuring unit has to scale with the frame.

### The Undecidability Problem
A window looking at a flat white wall has no high-frequency energy. A system forced to predict a blur width per window would falsely call the wall "blurry". We must acknowledge **undecidability**: a window with no texture measures *nothing*, not *zero*. If a window carries less than 200 edge pixels, it is marked as EMPTY (the pink areas later). Calling a clear sky blurred is the first false positive of this entire problem.

### The Reblurring Math (Zhuo & Sim)
How do we measure the blur width $ \sigma $ of an edge without knowing the original sharp image? We follow Zhuo & Sim (2011): we blur the image *again* on purpose.

![Reblur Math](assets/deep_reblur.png)

Do not compare an edge to anything else in the image; compare it to itself after a blur you chose. 
Model the edge as a step, already spread by an unknown Gaussian of width $ \sigma $. Its derivative is a Gaussian of that same width. The peak of the gradient is the edge contrast $ A $ divided by $ \sigma $, times a constant.

We blur it ourselves with a Gaussian we choose ($ \sigma_r $). Two Gaussians compose **in quadrature**, so the new width is $ \sqrt{\sigma^2 + \sigma_r^2} $. 
Take the ratio $ R $ of the two peaks. The constant cancels, and crucially, **the contrast $ A $ cancels too**. We are left with a closed-form solution for the absolute width in pixels:

$$
\sigma = \frac{\sigma_r}{\sqrt{R^2 - 1}}
$$

We run this with needle-like anisotropic kernels in 4 directions. An isotropic probe cannot answer this: a motion trail only destroys gradients perpendicular to itself and leaves parallel ones untouched.

### The Local Structure Tensor
We adapt the Structure Tensor from Step II.A, but instead of an unweighted mean over the whole frame, we use a weighted mean over a window.

![Local Tensor](assets/deep_12_tensor.png)

A separable Gaussian weight is used instead of a flat box ($ \frac{1}{N} \sum $). A box would make each window a hard cell, causing neighboring windows to disagree by a step. The Gaussian tapers to the edge, so the field of angles is continuous from one window to the next.

### Before Diffusion: The Raw Windows

This is what the mechanisms produce before a single pixel has been interpolated. The glyphs are not a drawing of the measurement; they **are** the measurement. The 2x2 symmetric tensor is an ellipse, its axes the eigenvectors.

![Windows Before Diffusion](assets/windows_before.png)

Read the rows:
1. **The Schnauzer (Control):** Every window is sharp. Ellipses are small and round. Round matters as much as small: it means no preferred direction.
2. **The Wheelie (Panning shot):** The rider is sharp (small round dots), but the street is smeared horizontally (flat segments). One frame, two answers. A global median width would call this photograph sharp and say nothing about the half of it that is moving.
3. **The Vase (Bokeh):** The background is flat and out of focus. Look at how much of that map is pink. There is nothing to measure. A system forced to produce a verdict per window would call it blurred. This system says nothing, and saying nothing is the correct answer.

---

## 🌊 5. Diffusion & The Final Fields <span id="diffusion"></span>

The grid gives a sparse, reliable field, but we need a dense one. We must fill the pink gaps.

![Diffusion](assets/deep_diffusion.png)

The solve is not a step-by-step algorithm; it is a minimization. We minimize an energy functional with two terms:
- **The Data Term:** Pulls the field $ u $ toward the measurement wherever a window made one.
- **The Smoothness Term:** Asks two neighboring pixels to agree. The price of disagreeing is a weight $ w_{pq} $ guided by the original log-luminance frame. 

Think of it as an electrical circuit: inside a flat wall, the luminance guide barely changes, conductance is high, and the blur measurement propagates freely. Across a sharp contour, the guide jumps, conductance collapses, and the propagation stops. 

The result is a dense, continuous map of the focal plane, drawn directly over the image.

![Maps](assets/deep_17_maps.png)

### The Final Climb
What if we could detect bokeh versus a missed subject not by a hard threshold, but by the way the subject is integrated?

<video width="100%" controls>
  <source src="assets/a23_pair.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

*(Above: Left, a wheelie the camera followed. Right, a subject that missed focus. The climb keeps the level where $ S $ peaks, measuring the solidity of the structure rather than relying on a single arbitrary cut).*

The photographer looks at the screen, sees the ellipses, understands the machine's reasoning instantly, and clicks Keep or Reject. 
That is true **Assisted Culling**.
