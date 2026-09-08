# Une meilleure démonstration du triple produit vectoriel — transcription fidèle

> 🧾 **Manuscrit original :** `triple-produit-vectoriel.pdf` (scan, 1 page) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`triple-produit-vectoriel.pdf`](triple-produit-vectoriel.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Une meilleure démonstration du triple produit vectoriel .pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

Soient $\vec{u}, \vec{v}, \vec{w} \in \mathbb{R}^3$. Mq $\vec{u} \wedge (\vec{v} \wedge \vec{w}) = (\vec{u} \cdot \vec{w})\vec{v} - (\vec{u} \cdot \vec{v})\vec{w}$.

- Si $\vec{v} \wedge \vec{w} = \vec{0}$ alors $\vec{u} \wedge (\vec{v} \wedge \vec{w}) = \vec{0}$. De plus $\exists k \in \mathbb{R} \mid \vec{w} = k\vec{v}$, d'où $(\vec{u} \cdot \vec{w})\vec{v} - (\vec{u} \cdot \vec{v})\vec{w} = k(\vec{u} \cdot \vec{v})\vec{v} - k(\vec{u} \cdot \vec{v})\vec{v} = \vec{0} = \vec{u} \wedge (\vec{v} \wedge \vec{w})$.

- Sinon, posons $\vec{w}' = \vec{w} - \frac{\vec{w} \cdot \vec{v}}{\lVert \vec{v} \rVert^2}\vec{v}$ et $\vec{z} = \vec{v} \wedge \vec{w}'$.

Or $\vec{v} \wedge \vec{w} \neq \vec{0}$, $\vec{w}' \neq \vec{0}$ et on vérifie que $\vec{v} \cdot \vec{w}' = \vec{0}$, ainsi $(\vec{v}, \vec{w}', \vec{z})$ est une base orthogonale directe.

$\exists! (\alpha, \beta, \gamma) \in \mathbb{R}^3 \mid \vec{u} = \alpha\vec{v} + \beta\vec{w}' + \gamma\vec{z}$.

D'où $\vec{u} \wedge (\vec{v} \wedge \vec{w}) = \vec{u} \wedge (\vec{v} \wedge (\vec{w}' + \frac{\vec{w} \cdot \vec{v}}{\lVert \vec{v} \rVert^2}\vec{v})) = \vec{u} \wedge \vec{z}$

$$= \alpha\vec{v} \wedge \vec{z} + \beta\vec{w}' \wedge \vec{z}$$

$$= \alpha\lVert \vec{v} \rVert\lVert \vec{z} \rVert\left(-\frac{\vec{w}'}{\lVert \vec{w}' \rVert}\right) + \beta\lVert \vec{w}' \rVert\lVert \vec{z} \rVert \times \frac{\vec{v}}{\lVert \vec{v} \rVert}$$

[encadré : or $\lVert \vec{z} \rVert = \lVert \vec{v} \rVert\lVert \vec{w}' \rVert$ car $\vec{v} \perp \vec{w}'$]

$$= -\alpha\lVert \vec{v} \rVert^2\left(\vec{w} - \frac{\vec{w} \cdot \vec{v}}{\lVert \vec{v} \rVert^2}\vec{v}\right) + \beta\lVert \vec{w}' \rVert^2\vec{v}\ \text{[+ membre raturé illisible]}$$

$$= -\alpha\lVert \vec{v} \rVert^2\vec{w} + \alpha(\vec{w} \cdot \vec{v})\vec{v} + \beta\lVert \vec{w}' \rVert^2\vec{v}\ \text{[raturé : recombinaison intermédiaire biffée]}$$

D'où $\vec{u} \wedge (\vec{v} \wedge \vec{w}) = -\alpha\lVert \vec{v} \rVert^2\vec{w} + \vec{v}(\alpha\,\vec{w} \cdot \vec{v} + \lVert \vec{w}' \rVert^2\beta)$.

Or $\vec{v} \cdot \vec{u} = \vec{v} \cdot (\alpha\vec{v} + \beta\vec{w}' + \gamma\vec{z}) = \alpha\lVert \vec{v} \rVert^2$ et $\vec{w} \cdot \vec{u} = \left(\vec{w}' + \frac{\vec{w} \cdot \vec{v}}{\lVert \vec{v} \rVert^2}\vec{v}\right) \cdot (\alpha\vec{v} + \beta\vec{w}' + \gamma\vec{z}) = \beta\lVert \vec{w}' \rVert^2 + \alpha(\vec{w} \cdot \vec{v})$.

Donc $\vec{u} \wedge (\vec{v} \wedge \vec{w}) = -(\vec{v} \cdot \vec{u})\vec{w} + \vec{v}(\vec{w} \cdot \vec{u})$.

En conclusion, $\forall \vec{u}, \vec{v}, \vec{w} \in \mathbb{R}^3,\ \vec{u} \wedge (\vec{v} \wedge \vec{w}) = (\vec{u} \cdot \vec{w})\vec{v} - (\vec{u} \cdot \vec{v})\vec{w}$.

---

## Figures

Aucune figure à reproduire : page unique vérifiée (équations à l'encre noire, encadré de norme, deux zones raturées ; aucun schéma vectoriel). Aucun script `reproduce_triple_produit_vectoriel_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $\wedge$ = produit vectoriel ; $\cdot$ = produit scalaire ; $\lVert\cdot\rVert$ = norme euclidienne.
- $\vec{w}'$ = composante de $\vec{w}$ orthogonale à $\vec{v}$ ; $\vec{z} = \vec{v} \wedge \vec{w}'$.
- $Mq$ = montrons que (orthographié « Mq » dès l'énoncé).
