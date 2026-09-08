# Division euclidienne polynomiale — transcription fidèle

> 🧾 **Manuscrit original :** `division-euclidienne-polynomes.pdf` (scan, 3 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à ~90 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`division-euclidienne-polynomes.pdf`](division-euclidienne-polynomes.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Division Euclidienne Polynomiale [titre souligné]

Soit $A(x) = \sum_{k=0}^n a_k x^k$, $B(x) = \sum_{k=0}^m b_k x^k \in \mathbb{K}[x]$, $B \neq 0$, $A = BQ + R$.

Théo : $\exists! (Q(x), R(x)) \in \mathbb{K}[x]^2 \mid \deg(R(x)) \leq m - 1$ et ?

- Si $n < m$, si $Q(x) \neq 0$, comme $\deg R < \deg B$, $\deg(BQ + R) > \deg(B) \Rightarrow n > m$ !! d'où $Q(x) = 0$ et $R(x) = A(x)$ d'où l'existence et l'unicité cherchée.
- Sinon comme $\deg R < \deg B$, $\deg A = \deg(BQ + R)$ [flèche vers :] $= \deg(BQ) + \deg R$ de degré $q$ ($car$ $Q, R \neq 0$) [$Q(x) \neq 0$ car sinon $\deg A = \deg R \Rightarrow n < m$ !!]

d'où $\deg Q = n - m \iff \exists! (q_k)_{k=0}^{n-m} \in \mathbb{K} \mid Q(x) = \sum_{k=0}^{n-m} q_k x^k$ avec $q_{n-m} \neq 0$. De même $\exists! (r_k)_{k=0}^r \in \mathbb{K}^{r+1} \mid R(x) = \sum_{k=0}^r r_k x^k$ avec $r \leq m - 1$.

Ainsi $A = BQ + R \iff \sum_{k=0}^n a_k x^k = \sum_{i=0}^m b_i x^i \sum_{j=0}^{n-m} q_j x^j + \sum_{k=0}^r r_k x^k$

$$= \sum_{i=0}^m \sum_{j=0}^{n-m} b_i q_j x^{i+j} + \sum_{k=0}^r r_k x^k$$

En posant $\forall k \in [\![m+1, n]\!]$, $b_k = 0$, $\forall k \in [\![n-m+1, n]\!]$, $q_k = 0$ et $\forall k \in [\![r+1, n]\!]$, $r_k = 0$, $A = BQ + R \iff \sum_{k=0}^n a_k x^k = \sum_{k=0}^n \sum_{i=0}^k b_i q_{k-i} x^k + \sum_{k=0}^n r_k x^k$

$$\iff \forall k \in [\![0, n]\!], a_k = \sum_{i=0}^k b_i q_{k-i} + r_k$$

## Page 2

$A = BQ + R \iff \forall k \in [\![m, n]\!]$, $\sum_{i=0}^k b_i q_{k-i} = a_k \iff (S)$ [et] $\sum_{i=0}^k q_i b_{k-i}$ [lecture incertaine — variante du membre de gauche] et $\forall k \in [\![0, n]\!]$ $r_k = a_k - \sum_{i=0}^k b_i q_{k-i}$.

[Système ? — début raturé] $(S)$ est un système linéaire de $n-m+1$ eqns à $n-m+1$ inconnues $(q_k)_{k=0}^{n-m}$ donné sous forme matricielle par

$$\underbrace{\begin{bmatrix} b_m & b_{m-1} & \cdots & b_{2m-n} \\ 0 & b_m & \cdots & b_{2m-n+1} \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & b_m \end{bmatrix}}_{M} \begin{bmatrix} q_0 \\ \vdots \\ \vdots \\ q_{n-m} \end{bmatrix} = \begin{bmatrix} a_m \\ \vdots \\ \vdots \\ a_n \end{bmatrix}$$

Ici nous considérons les $(q_k)_{k=0 \cdots n-m}$ tous nuls [lecture incertaine]. Car $\det M = b_m^{n-m+2}$ [lecture incertaine sur l'exposant] $\neq 0$ (car $B \neq 0$) alors les $(q_k)_{k=0}^{n-m}$ existent et sont uniques de même que les $r_k$ déterminés de façon unique par les expressions plus haut pour $k \in [\![0, m]\!]$ [lecture incertaine — probablement $[\![0, m-1]\!]$].

Mise en œuvre : $q_{n-m} = a_n / b_m$ ; $q_{n-m-1} = (a_{n-1} - b_{m-1}q_{n-m}) / b_m$ ; $\vdots$ ; $\forall k \in [\![0, n-m]\!]$ $q_k = (a_{k+m} - b_{k+m} \cdots$ [la suite est couverte par une grande croix biffant tout le bas de la page : $q_{n-m} = (a_{k+m} - b_{2m-n}q_{\cdots} - \cdots - b_{m-1}q_{n-m})/b_m = \cdots$ — lecture incertaine, calculs de mise en œuvre partiellement biffés].

## Page 3

Rq : Dans l'écriture matricielle précédente, pour $k < 0$, $b_k$ est pris $= 0$.

CQFD

---

## Figures

Aucune figure à reproduire : pages 1–3 relues visuellement (relecture 2026-09-07) ; la matrice $M$ est une formule, non un schéma manuscrit ; p. 3 = 2 lignes (Rq $b_k = 0$ pour $k < 0$ + CQFD souligné/flèche), sans schéma.

## Vocabulaire / notions

- **Division euclidienne** $A = BQ + R$, $\deg R < m - 1$ (convention d'auteur).
- **Système $(S)$** : $n-m+1$ équations à $n-m+1$ inconnues $(q_k)$.
- **Matrice triangulaire $M$**, $\det M = b_m^{n-m+2}$ [lecture incertaine sur l'exposant] $\neq 0$.
- **Mise en œuvre** : calcul de proche en proche des $q_k$ (bas de page biffé d'une grande croix).
