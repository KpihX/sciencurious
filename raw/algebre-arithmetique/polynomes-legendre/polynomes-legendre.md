# Polynômes de Legendre — transcription fidèle

> 🧾 **Manuscrit original :** `polynomes-legendre.pdf` (16 pages, scan manuscrit, encre bleue ; 499×720 pts, ~7,2 Mo) · ✍️ auteur non identifié. Construction des polynômes de Legendre comme base orthogonale de $\mathbb{R}[X]$ pour $P|Q = \int_{-1}^{1} P(t)Q(t)\,dt$ : processus de recherche (intégrations par parties, hypothèses simplificatrices), vérification (3–4 lemmes), normalisation (bêta d'Euler), formulation de Rodrigues, autres définitions (équation différentielle, endomorphisme), propriétés ($L_n(1)$, $L_n(-1)$, $L_n(0)$, parité, coefficients), identités combinatoires, équation de Legendre et relation de récurrence via la fonction génératrice.
> 🔍 **Statut :** lisible (~85 %), transcrit fidèlement. Aucune page dactylographiée (règle TAPUSCRIT sans objet). Aucune figure à reproduire (texte + équations uniquement).
> 📄 **Source scannée :** [`polynomes-legendre.pdf`](polynomes-legendre.pdf) (vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Polynômes de Legendre : Soit $E = \mathbb{R}[X]$. On munit $E$ du produit scalaire $P|Q = \int_{-1}^{1} P(t)Q(t)\,dt$

Note : Ces polynômes sont les plus simples possibles formant une base orthogonale de $E$

Désignons les par la famille $\mathcal{L} = \{L_n, n \in \mathbb{N}\}$ à déterminer. (avec $L_n$ de degré $n$ $\forall n \in \mathbb{N}$)

Astuce : Soit $m, n \in \mathbb{N}$ / $m > n$. On doit avoir $L_m|L_n = 0$

Il suffirait que $\forall k \in [\![0;n[\![$, $L_n|X^k = 0$ $\Leftrightarrow$ $L_n$ est orthogonal à tout polynôme de degré $< n$ ; et ainsi si $m > n$, on aurait alors $L_m|L_n = 0$

Processus de recherche :

NB : il ne s'agit pas d'une recherche exhaustive mais d'une recherche de $\mathcal{L}$ aussi simple que possible ce qui justifiera l'introduction progressive d'hypothèses simplificatrices.

Soit $n \in \mathbb{N}$. Cherchons $L_n$ aussi simple que possible

Soit $k \in [\![0;n[\![$.

On a : $L_n|X^k = 0 \Leftrightarrow \int_{-1}^{1} L_n(t)\,t^k\,dt = 0$

$\forall l \in \mathbb{N}$ posons $I_l L_n(t) = \underbrace{\int \dots \int}_{l \text{ fois}} L_n(t)\,dt^l$

---

## Page 2

Ainsi $L_n|X^k \Leftrightarrow \int_{-1}^{1} (I_1 L_n(t))'\,t^k\,dt = 0$

$\Leftrightarrow \left[I_1 L_n(t)\,t^k\right]_{-1}^{1} - k\int_{-1}^{1} I_1 L_n(t)\,t^{k-1}\,dt = 0$ pour $k \ge 1$ [reconstruction — motif : bas de page collé au bord, exposants peu lisibles]

$\Leftrightarrow -I_1 L_n(1)(1)^k = k\int_{-1}^{1} I_1 L_n(t)\,t^{k-1}\,dt$ [lecture incertaine]

Pour simplifier la recherche on va supposer $I_1 L_n(1) = 0$

Ainsi $L_n|X^k = 0 \Leftrightarrow \int_{-1}^{1} I_1 L_n(t)\,t^{k-1}\,dt = 0$ pour $k$ [lecture incertaine — « pour $k$ » seul, lire « pour $k \ge 1$ »]

En répétant le processus d'intégration par partie $k$ fois ($i \in [\![1;k]\!]$, $k \ge i$) et en fixant à chaque fois $I_i L_n(1) = 0$

on a : $L_n|X^k \Leftrightarrow \int_{-1}^{1} I_i L_n(t)\,t^{k-i}\,dt = 0$

En particulier, pour $i = k$, $L_n|X^k \Leftrightarrow \int_{-1}^{1} I_k L_n(t)\,dt = 0$

De ce qui précède il suffirait d'avoir $1$ et $-1$ comme racines de $I_k L_n$ pour tout $k \in [\![1;n]\!]$ et plus simplement [« plus simplement » raturé puis réécrit] d'avoir $1$ et $-1$ comme racines de $I_n L_n$.

($1$ et $-1$ comme racines de $I_n L_n$ [raturé et réécrit — lecture incertaine]. On inclut $n$ dû à la dernière égalité appliquée au cas $k = n$)

Ainsi il suffit d'avoir $I_n L_n = A_n((x-1)(x+1))^n = A_n(x^2-1)^n$ (vu que c'est un polynôme de degré $2n$) avec $A_n$ une constante pour $n$ fixé.

D'où $L_n(x) = A_n\,((x^2-1)^n)^{(n)}$

---

## Page 3

Vérification : Considérons $\mathcal{L} = \{L_n(x) = A_n(x^2-1)^{n(n)}, n \in \mathbb{N}\}$ où $(A_n)_{\mathbb{N}}$ est une suite quelconque / $\forall n \in \mathbb{N}$, $A_n \ne 0$.

• Mq $\mathcal{L}$ est une base de $\mathbb{R}[X]$.

Lemme 1 : $\forall n \in \mathbb{N}$, $L_n$ est un polynôme de degré $n$.

Ceci est dû au fait que le plus haut degré de $(x^2-1)^n$ [« le plus haut degré de $(x^2-1)^n$ » raturé] monôme de $A_n(x^2-1)^n$ est $A_n x^{2n}$ et donc le plus haut monôme de $L_n$ est $A_n A_{2n}^n x^n \ne 0$, d'où le résultat.

Lemme 2 : Toute famille $\mathcal{Q} = \{P_n(x) = \sum_{i=0}^{d_n} a_{n,i} x^i$ [lecture incertaine — indices], $n \in \mathbb{N}$ et $a_{n,d_n} \ne 0\}$, dite de polynômes échelonnés, forme une base de $\mathbb{R}[X]$.

• Libre : Soit $n \in \mathbb{N}^*$, $\mathcal{Q}_n = \{P_{d_k}(x) = \sum_{i=0}^{d_k} a_{k,i} x^i\}_{k=1}^n \subset \mathcal{Q}$ avec $a_{k,d_k} \ne 0$.

Cherchons $\beta_{k, k=\overline{1,n}}$ / $\sum_{k=1}^n \beta_k P_{d_k} = 0$ $(E)$.

SNALG on va supposer $\deg P_{d_n} > \deg P_{d_{n-1}} > \dots > \deg P_{d_1}$ [*sic* — SNALG, lire « sans nuire à la généralité » ; degrés strictement décroissants]

$(E) \Leftrightarrow \sum_{k=1}^n \beta_k \sum_{i=0}^{d_k} a_{k,i} x^i = 0$ avec $d_n > d_{n-1} > \dots > d_1$

$\Leftrightarrow \sum_{0 \le i \le d_k \le d_n} \beta_k a_{k,i} x^i = 0$

$\Leftrightarrow \sum_{i=0}^{d_n} \sum_{d_k \ge i} \beta_k a_{k,i} = 0$ | Rq : Dans $\sum_{d_k \ge i}$, $d_k$ ne vaut pas nécessairement pas par pas de $1$ [lecture incertaine]

$\Leftrightarrow \begin{cases} \beta_n a_{n,d_n} = 0 \to i = d_n \\ \beta_n a_{n,d_{n-1}} + \beta_{n-1} a_{n-1,d_{n-1}} = 0 \to i = d_{n-1} \\ \beta_n d_{n,n} + \beta_{n-1} d_{n-1,d_n} + \dots + \beta_1 a_{1,d_1} = 0 \to i = d_1 \end{cases}$ [reconstruction — motif : bas de page rogné]

---

## Page 4

Comme $\forall k \in [\![1;n]\!]$, $a_{k,d_k} \ne 0$ alors de proche en proche, on a : $\beta_n = \beta_{n-1} = \dots = \beta_1 = 0$, CQFD

• Génératrice : Soit $P(x) = \sum_{i=0}^n a_i x^i$. D'après ce qui précède, $\mathcal{Q}_n$ est libre et comme $\dim \mathbb{R}_n[X] = n$ alors $\mathcal{Q}_n$ est une base de $\mathbb{R}_n[X]$. Or $P \in \mathbb{R}_n[X]$ par conséquent $\exists \beta$ [premier jet biffé d'un grand trait en croix — remplacé par ce qui suit]

Génératrice : Soit $P(x) = \sum_{i=0}^n a_i x^i$. D'après ce qui précède, $\mathcal{Q}_n' = \{P_i\}_{i=0}^n \subset \mathcal{Q}$ est libre et comme $\dim \mathbb{R}_n[X] = n+1$ alors $\mathcal{Q}_n'$ est une base de $\mathbb{R}_n[X]$. Or $P \in \mathbb{R}_n[X]$, d'où $\exists!(\beta_k)_{k=0}^n$ / $P = \sum_{k=0}^n \beta_k P_k$, CQFD

D'où le résultat

En revenant à $\mathcal{L}$, comme $\mathcal{L}$ est une famille de polynômes échelonnés d'après le lemme 1, d'après le lemme 2, $\mathcal{L}$ forme une base de $\mathbb{R}[X]$.

---

## Page 5

• Mq $\mathcal{L}$ est orthogonale.

Lemme 3 : Soit $n \in \mathbb{N}^*$, [« $P_n(x) = \sum_{i=0}^n a_{n,i} x^i$ » raturé] $L_n(x) = A_n(x^2-1)^{n(n)}$. Soit $k \in [\![0;n[\![$. Mq $L_n|X^k = 0$

On a : $L_n|X^k = A_n\int_{-1}^{1} ((t^2-1)^n)^{(n)}\,t^k\,dt$

$= A_n\left(\left[((t^2-1)^n)^{(n-1)}\,t^k\right]_{-1}^{1} - k\int_{-1}^{1} ((t^2-1)^n)^{(n-1)}\,t^{k-1}\,dt\right)$

Lemme 4 : Soit $n \in \mathbb{N}$, $k \in [\![1;n]\!]$. Posons $L_{n,k}(x) = ((x^2-1)^n)^{(n-k)}$.

On a : $L_{n,k}(\pm 1) = 0$. En effet [« pour $k \le n-1$ » raturé]

On a : $L_{n,k}(x) = (((x-1)(x+1))^n)^{(n-k)}$

$= \sum_{i=0}^{n-k} C_{n-k}^i\,((x+1)^n)^{(i)}\,((x-1)^n)^{(n-k-i)}$ d'après Leibniz

$= \sum_{i=0}^{n-k} C_{n-k}^i\,A_n^i\,(x+1)^{n-i} \times A_n^{\,n-k-i}\,(x-1)^{k+i}$ [lecture incertaine — $A$ = arrangements]

$= (n-k)!\sum_{i=0}^{n-k} C_n^i C_n^{k+i}\,(x+1)^{n-i}\,(x-1)^{k+i}$ [reconstruction — motif : exposants superposés peu lisibles]

ainsi comme $n \ge k \ge 1$, $L_{n,k}(-1) = L_{n,k}(1) = 0$, CQFD car $n-i, k+i \ge 1$

Ainsi en appliquant ce lemme dans le lemme 3, on a : $L_n|X^k = -A_n k\int_{-1}^{1} ((t^2-1)^n)^{(n-1)}\,t^{k-1}\,dt$. En appliquant aussi $k$ fois une intégration par partie et en exploitant le lemme 4 (car $n-k \ge 1$ [lecture incertaine]), on aboutit à : $L_n|X^k = (-1)^k A_n k!\int_{-1}^{1} ((t^2-1)^n)^{(n-k)}\,dt = \left[((t^2-1)^n)^{(n-k-1)}\right]_{-1}^{1}$ [reconstruction — motif : suite page 6]

---

## Page 6

or d'après le lemme 4, comme $k+1 \in [\![2;n]\!] \subset [\![1;n]\!]$, on a : $L_n|X^k = 0$

En revenant à l'orthogonalité, soit $n, m \in \mathbb{N}$ / $m > n$. Mq $L_n|L_m = 0$

$\exists (a_i)_{i=\overline{0,n}}$ / $L_n(x) = \sum_{k=0}^n a_k x^k$

ainsi $L_m|L_n = \sum_{k=0}^n a_k\,L_m|X^k$. Comme $k \le n < m$ d'après le lemme 3, $L_m|X^k = 0$

d'où $L_m|L_n = 0$ CQFD

Donc $\mathcal{L} = \{L_n(x) = A_n(x^2-1)^{n(n)}, n \in \mathbb{N}$ avec $(A_n)_{\mathbb{N}}$ une suite réelle / $\forall n \in \mathbb{N}$, $A_n \ne 0\}$ est bien une base orthogonale de $\mathbb{R}[X]$.

Normalisation :

Soit $n \in \mathbb{N}^*$. Cherchons $A_n$ / $\|L_n\| = 1$

On a : $\|L_n\|^2 = \int_{-1}^{1} A_n((t^2-1)^n)^{(n)}\,L_n(t)\,dt$

$= A_n^2\left(\left[((t^2-1)^n)^{(n-1)}\,L_n(t)\right]_{-1}^{1} - \int_{-1}^{1} ((t^2-1)^n)^{(n-1)}\,(L_n)'(t)\,dt\right)$

$= 0$ d'après le lemme 4 (car $n \ge 1$) [le crochet est nul ; lecture incertaine]

En répétant ainsi l'intégration par partie, $n$ fois, on a : [suite page 7]

---

## Page 7

$\|L_n\|^2 = A_n^2\,(-1)^n\int_{-1}^{1} ((t^2-1)^n)\,((t^2-1)^n)^{(2n)}\,dt$ [reconstruction — motif : haut de page collé au bord]

$(x^2-1)^n$ est un polynôme de degré $2n$. Ainsi après $2n$ dérivées successives il ne reste plus que [symbole raturé]

d'où $\|L_n\|^2 = A_n^2\,(-1)^n\int_{-1}^{1} (2n)!\,(t^2-1)^n\,dt$ [Rq : $t^2-1 = (t-1)(t+1)$]

posons $u = \frac{1-t}{2}$

$\|L_n\|^2 = A_n^2\,(2n)!\,(-1)^n\int_{1}^{0} (-1)^n\,2^n\,u^n \times 2^n\,(1-u)^n\,(-2\,du)$

$= A_n^2\,(2n)!\,2^{2n+1}\int_{0}^{1} u^n\,(1-u)^n\,du$

$= A_n^2\,(2n)!\,2^{2n+1}\,\beta(n+1,n+1)$ où $\beta$ est la fct bêta d'Euler

$= A_n^2\,(2n)!\,2^{2n+1} \times \frac{\Gamma(n+1)\,\Gamma(n+1)}{\Gamma(2n+2)}$

$= \frac{A_n^2\,(2n)! \times 2^{2n+1} \times n! \times n!}{(2n+1)!}$

$\|L_n\|^2 = \frac{A_n^2 \times 2^{2n+1}\,{n!}^2}{2n+1}$

Ainsi $\|L_n\| = 1 \Leftrightarrow A_n = \frac{\sqrt{2n+1}}{2^n\,n!} \times \frac{1}{\sqrt{2}} = \frac{1}{2^n n!}\sqrt{n+\frac{1}{2}}$

• pour $n = 0$, $L_0(x) = A_0$ d'où $\|L_0\|^2 = 2A_0^2$ et pour avoir $\|L_0\| = 1$ il faut et il suffit que $A_0 = \frac{1}{\sqrt{2}} = \frac{1}{2^0\,0!}\sqrt{0+\frac{1}{2}}$

---

## Page 8

De façon générale $\mathcal{L} = \{L_n(x) = A_n\,(x^2-1)^{n(n)}, n \in \mathbb{N}\}$ est une base orthonormale de $\mathbb{R}[X]$ ssi $\forall n \in \mathbb{N}$, $A_n = \frac{1}{2^n n!}\sqrt{n+\frac{1}{2}}$.

Conventionnellement pour ne pas s'encombrer des radicaux, on définit les polynômes de [« Lagrange » raturé, corrigé en] Legendre suivant la formulation de Rodrigues : $\mathcal{L} = \{\frac{1}{2^n n!}(x^2-1)^{n(n)} = L_n(x), \forall n \in \mathbb{N}\}$

et on a : $\forall m, n \in \mathbb{N}$, $\boxed{L_n|L_m = \frac{2\,\delta_{mn}}{2n+1}}$

Autres deff [*sic* — lire « définitions »] :

• les polynômes de Legendre sont les solutions polynomiales de l'éqn diff [*sic* — lire « équation différentielle »] de Legendre : $\frac{d}{dx}\left((1-x^2)\,\frac{d}{dx}P_n(x)\right) + n(n+1)\,P_n(x) = 0$ dans le cas particulier où $n \in \mathbb{N}$. Ce sont encore les fonctions propres de l'endomorphisme définie [*sic* — lire « défini »] sur $\mathbb{R}(X)$ [*sic* — lire $\mathbb{R}[X]$] par $\forall P \in \mathbb{R}(X)$, $u(P) = \frac{d}{dx}\left((1-x^2)\,\frac{d}{dx}P(x)\right)$ pour la valeur propre $-n(n+1)$, $n \in \mathbb{N}$.

---

## Page 9

Rqs préliminaires [*sic* — lire « Remarques »] :

Soient $L_n(x) = \frac{1}{2^n n!}(x^2-1)^{n(n)}$, $n \in \mathbb{N}$

$= \frac{1}{2^n n!}\left((x-1)^n(x+1)^n\right)^{(n)}$

$= \frac{1}{2^n n!}\sum_{k=0}^n C_n^k\,((x-1)^n)^{(k)}\,((x+1)^n)^{(n-k)}$

$= \frac{1}{2^n n!}\sum_{k=0}^n C_n^k\,A_n^k\,(x-1)^{n-k}\,A_n^{\,n-k}\,(x+1)^k$

d'où $\boxed{L_n(x) = \frac{1}{2^n}\sum_{k=0}^n (C_n^k)^2\,(x-1)^{n-k}\,(x+1)^k} = \frac{n}{2^n}\sum_{k=0}^n (C_{n_0}^k)$ [reconstruction — motif : surcharge raturée illisible]

• Déduction : $L_n(1) = \frac{(C_n^n)^2}{2^n}(1+1)^n = 1$

$L_n(-1) = \frac{1}{2^n}(C_n^0)^2\,(-1-1)^n = (-1)^n$

$L_n(0) = \frac{1}{2^n}\sum_{k=0}^n (C_n^k)^2\,(-1)^k$

• Parité de $L_n$ : $L_n(-x) = \frac{1}{2^n}\sum_{k=0}^n (C_n^k)^2\,(-1)^k\,(x-1)^k\,(x+1)^{n-k}$ [reconstruction — motif : ligne très serrée]

$L_n(-x) = (-1)^n \cdot L_n(x) \Leftrightarrow \begin{cases} L_n \text{ paire ssi } n \text{ pair} \\ L_n \text{ impaire ssi } n \text{ impair} \end{cases}$

• Comme $L_n$ est un polynôme de degré $n$, le coefficient du monôme $x^k$ ($k \in [\![0;n]\!]$) est $\frac{L_n^{(k)}(0)}{k!} = \frac{1}{2^n n!\,k!}\,((x^2-1)^n)^{(n+k)}(0)$

---

## Page 10

• Formule générale de $P_{n,k}(x) = \frac{1}{2^n n!}(x^2-1)^{n(k)}$ [$P_{n,k}$ = dérivée $k$-ième de $(x^2-1)^n$ normalisée]

[« Approche 2 » raturé] Rq : si $k > 2n$, $P_{n,k}(x) = 0$

— Approche 1 :

$P_{n,k}(x) = \frac{1}{2^n n!}\left((x-1)^n(x+1)^n\right)^{(k)}$

$= \frac{1}{2^n n!}\sum_{i=0}^k C_k^i\,((x-1)^n)^{(i)}\,((x+1)^n)^{(k-i)}$

$= \frac{1}{2^n n!}\sum_{i=0}^k C_k^i\,A_n^i\,(x-1)^{n-i}\,A_n^{\,k-i}\,(x+1)^{n-k+i}$

$= \frac{k!}{2^n n!}\sum_{i=0}^n C_n^i C_n^{k-i}\,(x-1)^{n-i}\,(x+1)^{n-k+i} = \frac{k!}{2^n n!}\sum_{i=0}^k C_n^i C_n^{k-i}\,(x-1)^{n-i}(x+1)^{n-k+i}$ [les deux bornes $n$ et $k$ coexistent — lecture incertaine]

Ainsi le coef du monôme de degré $k$ dans $L_n(x)$ est $\frac{1}{2^n n!\,k!}(x^2-1)^{n(n+k)}(0) = \frac{1}{2^n n!\,k!} \times (n+k)!\sum_{i=k}^n C_n^i C_n^{i-k}\,(-1)^{n-i}$ [car $C_n^{-m} = 0$ si $m < 0$]

$= \frac{C_{n+k}^k}{C_{2n}^n}\sum_{i=k}^n C_n^i C_n^{i-k}\,(-1)^i$ [reconstruction — motif : exposants de $(-1)$ raturés et réécrits]

Ainsi par exemple, le coef du monôme de degré $n$ est $\boxed{\frac{C_{2n}^n}{2^n}}$

---

## Page 11

— Approche 2 :

$P_{n,k}(x) = \left(\sum_{i=0}^n C_n^i\,x^{2i}\,(-1)^{n-i}\right)^{(k)} \times \frac{1}{2^n n!}$

$= \frac{1}{2^n n!}\sum_{i \ge k/2}^n C_n^i\,(-1)^{n-i}\,A_{2i}^k\,x^{2i-k}$

Ainsi ce coef est : [« Ainsi ce coef est : » raturé]

$\frac{1}{2^n n!\,k!}(x^2-1)^{n(n+k)}(0) = \frac{1}{2^n n!\,k!} \times \sum_{i \ge (n+k)/2}^n C_n^i\,(-1)^{n-i}\,A_{2i}^{\,n+k}\,x^{2i-n-k}$

D'où $\frac{1}{2^n n!\,k!}(x^2-1)^{n(n+k)}(0) = \begin{cases} \text{si } n \text{ pair} \\ \quad \cdot \text{ Si } k \text{ pair : } \frac{C_n^{(n+k)/2}\,(-1)^{(n-k)/2} \times A_{n+k}^k}{2^n} \\ \quad \cdot \text{ Si } k \text{ impair, on a : } 0 \\ \cdot \text{Si } n \text{ impair} \\ \quad \cdot \text{ Si } k \text{ impair, on a : } \frac{C_n^{(n+k)/2}\,(-1)^{(n-k)/2}\,A_{n+k}^k}{2^n} \\ \quad - \text{Si } k \text{ pair, on a : } 0 \end{cases}$

De façon générale, $L_n(x) = \frac{1}{2^n n!}\sum_{i \ge n/2}^n C_n^i\,(-1)^{n-i}\,A_{2i}^n\,x^{2i-n}$

— Identités remarquables :

$L_n(0) = \frac{1}{2^n}\sum_{k=0}^n (C_n^k)^2\,(-1)^k = \frac{1}{2^n n!}\sum_{i \ge n/2}^n C_n^i\,(-1)^{n-i}\,A_{2i}^n\,0^{2i-n}$

$= \begin{cases} \dfrac{C_n^{n/2}\,(-1)^{n/2}}{2^n} & \text{si } n \text{ pair} \\ 0 & \text{si } n \text{ impair} \end{cases}$

---

## Page 12

d'où les identités : $\boxed{\sum_{k=0}^n (C_n^k)^2\,(-1)^k = \begin{cases} 0 & \text{si } n \text{ impair} \\ C_n^{n/2}\,(-1)^{n/2} & \text{si } n \text{ pair} \end{cases}}$

$\downarrow$ généralisation

• Pour les coefs [formule d'appel raturée] $\sum_{i=k}^n C_n^i C_n^{i-k}\,(-1)^i = \begin{cases} 0 & \text{si } k \text{ et } n \text{ de parités opposées} \\ C_n^{(n+k)/2}\,(-1)^{(n+k)/2} & \end{cases}$ [reconstruction — motif : seconde branche raturée et réécrite, exposants peu lisibles]

De façon générale pour $k \in [\![0;2n]\!]$, $P_{n,k}(x) = \frac{k!}{2^n n!}\sum_{i=0}^n C_n^i C_n^{k-i}\,(x-1)^{n-i}\,(x+1)^{n-k+i}$

$= \frac{1}{2^n n!}\sum_{i \ge k/2} C_n^i\,(-1)^{n-i}\,A_{2i}^k\,x^{2i-k}$ ($k \ge 0$)

• pour $x = 0$, $\sum_{i=0}^k C_n^i C_n^{k-i}\,(-1)^{n-i} = \begin{cases} 0 & \text{si } k \text{ impair ou } n < \frac{k}{2} \\ C_n^{k/2}\,(-1)^{\frac{n-k}{2}} & \end{cases}$ [reconstruction — motif : exposants raturés] [« $\sum C_n^i C_n^{k-i}$ » raturé puis réécrit]

• Pour $x = 1$, $\sum_{i \ge k/2}^n C_n^i\,(-1)^{n-i}\,A_{2i}^k = \begin{cases} 0 & \text{si } n > k \\ k!\,C_n^{k-n} \times 2^{2n-k} & \text{sinon} \end{cases}$

• Pour $x = -1$, $\sum_{i \ge k/2}^n C_n^i\,(-1)^{n+k-i}\,A_{2i}^k = \begin{cases} 0 & \text{si } n > k \\ k!\,C_n^{k-n} \times (-2)^{2n-k} & \text{sinon} \end{cases}$

---

## Page 13

De façon générale, pour $k, n \in \mathbb{N}$ — en prenant par convention $C_n^k = 0 \Leftrightarrow n > k$ [*sic* — lire $k > n$] et $C_n^{-k} = 0 \Leftrightarrow k \ne 0$ :

• $\sum_{i=k}^n C_n^i C_n^{i-k}\,(-1)^i = \begin{cases} 0 & \text{ssi } n+k \notin 2\mathbb{N} \text{ ou } n < k \\ C_n^{(n+k)/2}\,(-1)^{(n+k)/2} & \\ C_n^{(n-k)/2}\,(-1)^{(n-k)/2} & \text{sinon} \end{cases}$ [deux branches « sinon » coexistantes — lecture incertaine]

• $\sum_{i=k-n}^k C_n^i C_n^{k-i}\,(-1)^i = \begin{cases} 0 & \text{ssi } k \in 2\mathbb{N}+1 \text{ ou } n < k/2 \\ (-1)^{k/2}\,C_n^{k/2} & \text{sinon} \end{cases}$

• $\sum_{i \ge k/2}^n C_n^i\,(-1)^i\,A_{2i}^k = \begin{cases} 0 & \text{si } n > k \\ k!\,(-1)^n \times C_n^{k-n} \times 2^{2n-k} & \text{sinon} \end{cases}$

---

## Page 14

$L_n'(x) = \frac{1}{2^n}\sum_{k=0}^n (C_n^k)^2\,\left((n-k)(x-1)^{n-k-1}(x+1)^k + k\,(x-1)^{n-k}(x+1)^{k-1}\right)$

$((1-x^2)L_n'(x))'$ [calcul :] $= \frac{-1}{2^n}\sum_{k=0}^n (C_n^k)^2\,\Big((n-k)(n+k)(x-1)^{n-k-1} + k(n-k)(x-1)^{n-k}(x+1)^{k-1}$ [reconstruction — motif : exposants superposés illisibles] [idem]

$+ k\big((n+k+1)(x-1)^{n-k}(x+1)^{k-1} + k\,(x-1)^{n-k+1}(x+1)^{k-2}\big)\Big)$ [idem — exposants superposés illisibles, cf. ligne précédente]

$= \frac{-1}{2^n}\left(\sum_{k=0}^n (C_n^k)^2\,(n-k)^2\,(x-1)^{n-k-1}(x+1)^{k+1} + k^2(x-1)^{n-k+1}(x+1)^{k-1}\right.$ [idem — exposants superposés illisibles]

$\left. + 2k(n-k)\,(x-1)^{n-k}(x+1)^k + n\,(x-1)^{n-k}(x+1)^k\right)$

$= \frac{-1}{2^n}\left(n\,L_n(x) + \sum_{k=0}^{n-1} k^2\,(C_{n-1}^{\,n+k-1})^2 + \sum_{k=1}^n k^2\,C_{n-1}^{k-1}\right.$ [lecture incertaine] [(reconstruction — motif : fin de ligne rognée)]

$\left. + 2\sum_{k=0}^n k^2\,C_{n-1}^{k-1} \times C_{n-1}^{\,n-k}\,(x-1)^{n-k}(x+1)^k\right)$

$= -\frac{1}{2^n}\left(nL_n(x) + n^2\left(\sum_{k=0}^n (C_{n-1}^{\,n-k})^2\,(x-1)^{n-k}(x+1)^k + \sum_{k=0}^n (C_{n-1}^k)^2\right.\right.$ [(reconstruction — motif : exposants rognés)]

$\left.\left. + 2\sum_{k=0}^n C_{n-1}^{k-1}\,C_{n-1}^{\,n-k}\,(x-1)^{n-k}(x+1)^k\right)\right)$

$= -\frac{n}{2^n}\left(L_n(x) + n\left(\sum_{k=0}^n (C_{n-1}^{\,n-k})^2\,(x-1)^{n-k}(x+1)^k + \sum_{k=0}^n (C_{n-1}^k)^2\,(x-1)^{n-k}(x+1)^k + \sum_{k=0}^n C_{n-1}^{k-1}\,C_{n-1}^{\,n-k}\,(x-1)^{n-k}(x+1)^k\right)\right)$ [reconstruction — motif : bas de page très serré, parenthésage incertain]

car $C_{n-1}^n = 0$

---

## Page 15

$((1-x^2)L_n'(x))'$ [suite :]

$= -\frac{n}{2^n}\left(L_n(x) + n\left(\sum_{k=0}^n C_{n-1}^{k-1}\,(C_{n-1}^{k-1} + C_{n-1}^k)\,(x-1)^{n-k}(x+1)^k\right.\right.$

$\left.\left. + \sum_{k=0}^n C_{n-1}^k\,(C_{n-1}^k + C_{n-1}^{k-1})\,(x-1)^{n-k}(x+1)^k\right)\right)$

$= -n\left(L_n(x) + \frac{n}{2^n}\left(\sum_{k=0}^n C_{n-1}^{k-1} \times C_n^k\,(x-1)^{n-k}(x+1)^k\right.\right.$

$\left.\left. + \sum_{k=0}^n C_{n-1}^k\,C_n^k\,(x-1)^{n-k}(x+1)^k\right)\right)$

$= -n\left(L_n(x) + \frac{n}{2^n}\sum_{k=0}^n C_n^k\,(C_{n-1}^{k-1} + C_{n-1}^k)\,(x-1)^{n-k}(x+1)^k\right)$

$= -n\left(L_n(x) + \frac{n}{2^n}\sum_{k=0}^n C_n^k\,C_n^k\,(x-1)^{n-k}(x+1)^k\right)$

$= -n\left(L_n(x) + n\,L_n(x)\right)$

d'où $\underline{((1-x^2)\,L_n'(x))' = -n(n+1)\,L_n(x)}$ CQFD

\* Relation de récurrence : Sur $L_n$

• fonction génératrice : En faisant recoure [*sic* — lire « recours »] aux notions sur les séries de Lagrange [*sic* — lire « Legendre »], on a $\sum_{n=0}^{+\infty} P_n(x)\,t^n = \frac{1}{\sqrt{1-2xt+t^2}}$

---

## Page 16

Ainsi en dérivant, on a : $\frac{-t+x}{\sqrt{1-2xt+t^2}} = (1-2xt+t^2)\sum_{n=1}^{+\infty} n\,P_n(x)\,t^{n-1}$ [« (par rapport à $t$) » raturé en marge]

d'où $(-t+x)\sum_{n=0}^{+\infty} P_n(x)\,t^n = \sum_{n=0}^{+\infty} (n+1)\,P_{n+1}(x)\,t^n \times (1-2xt+t^2)$ [grand trait diagonal biffant le membre de droite — calcul repris ci-dessous]

c-à-d $-\sum_{n=0}^{+\infty} P_n(x)\,t^{n+1} + \sum_{n=0}^{+\infty} xP_n(x)\,t^n = \sum_{n=0}^{+\infty} (n+1)\,P_{n+1}(x)\,t^n$

$- 2x\sum_{n=0}^{+\infty} (n+1)\,P_{n+1}(x)\,t^{n+1} + \sum_{n=0}^{+\infty} (n+1)\,P_{n+1}(x)\,t^{n+2}$ [reconstruction — motif : ligne biffée en diagonale, ordre des termes incertain]

c-à-d $(-t+x)\sum_{n=0}^{+\infty} P_n(x)\,t^n = \sum_{n=0}^{+\infty} (n+1)\,P_{n+1}(x)\,t^n + 2x\sum_{n=1}^{+\infty} nP_n(x)\,t^n$ [lecture incertaine] $+ \sum_{n=2}^{+\infty} (n-1)\,P_{n-1}(x)\,t^n$

c-à-d $-\sum_{n=1}^{+\infty} P_{n-1}(x)\,t^n + x\sum_{n=0}^{+\infty} P_n(x)\,t^n = \sum_{n=0}^{+\infty} (n+1)\,P_{n+1}(x)\,t^n - 2x\sum_{n=1}^{+\infty} nP_n(x)\,t^n + \sum_{n=2}^{+\infty} (n-1)\,P_{n-1}(x)\,t^n$

D'où $\begin{cases} \cdot \text{ pour } n = 0, xP_0(x) = P_1(x) \\ \cdot \text{ pour } n = 1, -P_0(x)\,t + xP_1(x)\,t = P_2(x)\,t - 2xP_1(x)\,t \\ \cdot \text{ pour } n \ge 2, -P_{n-1}(x) + xP_n(x) + (n+1)P_{n+1}(x) - 2xnP_n(x) + (n-1)P_{n-1}(x) \end{cases}$ [termes raturés — branche n = 1] [signe ± raturé — lire +]

d'où $\boxed{(n+1)\,P_{n+1}(x) = x(2n+1)\,P_n(x) - n\,P_{n-1}(x)}, \forall n \in \mathbb{N}^*$ avec $P_0(x) = 1$, $P_0(x) = x$ [*sic* — lire $P_1(x) = x$]

---

## Figures

Aucune figure détectée sur les 16 pages : le manuscrit ne contient que du texte et des équations manuscrites (ni graphe, ni courbe de $L_n$/$P_n$, ni schéma). Motif : vérification visuelle page par page des rendus `/tmp/leg/page-*.png` — aucun axe, aucune courbe, aucun encadré de type illustration. P.8 (plg-08, sautée au passage précédent) vérifiée visuellement au 2e passage le 2026-09-07 (rendu `/tmp/s16/plg-p8-08.png`, r150) — base orthonormale ($A_n$), « Lagrange » raturé corrigé en Legendre, Rodrigues, $\boxed{L_n|L_m = 2\delta_{mn}/(2n+1)}$, « deff », « eqn diff », « définie », $\mathbb{R}(X)$ (*sic* maintenus) confirmés ; aucune figure p.8.

En conséquence : aucun script `reproduce_polynomes_legendre_N.py` créé, aucun PNG dans `polynomes-legendre/assets/` (dossier non créé), aucune image embarquée.

---

## Vocabulaire

- $M|N$ / $P|Q$ = produit scalaire $\int_{-1}^{1} P(t)Q(t)\,dt$ (barre verticale, jamais $\langle\cdot,\cdot\rangle$).
- $X^k$, $x^k$ = monômes ; $L_n$, $P_n$ = le même polynôme de Legendre (notation $L$ p. 1–15, $P$ p. 15–16).
- $(x^2-1)^{n(n)}$, $^{n(k)}$ = dérivée $n$-ième (resp. $k$-ième) ; $^{(n+k)}$, $'$ : mêmes conventions.
- $I_l$ = primitive $l$-ième itérée ; $I_i L_n(1) = 0$ = hypothèse simplificatrice.
- $C_n^k$ = coefficient binomial ; $A_n^k$, $A_{2i}^k$ = arrangements ; $\beta$, $\Gamma$ = fonctions d'Euler ; $\delta_{mn}$ = symbole de Kronecker.
- Mq = « montrons que » (lu « Mhy ») ; SNALG = « sans nuire à la généralité » [*sic*] ; Rq(s) = remarque(s) ; Rqs préliminaires = remarques préliminaires ; deff = définitions ; eqn diff = équation différentielle ; fct = fonction ; coef = coefficient ; CQFD ; NB ; càd ; Rq.
- Coquilles conservées avec [*sic*] : « Lagrange » pour Legendre (p. 8, 15), $C_n^k = 0 \Leftrightarrow n > k$ (p. 13), $P_0(x) = x$ pour $P_1$ (p. 16), « définie », « recoure », $\mathbb{R}(X)$ pour $\mathbb{R}[X]$, $\dim \mathbb{R}_n[X] = n$ (p. 4, premier jet).
- Passages biffés (non transcrits en propre, signalés en place) : premier jet « Génératrice » p. 4, « $P_n(x) = \sum a_{n,i}x^i$ » p. 5, « pour $k \le n-1$ » et « Ainsi ce coef est » p. 5/11, « Approche 2 » p. 10, membre de droite de l'équation génératrice p. 16.
