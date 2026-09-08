# Espaces vectoriels finis sur corps fini — transcription fidèle

> 🧾 **Manuscrit original :** `ev-fini-corps-fini.pdf` (scan, 4 pages, encre noire sur papier ligné, cahier photographié de biais ; paraphe « CP » p. 2) · ✍️ KpihX
> 🔍 **Statut :** lisible (~70 %), transcrit fidèlement. Page 1 : $|E| = q^n$ et comptage des bases. Page 2 : produit $\prod(q^n-q^k)$, lemme des Bergers et coefficient binomial de Gauss. Page 3 : $\mathbb{Z}/n\mathbb{Z}$ corps ssi $n$ premier. Page 4 : le sous-espace de parité de $V(n,2)$ sur $\mathbb{F}_2$.
> 📄 **Source scannée :** [`ev-fini-corps-fini.pdf`](ev-fini-corps-fini.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Cardinal $q^n$ et choix des vecteurs de base

[à gauche du trait vertical : fragment de la page voisine du cahier — tables « $0+0=0$ », « $0\cdot0=0$ », opérations booléennes et polynômes d'interpolation $l_i = \prod \frac{X-X_j}{X_i-X_j}$ ; hors présent manuscrit, non transcrit]

Soit $(E, +, \cdot)$ un $K$-ev de dim $n$ ($n \ge 1$) et $|K| = q$. $B = (e_i)_n$ une base de $E$.

Mq $|E| = q^n$

Ona : $|K^n|$ […] $\sum_{i=1}^n d_i e_i$ $\{\dots d_i \in K \dots\}$ [ligne empâtée — développement sur la base $B$]

d'où $|E| = |K|^n = q^n$

. Nombre de bases de $E$ : on a : $q^n - 1$ vecteurs non nuls dans $E$

Soit $e_1$ on a $q^n - 1$ possible choix

Soit $e_2$ // on a : $q^n - q$ −//− car l'ens des vecteurs colinéaires à $e_1$ est $C_1 = Vect(e_1) \Rightarrow |C_1| = q$

[Soit $e_3$ … ona : $q^n - q^2$ — ligne raturée]

Soit $e_3 \notin$ [Vect$(e_1,e_2)$ — empâté] on a : $q^n - q^2$ −//−

? $(n \ge 2)$

Soit $e_n \notin \sum d_i e_i$ ? $(n \ge 2)$ [passage empâté] ona : $q^n - q^{n-1}$ −//− $q^{n-1}(q-1)$

On a en tout $N = \sum_{k=0}^{n-1} q^n - q^k$ [*sic* — lire $\prod$, cf. page 2 ; la somme qui suit suppose $\sum$]

$= nq^n - \frac{1-q^n}{1-q}$ [un tracé parasite devant]

---

## Page 2 — Familles libres, lemme des Bergers, binomial de Gauss

Le nbre de bases de $E$ est donc $N = \prod_{k=0}^{n-1} (q^n - q^k)$

. Le nbre de familles de $k$ vecteurs linéairement indépen[dants] est défini de m̃ par $N = \prod_{k=0}^{\dots} (q^n - q^k)$ [lire « de même » ; bornes empâtées] et où […] $= k$ [passage empâté]

On construit ainsi tous les sev de $E$ mais chaque s.e.v est compté autant de fois qu'il a de base.

Lemme des Bergers : Si un ens $E$ possède une partition en $p$ sous-ens contenant chacun $r$ éléments alors $E$ contient $n = p \times r$ elts

. Le nbre de s.e.v de dim $k$ est donc (d'après ce lemme) (le coef binomial de Gauss) $\begin{bmatrix} n \\ k \end{bmatrix}_q = \frac{(q^n-1)\cdots(q^n-q^{k-1})}{(q^k-1)\cdots(q^k-q^{k-1})}$

$\begin{bmatrix} n \\ k \end{bmatrix}_q = \prod_{i=0}^{k-1} \frac{q^n-q^i}{q^k-q^i}$ [indices peu lisibles]

[un long trait vertical borde la droite de la page ; en bas à droite : paraphe « CP »]

---

## Page 3 — $\mathbb{Z}/n\mathbb{Z}$ est un corps ssi $n$ est premier

Théo : l'anneau commutatif unitaire $(\mathbb{Z}/n\mathbb{Z}, +, \cdot)$, $n \in \mathbb{N}^*$ [précision empâtée] est un corps ssi $n$ est un nbre $1^{er}$

$\Rightarrow$ / Supp $n$ $1^{er}$ ($\ge 2$). Soit $[i] \in \mathbb{Z}/n\mathbb{Z}$ [mot empâté]. Cherchons $[j] \in \mathbb{Z}/n\mathbb{Z}$ / $[i][j] = [1] \iff ij \equiv 1 [n]$

D'après le petit théo de Fermat, $i^{n-1} \equiv 1 [n]$

càd [mot raturé] $i \times i^{n-2} \equiv 1 [n]$. Prendre $j = i^{n-2}$

Ainsi $\mathbb{Z}/n\mathbb{Z}$ est un corps

$\Leftarrow$ / Supp $\mathbb{Z}/n\mathbb{Z}$ un corps et $n$ non $1^{er}$ (par l'absurde). $\exists i = \overline{1,n}$ / $i|n = d \ge 2$ car sinon $n$ serait premier [notation empâtée]

$\exists$ [mot raturé] $j = \overline{1,n}$ / $[i][j] = [1] \Rightarrow ij \equiv 1 [n] \Rightarrow \exists k \in \mathbb{N}$ / $ij = 1 + kn$

$\exists! (i', n') \in \mathbb{N}^{*2}$ / $i \wedge n = d$ et $i = i'd$ et $n = n'd$

Ainsi $[i][j] = [1] \Rightarrow d \mid i'j - n't = 1$ [lecture incertaine — membre médian empâté, $i', n'$ premiers entre eux, $t$ multiple] $\Rightarrow d \mid 1 \Rightarrow$ absurde !

D'où le résultat

---

## Page 4 — Le sous-espace de parité de $V(n,2)$ sur $\mathbb{F}_2$

Ex | $(\mathbb{F}_2, +, \cdot)$ où $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$ et [?] $(V(n,2), +^n, \cdot_n)$ [passage raturé : « … un $\mathbb{F}_2$-ev … »]

$\underbrace{(\dots, +^n, \cdot_n)}_{V(n,2)}$ [début empâté]

Mq $E = \{u \in V(n,2) / P(u) \in 2\mathbb{N}\}$ est un sev de $V(n,2)$

Soit $u \in V(n,2)$ $\exists d_i \in \{0,1\}$ [ensemble empâté — $\{0,1\}$ confirmé visuellement p. 4] / $u = ([d_1], [d_2], \dots, [d_n]) = \{[d_i]\}_n$

$P(u) = \sum_{i=1}^n d_i$ puisque compter les elts non nuls revient à sommer ces elts

. $P(0_{V(n,2)}) = \sum_{i=1}^n 0 = 0 \in 2\mathbb{N}$ d'où $0_{V(n,2)} \in E \Rightarrow E \neq \emptyset$

. Soit $(\alpha, u, v) \in \mathbb{F}_2 \times E^2$

ona : $P(\alpha u + v) = P([\alpha u_i + v_i]_n)$ $\forall i = \overline{1,n}$, $\exists! (q_i, r_i) \in \mathbb{N} \times [\dots]$ / $\alpha u_i + v_i = q_i \times 2 + r_i$ [l'ensemble d'arrivée de $r_i$ est empâté]

ainsi $P(\alpha u + v) = P([r_i]_n) = \sum_{i=1}^n \alpha u_i + v_i - 2q$ [le dernier terme est empâté]

$= \alpha \sum_{i=1}^n u_i + \sum_{i=1}^n v_i - 2q \in 2\mathbb{N}$ [sous chaque somme et sous $2q$ : accolade « $\in 2\mathbb{N}$ »]

d'où $\alpha u + v \in E$

D'où le résultat

---

## Figures

- Aucune figure pp. 1–4 relues (trait vertical p. 2 = bordure de mise en page, pas une figure ; paraphe « CP » p. 2 transcrit).

## Vocabulaire

$K$-ev dim $n$, $|E|=q^n$, bases, familles libres, lemme des Bergers, binomial de Gauss $\begin{bmatrix}n\\k\end{bmatrix}_q$, $\mathbb{Z}/n\mathbb{Z}$ corps ssi $n$ premier, poids $P(u)$, $V(n,2)$ sur $\mathbb{F}_2$, $Mq$/$Ona$.

## 📝 Notes de transcription (fidélité)

- Encre noire sur papier ligné, cahier photographié de biais (pages 1 et 4 en perspective) ; ratures et tracés parasites conservés et balisés.
- « −//− » = ditto (reprend « possibles choix » de la ligne du $e_1$) ; « // » après $e_2$ = condition abrégée (hors $C_1$, d'après la justification qui suit).
- Page 1 : $N = \sum_{k=0}^{n-1} (q^n-q^k)$ [*sic*] — le produit $\prod$ de la page 2 est la version corrigée.
- Notations d'origine : $Mq$, $Ona$, $K$-ev, $s.e.v$, $1^{er}$, $[i]$ classes, $i \wedge n$ = PGCD, $\begin{bmatrix} n \\ k \end{bmatrix}_q$ binomial de Gauss, $P(u)$ poids (somme des bits), $V(n,2)$ $= \{0,1\}^n$.
- Aucune figure à reproduire : ni courbe ni schéma (le trait vertical p. 2 est une bordure de mise en page).
