# 📅 Exploration Ideas

> 🧭 **Track future theoretical deep dives and mathematical derivations** in this project space.

---

## ✅ Immediate TODOs (merged from TODO.md, 2026-09-05)

### Content
- [ ] Add visual diagrams (Manim/D3/Mermaid) to Integration article
- [ ] Write article: "Transformers — A Visual Journey" (CS/AI)
- [ ] Write article: "Fourier — Seeing Sound" (Math/Physics)

### Infrastructure
- [ ] Set up automated visual generation pipeline (code-as-visual)
- [ ] Add Mermaid plugin to Docsify for inline diagrams
- [ ] Explore Manim integration for animated math explanations

---

## 🔲 1. Vision Transformers (ViTs) 🚀

- [ ] **🧩 The Preoccupation:** Analyze why removing convolutional inductive biases (spatial locality and translation equivariance) allows models to achieve higher capacity on massive datasets, but causes them to underperform on small datasets.
- [ ] **💡 The Intuition:** Explore the representation of images as sequences of patches (visual "words") and how self-attention creates global receptive fields starting at the very first layer.
- [ ] **📐 Mathematical Anatomy:**
  - **Patch Projection:** Derivation of how a 2D image $ X \in \mathbb{R}^{H \times W \times C} $ is flattened into patches $ X_p \in \mathbb{R}^{N \times (P^2 C)} $ and projected to embedding dimension $ d $.
  - **Self-Attention Mechanism:** Deconstruct the query-key-value scaling:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V
$$

- [ ] **🌊 Representation Propagation:** Formulate why residual connections in ViTs behave differently than in CNNs, showing how they preserve spatial information across deep stacks.

---

## 🔲 2. Diffusion Models 🌫️

- [ ] **🧩 The Preoccupation:** Explore how generative modeling can be formulated as a physical process of structured denoising rather than direct density estimation (like GANs or VAEs).
- [ ] **💡 The Intuition:** Understand how slowly destroying image structure with Gaussian noise allows us to learn a reverse trajectory to reconstruct images from pure chaos.
- [ ] **📐 Mathematical Anatomy:**
  - **Forward (Noising) Process:** The Markov chain adding noise over steps $ t $:

$$
q(x_t \mid x_{t-1}) = \mathcal{N}(x_t; \sqrt{1 - \beta_t} x_{t-1}, \beta_t I)
$$

    and the closed-form shortcut to sample at any step $ t $ given $ x_0 $ using $ \alpha_t = 1 - \beta_t $ and $ \bar{\alpha}_t = \prod_{i=1}^t \alpha_i $:

$$
q(x_t \mid x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1 - \bar{\alpha}_t) I)
$$

  - **Reverse (Denoising) Process:** Derivation of the parameterized reverse transition:

$$
p_\theta(x_{t-1} \mid x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))
$$

- **The Training Objective:** Simplifying the variational bound to a mean-squared error on the noise:

$$
L_{\text{simple}}(\theta) = \mathbb{E}_{t, x_0, \epsilon} \left[ \|\epsilon - \epsilon_\theta(x_t, t)\|^2 \right]
$$
