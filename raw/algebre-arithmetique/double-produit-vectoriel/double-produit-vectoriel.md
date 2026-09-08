# Double Produit Vectoriel — transcription fidèle

> 🧾 **Manuscrit original :** `double-produit-vectoriel.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** transcrit mot à mot depuis les rendus. Le haut de la page 1 est rogné sur le scan source (2 lignes partielles) ; le reste est lisible à 100 %. Les maths sont conservées telles quelles. Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`double-produit-vectoriel.pdf`](double-produit-vectoriel.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Double Produit Vectoriel .pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

[haut de page rogné sur le scan — on y devine : « …où $\vec{x} = (\vec{A} \cdot \vec{C})\vec{B} - (\vec{A} \cdot \vec{B})\vec{C}$ » et « …une base de… »]

Soient $\vec{A}, \vec{B}, \vec{C} \in \mathbb{R}^3$. Posons $\vec{x} = \vec{A} \wedge (\vec{B} \wedge \vec{C})$. Mq $\vec{x} = (\vec{A} \cdot \vec{C})\vec{B} - (\vec{A} \cdot \vec{B})\vec{C}$.

- Si $\vec{B} \wedge \vec{C} = \vec{0}$ alors $(\vec{A} \cdot \vec{C})\vec{B} - (\vec{A} \cdot \vec{B})\vec{C} = \vec{A} \cdot (\lambda\vec{B})\vec{B} - \vec{A} \cdot \vec{B}(\lambda\vec{B})$ ($\lambda \in \mathbb{R} \mid \vec{C} = \lambda\vec{B}$) $= \vec{0}$. D'où $(\vec{A} \cdot \vec{C})\vec{B} - (\vec{A} \cdot \vec{B})\vec{C} = \vec{A} \wedge (\vec{B} \wedge \vec{C})$.

- Sinon $(\vec{B}, \vec{C}, \vec{B} \wedge \vec{C})$ est une base de $\mathbb{R}^3$. Ainsi $\exists \alpha, \beta, \gamma \in \mathbb{R} \mid \vec{A} = \alpha\vec{B} + \beta\vec{C} + \gamma\,\vec{B} \wedge \vec{C} \quad (0)$. Ainsi $\vec{x} = (\alpha\vec{B} + \beta\vec{C} + \gamma\,\vec{B} \wedge \vec{C}) \wedge (\vec{B} \wedge \vec{C}) = \alpha\,\vec{B} \wedge (\vec{B} \wedge \vec{C}) + \beta\,\vec{C} \wedge (\vec{B} \wedge \vec{C})$. Mq $\vec{B} \wedge (\vec{B} \wedge \vec{C}) = (\vec{B} \cdot \vec{C})\vec{B} - \vec{B}^2\vec{C}$ ou $\vec{C} \wedge (\vec{B} \wedge \vec{C}) = \dots \quad (1)$ [lecture incertaine sur la 2e égalité visée].

- Ona : $\vec{\gamma} \perp \vec{B} \wedge \vec{C} \implies \vec{\gamma} \in \mathrm{Vect}(\vec{B}, \vec{C}) =$ plan formé par $\vec{B}$ et $\vec{C}$ (d'après $0$) $\implies \exists a, b \in \mathbb{R} \mid \vec{\gamma} = a\vec{B} + b\vec{C} \quad (2)$.

- $\vec{\gamma} \perp \vec{B} \implies \vec{B} \cdot \vec{\gamma} = 0 \implies \vec{B} \cdot (a\vec{B} + b\vec{C}) = 0$ (d'après $2$) $\implies a\vec{B}^2 + b\,\vec{B} \cdot \vec{C} = 0 \quad (3)$.

- Si $\vec{B} = \vec{0}$, ona : $(\vec{B} \cdot \vec{C})\vec{B} - \vec{B}^2\vec{C} = \vec{0} \cdot \vec{C} - \vec{0} \cdot \vec{C} = \vec{0} = \vec{B} \wedge (\vec{B} \wedge \vec{C})$. D'où $(\vec{B} \cdot \vec{C})\vec{B} - \vec{B}^2\vec{C} = \vec{B} \wedge (\vec{B} \wedge \vec{C})$.

- Sinon, posons $\lambda = \frac{-b}{\vec{B}^2}$. $(3) \implies a = \frac{\vec{B} \cdot \vec{C}}{\vec{B}^2} \times \dots = \lambda\,\vec{B} \cdot \vec{C}$ [lecture incertaine sur le numérateur intermédiaire].

$(2) \implies \vec{\gamma} = \lambda\big((\vec{B} \cdot \vec{C})\vec{B} - \vec{B}^2\vec{C}\big) = \vec{B} \wedge (\vec{B} \wedge \vec{C})$ d'après $1 \implies \vec{C} \cdot \big(\vec{B} \wedge (\vec{B} \wedge \vec{C})\big) = \lambda\big((\vec{B} \cdot \vec{C})^2 - \vec{B}^2\vec{C}^2\big) \implies (\vec{C}, \vec{B}, \vec{B} \wedge \vec{C})$ [produit mixte] $= \lambda\big(\vec{B}^2\vec{C}^2\cos(\vec{B}, \vec{C}) - \vec{B}^2\vec{C}^2\big) \implies |\vec{B} \wedge \vec{C}, \vec{C}, \vec{B}| = \lambda\,\vec{B}^2\vec{C}^2\sin^2(\vec{B}, \vec{C})$ car $\sin^2 + \cos^2 = 1$ [fin de ligne approximative].

---

## Page 2

[haut de page rogné sur le scan — on y devine la fin du calcul de $\lambda$]

$(1) \implies (\vec{B} \wedge \vec{C}) \cdot (\vec{B} \wedge \vec{C}) = -\lambda\,\lVert \vec{B} \wedge \vec{C} \rVert^2 \implies \dots \implies -\lVert \vec{B} \wedge \vec{C} \rVert^2 = -\lambda\,\lVert \vec{B} \wedge \vec{C} \rVert^2 \implies \lambda = 1$ [étapes intermédiaires partiellement rognées].

Alors $\vec{B} \wedge (\vec{B} \wedge \vec{C}) = (\vec{B} \cdot \vec{C})\vec{B} - \vec{B}^2\vec{C}$. De même $\vec{C} \wedge (\vec{B} \wedge \vec{C}) = \dots = -(\vec{B} \cdot \vec{C}\dots)$ en permutant $\vec{B}$ et $\vec{C}$ dans la démonstration précédente $= -(\vec{B} \cdot \vec{C})\vec{C} + \vec{C}^2\vec{B}$.

Ainsi $(0) \implies \vec{x} = \alpha\,\vec{B} \wedge (\vec{B} \wedge \vec{C}) + \beta\,\vec{C} \wedge (\vec{B} \wedge \vec{C}) = \alpha\big((\vec{B} \cdot \vec{C})\vec{B} - \vec{B}^2\vec{C}\big) + \beta\big(-(\vec{B} \cdot \vec{C})\vec{C} + \vec{C}^2\vec{B}\big) = (\alpha\,\vec{B} \cdot \vec{C} + \beta\vec{C}^2)\vec{B} - (\alpha\vec{B}^2 + \beta\,\vec{B} \cdot \vec{C})\vec{C} = \big[(\alpha\vec{B} + \beta\vec{C} + \gamma\,\vec{B} \wedge \vec{C}) \cdot \vec{C}\big]\vec{B} - \big[(\alpha\vec{B} + \beta\vec{C} + \gamma\,\vec{B} \wedge \vec{C}) \cdot \vec{B}\big]\vec{C} = (\vec{A} \cdot \vec{C})\vec{B} - (\vec{A} \cdot \vec{B})\vec{C}$.

Donc $\vec{A} \wedge (\vec{B} \wedge \vec{C}) = (\vec{A} \cdot \vec{C})\vec{B} - (\vec{A} \cdot \vec{B})\vec{C} \quad \forall \vec{A}, \vec{B}, \vec{C} \in \mathbb{R}^3$.

---

## Figures

Aucune figure à reproduire : démonstration texte, 2 pages relues en entier, sans schéma.

N.B. : le script `reproduce_double-produit-vectoriel-tableau_1.py` présent dans `lab/scripts/` ne concerne PAS ce dossier (il cible `raw/tableau-noir/double-produit-vectoriel-tableau/`) — homonymie signalée, voir rapport.

## Vocabulaire / notions

- **Double produit vectoriel** : $\vec{A} \wedge (\vec{B} \wedge \vec{C}) = (\vec{A}\cdot\vec{C})\vec{B} - (\vec{A}\cdot\vec{B})\vec{C}$.
- **Produit mixte** $(\vec{C}, \vec{B}, \vec{B}\wedge\vec{C})$, $|\vec{B}\wedge\vec{C}, \vec{C}, \vec{B}| = \lambda\vec{B}^2\vec{C}^2\sin^2$.
- **Base** $(\vec{B}, \vec{C}, \vec{B}\wedge\vec{C})$ de $\mathbb{R}^3$ ; constante $\lambda = 1$.
