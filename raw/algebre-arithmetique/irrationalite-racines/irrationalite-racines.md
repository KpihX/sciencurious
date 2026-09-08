# Irrationalité des racines carrées et n-ièmes — transcription fidèle

> 🧾 **Manuscrit original :** `irrationalite-racines.pdf` (scan, 6 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible, transcrit mot à mot. Les maths sont conservées telles quelles ; les ratures sont notées `[raturé]`, les lectures douteuses `[lecture incertaine — …]`.
> 📄 **Source scannée :** [`irrationalite-racines.pdf`](irrationalite-racines.pdf) (restaurée depuis Datas1, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

Irrationnalité de la racine carrée des nbres $1^{ers}$.

Théo1 : Soit $p \in \mathbb{P}$ (ens des nbres $1^{ers}$). On a : $\sqrt{p} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}}$ [lecture incertaine — complémentaire de $\mathbb{Q}$ dans $\mathbb{R}$, noté $C_{\mathbb{R}}^{\mathbb{Q}}$].

En effet supposons par l'absurde que $\sqrt{p} \in \mathbb{Q}$ alors $\exists!\ (a, b) \in \mathbb{Z} \times \mathbb{N}^*\ /\ a \land b = 1$ et $\sqrt{p} = a/b \implies b^2 p = a^2$.

Or : $a \land b = 1 \implies a^2 \land b^2 = 1$. Et comme $a^2 \mid (b^2 p)$ d'après le théo de Gauss, $a^2 \mid p$.

- Si $a \ne 1$ [lecture incertaine — « $a^2 \ne 1$ » possible, un éventuel carré est empâté ; « $a \ne 0$ » en dessous] on aboutit à une absurdité car $p$ aura plus de $2$ diviseurs parmi lesquels $1, p$ et $a^2$. Absurde !
- Si $a = 1$, $b^2 p = 1 \implies b = p = 1$ car $b, p \in \mathbb{N}^*$. Absurde !
- Si $a = 0$, $b^2 p = 0 \implies b = 0$ ou $p = 0$. Absurde !

D'où le résultat !

Rq : on généralise ainsi la démonstration de l'irrationnalité [lecture incertaine — mot en marge droite « tel »].

Théo2 (conséquence) : la racine carrée d'un entier naturel $\ge 2$ est irrationnelle ssi il existe dans la décomposition en pfp de cet entier, au moins un nbre $1^{er}$ élevé à une puissance impaire.

En effet, soit $n \in \mathbb{N}^* \setminus \{1\}$. $\exists!\ m \in \mathbb{N}^*,\ \exists!\ ((p_i)_{1, m}, (\alpha_i)_{1, m}) \in \mathbb{P}^m \times \mathbb{N}^{*m}\ /\ n = \prod_{k=1}^m p_k^{\alpha_k}$ [lecture incertaine — bas de page rogné, suite page 2].

## Page 2

[raturé : « Supposons $\exists\ k \in [\![1, m]\!]$ … »].

Quitte à réassigner les indices des facteurs de la décomp en pfp de $n$ supposons que $\alpha_i = 2\beta_i + 1\ \forall\ i \in [\![1, r]\!]$ pour un certain $r \in [\![0, m]\!]$ et que $\alpha_i = 2\beta_i\ \forall\ i \in [\![r+1, m]\!]$ (avec $\beta_i \in \dots$) [lecture incertaine — fin rognée à droite].

On a : $\sqrt{n} = \sqrt{\prod_{i=1}^r p_i} \times \prod_{i=1}^m p_i^{\beta_i}$ (Rq : pour $r = 0$, $\alpha_i \in 2\mathbb{N}^*\ \forall\ i$).

Ainsi $\sqrt{n} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}} \iff \sqrt{\prod_{i=1}^r p_i} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}}$ et $r \ge 1$.

Lemme1 (Version améliorée du théo1) : Soit $r \in \mathbb{N}^*$, $(P_i)_{\dots} \in \mathbb{P}^r$. On a : $\sqrt{\prod_{i=1}^r P_i} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}}$.

En effet supp par l'absurde $\exists$ [raturé] que $\sqrt{\prod_{i=1}^r P_i} \in \mathbb{Q}$ alors $\exists!\ (a, b) \in \mathbb{N} \times \mathbb{N}^*\ /\ a \land b = 1$ et $\sqrt{\prod_{i=1}^r P_i} = \frac{a}{b} \implies b^2 \prod_{i=1}^r P_i = a^2$.

