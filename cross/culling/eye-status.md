# 👁️ Eye Status: Geometry vs Deep Learning

> 🧠 **Deconstructing the eye** — why geometric heuristics are fast but fragile, the derivation of the Eye Aspect Ratio (EAR), the necessity of a 6-class taxonomy, and how abstention saves the pipeline.
>
> 📅 Date: 2026-09-05
> 👤 Author: KpihX
> 📚 Code & Repo: [GitHub](https://github.com/KpihX/culling-presentation) · [GitLab](https://gitlab.com/kpihx/culling-presentation)

> 🔗 **Prequel:** [Assisted Culling: A Signal is Not a Verdict](culling.md)

---

## 📋 Table of Contents

1. [The Preoccupation: The Micro-Expression](#-1-the-preoccupation-the-micro-expression)
2. [The Geometric Approach: EAR and its Variants](#-2-the-geometric-approach-ear-and-its-variants)
3. [The Failure of the Scalar Threshold](#-3-the-failure-of-the-scalar-threshold)
4. [The Learned Approach: The 6-Class Taxonomy](#-4-the-learned-approach-the-6-class-taxonomy)
5. [The Squeeze: Crop Resolution & Training Regimes](#-5-the-squeeze-crop-resolution--training-regimes)
6. [Evaluation: The Confusion Cost](#-6-evaluation-the-confusion-cost)
7. [References](#references)

---

## 🧩 1. The Preoccupation: The Micro-Expression <span id="preoccupation"></span>

In portrait photography, a blink is the cheapest and most objective reason to discard a frame. An eye closed at the wrong moment ruins a shot. Therefore, tracking eye status is the highest-ROI filtering mechanism in an automated pipeline. 

<video width="100%" controls>
  <source src="assets/eye_closing.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

However, an eye is not a clean geometric shape. It is subjected to heavy makeup, reflections from glasses, extreme roll angles, and partial occlusions from hair or hands. A culling system must survive these without throwing away a great photo due to a bad read.

![Eye Pipeline](assets/02-eye-pipeline.png)

*(Above: The dual-branch architecture. Both branches rely on the same upstream face detection and landmarking. A failure in the landmarks cascades through both branches).*

---

## 📐 2. The Geometric Approach: EAR and its Variants <span id="geometric"></span>

The most computationally efficient way to determine if an eye is open is purely geometric. We use an upstream face detector (like SCRFD or RetinaFace) to extract a bounding box, followed by a dense landmarking model (e.g., InsightFace 2d106det) to place points on the facial features.

### The Classic EAR ($ EAR_g $)

Using the 6 classic points bounding the eye, Soukupová & Čech (2016) defined the **Eye Aspect Ratio (EAR)**:

$$
\text{EAR}_g = \frac{\|p_2 - p_6\| + \|p_3 - p_5\|}{2 \|p_1 - p_4\|}
$$

- **Numerator:** The sum of the two vertical distances between the upper and lower eyelids.
- **Denominator:** The horizontal distance between the canthal corners, multiplied by 2.

Because this ratio divides a vertical span by a horizontal span measured on the *same object*, it is mathematically **scale-invariant**. An eye close to the lens and an eye far away will produce the exact same EAR. It requires no per-camera calibration. 

As the eye closes, the numerator collapses toward 0, while the denominator stays constant. A simple threshold separates "open" from "closed".

### The Robust EAR ($ EAR_r $): Eigen-Analysis of the Eye Cloud

The classic $ EAR_g $ depends strictly on point *ordering*. If the landmarker swaps "upper" and "lower" points (which happens frequently as the eye closes and the points merge), the formula breaks. 

We propose a more robust variant, **$ EAR_r $**. Instead of pairing specific points, we treat the eye's landmarks as an unordered point cloud $ X $. We compute the covariance matrix $ X^T X $ and extract its eigenvectors and eigenvalues. 

The two eigenvectors represent the main axes of the eye (its length $ u $ and its opening $ v $). The eigenvalues are the variances (squared lengths) along these axes. We define the robust EAR as:

$$
\text{EAR}_r = \frac{\sqrt{\lambda_{\text{minor}}}}{\sqrt{\lambda_{\text{major}}}} = \frac{\|v\|}{\|u\|}
$$

**Why $ EAR_r $ is superior:**
1. **Unordered:** It does not care which point is which.
2. **Rotation invariant:** A 40-degree head roll simply rotates the eigenvectors. The ratio remains completely unchanged.
3. **Noise resistant:** A single jittering landmark perturbs a 10-point covariance matrix far less than it perturbs the single distance pair it belongs to.

---

## 📉 3. The Failure of the Scalar Threshold <span id="failure"></span>

Geometry is elegant, but it hits a wall on real data.

When we plot the density of $ EAR_r $ for open (blue) and closed (red) eyes on a webcam dataset (Eyeblink8), we see two distinct peaks separated by a deep valley. 
However, when plotted on **FFHQ** (high variance, diverse portraits), the populations overlap. There is no valley; there is a slope. 

### The Limits of Calibration
We ran a sweep of 55 candidate thresholds, taking the `argmax` on the macro-$ F_1 $ score. The optimal threshold shifted by up to 0.06 depending on the dataset. 

Furthermore, geometry fails catastrophically on **makeup**. Heavy eyeliner forces the landmarker to place the "eyelid" points far apart, even when the eye is tightly shut. The geometry confidently outputs $ EAR_r = 0.47 $ (wide open), and no threshold adjustment can fix it, because the input to the threshold is fundamentally false.

The line literally runs through the data: two eyes on the *same face* in the *same photograph* can yield $ EAR_r $ values that straddle the threshold. A single scalar is not expressive enough to capture "openness".

---

## 🧠 4. The Learned Approach: The 6-Class Taxonomy <span id="learned"></span>

To survive real-world portraits, we abandon the threshold and train a Convolutional Neural Network (CNN) directly on the image crop of the eye. 

Instead of a binary "Open/Closed", the network is trained on a rich 6-class taxonomy:
1. `o` : Open
2. `c` : Closed
3. `ms` : Mi-squint (partially narrowed)
4. `mb` : Mi-blink (partially closed, mid-action)
5. `la` : Looking Away
6. **`u` / `n` : Unknown / Not an eye (Abstention)**

### The Absolute Necessity of Abstention
If a woman is at the edge of the frame and only her left eye is visible, the landmarker will return a black square for the right eye crop. If our network is binary, it is forced to guess "Open" or "Closed" for a black square. 

By adding the abstention class, the network can answer `n` (Not an eye). If heavy glare obscures the pupil, the network answers `u` (Unknown). This abstention is a *decision* made by the model, allowing the culling pipeline to defer judgment rather than throwing away a photo based on a hallucinated read.

---

## ⚙️ 5. The Squeeze: Crop Resolution & Training Regimes <span id="training"></span>

### The Squeeze (Input Resolution)
The first iteration of this network scored an abysmal **0.03 macro-$ F_1 $**. The model was learning nothing. The error wasn't the architecture; it was the crop. We were feeding a 64x64 pixel crop of the *entire face*. At that scale, an eye is roughly 8 pixels wide. The state of the eyelid is physically absent from the signal. 
*Lesson: Before blaming the model, ensure the evidence physically exists in the input tensor.*

We switched to a 128x128 crop centered strictly on the eye's PCA frame (derived from $ EAR_r $), and the score jumped to 0.81. 

### The Optimization Recipe
We fine-tuned a **RegNetY-3.2GF** (19 million parameters) using only 1,733 annotated crops. With such a massive parameter-to-data mismatch, the training schedule is everything.

1. **Epoch 1-4 (The Linear Probe):** Backbone is frozen (`requires_grad = False`). Only the classification head trains at a high learning rate ($ 10^{-3} $) to organize the random weights.
2. **Epoch 5 (The Switch):** The backbone is unfrozen. Crucially, the **optimizer is thrown away and rebuilt**. If we kept the AdamW state, the momentum accumulated over the head would violently perturb the 19 million backbone parameters. The learning rate drops 17-fold.
3. **Epoch 5-40 (Cosine Annealing):** The learning rate follows a cosine decay to zero. The model is extremely stable at the end. We save the **Exponential Moving Average (EMA)** of the weights at Epoch 40, avoiding validation-based early stopping.

---

## 📊 6. Evaluation: The Confusion Cost <span id="evaluation"></span>

The network achieved a macro-$ F_1 $ of **0.933** on the held-out set. But accuracy is a misleading metric for culling.

Standard cross-entropy loss treats all errors equally. But confusing an open eye for a squint is a minor disagreement; confusing a closed eye for an open eye is a catastrophic failure (a bad photo is kept). 

We implemented a **Cost Matrix Loss**. We fitted Gaussians over the $ EAR_r $ distribution for each class, and computed the Bhattacharyya distance between them. The closer two classes are geometrically, the lower the penalty for confusing them. 

The resulting confusion matrix proves the concept: almost all errors sit exactly on the diagonal (e.g., `o` confused with `ms`). The dangerous crossing (predicting `o` when truth is `c`) happened exactly *once* in the entire test set, and the network's confidence on that error was $ 0.34 $ — perfectly situated for the abstention mechanism to catch it.

---

**Navigation :** ⬅ [Assisted Culling](culling.md) · 🏠 [Home](../../README.md) · [Blur Detection ➡](blur.md)