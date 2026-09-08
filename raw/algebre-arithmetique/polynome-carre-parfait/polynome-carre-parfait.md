# n tel que p(n) carré parfait — transcription fidèle

> 🧾 **Manuscrit original :** `polynome-carre-parfait.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** transcrit mot à mot depuis les rendus (zoom ×200 sur la ligne $Q(n)$ ambiguë). Le haut de la page 1 est la fin d'un exemple précédent. Les maths sont conservées telles quelles, incohérences apparentes signalées sans correction.
> 📄 **Source scannée :** [`polynome-carre-parfait.pdf`](polynome-carre-parfait.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/n tel que p(n) carré parfait .pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

[haut de page : fin d'un exemple précédent — « Donc $an^2+bn+b$, $P(n) \leq Q(n) \implies \begin{cases} 2a = 6 \\ a+2b = 11 \\ \vdots \end{cases}$, on peut prendre $a = 3$ et $b = 1$ [*sic* — $b$ ressemble à $4$], ainsi $P(n) = (n^2+3n+1)^2+30$ »]

Cherchons $n \in \mathbb{N} \mid n^4+6n^3+11n^2+3n+31 = P(n)$ soit un carré parfait. Cherchons à encadrer $P(n)$ par 2 carrés successifs de la forme $(n^2+an+b)^2 < P(n) < (n^2+an+b')^2$ en vue d'avoir [membre biffé d'un trait horizontal : « nécessairement $P(n) = (n^2+an+b+1)$ », lu tel quel] $(a, b \in \mathbb{Z})$, $b' > b+1$.

Ona : $P(n) - (n^2+an+b)^2 = (6-2a)n^3 + (11-a^2-2b)n^2 + (3-2ab)n + 31-b^2$. On va prendre $a \mid 6-2a = 0$ c-à-d $a = 3$ en vue de simplifier l'étude.

$P(n) - (n^2+3n+b)^2 = 2(1-b)n^2 + 3(1-2b)n + 31-b^2 =: Q(n)$ [le $n$ du terme médian est peu visible — restitué par le calcul].

On veut avoir $Q(n)$ de signe constant. Pour cela il suffit d'avoir $\Delta < 0$ c-à-d $9(1-2b)^2 - 8(1-b)(31-b^2) \leq 0$ et ainsi $Q(n)$ aura le signe de $2(1-b)$. Puisqu'on veut $Q(n) > 0$ il faut $2(1-b) > 0$. En testant le cas simple $b = 0$, on a bien $\Delta = 81-8 \times 31 < 0$. Et ainsi $P(n) > (n^2+3n)^2$.

Pour $Q(n) := P(n) - (n^2+3n+1)^2 = 2-2n^2+3n+27$ [glyphes lus tels quels au zoom — « $3n$ » peut être « $3b$ » ; cette expression ne coïncide pas avec le calcul direct $-3n+30$, incohérence signalée sans correction], on a $Q(n) < 0$ pour $n \geq 3$ ou $n \leq -7$. Ainsi [suite p. 2].

---

## Page 2

- Pour $n \geq 3$ ou $n \leq -7$ [« $n \geq 3$ » ressemble à « $n \geq 11$ » — lecture incertaine ; borne sup. partiellement rognée], $(n^2+3n)^2 < \underbrace{n^4+6n^3+11n^2+3n+31}_{P(n)} < (n^2+3n+1\dots)^2$ [membre de droite rogné].

Ainsi $P(n)$ est un carré parfait ssi $P(n) = (n^2+3n+1)^2$, c-à-d $n^4+6n^3+11n^2+3n+31 = n^4+6n^3+11n^2+6n+1$, c-à-d $n = 10$.

- Pour $n \in \{-6, -5, -4, -3, -2, -1, 0, 1, 2\}$, on vérifie que $P(n)$ n'est pas un carré parfait.

Donc $n^4+6n^3+11n^2+3n+31$ carré parfait ssi $n = 10$.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée (texte + équations, encadrement par carrés successifs, aucune courbe) ; p. 2 = disjonction de cas textuelle. Aucun script `reproduce_polynome_carre_parfait_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $P(n) = n^4+6n^3+11n^2+3n+31$, $Q(n)$ = différence à un carré candidat ; $Ona$ = on a.
- $\Delta$ = discriminant ; $ssi$ = si et seulement si ; « carré parfait » = carré d'entier.