Or : $a \land b = 1 \implies a^2 \land b^2 = 1$ et car $a^2 \mid (b^2 \prod P_i)$ alors d'après le théo de Gauss, $a^2 \mid \prod_{i=1}^r P_i \implies \exists\ k \in [\![1, r]\!]$ / [lecture incertaine — « $a \mid P_k$ » rogné]. On ne peut qu'avoir $a \in \{0, 1\}$ [*sic* — le manuscrit porte bien « $a \in \{0,1\}$ », cohérent avec $a^2 \in \{0,1\}$] car sinon $P_k$ aurait plus de $2$ diviseurs, pour ne citer que $1, a$ et $a^2$.

Or $\sqrt{\prod P_i} > 1 \implies a^2 > 1 \implies a > 1$. Absurde !

D'où le résultat !

Ainsi en revenant au théo2, $\sqrt{n} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}} \iff r \ge 1$ et $\sqrt{\prod_{i=1}^r P_i} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}} \to$ pas vrai pour $r = 0$ [lecture incertaine — bas de page rogné].

## Page 3

D'où le résultat.

Théo3 : Le théo 3 [sic — le manuscrit porte « Le théo 3 », lire Théo2] reste valable quand bien même $n \in \mathbb{Q}_+^* \setminus \{1\}$ [lecture incertaine — ligne surchargée avec rature « $1, \dots, r$ »].

Définition (préliminaire) : Soit $r \in \mathbb{Q}_+$. $\exists!\ n \in \mathbb{N}^*$ et $\exists!\ (p_k)_{k, 1, n}^n$ [lecture incertaine — notation des familles] $\in \mathbb{P}^n \times \mathbb{Z}^n\ /\ r = \prod_{k=1, 2, 3, 4}^n p_k^{\alpha_k}$ [lecture incertaine — indices]. ($q, 1$) $\ne$ ($1, 2$) [lecture incertaine — marge droite].

- existence : Soit $r \in \mathbb{Q}^*$. $\exists!\ (p, q) \in \mathbb{N}^* \times \mathbb{N}^*\ /\ p \land q = 1$ et $r = p/q$ et car $p, q \in \mathbb{N}^*$, $\exists\ n, m \in \mathbb{N}$, $\exists\ (p_i)_{i=1}^n, (q_j)_{j=1}^m, (\alpha_i)_{i=1}^n, (\beta_j)_{j=1}^m \in \mathbb{P}^n \times \mathbb{P}^m \times \mathbb{Z}^n \times \mathbb{Z}^m\ /\ p = \prod_{i=1}^n p_i^{\alpha_i}$ et $q = \prod_{j=1}^m q_j^{\beta_j}$ donc $r = \prod_{i=1}^n p_i^{\alpha_i} \prod_{j=1}^m q_j^{-\beta_j}$ (vu que $r \ne 1$ on a bien $n+m \in \mathbb{N}^*$).

- unicité : Soit $r \in \mathbb{Q}^* \setminus \{1\}$. Supposons $\exists\ n, m \in \mathbb{N}^*$, $\exists\ (p_k)_{k=1}^n, (q_k)_{k=1}^m$ [raturé], $(\alpha_k)_{k=1}^n, (\beta_k)_{k=1}^m \in \mathbb{P}^n \times \mathbb{P}^m \times \mathbb{Z}^n \times \mathbb{Z}^m$ [lecture incertaine] $r = \prod_{k=1}^n p_k^{\alpha_k} = \prod_{k=1}^m q_k^{\beta_k}$ (1).

Quitte à considérer d'abord dans les différents produits les facteurs premiers avec une puissance $> 0$, supposons que $\prod p_k^{\alpha_k} = \prod_{k=1}^r p_k^{\alpha_k} \times \prod_{k=r+1}^n p_k^{-\alpha'_k}$ et $\prod q_k^{\beta_k} = \prod_{k=1}^r q_k^{\beta_k} \times \prod_{k=s+1}^m q_k^{-\beta'_k}$ avec $\alpha'_k = \alpha_k > 0$ pour $k \in [\![1, r]\!]$, $\alpha'_k = -\alpha_k > 0$ pour $k \in [\![r+1, n]\!]$ (et de même pour $\beta'$ [lecture incertaine — « $1 \le k \le n$ »]).

