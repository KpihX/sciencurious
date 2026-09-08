# Intégration avec les sommes de Riemann — transcription fidèle

> 🧾 **Manuscrit original :** `sommes-riemann.pdf` (scan, 1 page) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`sommes-riemann.pdf`](sommes-riemann.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Intégration avec les sommes de Riemann .pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

$$J(x) = \int_0^{2\pi} \ln|x^2 - 2x\cos t + 2|\,dt, \quad x \in \mathbb{R} \setminus \{1, \dots\} \text{ [lecture incertaine sur l'ensemble exclu]}$$

$\forall x \in \mathbb{R} \setminus \{0, 1\}$, $\forall t \in [0, 2\pi]$, $x^2 - 2x\cos t + 2 \geq x^2 - 2x\cos t + \cos^2 t = (x - \cos t)^2 > 0$ car $x \notin \{0, 1\}$ [lue telle quelle — la minoration stricte vaut dès que $x \neq \cos t$].

Ainsi $f_x(t) = \ln(x^2 - 2x\cos t + 2)$ est bien définie $\forall t \in [0, 2\pi]$. De plus $f_x$ est continue sur $[0, 2\pi]$ et donc intégrable au sens de Riemann. Par conséquent :

$$J(x) = \lim_{n \to +\infty} \frac{2\pi}{n} \sum_{k=0}^{n-1} \ln\left(x^2 - 2x\cos\left(\tfrac{2\pi}{n}k\right) + 2\right)$$

$$= \lim_{n \to +\infty} \frac{2\pi}{n} \sum_{k=0}^{n-1} \ln\left|\left(x - e^{i\frac{2\pi}{n}k}\right)\left(x - e^{-i\frac{2\pi}{n}k}\right)\right|$$

$$= \lim_{n \to +\infty} \frac{2\pi}{n} \ln\left(\prod_{k=0}^{n-1} \left(x - e^{i\frac{2\pi}{n}k}\right)\left(x - e^{-i\frac{2\pi}{n}k}\right)\right)$$

$$= \lim_{n \to +\infty} \frac{2\pi}{n} \ln\left(\prod_{k=0}^{n-1} \left(x - e^{i\frac{2\pi}{n}k}\right) \prod_{k=0}^{n-1} \left(x - e^{-i\frac{2\pi}{n}k}\right)\right)$$

$$= \lim_{n \to +\infty} \frac{2\pi}{n} \ln\big((x^n - 1)(x^n - 1)\big)$$

[encadré : Conclusion — $J(x) = 0$ si $|x| \leq 1$, $4\pi\ln|x|$ si $|x| > 1$]

D'où $J(x) = \lim_{n \to +\infty} \frac{4\pi}{n}\ln|x^n - 1|$.

- Si $|x| < 1$, $J(x) = \lim_{n \to +\infty} \frac{4\pi}{n}\ln(1 - x^n) = 0$.
- Si $|x| > 1$, $J(x) = \lim_{n \to +\infty} \frac{4\pi}{n}\big(n\ln|x| + \ln|1 - x^{-n}|\big) = 4\pi\ln|x| + \lim_{n \to +\infty} \frac{4\pi\ln|1 - x^{-n}|}{-x^n} \times \frac{-x^n}{n}$ [raturé en marge] $= 4\pi\ln|x| + 4\pi \times 1 \times 0$.

---

## Figures

Aucune figure à reproduire : p. 1 (unique) vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q14-riemann-1.png`, r150) — texte + équations, encadré « Conclusion » et rature marginale confirmés, aucune figure. Aucun script `reproduce_sommes-riemann_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- `J(x) = ∫₀^{2π} ln|x²−2x·cos t+2| dt` ; racines de l'unité (`xⁿ−1`) ; sommes de Riemann (`2π/n·Σ`, une ligne).
- Titre générique vs contenu unique `J(x)` (voir rapport : nom partiellement trompeur, sans agir).
