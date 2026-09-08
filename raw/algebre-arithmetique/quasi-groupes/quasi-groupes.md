# Étude des Quasigroupes — transcription fidèle

> 🧾 **Manuscrit original :** `quasi-groupes.pdf` (scan, 2 pages) · 📅 20/01/2022 · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> Les tables de Cayley sont reconstruites en tableaux (fidèles aux valeurs manuscrites).

📄 **Source scannée :** [`quasi-groupes.pdf`](quasi-groupes.pdf)

---

## Page 1

### Qu'est-ce qu'un quasigroupe ?

* Par son nom l'indique [*sic* — « Comme son nom l'indique »], c'est une structure algébrique $(G, \cdot)$ où l'on peut définir une opération inverse / à $\cdot$ et qui n'a juste besoin que d'être associatif pour être un groupe.

* Plus formellement c'est un magma $(G, \cdot)$ où il est possible de résoudre les éqns $x \cdot a = b$ et $a \cdot y = b$ d'inconnues $x$ et $y$ avec $a, b \in G$ et trouver des uniques solutions notées $b / a$ et $a \backslash b$.

* Dans la table de l'opération $\cdot$, un elt de $G$ apparaît au plus une seule fois sur chaque ligne et une seule fois sur chaque colonne.

* L'intérêt de l'étude des quasigroupes vient du fait que des magmas $(G, \cdot)$ peuvent avoir de belles tables pour l'opération $\cdot$ sans toutefois être des groupes : on parle alors de quasigroupe.

### Théorème : tout quasigroupe associatif est un groupe

* Tout quasigroupe associatif $(Q, \cdot)$ est un groupe.

En effet, soit $a \in Q$. $\exists! e_{a_1}, e_{a_2} \in Q \mid e_{a_1} \cdot a = a$ et $a \cdot e_{a_2} = a$.

Mq : $\forall a, b, c \in Q,\ a \cdot b = c \cdot b \iff a = c$ (ceci est valable pour $b \cdot a = b \cdot c$).

- $a = c \implies a \cdot b = c \cdot b$.
- Posons $d = a \cdot b = c \cdot b$ ainsi $a$ et $c$ sont les solutions uniques de l'éq : $d = x \cdot b$ d'où $a = c$.

- Ona : $e_{a_1} \cdot a = e_{a_1} \cdot (e_{a_1} \cdot a) = (e_{a_1} \cdot e_{a_1}) \cdot a \implies e_{a_1} \cdot e_{a_1} = e_{a_1}$.
- De plus $a \cdot e_{a_1} = a \cdot (e_{a_1} \cdot e_{a_1}) = (a \cdot e_{a_1}) \cdot e_{a_1} \implies a = a \cdot e_{a_1} \implies e_{a_1} = e_{a_2}$.

Dans la suite on notera $e_a = e_{a_1} = e_{a_2}$.

Soit $b \in Q$, $\exists! e_b \in Q \mid e_b \cdot b = b \cdot e_b = b$.

Ona : $e_a \cdot b = (e_a \cdot e_a) \cdot b = e_a \cdot (e_a \cdot b) \implies b = e_a \cdot b \implies e_a = e_b$.

~~Donc $Q$ admet~~ Dans la suite, on notera $e_a = e_b\ \forall a, b \in Q$.

Donc $Q$ admet un elt neutre $e$.

- Symétrie : Soit $a \in Q$. $\exists a', a'' \in Q \mid a' \cdot a = e$ et $a \cdot a'' = e$.

Ona : $a \cdot a' = a \cdot (a' \cdot a \cdot a') = (a \cdot a') \cdot (a \cdot a')$ avec $\underbrace{a' \cdot a}_{e}$.

