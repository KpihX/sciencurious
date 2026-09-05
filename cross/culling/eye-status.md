# 👁️ Eye Status: Geometry vs Deep Learning

> 🧠 **Deconstructing the eye** — why geometric heuristics are fast but fragile, and how a learned network with the right to abstain brings robustness to facial analysis.
>
> 📅 Date: 2026-09-05
> 👤 Author: KpihX
> 📚 Code & Repo: [GitHub](https://github.com/KpihX/culling-presentation) · [GitLab](https://gitlab.com/kpihx/culling-presentation)

> 🔗 **Prequel:** [Assisted Culling: A Signal is Not a Verdict](culling.md)

---

## 📋 Table of Contents

1. [The Preoccupation: The Blink](#-1-the-preoccupation-the-blink)
2. [The Geometric Approach: EAR](#-2-the-geometric-approach-ear)
3. [The Learned Approach: A 6-Class Network](#-3-the-learned-approach-a-6-class-network)
4. [References](#references)

---

## 🧩 1. The Preoccupation: The Blink <span id="preoccupation"></span>

In portrait photography, timing is everything. A burst of shots might capture a perfect smile, but if the eyes are caught mid-blink, the photo is ruined. Detecting eye status (open vs. closed) is the cheapest and most objective way to filter a burst.

However, the "eye" is a highly variable visual feature. Glasses, reflections, makeup, extreme angles, and partial occlusions make classical computer vision algorithms stumble. 

<video width="100%" controls>
  <source src="assets/eye_closing.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 📐 2. The Geometric Approach: EAR <span id="ear"></span>

The fastest way to determine eye status requires zero training: **geometry**. 

Using a facial landmark detector (e.g., MediaPipe or dlib), we extract a mesh of the face. For each eye, we isolate specific points along the eyelid contour (typically 6 points). 

We compute the **Eye Aspect Ratio (EAR)**, introduced by Soukupová & Čech (2016):

$$
\text{EAR} = \frac{\|p_2 - p_6\| + \|p_3 - p_5\|}{2 \|p_1 - p_4\|}
$$

- The numerator computes the vertical distances between the upper and lower eyelid points.
- The denominator computes the horizontal distance between the corners of the eye.
- The factor of 2 normalizes the result.

**The Pros:** It is incredibly fast, operates in real-time, and has zero trainable weights.
**The Cons:** It is extremely brittle. If the landmark detector fails due to heavy makeup, glare on glasses, or an extreme profile angle, the EAR becomes meaningless. Furthermore, it requires a hard threshold to decide "open" vs "closed", which requires sweeping over validation sets to maximize the macro-F1 score.

## 🧠 3. The Learned Approach: A 6-Class Network <span id="learned"></span>

To survive real-world photography, we turn to deep learning. Instead of relying on a fragile geometric intermediate step, we train a lightweight convolutional network (like a customized RegNet or MobileNet) to look directly at the cropped eye patch.

![Eye Pipeline](assets/02-eye-pipeline.png)

Instead of a binary "Open/Closed", the network predicts over a nuanced taxonomy:
1. Open
2. Closed
3. Partially Open
4. Looking Away
5. Occluded (hair, hand)
6. **Abstention (Unreadable)**

### The Power of Abstention

The critical feature here is the 6th class. If the network is confused by a massive reflection on a pair of sunglasses, it does not randomly guess "Open" or "Closed". It abstains. 

This brings us back to the core philosophy: a signal, not a verdict. An abstention tells the pipeline "I cannot confidently rank this based on the eyes; fall back to the blur module or ask the human."

---

**Navigate:** ⬅ [Assisted Culling](culling.md) · 🏠 [Home](../../README.md) · [Blur Detection ➡](blur.md)
