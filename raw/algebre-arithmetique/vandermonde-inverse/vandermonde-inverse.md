# Inversion matricielle de Vandermonde — transcription fidèle

> 🧾 **Manuscrit original :** `vandermonde-inverse.pdf` (scan, 3 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à ~90 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`vandermonde-inverse.pdf`](vandermonde-inverse.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Inversion matricielle de Vandermonde [titre, pastille ① en haut à droite]

$V_n = \mathrm{Vand}(a_0 \cdots a_{n-2} / a_0 \cdots a_{n-2})$ [lecture incertaine — matrice $n \times n$ :] $\begin{vmatrix} 1 & & 1 \\ & & \\ a_0^{n-2} & & a_{n-2}^{n-2} \end{vmatrix}$ [première et dernière lignes visibles, intérieur peu lisible]

$$P = (X - a_0) \cdots (X - a_{n-2}) = \sum_{k=0}^{n-2} \alpha_k X^k + X^{n-1}$$

$L_n \leftarrow L_n + \sum_{k=0}^{n-2} \alpha_k L_{k+1}$ [opération sur les lignes]

$a_{n-1}^{?} \leftarrow a_{n-1}^{?} + \sum_{k=0}^{n-2} \alpha_k a_k^{?} = P(a_k) = \begin{cases} 0 \text{ si } k \leq n-2 \\ \prod_{k=0}^{n-2}(a_{n-1} - a_k) \end{cases}$ [lecture incertaine sur les exposants]

$$V_n = \begin{vmatrix} 1 & \cdots & 1 \\ a_0 & \cdots & a_{n-2} \\ a_0^{n-2} & \cdots & a_{n-2}^{n-2} \\ 0 & \cdots & 0 & \prod(a_{n-1} - a_k) \end{vmatrix} = \prod_{k=0}^{n-2}(a_{n-1} - a_k)\, V_{n-2} \text{ [lecture incertaine sur l'indice — probablement $V_{n-1}$]}$$

$$V_n = \prod_{k=1}^{n-2} \prod_{k=0}^{k-2}(a_k - a_k) \text{ [lecture incertaine]}$$

$$= \prod_{0 \leq i, j \leq n-2}(a_j - a_i) \text{ [lecture incertaine — probablement $\prod_{0 \leq i < j \leq n-2}$]}$$

D'où pour $(a_i)_{i=0}^{n-2} \mid \forall i, j \in [\![0, n-2]\!]$ $i \neq j \Rightarrow a_i \neq a_j$, $\det(V_n) = V_n \neq 0$ d'où $V_n$ est inversible.

Considérons $\varphi_k : \mathbb{R}_{n-2}[X] \longrightarrow \mathbb{R}$, $P \longmapsto \varphi_k(P) = P(a_k)$, $\forall k \in [\![0, n-2]\!]$

[ligne très peu lisible : $(L_{n-1}, L_{n-2}) \times (L_{n-1} + L_n \cdots)$ — lecture incertaine] $t.q.t$ $fl(\mathbb{R}_{n-2}[X])$ [les $\varphi_k$ sont des formes linéaires]

$t.n.t$ $C_{k=0}^{n-2}$ [lecture incertaine] est libre car génératrice car $\bigcap_{k=0}^{n-2} \mathrm{Ker}\, \varphi_k = \{0_{\mathbb{R}}\}$ [lecture incertaine sur le second membre — probablement $\{0\}$].

## Page 2

[pastille ② en haut à droite]

Vu que pour $p \in \bigcap_{k=0}^{n-2} \mathrm{Ker}\, \varphi_k$, $p$ a $n$ racines distinctes [lecture incertaine — probablement $n-1$] : $a_0, \cdots, a_{n-2}$ et ce $P \in \mathbb{R}_{n-2}[X]$, $P = 0_{\mathbb{R}[X]}$

Alors $\varphi_{k=0}^{n-2}$ [les $(\varphi_k)$] base de $fl(\mathbb{R}_{n-2}[X])$ [le dual]

[Matrice/tableau d'essai entièrement biffé d'un grand gribouillis en zigzag : on y devine des lignes « 1 2 3 4 5 … n-2 », « 3 4 … », « 4 2 3 », « 2 3 4 » — brouillon abandonné, non transcrit.]

Posons $\forall i \in [\![0, n-2]\!]$, $L_i = \prod_{j \neq i} \frac{(X - a_j)}{a_i - a_j}$

$\forall k \in [\![0, n-2]\!]$ $\varphi_k(L_i) = L_i(a_k) = \begin{cases} 0 \text{ si } i \neq k \\ 1 \text{ sinon} \end{cases} = \delta_{ik}$

D'où $(L_i)_{i=0}^{n-2}$ est la base préduale associée à la base duale $\Phi = (\varphi_k)_{k=0}^{n-2}$

Il vient $(P_S^{?} \cdots P_\Phi^B)$ [lecture incertaine] $\Rightarrow \begin{bmatrix} 1 & \cdots & 1 \\ \vdots & & \vdots \\ a_0^{n-2} & \cdots & a_{n-2}^{n-2} \end{bmatrix}^{-1} = {}^tP_\Phi^1$ [lecture incertaine sur la notation de la transposée]

où $L_i = \frac{1}{\prod_{j \neq i}(a_i - a_j)}\left(\sum_{k=0}^{n-2} X^k(-1)^{n-2-k}\sum_{\substack{J \subseteq I_{n-2,i} \\ |J| = n-2-k}} \prod_{j \in J} a_j\right)$ où $I_{n-2,i} = [\![0, n-2]\!] \setminus \{i\}$ [lecture incertaine sur le second $J \subseteq \cdots$ du manuscrit]

## Page 3

[pastille ③ en haut à droite]

D'où ${}^tP_\Phi^1 = \left[\frac{1}{\prod_{k \neq j}(a_j - a_k)} \cdots \sum \prod a_k\right]_{i,j=0}^{\cdots}$ [première forme très peu lisible, reprise ci-dessous]

D'où $\begin{bmatrix} 1 & \cdots & 1 \\ \vdots & & \vdots \\ a_0^{n-2} & \cdots & a_{n-2}^{n-2} \end{bmatrix}^{-1} = \left[\frac{(-1)^{n-1-j}}{\prod_{k \neq i}(a_i - a_k)} \sum_{\substack{J \subseteq I_{n-2,i} \\ |J| = n-1-j}} \prod_{k \in J} a_k\right]_{i,j=0}^{?}$ où $I_{n-2,i} = [\![0, n-2]\!] \setminus \{i\}$

$$= \left[\frac{(-1)^j}{\prod_{k=0, k \neq i}^{?}(a_i - a_k)} \sum_{\substack{K \subseteq I_{n-2,i} \\ |K| = n-2-j}} \prod_{k \in K} a_k\right]_{i,j=0}^{n-2} \text{ où } I_{n-2,i} = [\![0, n-2]\!] \setminus \{i\}$$

Appl. $[A_2]^{-1} = I_2$ [titre de section, lecture incertaine]

- $\begin{bmatrix} 1 & 1 \\ a_0 & a_1 \end{bmatrix}^{-1} = \begin{bmatrix} \frac{a_1}{a_1-a_0} & \frac{-1}{a_1-a_0} \\ \frac{+a_0}{a_0-a_1} & \frac{-1}{a_0-a_1} \end{bmatrix} = \frac{1}{a_1-a_0}\begin{bmatrix} a_1 & -1 \\ -a_0 & 1 \end{bmatrix}$

- $\begin{bmatrix} 1 & 1 & 1 \\ a_0 & a_1 & a_2 \\ a_0^2 & a_1^2 & a_2^2 \end{bmatrix}^{-1}_{(n=3)} = \begin{bmatrix} \frac{a_1 a_2}{(a_1-a_0)(a_2-a_0)} & -\frac{a_1+a_2}{(a_1-a_0)(a_2-a_0)} & \frac{1}{(a_1-a_0)(a_2-a_0)} \\ \frac{a_0 a_2}{(a_0-a_1)(a_2-a_1)} & -\frac{a_0+a_2}{(a_0-a_1)(a_2-a_1)} & \frac{1}{(a_0-a_1)(a_2-a_1)} \\ \frac{a_0 a_1}{(a_0-a_2)(a_1-a_2)} & -\frac{a_0+a_1}{(a_0-a_2)(a_1-a_2)} & \frac{1}{(a_0-a_2)(a_1-a_2)} \end{bmatrix}$

---

## Figures

Aucune figure à reproduire : pp. 1 et 3 vérifiées S4 (pastilles ①/③, matrices et inverses 2×2/3×3 — équations seules) ; p. 2 vérifiée (pastille ②, grand gribouillis en zigzag = brouillon de matrice abandonné, non transcrit — pas une illustration). Aucun script `reproduce_vandermonde_inverse_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $V_n = \mathrm{Vand}$ = matrice de Vandermonde ; pastilles ①②③ = pagination manuscrite.
- $L_i$ = polynômes de Lagrange ; $\delta_{ik}$ = symbole de Kronecker ; $t.q.t$ = tel que tel(s).
- $P_\Phi$, ${}^tP$ = matrices de passage (notations incertaines) ; $fl$ = formes linéaires.
