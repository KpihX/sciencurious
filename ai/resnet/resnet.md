# ResNet: Deep Residual Learning for Image Recognition

> 🧠 **A complete theoretical exploration** — the degradation problem, the residual reformulation, the block anatomy, and the clean-path gradient proof.
>
> 📅 Date: 2026-08-03
> 👤 Author: KπX × Explore agent
> 📚 Based on the original papers (see [References](#references))

> 🔗 **Sequel:** [RegNet — Designing Network Design Spaces](../regnet/regnet.md) — from the residual block to the design space.

---

## 📋 Table of Contents

1. [The Preoccupation: The Degradation Problem](#-1-the-preoccupation-the-degradation-problem)
2. [The Intuition: Identity Preconditioning](#-2-the-intuition-identity-preconditioning)
3. [The Toy Proof: Why Plain Networks Cannot Learn Identity](#-3-the-toy-proof-why-plain-networks-cannot-learn-identity)
4. [Generalizing to Multi-Dimensional Space](#-4-generalizing-to-multi-dimensional-space)
5. [The Anatomy of Residual Units](#-5-the-anatomy-of-residual-units)
6. [Gradient Propagation & The Clean Path Proof](#-6-gradient-propagation--the-clean-path-proof)
7. [Summary Table](#-7-summary-table)
8. [References](#references)

---

## 🧩 1. The Preoccupation: The Degradation Problem

### 📉 The Symptom

Before 2015, the prevailing belief in deep learning was simple: **deeper is better**. More layers meant more abstract features, which should mean better accuracy.

However, researchers ran into a brick wall called the **Degradation Problem**:

- When networks became too deep (e.g., jumping from 20 to 56 layers), the **training error** (not just the validation error) got significantly worse.
- This is **not overfitting**: overfitting produces low training error but high testing error. Here, the model couldn't even fit the training data.

### 🧱 The Paradox

In theory, a 56-layer network should be able to copy the exact features of a 20-layer network by simply setting the remaining 36 layers to perform an **identity mapping**:

$$
f(x) = x
$$

Yet standard optimization methods (like Stochastic Gradient Descent) failed to find this apparently simple solution. He et al. (2016) summarize the hypothesis:

> "If the added layers can be constructed as identity mappings, a deeper model should have training error no greater than its shallower counterpart. The degradation problem suggests that the solvers might have difficulties in approximating identity mappings by multiple nonlinear layers."

---

## 💡 2. The Intuition: Identity Preconditioning

### ⚖️ The Toy Weight Analogy

Imagine a layer that must estimate your current weight \( H(x) \) given your weight last year \( x \).

**🔴 Plain Net Strategy:** The network must learn to map \( x \) directly to \( H(x) \). If your weight doesn't change, the network has to reconstruct the entire signal from scratch through multiple matrix multiplications:

$$
H(x) \approx 70
$$

**🟢 Residual Net Strategy:** Instead of predicting the final weight, force the network to only predict the **difference** (the residual) \( F(x) = H(x) - x \), then add the starting weight back:

$$
H(x) = F(x) + x
$$

If your weight doesn't change, the network only needs to learn to output **zero**:

$$
F(x) \approx 0
$$

> 🎯 **Key insight:** In deep learning, pushing weights toward zero is **easy** for optimizers (helped by L2 regularization/weight decay). Pushing weights to reconstruct a perfect copy of the input through nonlinear layers is **hard**.

### 🔓 What This Unlocks

By changing the default state of every block to an **identity mapping** (when weights are zero):

1. **🚀 Infinite depth scaling** — redundant layers can be bypassed (\( F(x) \to 0 \)), matching the shallower network's performance at worst.
2. **🌊 Smooth gradient flow** — the gradient of the identity path is always 1, creating a "superhighway" for gradients.

### 📐 The Mathematical Reformulation

Let \( x \) be the input vector and \( H(x) \) the desired underlying mapping. The stacked layers are explicitly asked to fit the **residual function**:

$$
F(x) := H(x) - x
$$

The original mapping is recast as:

$$
H(x) = F(x) + x
$$

This is realized with **shortcut connections** (also called *skip connections*) that perform identity mapping, adding their output to the stacked layers' output — with **no extra parameters and no added computational complexity**.

---

## 🪜 3. The Toy Proof: Why Plain Networks Cannot Learn Identity

> 🎯 **Goal:** Prove mathematically why a *plain* network cannot easily learn the identity mapping \( H(x) = x \) as it deepens, whereas a *residual* network does so naturally.

### 🗺️ Proof Strategy

1. Reduce the network to **1D**: a single real-valued input \( x \) through a chain of \( L \) layers.
2. Strip away nonlinearities (assume activations in their linear region, e.g., \( x > 0 \) for ReLU) to isolate weight dynamics.
3. Compare two architectures:
   - 🔴 **The Plain Chain**: a stack of multiplicative linear layers.
   - 🟢 **The Residual Chain**: a stack of layers with identity skip connections.
4. Analyze two phenomena:
   - **Initialization & target alignment**: the output at step zero.
   - **Gradient stability**: the backpropagation dynamics.

### 3.1 The Two Toy Models

**🔴 Plain Network:** Each layer multiplies its input by a weight \( w_l \):

$$
y_{\text{plain}} = \left( \prod_{i=1}^{L} w_i \right) x
$$

To represent the identity \( H(x) = x \), the network must satisfy:

$$
\prod_{i=1}^{L} w_i = 1
$$

**🟢 Residual Network:** Each layer adds its input to the residual transformation, \( y_l = y_{l-1} + w_l y_{l-1} = (1 + w_l) y_{l-1} \):

$$
y_{\text{res}} = \left( \prod_{i=1}^{L} (1 + w_i) \right) x
$$

To represent the identity, the network must satisfy:

$$
\prod_{i=1}^{L} (1 + w_i) = 1
$$

### 3.2 The Initialization Phase (The "Dead Start")

Weights are initialized to small random values near zero, e.g., \( w_i \sim \mathcal{N}(0, \sigma^2) \) with \( \sigma^2 \ll 1 \).

**🔴 Plain Net at initialization** (say \( w_i = 0.5 \), \( L = 50 \)):

$$
y_{\text{plain}} = (0.5)^{50} \cdot x \approx 8.88 \times 10^{-16} \cdot x
$$

The signal is **completely extinguished** — extreme signal attenuation. To reach identity, the solver must push the weight *product* to exactly 1, a highly coupled, non-convex search.

**🟢 ResNet at initialization** (weights near zero, say \( w_i = 0 \)):

$$
y_{\text{res}} = \left( \prod_{i=1}^{50} (1 + 0) \right) x = 1^{50} \cdot x = x
$$

Even with small perturbations (\( w_i = 0.01 \)):

$$
y_{\text{res}} = (1.01)^{50} \cdot x \approx 1.64 \cdot x
$$

The signal is **preserved**! The network is *preconditioned* near the identity — the solver only learns tiny residual corrections, not a reconstruction from nothing.

### 3.3 Gradient Dynamics (Backpropagation Proof)

Let \( E \) be the loss. By the chain rule, updating weight \( w_l \) requires \( \frac{\partial E}{\partial w_l} \).

**🔴 Plain chain gradient:**

$$
\frac{\partial E}{\partial w_l} = \frac{\partial E}{\partial y_{\text{plain}}} \cdot \left( \prod_{i \neq l}^{L} w_i \right) x
$$

With \( w_i = 0.5 \) and \( L = 50 \):

$$
(0.5)^{49} \approx 1.77 \times 10^{-15}
$$

💥 **Vanishing gradient:** the gradient at early layers is essentially **zero** — the network cannot learn.

**🟢 ResNet chain gradient:**

$$
\frac{\partial E}{\partial w_l} = \frac{\partial E}{\partial y_{\text{res}}} \cdot \left( \prod_{i \neq l}^{L} (1 + w_i) \right) x
$$

With weights initialized to zero:

$$
\prod_{i \neq l}^{L} (1 + 0) = 1^{L-1} = 1
$$

So:

$$
\frac{\partial E}{\partial w_l} = \frac{\partial E}{\partial y_{\text{res}}} \cdot x
$$

🛡️ **Gradient preservation:** the gradient flows back **unimpeded** to every layer, no matter how deep (\( L \to \infty \)).

---

## 🌐 4. Generalizing to Multi-Dimensional Space

### 4.1 The Recurrence Relation

Let \( x_l \) be the input feature vector to the \( l \)-th residual unit:

$$
x_{l+1} = x_l + F(x_l, W_l)
$$

where \( F(x_l, W_l) \) is the residual function (a stack of convolutional layers, batch normalization, and activations).

### 4.2 The Unrolled Sum

Applying the recurrence recursively from layer \( l \) to a deep layer \( L \):

$$
x_{l+2} = x_l + F(x_l, W_l) + F(x_{l+1}, W_{l+1})
$$

Generalizing:

$$
x_L = x_l + \sum_{i=l}^{L-1} F(x_i, W_i)
$$

**Two beautiful properties:**

1. **➕ Additive representation:** \( x_L \) is a *sum* of the shallow feature \( x_l \) plus intermediate residuals — contrasted with plain networks, where \( x_L \) is a *product*: \( \prod_{i=l}^{L-1} W_i \cdot x_l \).
2. **🛡️ Signal preservation:** the raw feature \( x_l \) is directly carried to the final feature \( x_L \).

### 4.3 The Gradient Flow Proof

Applying the chain rule to the unrolled sum:

$$
\frac{\partial E}{\partial x_l} = \frac{\partial E}{\partial x_L} \cdot \frac{\partial x_L}{\partial x_l}
$$

Since \( \frac{\partial x_l}{\partial x_l} = I \) (the identity matrix):

$$
\frac{\partial E}{\partial x_l} = \frac{\partial E}{\partial x_L} \left( I + \frac{\partial}{\partial x_l} \sum_{i=l}^{L-1} F(x_i, W_i) \right)
$$

**Deconstruction of the parenthesized term:**

1. **🛡️ The Identity Guard \( I \):** the gradient from the deepest layer \( L \) propagates to layer \( l \) **without scaling or decay**.
2. **📉 Vanishing protection:** even if all residual Jacobians vanish (\( \sum \frac{\partial F}{\partial x} \to 0 \)), the term stays close to \( I \) — never zero.
3. **🚫 No explosion:** gradient is scaled *additively* (\( I + \sum \dots \)), not multiplicatively (\( \prod W_i \)).

---

## 🧬 5. The Anatomy of Residual Units

### 5.1 The Basic Block (ResNet-18 / ResNet-34)

Two stacked \( 3 \times 3 \) convolutions with a shortcut connection. Mathematically:

$$
y = F(x, \{W_1, W_2\}) + x
$$

with

$$
F(x, \{W_1, W_2\}) = \text{BN}(W_2 * \sigma(\text{BN}(W_1 * x)))
$$

where \( * \) is convolution, \( \sigma \) is ReLU, and BN is batch normalization. The block output:

$$
x_{\text{next}} = \sigma(y)
$$

#### 🧱 Identity Basic Block (no dimension change)

Input tensor: \( (C_{\text{in}}, H, W) \).

| Layer | Kernel | Stride | Padding | In ch. | Out ch. | Activation | Output shape |
|-------|--------|--------|---------|--------|---------|------------|--------------|
| Conv \( W_1 \) | \( 3 \times 3 \) | 1 | 1 | \( C_{\text{in}} \) | \( C_{\text{in}} \) | BN + ReLU | \( (C_{\text{in}}, H, W) \) |
| Conv \( W_2 \) | \( 3 \times 3 \) | 1 | 1 | \( C_{\text{in}} \) | \( C_{\text{in}} \) | BN only | \( (C_{\text{in}}, H, W) \) |
| Shortcut | identity \( h(x) = x \) | — | — | — | — | — | \( (C_{\text{in}}, H, W) \) |

Output spatial size check:

$$
H_{\text{out}} = \left\lfloor \frac{H - 3 + 2(1)}{1} \right\rfloor + 1 = H
$$

Then \( y = F(x) + x \) (element-wise, no parameters) and \( x_{\text{next}} = \sigma(y) \).

#### 📉 Projection Basic Block (downsampling: \( H \to \frac{H}{2} \), \( C_{\text{in}} \to C_{\text{out}} = 2 C_{\text{in}} \))

Input tensor: \( (C_{\text{in}}, H, W) \).

| Layer | Kernel | Stride | Padding | In ch. | Out ch. | Activation | Output shape |
|-------|--------|--------|---------|--------|---------|------------|--------------|
| Conv \( W_1 \) | \( 3 \times 3 \) | **2** | 1 | \( C_{\text{in}} \) | \( C_{\text{out}} \) | BN + ReLU | \( (C_{\text{out}}, \frac{H}{2}, \frac{W}{2}) \) |
| Conv \( W_2 \) | \( 3 \times 3 \) | 1 | 1 | \( C_{\text{out}} \) | \( C_{\text{out}} \) | BN only | \( (C_{\text{out}}, \frac{H}{2}, \frac{W}{2}) \) |
| **Shortcut \( W_s \)** | \( 1 \times 1 \) | **2** | 0 | \( C_{\text{in}} \) | \( C_{\text{out}} \) | BN only | \( (C_{\text{out}}, \frac{H}{2}, \frac{W}{2}) \) |

Spatial halving check (stride 2):

$$
H_{\text{out}} = \left\lfloor \frac{H - 3 + 2(1)}{2} \right\rfloor + 1 = \left\lfloor \frac{H - 1}{2} \right\rfloor + 1 = \frac{H}{2}
$$

The general block equation with projection shortcut:

$$
y = F(x, \{W_i\}) + W_s x
$$

> 💡 The identity shortcut is **sufficient** to address the degradation problem and is more economical; \( W_s \) (a \( 1 \times 1 \) convolution) is used **only** when matching dimensions (He et al., 2016).

### 5.2 The Bottleneck Block (ResNet-50 / 101 / 152)

For deep networks, stacking \( 3 \times 3 \) convolutions becomes too expensive. The Bottleneck uses **three** layers: a \( 1 \times 1 \) to *reduce* channels (squeeze), a \( 3 \times 3 \) to process spatially (the "bottleneck"), and a \( 1 \times 1 \) to *restore* channels (expand).

#### 🧱 Identity Bottleneck Block

Input: \( (C_{\text{in}}, H, W) \), with \( C_{\text{in}} \) already large (e.g., 256).

| Layer | Kernel | Stride | Padding | In ch. | Out ch. | Activation | Output shape |
|-------|--------|--------|---------|--------|---------|------------|--------------|
| Conv 1 (reduce) | \( 1 \times 1 \) | 1 | 0 | \( C_{\text{in}} \) | \( C_{\text{mid}} = \frac{C_{\text{in}}}{4} \) | BN + ReLU | \( (C_{\text{mid}}, H, W) \) |
| Conv 2 (process) | \( 3 \times 3 \) | 1 | 1 | \( C_{\text{mid}} \) | \( C_{\text{mid}} \) | BN + ReLU | \( (C_{\text{mid}}, H, W) \) |
| Conv 3 (restore) | \( 1 \times 1 \) | 1 | 0 | \( C_{\text{mid}} \) | \( C_{\text{in}} \) | BN only | \( (C_{\text{in}}, H, W) \) |
| Shortcut | identity | — | — | — | — | — | \( (C_{\text{in}}, H, W) \) |

Addition: \( y = F(x) + x \), output \( x_{\text{next}} = \sigma(y) \).

#### 📉 Projection Bottleneck Block (modern ResNet-B variant)

The downsampling stride is placed on the \( 3 \times 3 \) convolution (avoids information loss).

Input: \( (C_{\text{in}}, H, W) \).

| Layer | Kernel | Stride | Padding | In ch. | Out ch. | Activation | Output shape |
|-------|--------|--------|---------|--------|---------|------------|--------------|
| Conv 1 (reduce) | \( 1 \times 1 \) | 1 | 0 | \( C_{\text{in}} \) | \( C_{\text{mid}} = \frac{C_{\text{out}}}{4} \) | BN + ReLU | \( (C_{\text{mid}}, H, W) \) |
| Conv 2 (downsample) | \( 3 \times 3 \) | **2** | 1 | \( C_{\text{mid}} \) | \( C_{\text{mid}} \) | BN + ReLU | \( (C_{\text{mid}}, \frac{H}{2}, \frac{W}{2}) \) |
| Conv 3 (restore) | \( 1 \times 1 \) | 1 | 0 | \( C_{\text{mid}} \) | \( C_{\text{out}} \) | BN only | \( (C_{\text{out}}, \frac{H}{2}, \frac{W}{2}) \) |
| **Shortcut \( W_s \)** | \( 1 \times 1 \) | **2** | 0 | \( C_{\text{in}} \) | \( C_{\text{out}} \) | BN only | \( (C_{\text{out}}, \frac{H}{2}, \frac{W}{2}) \) |

Addition: \( y = F(x) + W_s x \), output \( x_{\text{next}} = \sigma(y) \).

> 💡 **Why identity shortcuts matter for bottlenecks:** if the identity shortcut were replaced with a projection on the bottleneck architecture, both time complexity and model size would be **doubled** — the shortcut connects the two high-dimensional ends. Identity shortcuts give the most efficient deep models.

---

## 🌊 6. Gradient Propagation & The Clean Path Proof

> 📚 This section follows He et al. (2016b), *"Identity Mappings in Deep Residual Networks"*.

### 6.1 The Principle of the Clean Path

**Standard (post-activation) unit:**

$$
y_l = x_l + F(x_l, W_l)
$$

$$
x_{l+1} = \sigma(y_l)
$$

**Pre-activation unit (the "clean path"):**

$$
x_{l+1} = x_l + F(\hat{f}(x_l), W_l)
$$

where \( \hat{f} \) is BN + ReLU applied *before* the weight layers.

In the post-activation design, the signal exiting the block is \( \sigma(y_l) \) — filtered by a nonlinearity. In the pre-activation design, the raw signal \( x_l \) passes through **untouched** — a literal wire between blocks.

### 6.2 Gradient Death — Post-Activation Case 💀

Forward pass through the standard block:

$$
y_l = x_l + F(x_l, W_l)
$$

$$
x_{l+1} = \sigma(y_l)
$$

Gradient by the chain rule:

$$
\frac{\partial E}{\partial x_l} = \frac{\partial E}{\partial x_{l+1}} \cdot \sigma'(y_l) \cdot \left( I + \frac{\partial F(x_l, W_l)}{\partial x_l} \right)
$$

with

$$
\sigma'(y_l) =
\begin{cases}
1 & \text{if } y_l > 0 \\
0 & \text{if } y_l < 0
\end{cases}
$$

💥 **The fatal observation:** the factor \( \sigma'(y_l) \) multiplies *everything* — including the identity term \( I \). If \( y_l < 0 \), the **entire gradient dies**, even the part flowing through the shortcut. Across \( L \) blocks, if any single \( \sigma'(y_l) = 0 \), the gradient to early layers is **exactly zero**.

### 6.3 The Clean Path — Pre-Activation Case 🌈

Forward pass:

$$
x_{l+1} = x_l + F(\hat{f}(x_l), W_l)
$$

Gradient:

$$
\frac{\partial E}{\partial x_l} = \frac{\partial E}{\partial x_{l+1}} \cdot \left( I + \frac{\partial F(\hat{f}(x_l), W_l)}{\partial x_l} \right)
$$

**Side-by-side contrast:**

$$
\text{Post-activation:} \quad \frac{\partial E}{\partial x_l} = \underbrace{\sigma'(y_l)}_{\text{kills the path}} \cdot \frac{\partial E}{\partial x_{l+1}} \cdot \left( I + \frac{\partial F}{\partial x_l} \right)
$$

$$
\text{Pre-activation:} \quad \frac{\partial E}{\partial x_l} = \frac{\partial E}{\partial x_{l+1}} \cdot \left( I + \frac{\partial F}{\partial x_l} \right)
$$

🟢 The \( \sigma'(y_l) \) factor has **vanished** from the shortcut path. The identity term \( I \) is now *truly* clean:

- ❌ No activation can zero it out.
- ❌ No scaling can shrink it.
- ✅ It is always exactly \( I \), at every block.

### 6.4 The Global Unrolling — The Master Formula 🎓

Unrolling the pre-activation recurrence across all blocks from \( l \) to \( L \):

$$
x_L = x_l + \sum_{i=l}^{L-1} F(\hat{f}(x_i), W_i)
$$

Differentiating:

$$
\frac{\partial E}{\partial x_l} = \frac{\partial E}{\partial x_L} \left( I + \frac{\partial}{\partial x_l} \sum_{i=l}^{L-1} F(\hat{f}(x_i), W_i) \right)
$$

**Two additive channels:**

1. **🛡️ The Direct Channel (\( I \)):** \( \frac{\partial E}{\partial x_L} \) propagates **unchanged** from layer \( L \) back to layer \( l \) — no weights, no activations, no scaling.
2. **🔀 The Branch Channel (\( \sum \)):** gradients through the residual branches; can shrink or vanish, but never alone decides the gradient's fate.

**The fundamental guarantee:**

> 🏆 **The gradient can NEVER vanish, because the \( I \) term is always present.** Even in the worst case where every residual branch produces zero gradient, the gradient reduces to \( \frac{\partial E}{\partial x_l} = \frac{\partial E}{\partial x_L} \cdot I \) — a perfect, lossless transmission.

This is why ResNets with identity shortcuts train successfully at **100+ layers** on CIFAR-10 (the paper demonstrates **1001-layer** networks) while plain networks collapse around 20 layers.

---

## 📊 7. Summary Table

| Concept | Plain Network | Residual Network |
|---------|---------------|------------------|
| Layer mapping | \( H(x) \) directly | \( F(x) + x \), with \( F(x) = H(x) - x \) |
| Identity to learn | \( \prod w_i = 1 \) (hard) | \( \prod (1 + w_i) = 1 \), i.e. \( w_i \to 0 \) (easy) |
| Initialization state | Signal extinguished | Preconditioned near identity |
| Gradient scaling | Multiplicative \( \prod w_i \) | Additive \( I + \sum \dots \) |
| Vanishing gradients | Exponential decay | Structurally impossible |
| Signal path | Through all nonlinearities | Clean wire (pre-activation) |

---

## 📚 References

1. **K. He, X. Zhang, S. Ren, J. Sun.** *"Deep Residual Learning for Image Recognition."* IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016. arXiv:1512.03385.
   - [CVPR paper (open access)](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)
   - [Microsoft Research copy](https://www.microsoft.com/en-us/research/wp-content/uploads/2021/07/Deep-Residual-Learning-for-Image-Recognition.pdf)
   - [arXiv](https://arxiv.org/abs/1512.03385)

2. **K. He, X. Zhang, S. Ren, J. Sun.** *"Identity Mappings in Deep Residual Networks."* European Conference on Computer Vision (ECCV), 2016. arXiv:1603.05027.
   - [arXiv](https://doi.org/10.48550/arxiv.1603.05027)
   - [GitHub: resnet-1k-layers](https://github.com/KaimingHe/resnet-1k-layers)

3. **A. Zhang, Z. C. Lipton, M. Li, A. J. Smola.** *"Dive into Deep Learning" (D2L), Chapter 8.6: Residual Networks (ResNet) and ResNeXt.*
   - [d2l.ai — 8.6 Residual Networks (ResNet)](https://d2l.ai/chapter_convolutional-modern/resnet.html)

4. **S. R. Rath.** *"Residual Neural Networks — ResNets: Paper Explanation."* DebuggerCafe, 2021.
    - [debuggercafe.com](https://debuggercafe.com/residual-neural-networks-resnets-paper-explanation/)
