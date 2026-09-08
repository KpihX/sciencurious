# Somme de Bâle via Fourier — transcription fidèle

> 🧾 **Manuscrit original :** `somme-bale-fourier.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** calculs de coefficients de Fourier suivis ; une ligne d'arrivée (question 1/) en `[lecture incertaine — …]`, ratures et renvois biffés conservés. Transcrit mot à mot.
> 📄 **Source scannée :** [somme-bale-fourier.pdf](somme-bale-fourier.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Ex 2

1/ Travail [lecture incertaine — un mot, « Travail »].

2/ $\forall n \in \mathbb{N},\ A_n(F) = \frac{2}{\pi}\left(\int_0^\pi F(x)\sin(nx)\,dx\right)$ car $x \mapsto F(x)\sin(nx)$ est paire du fait que $F$ et $\sin$ sont impaires.

$$= \frac{2}{\pi}\left(\underbrace{\int_0^{\pi/2} x\sin nx\,dx}_{A} + \int_{\pi/2}^\pi (\pi - x)\sin nx\,dx\right)$$

$$= \frac{2}{\pi}\left(A + \int_0^{\pi/2} t\sin(n(\pi - t))\,dt\right) \text{ où } t = \pi - x$$

$$= \frac{2}{\pi}\left(A + \int_0^{\pi/2} t\left(\sin n\pi\cos nt - \cos n\pi\sin nt\right)dt\right)$$

[raturé : fins de mots sous « $\cos nt$ » et « $\sin nt$ »]

$$= \frac{2}{\pi}\left(A + \int_0^{\pi/2} t\left(0 - (-1)^n\sin nt\right)dt\right)$$

Donc $A_n(F) = \frac{2}{\pi}\left(1 - (-1)^n\right)\int_0^{\pi/2} x\sin nx\,dx$.

3/ $\forall n \in \mathbb{N},\ A_{2n}(F) = \frac{2}{\pi}(1 - 1)\int_0^{\pi/2} x\sin(2nx)\,dx = 0$ [biffé d'une grande croix, réécrit page 2].

4/ $\forall n \in \mathbb{N},\ A_{2n+1}(F) = $ … [biffé d'une grande croix, réécrit page 2].

## Page 2

3/ $\forall n \in \mathbb{N},\ A_{2n}(F) = \frac{2}{\pi}(1 - 1)\int_0^{\pi/2} x\sin(2nx)\,dx = 0$.

4/ $\forall n \in \mathbb{N},\ A_{2n+1}(F) = \frac{-8}{\pi(2n+1)}\int_0^{\pi/2} x\cos((2n+1)x)\,dx$

$$= \frac{-4}{\pi(2n+1)}\left(\left[x\sin((2n+1)x)\right]_0^{\pi/2} - \int_0^{\pi/2} \cos((2n+1)x)\,dx\right)$$

$$= \frac{-4}{\pi(2n+1)}\left(0 - 0 - \frac{1}{(2n+1)}\left[\sin((2n+1)x)\right]_0^{\pi/2}\right)$$

$$A_{2n+1}(F) = \frac{4}{\pi(2n+1)^2}\left((-1)^n - 0\right).$$

5/ a) $\forall x \in \mathbb{R},\ F(x) = \sum_{k=0}^{+\infty} \underbrace{A_{2k}(F)}_{0}\sin(2kx) + \sum_{k=0}^{+\infty} A_{2k+1}(F)\sin((2k+1)x)$

$$F(x) = \sum_{k=0}^{+\infty} \frac{4(-1)^k}{\pi(2k+1)^2}\sin((2k+1)x).$$

En vue de se débarrasser de $(-1)^n$ on va prendre $x = \pi/2$. Dans ce cas $F(\pi/2) =$ [raturé : un terme] $= \frac{4}{\pi}\sum_{k=0}^{+\infty} \frac{(-1)^k(-1)^k}{(2k+1)^2}$, d'où $\sum_{k=0}^{+\infty} \frac{1}{(2k+1)^2} = \frac{\pi^2}{8}$.

b) $\sum_{n=1}^{+\infty} \frac{1}{n^2} = \sum_{k=0}^{+\infty} \frac{1}{(2k+1)^2} + \sum_{k=1}^{+\infty} \frac{1}{(2k)^2} = \frac{\pi^2}{8} + \frac{1}{4}\sum_{k=1}^{+\infty} \frac{1}{k^2}$, d'où $\sum_{k=1}^{+\infty} \frac{1}{k^2} = \frac{\pi^2}{8(1 - 1/4)} = \frac{\pi^2}{6}$.

• $\sum_{n=1}^{+\infty} \frac{(-1)^{n-1}}{n^2} = \sum_{k=0}^{+\infty} \frac{(-1)^{2k+1-1}}{(2k+1)^2} + \sum_{k=1}^{+\infty} \frac{(-1)^{2k-1}}{(2k)^2} = \frac{\pi^2}{8} - \frac{1}{4}\sum_{k=1}^{+\infty} \frac{1}{k^2} = \frac{\pi^2}{8} - \frac{1}{4}\frac{\pi^2}{6} = \frac{\pi^2}{12}$.

## Figures

Aucune figure : 2 pages de calculs manuscrits (crayon) seuls, sans schéma ni graphe (transcription § Statut : questions 3/–4/ biffées d'une croix, réécrites p. 2 ; confirmé p. 1 sur source le 2026-09-07 — coefficients $A_n(F)$ — rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07 — rendu `/tmp/s11/`, 0 figure à reproduire). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- Ex 2 ; $F$ : fonction en dent de scie (impaire) ; $A_n(F)$ : coefficients de Fourier en sinus.
- $A$ : intégrale auxiliaire $\int_0^{\pi/2} x\sin nx\,dx$ ; $t = \pi - x$ : changement de variable.
- $\sum 1/(2k+1)^2 = \pi^2/8$, $\sum 1/n^2 = \pi^2/6$, $\sum (-1)^{n-1}/n^2 = \pi^2/12$ : résultats (soulignés).