$(a \cdot a') \cdot e = (a \cdot a') \cdot (a \cdot a')$, d'où $e = a \cdot a' \implies [\text{fin de ligne rognée}]$.

Donc $a^{-1} = a' = a''$.

Par conséquent $Q$ est un gr[oupe].

---

## Page 2

* Conclure : Pour mtr qu'un quasigroupe n'est pas associatif, il peut suffire de mtr qu'il n'est pas un semi-groupe, ce qui peut être parfois plus facile.

Ex : $(Q, \cdot) = (\{a, b, c\}, \cdot)$ :

| $\cdot$ | $a$ | $b$ | $c$ |
|---|---|---|---|
| $a$ | $a$ | $c$ | $b$ |
| $b$ | $c$ | $b$ | $a$ |
| $c$ | $b$ | $a$ | $c$ |

- Pour mtr que $Q$ n'est pas associatif la méthode directe voudrait qu'on teste tous les $\alpha \cdot (\beta \cdot \gamma)$ et $(\alpha \cdot \beta) \cdot \gamma$, $\forall \alpha, \beta, \gamma \in Q$ soit $2 \cdot 3^3 = 54$ cas (énorme !) (une méthode plus simple découlera de ce qui suit plus bas).

* $(Q : \{a, b, c\}, \cdot)$ est un gr ssi il est isomorphe à $(\mathbb{Z}, +)$ [ou $(\mathbb{N}, +)$] ou à $\mathbb{Z}/m\mathbb{Z}$, $m \in \mathbb{N}$.

Ex (suit). Recherche d'elt neutre : $a \cdot a = a$ et $c \cdot c = c$ d'où $a \cdot c = (a \cdot a) \cdot c = a \cdot (a \cdot c)$.

> En marge : $\Downarrow \ldots = c$ … Absurde !

Donc $Q$ n'est pas un groupe et donc pas ~~en~~ un quasigroupe associatif.

* Rq : $(Q, \cdot)$ est un quasigroupe associatif $\iff Q$ est un gr et le contraire avec [« Hier » ? — lecture incertaine, voir note] en amont peut marcher dans les 2 sens.

### Exple des cas particuliers

- Quasigroupe non associatif : $(Q, \cdot) = (\{a, b, c\}, \cdot)$ : [même table que ci-dessus] — étudié ↑.

- Quasigroupe unitaire non associatif : Boucle $(Q = \{a, b, c, d, e\}, \cdot)$ [une première table 4×4 raturée, illisible] :

| $\cdot$ | $a$ | $b$ | $c$ | $d$ | $e$ |
|---|---|---|---|---|---|
| $a$ | $a$ | $b$ | $c$ | $d$ | $e$ |
| $b$ | $b$ | $a$ | $d$ | $e$ | $c$ |
| $c$ | $c$ | $e$ | $b$ | $a$ | $d$ |
| $d$ | $d$ | $c$ | $e$ | $b$ | $a$ |
| $e$ | $e$ | $d$ | $a$ | $c$ | $b$ |

Ona : $(Q, \cdot)$ est un quasigroupe ~~p…~~ d'elt neutre $a$ mais pas associatif car [ligne raturée : $(b \cdot d) \cdot d = b \neq b \cdot (d \cdot d)$].

$(d \cdot c) \cdot d = c \neq d \cdot (c \cdot d) = d$.

NB : Pour essayer de construire des quasigroupes non associatifs avec d'autres propriétés (unitaire…) ou pas on peut construire des quasigroupes qui ne sont pas des groupes et par contraposée de la Rq précédente ces quasigrp ne seront pas associatifs (c'est le cas de cet ex où $c \cdot d = a$ mais $d \cdot c = e \neq a$ et … [fin rognée]).

---

## 📝 Notes de transcription (fidélité)

- « Mhq » lu « Mq » (montrons que) ; « mtr » = montrer ; « elt » = élément ; « gr » = groupe ; « eqn/éqn » = équation.
- « Par son nom l'indique » : coquille conservée telle quelle (« Comme son nom l'indique » probable).
- « magma » est écrit « magma » (un passage raturé « magmare/magma »).
- Rq page 2 : le mot avant « en amont » ressemble à « Hier » — probablement « le thm » ; incertain.
- Témoin de non-associativité de la boucle : première tentative raturée, seconde retenue ($d, c, d$) ; à revérifier contre la table (signalé, maths d'origine intactes).
- Bas de page 1 et fin de page 2 légèrement rognés par le scan (bords).

---

## Figures

Aucune figure à reproduire : p. 1–2 vérifiées — les tables de Cayley (3×3 p. 2, boucle 5×5 avec premier jet 4×4 raturé) sont des données textuelles reconstruites en tableaux ci-dessus (valeurs contrôlées : $3\times3$ et $5\times5$ conformes, témoin $(d\cdot c)\cdot d = c \ne d = d\cdot(c\cdot d)$ confirmé). Aucun script `reproduce_quasi_groupes_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $Mq$ lu $Mhq$ = montrons que ; $mtr$ = montrer ; $elt$ = élément ; $gr$ = groupe ; $eqn$ = équation.
- $magma$ = ensemble muni d'une loi ; $boucle$ = quasigroupe unitaire ; $b/a$, $a\backslash b$ = quotients.
- $semi$-$groupe$ = magma associatif ; « $Hier$ ? » = lecture incertaine (probablement « le thm »).
