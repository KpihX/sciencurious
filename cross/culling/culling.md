# 📸 Assisted Culling: A Signal is Not a Verdict

> 🧠 **Designing the ultimate photo-sorting assistant** — why treating metrics as absolute verdicts fails, the trap of dataset bias, and how a pipeline combining geometric logic with deep features enables true assisted culling.
>
> 📅 Date: 2026-09-05
> 👤 Author: KpihX
> 📚 Code & Repo: [GitHub](https://github.com/KpihX/culling-presentation) · [GitLab](https://gitlab.com/kpihx/culling-presentation)

---

## 📋 Table of Contents

1. [The Preoccupation: From Automation to Assistance](#-1-the-preoccupation-from-automation-to-assistance)
2. [The Core Philosophy: A Signal, Not a Verdict](#-2-the-core-philosophy-a-signal-not-a-verdict)
3. [The Foundation: Datasets and Their Traps](#-3-the-foundation-datasets-and-their-traps)
4. [The Final Pipeline Synthesis](#-4-the-final-pipeline-synthesis)
5. [References](#references)

---

## 🧩 1. The Preoccupation: From Automation to Assistance <span id="preoccupation"></span>

In a professional portrait or wedding shoot, a photographer can easily capture thousands of images. The process of discarding the flawed shots (blinks, out-of-focus, motion smear) to keep only the best is known as **culling**. 

The natural instinct of computer vision engineers is to *automate* this process: build an end-to-end neural network that ingests a photograph and outputs a binary `keep` or `discard` score. This black-box approach dominates many commercial tools, but it fundamentally misunderstands the artistic intent of photography.

### The Limits of a Black-Box Score

- **Context is King:** A completely blurred background is a desirable effect (bokeh) in a portrait, but a ruined shot in landscape photography.
- **The "Laughing Blink":** A subject with closed eyes is usually a reject. However, if the subject is roaring with laughter, the closed eyes represent genuine emotion, and the photo might be the best of the session.
- **Uninterpretable Numbers:** A score of "86% blurry" or "Quality: 4/10" offers no diagnostic value. If the AI deletes an image, the photographer has no way to understand *why*, making the tool impossible to trust.

---

## 💡 2. The Core Philosophy: A Signal, Not a Verdict <span id="philosophy"></span>

To solve these contradictions, this project is built on two absolute rules:

1. **A metric is a signal, never a verdict.** The AI is not allowed to decide alone. Its job is to extract highly specific, localized signals (e.g., "the left eye is closed", "the subject is in motion") and present them.
2. **A score you cannot read is not a result.** If an image is flagged for motion blur, the system must draw the precise direction and magnitude of that blur on the image. An orientation becomes an ellipse; a blur width becomes a colored region. The claim must be visually contradictable by the human operator.

We do not build an automatic culler. We build an **Assisted Culling** tool: the machine narrows the field and explains its reasoning; the photographer decides.

This translates into two sovereign sub-systems:
- 👁️ **Eye Status:** Reading the state of the eyes (Open, Closed, Squinting, etc.).
- 🌫️ **Blur Detection:** Mapping sharpness, motion, and defocus across the image plane.

---

## 🏗️ 3. The Foundation: Datasets and Their Traps <span id="datasets"></span>

Before any architecture is drawn, the data must be audited. In this project, dataset bias is the primary cause of architectural failure.

### The Eye Status Data Trap
Most commercial models use standard video datasets like **Eyeblink8**. Eyeblink8 has perfect frame-by-frame annotations for blinks. However, it consists of only 4 subjects, sitting head-on in front of a webcam in a single room. 
If we train or calibrate a model on Eyeblink8, we build a model that understands *webcams*, not photography.

Real photography involves diverse lighting, heavy makeup, glasses, extreme profiles, and occlusions. To represent reality, we use **FFHQ** (Flickr-Faces-HQ, 70,000 highly diverse portraits). The catch? FFHQ has *no eye state annotations*. 

**The Lesson:** We must build the labels before building the model. (Using VLLM pre-annotation followed by rigorous human review).

### The Blur Data Trap
For blur, we often combine datasets like **Kwentar** (global blur states) and **CUHK** (a local blur detection dataset). 

If we feed a classifier this combined dataset blindly, the network quickly learns a catastrophic shortcut:
- `local_motion` is entirely from the CUHK dataset.
- `global_defocus` is entirely from the Kwentar dataset.

The network does not learn what "motion blur" looks like. It learns to recognize the noise signature, color profile, and lens characteristics of the cameras used to shoot the CUHK dataset. The class and the archive become mathematically indistinguishable. 

> 🎯 **Key insight:** You must audit your datasets before defining your architecture. If a class exists only in one dataset, a lazy model will just learn the dataset's signature.

---

## 🧬 4. The Final Pipeline Synthesis <span id="synthesis"></span>

The two modules (Eye Status and Blur) are processed in parallel, culminating in a logical synthesis that respects the photographer's workflow.

![The Synthesis Pipeline](assets/04-blur-pipeline-finale.png)

*(Above: The comparative blur pipeline, routing through CNN classification and physical window field analysis).*

### Synthesis on a Single Image (The AND Gate)
When evaluating a single photograph, the system uses a logical **AND**. A photo is flagged as a potential reject only if a module explicitly opposes it (e.g., Blur module says "Defocused" AND Eye module says "Closed"). Crucially, modules possess an **Abstention Class**. If the eye module cannot read the eye due to sunglare, it abstains. The photo survives the filter rather than being wrongfully discarded.

### Synthesis on a Burst (Veto and Rank)
Photographers shoot in bursts (e.g., 5-10 frames per second). Over a burst, the composition is fixed, but the micro-expressions change.
1. **The Veto (Blur):** A severely blurred photo in a burst is unrecoverable. The blur module acts as an absolute veto, instantly filtering out the ruined frames.
2. **The Rank (Eyes):** Among the sharp survivors of the veto, the eye module ranks them. A fully open eye outranks a half-closed one.

This division of labor mirrors human logic: *first ensure the shot is technically viable, then pick the best expression.*

---

**Navigation :** 🏠 [Home](../../README.md) · [Eye Status : The Sequel ➡](eye-status.md)