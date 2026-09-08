# Intégrale sinusoïdale $\int_0^{\pi/2}\frac{\cos x - \sin x\cos x}{1+\sin x}\,dx$ — transcription fidèle

> 🧾 **Manuscrit original :** `integrale-sinusoidale.pdf` (scan, 3 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à ~85 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`integrale-sinusoidale.pdf`](integrale-sinusoidale.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

$$I = \int_0^{\pi/2} \frac{\cos x - \sin x\cos x}{1+\sin x}\,dx$$

$$= \int_0^{\pi/2} \frac{\cos x}{1+\sin x}\,dx - \int_0^{\pi/2} \frac{\sin x\cos x\,(1-\sin x)}{(1+\sin x)(1-\sin x)}\,dx$$

$$= \big[\ln|1+\sin x|\big]_0^{\pi/2} - \int_0^{\pi/2} \frac{\sin x\cos x\,(1-\sin x)}{1-\sin^2 x}\,dx$$

$$= \ln 2 - \int_0^{\pi/2} \frac{\sin x - \sin x \cdot [\cdots]}{\cos x}\,dx \text{ [second terme du numérateur peu lisible]}$$

$$= \ln 2 + \int_0^{\pi/2} \frac{-\sin x}{\cos x}\,dx + \int_0^{\pi/2} \frac{(1-\cos^2 x)}{\cos x}\,dx$$

$$= \ln 2 + \big[\ln|\cos x|\big]_0^{\pi/2} - \int_0^{\pi/2} \cos x\,dx + \int_0^{\pi/2} \frac{1}{\cos x} \cdot \frac{\cos x}{\cos x}\,dx \text{ [lecture incertaine sur la décomposition]}$$

$$= \ln 2 + \lim_{x \to \pi/2} \ln|\cos x| - \big[\sin x\big]_0^{\pi/2} + \int_0^{\pi/2} \frac{\cos x}{(1-\sin x)(1+\sin x)}\,dx$$

$$= \ln 2 - 1 + \lim_{x \to \pi/2} \ln|\cos x| + \frac{1}{2}\int_0^{\pi/2} \frac{\cos x}{1-\sin x} + \frac{\cos x}{1+\sin x}\,dx$$

$$= \ln 2 - 1 + \lim_{x \to \pi/2} \ln|\cos x| + \frac{1}{2}\big[-\ln|1-\sin x| + \ln|1+\sin x|\big]_0^{\pi/2}$$

[raturé : $= \ln 2 - 1 + \lim_{x \to \pi/2} \ln|\cos x| + \frac{1}{2}\left[\ln\left|\frac{1+\sin x}{1-\sin x}\right|\right]_0^{\pi/2}$]

$$= \ln 2 - 1 + \lim_{x \to \pi/2} \frac{\ln|\cos x| - \ln|1-\sin x|}{2} + \frac{1}{2}(\ln 2)$$

$$= \frac{3}{2}\ln 2 - 1 + \lim_{x \to \pi/2} \ln\left|\frac{\cos x}{\sqrt{1-\sin x}}\right|$$

[raturé : $+ \lim_{x \to 0} \ln|\cdots|$ — ligne biffée en bas de page.]

## Page 2

$$l = \lim_{y \to 0} \ln\left|\frac{\cos(y+\pi/2)}{\sqrt{1-\sin(y+\pi/2)}}\right| \text{ [lecture incertaine sur le changement de variable]}$$

$$l_1 = \lim_{x \to \pi/2} \frac{\cos x}{\sqrt{1-\sin x}} = \lim_{x \to \pi/2} \sqrt{\cos^2 x \times \frac{1+\sin x}{(1-\sin x)(1+\sin x)}}$$

[grande croix biffant le calcul intermédiaire] $= \lim \sqrt{1+\sin x} = \sqrt{2}$

$$l_2 = \lim_{x \to \pi/2^+} \text{ [inachevé]}$$

$$I = \frac{3}{2}\ln 2 - 1 + \lim_{x \to \pi/2} \ln\frac{|\cos x|}{\sqrt{1-\sin x}} + \lim_{x \to \pi/2} \ln\sqrt{\frac{\cos^2 x}{1-\sin x} \times \frac{1+\sin x}{1+\sin x}} + \lim_{x \to \pi/2} \ln\sqrt{1+\sin x}$$

$$I = \frac{3}{2}\ln 2 - 1 + \ln\sqrt{2} = 2\ln 2 - 1$$

## Page 3

[Second calcul, plus direct. En marge droite, texte fantôme d'une autre page, non transcrit.]

$$I = \int_0^{\pi/2} \frac{\cos x - \sin x\cos x}{1+\sin x}\,dx$$

$$= \int_0^{\pi/2} \frac{\cos x\,(1-\sin x)}{1+\sin x}\,dx$$

$$= \int_0^{\pi/2} \cos x\left(-1 + \frac{2}{1+\sin x}\right)dx$$

$$= \int_0^{\pi/2} \left(-\cos x + \frac{2\cos x}{1+\sin x}\right)dx$$

$$= \big[-\sin x + 2\ln|1+\sin x|\big]_0^{\pi/2}$$

$$I = -1 + 2\ln 2 = \ln\left(\frac{4}{e}\right)$$

Déduction $J = \int_0^{\pi/2} \frac{\sin x\cos x}{1+\sin x}\,dx = \int_0^{\pi/2} \frac{\cos x\,(1+\sin x) + \cos x}{1+\sin x}\,dx$ [lecture incertaine sur le signe — probablement $-\cos x$]

$$= \text{[raturé]} -I + \big[\ln|1+\sin x|\big]_0^{\pi/2}$$

$$= 1 - 2\ln 2 + \ln 2$$

$$= 1 - \ln 2$$

$$= \ln\left(\frac{e}{2}\right)$$

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q11-sinus-1.png`, r150) — texte + équations, rature de bas de page confirmée, aucune figure ; pp. 2–3 revérifiées visuellement au second passage le 2026-09-07 (rendus `/tmp/s8/sinus-2.png` et `/tmp/s8/sinus-3.png`, r150) — texte + équations uniquement, aucune figure ; texte fantôme en marge p. 3 exclu. Aucun script `reproduce_integrale-sinusoidale_N.py`, aucun PNG (aucun `assets/` créé, vérifié `uv run`).

---

## Vocabulaire

- `l, l₁, l₂` = limites intermédiaires en `x → π/2` ; `ln` = logarithme ; second calcul p. 3 = voie directe (`−cos x + 2cos x/(1+sin x)`).
- `J` = intégrale déduite `∫₀^{π/2} sin x·cos x/(1+sin x) dx = 1 − ln 2`.