## Page 4

pour un certain $r \in [\![0, n]\!]$ et $s \in [\![0, m]\!]$ : $(1) \implies \underbrace{\prod_{k=1}^r p_k^{\alpha'_k}}_{(1)} \times \underbrace{\prod_{k=s+1}^m q_k^{\beta'_k}}_{(2)} = \underbrace{\prod_{k=r+1}^n p_k^{\alpha'_k}}_{(3)} \underbrace{\prod_{k=1}^s q_k^{\beta'_k}}_{(4)}$.

Supp $n \ne m$, sans nuire à la généralité supposons en plus $m > n$. $\exists\ i \in [\![1, m]\!]$ [raturé : « $+ $ »].

Chaque facteur [lecture incertaine — « facteur » surchargé] de (1) divise (3)×(4) et œ [sic] il est $1^{er}$ avec (3), il divise (4) et ainsi $\exists\ q_k^{\beta'_k}$ dans (4) / $p_k = q_k$ et $\alpha'_k \le \beta'_k$. Inversement $q_k^{\beta'_k}$ divise (1)×(2) et œ il est $1^{er}$ avec (2), il divise (1) et ne peut diviser que $p_k^{\alpha'_k}$ d'où $\beta'_k \le \alpha'_k$. Donc $p_k^{\alpha'_k} = q_k^{\beta'_k}$.

En effectuant le même raisonnement sur les facteurs de (2), (3) et (4) on aboutit au fait que $\prod p_k^{\alpha'_k}$ [lecture incertaine — indices rognés] d'où $\prod p_k^{\alpha_k}$ [lecture incertaine] $= \prod q_k^{\beta_k}$ [lecture incertaine]. D'où l'unicité.

Rq : Soit $r \in \mathbb{Q}^* \setminus \{1\}$. L'écriture $r = \prod_{k=1}^n p_k^{\alpha_k}$ où $n \in \mathbb{N}^*$, $(p_k)_{k=1}^n \in \mathbb{P}^n$, $(\alpha_k)_{k=1}^n \in \mathbb{Z}^{*n}$, sera appelée dans la suite « décomposition en produit de facteurs $1^{ers}$ de $r$ » en abrégé « DPFP de $r$ ».

Pour l'obtenir, en partant de l'écriture unique $r = p/q$ où $(p, q) \in \mathbb{N}^{*2}$ avec $p \land q = 1$ et $(p, q) \ne (1, 1)$ il suffit de faire le ratio [raturé : « des »] des DPFD de $p$ et $q$.

## Page 5

Démonstration du théo3 : Soit $r \in \mathbb{Q}_+ \setminus \{0, 1\}$. $\exists!\ n \in \mathbb{N}^*$ et $\exists!\ (p_k)_{k=1}^n, (\alpha_k)_{k=1}^n \in \mathbb{P}^n \times \mathbb{Z}^{*n}\ /\ r = \prod_{k=1}^n p_k^{\alpha_k}$.

SNALG supposons que $\alpha_i = 2\beta_i + 2$ [lecture incertaine — manuscrit « $2\beta_i + 2$ », attendre $2\beta_i+1$ par parallèle avec page 2] $\forall\ i \in [\![1, r]\!]$ pour un certain $r \in [\![0, m]\!]$ et que $\alpha_i = 2\beta_i\ \forall\ i \in [\![r+1, m]\!]$ (avec $\beta_i \in \mathbb{Z}\ \forall\ i$).

On a : $\sqrt{r} = \sqrt{\prod_{i=1}^r p_i} \times \prod_{i=1}^m p_i^{\beta_i}$ (Rq : pour $r = 0$, $\alpha_i \in 2\mathbb{N}^*\ \forall\ i$).

Ainsi $\sqrt{r} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}} \iff r \ge 1$ et $\underbrace{\sqrt{\prod_{i=1}^r p_i} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}}}_{\text{pas vrai d'après le lemme 1}}$.

CQFD.

Théo : (vers une généralisation des théorèmes précédents) La racine $n$-ième ($n \in \mathbb{N}^* \setminus \{1\}$) d'un nbre rationnel $\in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}}$ [lecture incertaine — « (dans $\mathbb{R}$) » en marge] ssi dans sa DPFP, intervient au moins un nbre $1^{er}$ élevé à une puissance non multiple de $n$.

En effet soit $n \in \mathbb{N}^* \setminus \{1\}$ et $r \in \mathbb{Q}_+^* \setminus \{1\}$. $\exists!\ m \in \mathbb{N}^*$, $\exists!\ (p_k)_{k=1}^m, (\alpha_k)_{k=1}^m \in \mathbb{P}^m \times \mathbb{Z}^{*m}\ /\ r = \prod_{k=1}^m p_k^{\alpha_k}$.

Soit $r =$ nbre de facteurs $1^{ers}$ élevés à une puissance non multiple de $n$. ($r \in [\![0, m]\!]$).

Quitte à réassigner les indices des facteurs de la DPFD [sic — lire DPFP] par, supposons $\forall\ i \in [\![1, r]\!]$, $\alpha_i = n\beta_i +$ [raturé] ($\beta_i \in$ ?, $r_i \in [\![1, n-1]\!]$ ?) et que [lecture incertaine — bas de page rogné, suite page 6].

## Page 6

On a : $\sqrt[n]{r} = \sqrt[n]{\prod_{i=1}^r p_i^{r_i}} \times \prod_{i=1}^m p_i^{\beta_i}$.

Ainsi $\sqrt[n]{r} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}} \iff r \ge 1$ et $\sqrt[n]{\prod_{i=1}^r p_i^{r_i}} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}}$ (1).

