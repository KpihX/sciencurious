# Dérivation demi-ordre (racine carrée de la dérivation) — transcription fidèle

> 🧾 **Manuscrit original :** `derivation-demi-ordre.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible (~90 %), transcrit fidèlement. $T \circ T = D$ impossible sur $\mathbb{K} = \mathbb{R}$, possible sur $\mathbb{K} = \mathbb{C}$ (construction explicite). Quelques insertions interlignes et une ligne raturée en bas de page 1 (signalées).
> 📄 **Source scannée :** [`derivation-demi-ordre.pdf`](derivation-demi-ordre.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Cas $\mathbb{K} = \mathbb{R}$ : impossibilité

[en haut à gauche, encadré : « 2435 » — lecture incertaine, probablement une note]

\* Cas $\mathbb{K} = \mathbb{R}$ / Supp $\exists T \in \mathcal{L}(E)$ / $T \circ T = D$ [« Supp » lu tel quel, pour « Supposons »]

Remq : $\ker T \subset \ker D$ car $\forall f \in \ker T$,

$$D(f) = T(T(f)) = T(0_E) = 0_E$$

En désignant par $1_E : \mathbb{R} \to \mathbb{R}$ / $x \mapsto 1$. On a :

$$\ker D = \mathbb{R} \cdot \{1_E\} \implies \dim \ker D = 1$$

Or $\ker T \subset \ker D \implies \dim \ker T \in \{0, 1\}$

— Supp par l'absurde que $\dim \ker T = 0 \iff \ker T = \{0_E\}$

Soit $f \in \ker D$ [insertion interligne au-dessus : « $\times 0_E$ ? » — lecture incertaine]. On a : $D(f) = T(T(f))$

or $f \neq 0_E$ alors $T(f) \neq 0_E \implies D(f) = T(T(f)) \neq 0_E$

ainsi que $\ker T = \{0_E\}$ ; ce qui est absurde car $f \in \ker D$

Ainsi $\dim \ker T = 1$ d'où $\ker T = \ker D$

or $D = T \circ T$ d'où $\ker D = T^{-1}(\ker T) = T^{-1}(\ker D)$

[raturé : « Soit $f = \dots \in \ker D$ » — ligne entièrement biffée]

De plus $T^2(\ker D) = T^{-1}(T^2(\ker D)) = T^{-1}(\ker D) = \ker D$

[raturé : ligne biffée mentionnant une application $\mathbb{R} \to \mathbb{R}$ et « $T^{-1}(\ker D) = \mathbb{R} \cdot \{1_E\}$ » — lecture incertaine car raturé]

Donc $\forall T \in \mathcal{L}(E)$, $T \circ T \neq D$

## Page 2 — Cas $\mathbb{K} = \mathbb{C}$ : construction

\* Cas $\mathbb{K} = \mathbb{C}$

Remarquons que $\forall f \in E$, $\exists f_r, f_i \in \mathcal{C}^{\infty}(\mathbb{R}, \mathbb{R})$ / $f = f_r + i f_i$

Soit alors $f = f_r + i f_i \in E$. Posons $T(f) = f_i' + i f_r$ [l'indice du premier terme lu $i$ : $f_i'$]

On vérifie bien que $T$ est linéaire et que $T \circ T = D$

Vu que $\forall f = f_r + i f_i \in E$, $T(T(f)) = T(f_i' + i f_r) = f_r' + i f_i' = f' = D(f)$

[encadré en bas à gauche : « 24,54 » — lecture incertaine, probablement une note]

[bas de page coupé : début d'une ligne « En … » — suite sur une autre feuille, hors manuscrit]

---

## Figures

- Aucune figure sur les 2 pages (vérifié p. 1–2, document complet).

## Vocabulaire

dérivation $D$, demi-ordre $T\circ T=D$, $\ker$, $\dim$, $\mathcal{L}(E)$, $\mathcal{C}^{\infty}$, $1_E$/$0_E$, $Supp$ (= Supposons).

## 📝 Notes de transcription (fidélité)

- $E$ désigne implicitement l'espace des fonctions indéfiniment dérivables (contexte : $\mathcal{C}^{\infty}$), $D$ l'opérateur de dérivation, $0_E$ la fonction nulle, $1_E$ la fonction constante égale à $1$.
- Page 1 : l'argument « $f \neq 0_E \implies T(T(f)) \neq 0_E$ » utilise $\ker T = \{0_E\}$ (injectivité de $T$ sur les deux applications successives) ; le manuscrit écrit « ainsi que $\ker T = \{0_E\}$ » là où on attendrait « or $T(f) \notin \ker T$ » — conservé tel quel, sans correction.
- Aucune figure ni schéma sur les 2 pages.
