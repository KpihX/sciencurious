# 🌫️ Blur: From Scalar Scores to Spatial Fields

> 🧠 **Making blur inspectable** — why global scalar metrics fail to distinguish bokeh from motion, the dataset trap of CNNs, and how modeling blur as a continuous vector field bridges the gap between deep learning and physics.
>
> 📅 Date: 2026-09-05
> 👤 Author: KpihX
> 📚 Code & Repo: [GitHub](https://github.com/KpihX/culling-presentation) · [GitLab](https://gitlab.com/kpihx/culling-presentation)

> 🔗 **Prequel:** [Eye Status: Geometry vs Deep Learning](eye-status.md)

---

## 📋 Table of Contents

1. [The Preoccupation: Is this picture sharp?](#-1-the-preoccupation-is-this-picture-sharp)
2. [The Classical Bank (Global Scalars)](#-2-the-classical-bank-global-scalars)
3. [The Learned Approach & The Corpus Trap](#-3-the-learned-approach--the-corpus-trap)
4. [The Window-Based Approach (Fields)](#-4-the-window-based-approach-fields)
5. [The Fusion Judge](#-5-the-fusion-judge)
6. [References](#references)

---

## 🧩 1. The Preoccupation: Is this picture sharp? <span id="preoccupation"></span>

Unlike eye status, which has a discrete, nameable answer, blur does not. 
A photograph can have global motion blur, global defocus, local motion (subject moving), or bokeh (background defocus). A culling system must distinguish a ruined photo from artistic intent. 

---

## 📉 2. The Classical Bank (Global Scalars) <span id="classical"></span>

We start by running the log-luminance frame through classical operators to see what they can separate.

![Structure Tensor Math](assets/tensor_math.png)

1. **Laplacian Variance and Tenengrad:** Both fall by a factor of 25 from sharp to motion to defocus. They answer the question *"how much?"* perfectly.
2. **The Structure Tensor ($ T $):** The gradient $ g = [G_x, G_y]^T $. The tensor is $ T = \overline{g g^T} $. The eigenvalues $ \lambda_1, \lambda_2 $ are not proxies for directional energies; they *are* them.
3. **Coherence ($ \rho $):** The normalized difference of the two eigenvalues. Zero for a disc (defocus or sharp). One for a smear (motion). This is the categorical axis that separates motion from everything else.

Two magnitudes and one axis. The classical bank carries a real signal.

---

## 🧠 3. The Learned Approach & The Corpus Trap <span id="cnn"></span>

Since the classical bank carries a signal, the obvious next step is to put it into a classifier. We define 5 classes: `sharp`, `global_motion`, `global_defocus`, `local_motion`, and `bokeh`.

But here lies the trap.

![Corpus Trap](assets/corpus.png)

We used two datasets: Kwentar (which has the global states) and CUHK (a blur-detection set with only local states). Put them together, and look at what the classifier sees: two disjoint blocks. 

`local_motion` means CUHK and `global_defocus` means Kwentar. The class and the archive are the exact same fact. The network learns to recognize the dataset signature, not the blur. You cannot solve a dataset problem with an architecture. We had to heavily curate 8 different archives to ensure at least 3 sources per class.

---

## 📐 4. The Window-Based Approach (Fields) <span id="window"></span>

A CNN outputs a global class. But blur varies across the image. We need a map. We divide the image into windows and compute the classical metrics (and a lightweight CNN embedding) per window. 

The structure tensor of a window is a 2x2 symmetric matrix, which geometrically represents an ellipse. The output is not a color map, it is the actual ellipses drawn over the image.

![Windows Before Diffusion](assets/windows_before.png)

Read the rows across:
1. **The Schnauzer (Control):** Every window is sharp. Ellipses are small and round. 
2. **The Wheelie (Panning shot):** The rider is sharp (small round dots), but the street is smeared horizontally (flat segments). One frame, two answers. A global median width would just average them and be wrong everywhere. 
3. **The Vase (Bokeh):** The background is flat and out of focus. A flat surface has near-zero high-frequency energy. There is nothing to measure. A system forced to predict per window would call it blurred. This system says nothing (the pink areas), which is the physical truth.

To fill the pink gaps, we use a diffusion process. We minimize an energy functional where windows pull the field toward their measurement, but the smoothness constraint is guided by the image's original luminance. The result is a dense, continuous map of the focal plane.

<video width="100%" controls>
  <source src="assets/blur_moto.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

*(Above: The vector field overlay. Notice the large circles in the bokeh, and the sharp dots on the subject).*

---

## ⚖️ 5. The Fusion Judge <span id="fusion"></span>

When the CNN tower predicts a local class, how do we decide if the subject is sharper than the outside (a keeper) or worse (a reject)?

We use a salient-object mask (S3OD) to split the frame into Subject and Outside. We then use 3 probes (Laplacian Variance, Tenengrad, and the CNN Embedding gap). All three compute a bounded score from -1 (background sharper) to +1 (subject sharper).

![The Judges](assets/judges.png)

We don't trust just the network. The CNN probe alone is the *weakest* of the three (0.908). But the weighted fusion of all three reaches 0.951. The fusion is not a hedge; it is the result.

Finally, we ship an abstention band $ \tau $. If the frame is too close to call, the module refuses to decide, passing the vector field map to the photographer.

![The Blur Rule](assets/blur_rule.png)

This is Assisted Culling.

---

**Navigation :** ⬅ [Eye Status](eye-status.md) · 🏠 [Home](../../README.md)