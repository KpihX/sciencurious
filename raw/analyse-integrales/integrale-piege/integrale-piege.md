# Une intégrale avec piège — transcription fidèle

> 🧾 **Manuscrit original :** `integrale-piege.pdf` (scan, 1 page) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`integrale-piege.pdf`](integrale-piege.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Une intégrale avec piège .pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

Explicitons $F(x) = \int \underbrace{\sqrt{\frac{1 + \sqrt{1 + x^2}}{1 + x^2}}}_{f(x)} dx$ sur $I = {]-1}, 1[$.

Car $f$ continue sur ${]-1}, 1[$, $F$ existe à une constante près. Soit $x \in I$.

- Si $x \in {]0}, 1[ \cap I$, posons $t = \sqrt{1 + x^2} \iff x = \sqrt{1 + t^2} = \varphi(t)$ [lecture incertaine sur la réciproque exacte]. Car $f$ continue sur ${]0}, 1[$ et $\varphi$ est bijective de ${]0}, 1[ \to {]0}, 1[$ et de classe $C_1$ sur ${]0}, 1[$ alors

$$F(x) = \int \frac{\sqrt{1 + t}}{t} \times \frac{-2t\,dt}{\sqrt{1 + t^2}} = -2 \int \frac{1}{\sqrt{1 + t}}\,dt$$

$$= 4\sqrt{1 + t} + c \quad \text{[flèche : pour un certain } c \in \mathbb{R} \text{]}$$

$$F(x) = 4\sqrt{1 - \sqrt{1 + x^2}} + c$$

- Si $x \in {]-1}, 0[$, car $f$ paire, $F(x) = -\int \sqrt{\frac{1 + \sqrt{1 + (-x)^2}}{1 + (-x)^2}}\,d(-x) = -F(-x)$ où $-x \in {]0}, 1[$.

D'où de façon générale à une cte $c$ près $\in \mathbb{R}$ :

$$F(x) = \begin{cases} c & \text{si } x = 0 \\ \dfrac{4|x|}{x}\sqrt{1 - \sqrt{1 + x^2}} & \text{si } x \in {]-1}, 1[ \setminus \{0\} \end{cases}$$

---

## Figures

Aucune figure à reproduire : p. 1 (unique) vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q06-piege-1.png`, r150) — texte + équations, ratures/surcharges confirmées, aucune figure. Aucun script `reproduce_integrale-piege_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- `φ` = changement de variable (bijection `C₁`) ; `f` paire ⇒ `F` impaire (à une constante près) ; `cte` = constante.
- Le « piège » du titre n'est pas explicité dans la page (voir rapport : nom à justifier).
