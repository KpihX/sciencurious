# 🌫️ Blur: From Scalar Scores to Spatial Fields

> 🧠 **Making blur inspectable** — why global scalar metrics fail to distinguish bokeh from motion, the architecture of the CNN judge, and how modeling blur as a continuous vector field bridges the gap between deep learning and physics.
>
> 📅 Date: 2026-09-05
> 👤 Author: KpihX
> 📚 Code & Repo: [GitHub](https://github.com/KpihX/culling-presentation) · [GitLab](https://gitlab.com/kpihx/culling-presentation)

> 🔗 **Prequel:** [Eye Status: Geometry vs Deep Learning](eye-status.md)

---

## 📋 Table of Contents

1. [The Preoccupation: The Subjectivity of Blur](#-1-the-preoccupation-the-subjectivity-of-blur)
2. [Phase I: The Classical Bank (Global Scalars)](#-2-phase-i-the-classical-bank-global-scalars)
3. [Phase II: The CNN Classifier (And Its Data Trap)](#-3-phase-ii-the-cnn-classifier-and-its-data-trap)
4. [Phase III: The Window Vector Field (Physical Interpretation)](#-4-phase-iii-the-window-vector-field-physical-interpretation)
5. [The Final Decision: Subject vs Background](#-5-the-final-decision-subject-vs-background)
6. [References](#references)

---

## 🧩 1. The Preoccupation: The Subjectivity of Blur <span id="preoccupation"></span>

A closed eye is an objective defect. Blur is not. 
Blur is highly subjective and deeply tied to artistic intent. 

There are multiple types of blur:
- **Global Motion Blur:** The camera shook. (Reject).
- **Global Defocus:** The camera missed the focal plane entirely. (Reject).
- **Local Motion:** The subject moved rapidly while the background remained sharp. (Reject, usually).
- **Bokeh (Local Defocus):** The subject is in sharp focus, but a shallow depth of field intentionally blurs the background. (Keep! This is often the desired aesthetic).

If an algorithm simply outputs a scalar value like "0.82 Blurry", it is fundamentally useless to a photographer. Did it detect camera shake, or did it detect the beautiful bokeh? We must move from an abstract score to a spatial map.

---

## 📉 2. Phase I: The Classical Bank (Global Scalars) <span id="classical"></span>

Before training neural networks, we must extract the maximum amount of signal using classic image processing. We run the log-luminance frame through three deterministic operators:

### 1. Variance of the Laplacian
The Laplacian operator (the trace of the Hessian matrix) acts as a 2nd-order derivative, highlighting regions of rapid intensity change (edges). 
By computing the variance of the Laplacian across the image, we get a measure of high-frequency energy. A sharp image has many crisp edges (high variance). A blurry image is flat (low variance).

### 2. The Structure Tensor & Coherence
To separate *motion* blur from *defocus* blur, we need directionality. We compute the image gradients $ g = [\nabla_x, \nabla_y]^T $. 
The Structure Tensor $ T $ is defined as the outer product of the gradients averaged over a neighborhood:

$$
T = \overline{g g^T} = \begin{bmatrix} \overline{G_x^2} & \overline{G_x G_y} \\ \overline{G_x G_y} & \overline{G_y^2} \end{bmatrix}
$$

The eigenvalues $ \lambda_1, \lambda_2 $ of $ T $ describe the energy along the principal axes. 
- If $ \lambda_1 \approx \lambda_2 $, the blur is isotropic (a circle) → **Defocus**.
- If $ \lambda_1 \gg \lambda_2 $, the energy is highly directional (a line) → **Motion smear**.

We compute the coherence $ \rho $:

$$
\rho = \frac{(\lambda_1 - \lambda_2)^2}{(\lambda_1 + \lambda_2)^2}
$$

Coherence approaches 1 for a streak (motion) and 0 for a disc (defocus). 

**The Limitation:** These classical metrics are fast and mathematically sound, but they are *global*. They average the subject and the background together. A sharp subject against heavy bokeh yields a middling score, indistinguishable from a globally mild defocus.

---

## 🧠 3. Phase II: The CNN Classifier (And Its Data Trap) <span id="cnn"></span>

To gain spatial understanding, we turn to Convolutional Neural Networks (CNNs). We define a 5-class taxonomy: `sharp`, `global_motion`, `global_defocus`, `local_motion`, and `bokeh`.

### The Dataset Catastrophe
We combined two datasets: **Kwentar** (which contains global motion and global defocus) and **CUHK** (which contains local motion and bokeh).

When we trained a CNN on this, it quickly achieved high accuracy. But it was a trap. The model realized that `local_motion` *only* existed in the CUHK dataset, and `global_defocus` *only* existed in Kwentar. The network stopped looking for blur and started looking for the sensor noise, color profile, and lens characteristics of the specific cameras used in those datasets. 

**The architecture cannot solve a dataset problem.** We had to aggressively curate 8 different archives to ensure at least 3 separate camera sources existed for every single class before the CNN was forced to actually learn the physics of blur.

---

## 📐 4. Phase III: The Window Vector Field (Physical Interpretation) <span id="window"></span>

Even with a perfect dataset, a CNN outputs a black-box class label. If it predicts `local_motion`, the photographer cannot see *where* the motion is or *why* the network decided that.

To achieve **Assisted Culling**, we slice the image into overlapping windows. We do not ask the network for a class; we ask it for a physical measurement. Each window predicts a vector:
- **Magnitude:** The width of the blur kernel.
- **Orientation:** The angle of the smear.

These predictions are projected back onto the image as geometric glyphs (ellipses). 

<video width="100%" controls>
  <source src="assets/blur_moto.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

*(Above: The vector field at work. Notice the ellipses on the background are large circles (defocus), while the ellipses on the moving wheels are flat, horizontal segments (motion smear). The subject's torso is sharp (small dots).)*

### Field Diffusion
A flat wall has no high-frequency energy. A window looking purely at a white wall cannot measure blur, because there are no edges to smear. 
Instead of forcing the network to guess, the window outputs an *empty* reading. We then use a diffusion algorithm (minimizing an energy functional) to propagate the blur readings from the edges into the flat regions, using the image's original luminance as a guiding wire. The result is a dense, continuous, physically accurate map of the focal plane.

---

## ⚖️ 5. The Final Decision: Subject vs Background <span id="fusion"></span>

We have an incredible spatial map, but we still need to make a culling decision. 

Using an off-the-shelf Salient Object Detection (S3OD) mask, we split the frame into two regions: **Subject** and **Outside**.

We compute our metrics (Laplacian Variance, Tenengrad, and the CNN embedding features) independently on the Subject and on the Outside. For each metric, we compute a normalized differential:

$$
\text{Score} = \frac{\text{Subject} - \text{Outside}}{|\text{Subject}| + |\text{Outside}| + \epsilon}
$$

This bounds the score between -1 and +1. Positive means the subject is sharper (keep, bokeh). Negative means the background is sharper (reject, missed focus).

Instead of relying on the CNN alone (which scored 0.908), we **fuse** the three metrics. The weighted fusion achieves 0.951 accuracy. We set an abstention band $ \tau $ around zero: if the score is too close to call, the module abstains, passing the image to the photographer with the vector field overlay visible.

The photographer looks at the screen, sees the ellipses, understands the machine's reasoning instantly, and clicks Keep or Reject. 
That is true **Assisted Culling**.

---

**Navigation :** ⬅ [Eye Status](eye-status.md) · 🏠 [Home](../../README.md)
