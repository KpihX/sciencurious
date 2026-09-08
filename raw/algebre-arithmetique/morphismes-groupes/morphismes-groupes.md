# Morphismes de groupes (Lagrange, sous-groupes distingués, noyau-image) — transcription fidèle

> 🧾 **Manuscrit original :** `morphismes-groupes.pdf` (scan, 4 pages, encre bleue sur papier ligné) · ✍️ KpihX
> 🔍 **Statut :** lisible (~80 %), transcrit fidèlement. Page 1 : preuve du théorème de Lagrange. Page 2 : équivalence des caractérisations d'un sous-groupe distingué (bords rognés, passages empâtés signalés). Pages 3–4 : cardinal du groupe source via noyau et image, puis corollaire d'injectivité.
> 📄 **Source scannée :** [`morphismes-groupes.pdf`](morphismes-groupes.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Théorème de Lagrange

Théo de Lagrange : Soit $(G, \cdot)$ un groupe / $|G| \in \mathbb{N}^*$ et $H \le G$. Mq $|G| = |H||G/H|$

Car $G/H$ est un système de partitions de $G$ alors $|G| = \sum_{F \in G/H} |F|$

Or $\forall F \in G/H$, $\exists x \in G$ / $F = xH = \{xh, h \in H\}$

Considérons $\varphi : H \to F$ / $h \mapsto xh$. $\varphi$ est bien surjective. De plus $\varphi$ est injective car $\forall h_1, h_2 \in H$, $\varphi(h_1) = \varphi(h_2) \Rightarrow xh_1 = xh_2 \Rightarrow h_1 = h_2$

Donc $\varphi$ bijective. Par conséquent $|F| = |H|$

Ainsi $|G| = \sum_{F \in G/H} |H| = |G/H||H|$

---

## Page 2 — Caractérisations d'un sous-groupe distingué

[haut de page : trace d'une autre feuille, illisible — « …(En)… » ; bord gauche rogné]

[…] Il y a équivalence entre (Pour $(G, \cdot)$ un groupe et $H \le G$) :

1. $H \triangleleft G$
2. $\forall g \in G,\ gH = Hg$
3. $(G/H)$ gauche admissible [lecture incertaine — fin de ligne empâtée]
4. $(G/H)$ droite admissible [lecture incertaine — fin de ligne empâtée]

Schéma de démonstration : triangle ③ en haut, ① ⟹ ② au milieu, ④ en bas, avec flèches ② vers ③, ③ vers ①, ① vers ②, ② vers ④ et ④ vers ①.

①⟹② / Soit $g \in G$. Ona : $gH = (gHg^{-1})g \subseteq Hg$ et de même [passage empâté — symétrique en $g^{-1}$] $\subseteq gH$ d'où $gH = Hg$

②⟹③ / Soit $x, y, u, v \in G$ / $[x]_g = [y]_g$ et $[u]_g = [v]_g$ [lecture incertaine — l'indice $g$ (gauche) est empâté]. Mq $[xu]_g = [yv]_g$. Ona : $(xu)H = x(uH) = x(vH)$ [car $uH = vH$] et $(xv)H$ [puis] $= x(Hv) = (xH)v = (yH)v = yvH$ [lecture incertaine — lettres $u$/$v$/$x$ empâtées ; usage de ② : $vH = Hv$ et $xH = yH$]

- on demontre de même ②⟹④

③⟹① / Soit $y \in G$, $h \in H$. Mq $yhy^{-1} \in H$ [lecture incertaine — la place de l'inverse est empâtée]. Ona : $[yhy^{-1}]_g = [y]_g[h]_g[y]_g^{-1}$ [avec un passage raturé au milieu du calcul] … $= [e]_g = H$ … Ainsi $yhy^{-1} \in H$ [lecture incertaine — même réserve sur l'inverse]

\* on montre de même que ④⟹①

D'où le résultat ! [signature, doublement souligné]

[en marge droite, vertical, grandes lettres : PROUVÉ]

---

## Page 3 — Cardinal, noyau et image (début)

[en haut à droite : de cardinaux finis]

Théo : Soient $(G_1, \times)$, $(G_2, \circ)$ 2 groupes, et $\varphi$ un homomorphisme de $G_1 \to G_2$. Ona : $|G_1| = |\mathrm{Ker}\,\varphi||\mathrm{Im}\,\varphi|$ et dans la mesure où $\varphi$ est surjective $|G_1| = |\mathrm{Ker}\,\varphi||G_2|$

En effet [« en considérant la projection canonique » raturé] vu que $\mathrm{Ker}\,\varphi \triangleleft G_1$ la projection canonique $p : (G_1, \times) \longrightarrow (G_1/\mathrm{Ker}\,\varphi, \bar{\times})$ / $y \longmapsto \bar{y}$ est un homomorphisme surjectif bien défini. Et après [d'après] le théo de la décomposition canonique, $\exists!$ $\chi$ bijective / $\varphi = \chi \circ p$ : $(G_1, \times) \xrightarrow{\varphi} (\varphi(G_1) \subseteq G_2, \circ)$

[diagramme triangulaire : $p$ flèche vers $(G_1/\mathrm{Ker}\,\varphi, \bar{\times})$, $\chi$ flèche vers $(\varphi(G_1) \subseteq G_2, \circ)$]

---

## Page 4 — Cardinal, noyau et image (fin) et corollaire

D'après le théo de Lagrange, $|G_1| = |\mathrm{Ker}\,\varphi||G_1/\mathrm{Ker}\,\varphi|$ vu que $\mathrm{Ker}\,\varphi \le G_1$ $= |\mathrm{Ker}\,\varphi||\varphi(G_1)|$ vu que $\chi : G_1/\mathrm{Ker}\,\varphi \to \varphi(G_1)$ [bijective, implicite]

Donc $|G_1| = |\mathrm{Ker}\,\varphi||\mathrm{Im}\,\varphi|$ [souligné]

Dans la mesure où $\varphi$ surjective, $\mathrm{Im}\,\varphi = G_2$ d'où $|G_1| = |\mathrm{Ker}\,\varphi||G_2|$

Corollaire $\varphi$ bijective $\iff$ $\mathrm{Ker}\,\varphi = \{e_{G_1}\}$ [lecture incertaine — l'élément neutre est tracé en cursive]

En effet D'après ce qui précède, [un mot raturé] $\varphi$ bijective $\Longrightarrow \begin{cases} |G_1| = |\mathrm{Ker}\,\varphi||\mathrm{Im}\,\varphi| \\ |G_1| = |G_2| \end{cases} \Longrightarrow |\mathrm{Ker}\,\varphi| = 1$

$\iff \mathrm{Ker}\,\varphi = \{e_{G_1}\}$ [souligné]

---

## 📝 Notes de transcription (fidélité)

- Encre bleue sur papier ligné à marge rouge ; pages 3–4 très lisibles, pages 1–2 avec bords rognés et tracés empâtés (chaque doute est balisé).
- Notations d'origine conservées : $Mq$ = montrons que, $Ona$ = on a, $H \le G$ / $H \triangleleft G$, $[x]_g$ = classe à gauche, $\mathrm{Ker}\,\varphi$ / $\mathrm{Im}\,\varphi$ / $\varphi(G_1)$.
- Page 2 : les intitulés exacts des points ③ et ④ (« … admissible ») sont empâtés ; les implications ②⟹④ et ④⟹① sont admises « de même » sans détail.
- Aucune figure à reproduire : les deux schémas (triangle d'implications p. 2, triangle $p$/$\chi$ p. 3) sont des croquis de preuve décrits en place.

---

## Figures

Aucune figure à reproduire (aucun graphe/courbe/schéma géométrique) : pp. 1 et 4 re-vérifiées S4 (Lagrange p. 1, noyau-image + corollaire p. 4 — texte seul) ; p. 2–3 vérifiées — les deux croquis logiques (« Schéma de démonstration » ①②③④ p. 2, triangle $p$/$\chi$ p. 3, marge « PROUVÉ ») sont transcrits en place ci-dessus. Aucun script `reproduce_morphismes_groupes_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $Mq$ = montrons que ; $Ona$ = on a ; $H \le G$ = sous-groupe, $H \triangleleft G$ = distingué.
- $G/H$ = classes à gauche ; $[x]_g$ = classe à gauche de $x$ ; $\mathrm{Ker}\,\varphi$ / $\mathrm{Im}\,\varphi$ / $\varphi(G_1)$.
- $p$ = projection canonique ; $\chi$ = isomorphisme de décomposition canonique.
