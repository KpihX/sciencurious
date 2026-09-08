# Intégrales fiche 2 — $\int_0^\pi e^{\sin x}dx$ (série entière, Wallis) — transcription fidèle

> 🧾 **Manuscrit original :** `integrales-fiche-2.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** partiellement lisible (~70 %), transcrit fidèlement. Développement $e^{\sin x} = \sum (\sin x)^k/k!$, récurrence de Wallis $J_k = (k-1)/k\, J_{k-2}$ séparée en cas pair/impair, formule finale en double série, puis trois pistes complémentaires (dont $\int (x\ln x)^k$ et le binôme complexe avec cas délicat $2j-k = 0$). Détails de factorielles empâtés au milieu (signalés) ; les formules « Donc » sont nettes.
> 📄 **Source scannée :** [`integrales-fiche-2.pdf`](integrales-fiche-2.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Série entière et récurrence de Wallis

$\boxed{I = \int_0^\pi e^{\sin x}\,dx = ?}$

$I = \int_0^\pi e^{\sin x}\,dx$. Car $\forall x \in \mathbb{R}$, $e^x = \sum_{k=0}^{+\infty} \frac{x^k}{k!}$

avec $\forall x \in \mathbb{R}$, $e^{\sin x} = \sum_{k=0}^{+\infty} \frac{(\sin x)^k}{k!}$

avec $I = \int_0^\pi \sum_{k=0}^{+\infty} \frac{(\sin x)^k}{k!}\,dx = \left(\sum_{k=2}^{+\infty} \frac{1}{k!}\int_0^\pi (\sin x)^k\,dx\right) + \int_0^\pi \frac{(\sin x)^0}{0!}\,dx + \int_0^\pi \frac{\sin x}{1!}\,dx$

$$= \sum_{k=2}^{+\infty} \frac{1}{k!}J_k + \pi + 2$$

$\forall k \in \mathbb{N}^*$, $J_k = -\left[\cos x\sin^{k-1}x\right]_0^\pi + \int_0^\pi (\cos x)(k-1)\cos x\sin^{k-2}x\,dx$ [le membre de gauche « $J_k =$ » est peu lisible]

$$= (k-1)\int_0^\pi (1-\sin^2x)\sin^{k-2}x\,dx$$

$$= (k-1)(J_{k-2} - J_k)$$

Donc $J_k = \frac{(k-1)}{k}J_{k-2}$

— Si $k = 2k'$ ($k' \in \mathbb{N}^*$), $J_{2k'} = \frac{2k'-1}{2k'}J_{2k'-2} = \frac{(2k'-1)(2k'-3)\times\cdots\times 3\times 1}{(2k')(2k'-2)\times\cdots\times 4\times 2}J_0$ [ligne médiane raturée et réécrite]

$= \frac{(2k'-1)!}{(2k')(2k'-2)\times\cdots\times 4\times 2}J_0$ [restitution — ligne empâtée]

$= \frac{\pi(2k'-1)!}{2^{k'}(2k'-2)\times\cdots\times 2}$ [ligne empâtée]

$= \frac{\pi(2k'-1)!}{2k'!\times(2^{k'-1}\times(k'-1)\times\cdots\times 1)}$ [ligne empâtée]

Donc $J_{2k'} = \frac{\pi(2k'-1)!}{k'!\,2^{2k'-1}[(k'-1)!]^2}$

— Si $k = 2k'+1$ ($k' \in \mathbb{N}^*$), $J_{2k'+1} = \frac{2k'}{2k'+1}J_{2k'-1}$

$= \frac{(2k')(2k'-2)\times\cdots\times 4\times 2}{(2k'+1)(2k'-1)\times\cdots\times 5\times 3} \times J_{2\times 1-1}$

$= \frac{(2k')(2k'-2)\times\cdots\times 4\times 2}{(2k'+1)!} \times \dots \times J_1$ [ligne empâtée]

$= \frac{(2^{k'} \times k'(k'-1)\times\cdots\times 2\times 1)^2}{(2k'+1)!} \times 2$

$= \frac{2^{2k'+1}(k'!)^2}{(2k'+1)!}$

## Page 2 — Formule finale et pistes complémentaires

avec $I = \sum_{k=2}^{+\infty} \frac{1}{k!}J_k + \pi + 2$

$= \pi+2 + \sum_{i=1}^{+\infty} \frac{1}{(2i)!}J_{2i} + \sum_{j=1}^{+\infty} \frac{1}{(2j+1)!}J_{2j+1}$

$= \pi+2 + \sum_{i=1}^{+\infty} \frac{1}{(2i)!} \times \frac{\pi(2i-1)!}{i!\,2^{2i-1}[(i-1)!]^2} + \sum_{j=1}^{+\infty} \frac{1}{(2j+1)!} \times \frac{2^{2j+1}(j!)^2}{(2j+1)!}$

$= \pi+2 + 2\pi\sum_{i=1}^{+\infty} \frac{1}{(2i)\times i!\times 2^{2i}\times i!\times\cdots} + \sum_{j=1}^{+\infty} \frac{2^{2j}2^{2j}(j!)^2}{((2j+1)!)^2}$ [ligne empâtée]

Donc $I = \int_0^\pi e^{\sin x}\,dx = \pi\left(1+\sum_{i=1}^{+\infty} \frac{1}{2^{2i}(i!)^2}\right) + 2\left[1+\sum_{j=1}^{+\infty} 2^{2j}\left[\frac{j!}{(2j+1)!}\right]^2\right]$ [restitution d'après les lignes précédentes — coefficients intermédiaires empâtés]

ou encore $I = \int_0^\pi e^{\sin x}\,dx = \pi\sum_{i=0}^{+\infty} \frac{1}{2^{2i}(i!)^2} + 2\sum_{j=0}^{+\infty} 2^{2j}\left[\frac{j!}{(2j+1)!}\right]^2$

ou encore $I = \int_0^\pi e^{\sin x}\,dx = \sum_{k=0}^{+\infty}\left[\frac{\pi}{2^{2k}(k!)^2} + 2^{2k+1}\left(\frac{k!}{(2k+1)!}\right)^2\right]$ [sommation des deux séries en une seule — ligne biffée d'un trait]

… $x^x = e^{\dots}$ alors $I_k = \int_a^b (x\ln x)^k\,dx$ [début raturé — amorce « $x^x$ » levée visuellement p.2 r150 2026-09-07 (`/tmp/s9/fiche2-2.png`)]

$= \frac{1}{k+1}\left|\left[x^{k+1}(\ln x)^k\right]_a^b - \int_a^b x^{k+1} \times k(\ln x)^{k-1} \times \frac{1}{x}\,dx\right|$ [ratures multiples]

$= \frac{1}{k+1}\left|A - k\int_a^b x^k(\ln x)^{k-1}\,dx\right|$ où $A = \left[x^{k+1}(\ln x)^k\right]_a^b$ [restitution d'après le contexte]

On pourrait poser $J_k(x) = \int^x x^{k}\dots\,dx$, $x \in \mathbb{R}$, $k \in \mathbb{N}$ et là on aurait $J_0(x) = x$, $J_1(x) = 1-\cos x$ et $\forall k \in \mathbb{N}^*$, $\forall \dots$, $J_k(x) = \frac{(k-1)}{k}J_{k-2}(x) + \frac{\dots}{k}\dots$ [très empâté — $J_0(x) = x$ levé visuellement p.2 r150 2026-09-07] et utiliser alors $J_k(\pi)$.

En écrivant $\sin x = \frac{e^{ix}-e^{-ix}}{2i}$ on pourrait encore remarquer que $I = \sum_{k=0}^{+\infty} \frac{1}{k!}J_k = \sum_{k=0}^{+\infty} \frac{1}{k!\,2^k i^k}\sum_{j=0}^k C_k^j(-1)^j \frac{\left(e^{i\pi(2j-k)}-1\right)}{i(2j-k)}$ et procéder au calcul délicat du cas où $2j-k = 0$

---

## 📝 Notes de transcription (fidélité)

- La récurrence $J_k = (k-1)/k\, J_{k-2}$ vient de l'IPP $u = \sin^{k-1}x$, $dv = \sin x\,dx$ ; $J_0 = \pi$, $J_1 = 2$.
- Les chaînes de factorielles du cas pair sont les plus abîmées (rature médiane) ; en revanche les formules finales « Donc $J_{2k'} = \dots$ » et « Donc $I = \dots$ » sont nettes et transcrites telles quelles.
- Page 2 : le calcul $\int_a^b (x\ln x)^k dx$ est une piste latérale inachevée (ratures), conservée comme telle.
- Aucune figure ni schéma sur les 2 pages.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q10-fiche2-1.png`, r150) — feuille pliée, formule encadrée `I = ∫₀^π e^{sin x}dx` en haut à droite confirmée, aucune figure ; p. 2 vérifiée visuellement le 2026-09-07 (rendu `/tmp/s9/fiche2-2.png`, r150, 2e passage) — triple formule `Donc / ou encore` (3e biffée d'un trait), piste `(x ln x)^k` raturée et binôme complexe (`2j−k = 0`) confirmés, aucune figure. Aucun script `reproduce_integrales-fiche-2_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- `J_k = ∫₀^π (sin x)^k dx`, `J₀ = π`, `J₁ = 2` ; récurrence de Wallis `J_k = (k−1)/k·J_{k−2}` (IPP).
- Cas délicat `2j−k = 0` (binôme complexe, p. 2) ; piste latérale `(x ln x)^k` inachevée.
