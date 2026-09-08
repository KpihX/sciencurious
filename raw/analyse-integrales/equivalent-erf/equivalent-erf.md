# Équivalent de Erf au voisinage de l'infini — transcription fidèle

> 🧾 **Manuscrit original :** `equivalent-erf.pdf` (scan, 1 page) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`equivalent-erf.pdf`](equivalent-erf.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Équivalent de Erf au voisinage de l_infini .pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

### Théo : soit $x \in \mathbb{R}$.\quad $\int_x^{+\infty} e^{-t^2} dt \underset{x \to +\infty}{\sim} \frac{e^{-x^2}}{2x}$

En effet, soit $t \in \mathbb{R}_+^*$.

$$\left(\frac{e^{-t^2}}{2t}\right)' = -e^{-t^2} - \frac{1}{2t^2}e^{-t^2} = -e^{-t^2}\left(1 + \frac{1}{2t^2}\right)$$

Posons $f(t) = e^{-t^2}\left(1 + \frac{1}{2t^2}\right) \underset{t \to +\infty}{\sim} e^{-t^2}$. Soit $x \in \mathbb{R}_+^*$.

Comme $\int_x^{+\infty} e^{-t^2} dt$ et $\int_x^{+\infty} f(t) dt = \frac{e^{-x^2}}{2x}$ sont 2 IIS en $+\infty$ de fonctions positives et que $f(t) \underset{t \to +\infty}{\sim} e^{-t^2}$, alors $\int_x^{+\infty} e^{-t^2} dt \underset{x \to +\infty}{\sim} \int_x^{+\infty} f(t) dt = \frac{e^{-x^2}}{2x}$. CQFD.

---

## Figures

Aucune figure à reproduire : p. 1 (unique) vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q02-erf-1.png`, r150) — texte + équations, aucune figure. Aucun script `reproduce_equivalent-erf_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- `IIS` = intégrale impropre (singulier/pluriel tel quel) ; `∼` = équivalent ; `CQFD` = ce qu'il fallait démontrer.
- `Théo` = théorème ; queue gaussienne `∫ₓ^∞ e^(−t²)dt` (le titre parle d'« Erf », voir rapport : nom approximatif).