Lemme2 : (Version généralisée du lemme1). Soient $n \in \mathbb{N}^* \setminus \{1\}$, $r \in \mathbb{N}^*$ [lecture incertaine — « $r \in \mathbb{N}^*$ »], $((p_i)_{i=1}^r, (r_i)_{i=1}^r) \in \mathbb{P}^r \times [\![0, n]\!]^r$ [lecture incertaine — exposants]. On a : $\sqrt[n]{\prod_{i=1}^r p_i^{r_i}} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}}$.

En effet on supp par l'absurde que $\sqrt[n]{\prod_{i=1}^r p_i^{r_i}} \in \mathbb{Q}$, alors $\exists!\ a, b \in \mathbb{N} \times \mathbb{N}^*\ /\ a \land b = 1$ et $\sqrt[n]{\prod_{i=1}^r p_i^{r_i}} = \frac{a}{b} \implies b^n \prod_{i=1}^r p_i^{r_i} = a^n$.

Or : $a \land b = 1 \implies a^n \land b^n = 1$ et comme $a^n \mid (b^n \prod_{i=1}^r p_i^{r_i})$, d'après le théo de Gauss $a^n \mid \prod_{i=1}^r p_i^{r_i}$ d'où $\exists\ k \in [\![1, r]\!]$ / $a^n \mid p_k^{r_k}$. On ne peut qu'avoir $a \in \{0, 1\}$ car sinon $p_k^{r_k}$ aurait plus de $r_k+1$ diviseurs en comptant déjà les $n+1 > r_k+1$ premiers diviseurs $1, a, \dots, a^n$, ce qui serait absurde car que $\mathcal{D}_+(p_k^{r_k}) = \{1, p_k, \dots, p_k^{r_k}\}$ [lecture incertaine — « car que » sic].

Or $a^n = b^n \prod_{i=1}^r p_i^{r_i} > 1$ absurde ! car $a \in \{0, 1\}$.

D'où le résultat !

Ainsi (1) : $\sqrt[n]{r} \in \mathbb{C}_{\mathbb{R}}^{\mathbb{Q}} \iff r \ge 1$. CQFD.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée (texte + équations, marge « tel ») ; pp. 2–6 vérifiées S4 (théo 2/3, lemmes 1/2 — texte seul, p. 5 : manuscrit porte bien « $2\beta_i+2$ » [*sic* — attendre $2\beta_i+1$]). Aucun script `reproduce_irrationalite_racines_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $\mathbb{P}$ = nombres premiers ; $DPFP$ = décomposition en produit de facteurs premiers ; $a \land b$ = PGCD.
- $\mathbb{C}_{\mathbb{R}}^{\mathbb{Q}}$ = complémentaire de $\mathbb{Q}$ dans $\mathbb{R}$ (irrationnels) ; $SNALG$ = sans nuire à la généralité.
- $pfp$ = produit de facteurs premiers ; $Rq$ = remarque ; $supp$ = supposons.
