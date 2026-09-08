# Polynôme produit-somme, indépendance et indicatrice d'Euler — transcription fidèle

> 🧾 **Manuscrit original :** `polynome-produit-somme-independance.pdf` (scan, 6 pages) · 📅 16/10/2021 · ✍️ KpihX
> 🔍 **Statut :** lisible, transcrit mot à mot. Les maths sont conservées telles quelles ; les ratures sont notées `[raturé]`, les lectures douteuses `[lecture incertaine — …]`.
> 📄 **Source scannée :** [`polynome-produit-somme-independance.pdf`](polynome-produit-somme-independance.pdf) (restaurée depuis Datas1, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

Exo1 (Algèbre) : Soit $P \in \mathbb{C}_n[X]$. Vu que [lecture incertaine — amorce coupée en haut de page]

D'après le théo de Gauss, $\exists!\ (a_n, \dots) \in \mathbb{C}\ /\ P(X) = a_n \prod_{i=1}^n (X - x_i)$

(avec éventuellement le cas où $\exists\ i, j \in [\![1, n]\!]\ /\ x_i = x_j$)

alors $P(X) = a_n \sum_{J \subseteq I_n} (-1)^{|J|} X^{n-|J|} \prod_{j \in J} x_j$

où $I_n = [\![1, n]\!]$ [lecture incertaine — noté « $x_1, \dots, x_n$ » sous la somme] et $x_1, \dots, x_n$.

Preuve : Il suffit de mtq $\forall\ X, (x_i)_{i} \in K$ sous $K$ est un corps commutatif [lecture incertaine — fin de ligne] :

$$\prod_{i=1}^n (X - x_i) = \sum_{J \subseteq I_n} (-1)^{|J|} X^{n-|J|} \prod_{j \in J} x_j \text{ avec } \prod_{j \in \emptyset} x_j = 1$$

Métho : Tout terme du développement de $\prod$ est obtenu en prélevant un terme dans chaque facteur et en effectuant le produit. Ainsi pour chaque terme de $\prod$, $\exists\ K \in [\![0, n]\!],\ (i_j)_{k \in [\![1, n]\!]}$ tel que pour l'avoir, on a prélevé $X$ dans $n-K$ facteurs (et les scalaires $(x_{ij})$ dans les $K$ autres facteurs) et puis on a effectué leur produit avec $\sum_{1 \le i_1 < \dots < i_K \le n} \prod_{j=1}^K (-x_{ij})$ [lecture incertaine — ligne de calcul raturée/surchargée].

Ainsi : $\prod_{i=1}^n (X - X_i) = \sum_{K=0}^n \sum_{1 \le i_1 < \dots < i_K \le n} X^{n-K} \prod_{j=1}^K (-X_{ij})$ [lecture incertaine — le manuscrit porte « $\prod (1 - X_{ij})$ », lecture retenue $(-X_{ij})$ par cohérence avec la suite]

$$= \sum_{K=0}^n (-1)^K X^{n-K} \sum_{1 \le i_1 < \dots < i_K \le n} \prod_{j=1}^K X_{ij}$$

Donc $\prod_{i=1}^n (X - X_i) = \sum_{J \subseteq I_n} (-1)^{|J|} X^{n-|J|} \prod_{j \in J} X_j$ où $I_n = [\![1, n]\!]$.

## Page 2

Théo : Soit $n \in \mathbb{N}^*$ et $P(n)$ : « $\forall\ X,\ \forall\ (x_i)_n \in K$, $\prod_{i=1}^n (X - x_i) = \sum_{J \subseteq [\![1, n]\!]} (-1)^{|J|} X^{n-|J|} \prod_{j \in J} x_j$ avec $\prod_{j \in \emptyset} x_j = 1$ ».

Pour $n = 1$, $\sum_{J \subseteq [\![1, 1]\!]} (-1)^{|J|} X^{1-|J|} \prod_{j \in J} x_j = \underbrace{(-1)^0 X^{1-0} \times 1}_{J = \emptyset} + \underbrace{(-1)^1 X^{1-1} X_1}_{J = \{1\}}$

$$= X - X_1 = \prod_{i=1}^1 (X - x_i)$$

donc $P(1)$ vraie.

— Supp que pour $n \in \mathbb{N}^*$, $P(n)$ est vraie et mtq $P(n+1)$ l'est aussi. Soient $X, (x_i)_{1, n+1} \in K$.

On a : $\prod_{i=1}^{n+1} (X - X_i) = (X - X_{n+1}) \sum_{J \subseteq [\![1, n]\!]} (-1)^{|J|} X^{n-|J|} \prod_{j \in J} X_j$ car $P(n)$ vraie

$$= \sum_{J \subseteq [\![1, n]\!]} (-1)^{|J|} X^{n+1-|J|} \prod_{j \in J} X_j + \sum_{J \subseteq [\![1, n]\!]} (-1)^{|J|+1} X^{n-|J|} \left(\prod_{j \in J} X_j\right) X_{n+1} \text{ [lecture incertaine — découpage $n+1 \notin J$ / $n+1 \in J$]}$$

$$= \sum_{\substack{J \subseteq [\![1, n+1]\!] \\ n+1 \notin J}} (-1)^{|J|} X^{n+1-|J|} \prod_{j \in J} X_j + \sum_{\substack{J \subseteq [\![1, n+1]\!] \\ n+1 \in J}} (-1)^{|J|} X^{n+1-|J|} \prod_{j \in J} X_j \text{ [lecture incertaine — reparamétrisation, bas de page très chargé]}$$

$$= \sum_{J \subseteq [\![1, n+1]\!]} (-1)^{|J|} X^{n+1-|J|} \prod_{j \in J} X_j.$$

## Page 3

d'où $P(n+1)$ vraie.

CQFD.

Corollaire : Pour $P \in \mathbb{C}_n[X]$ ($n \in \mathbb{N}^*$). Vu $\exists\ (a_i)_{0, n},\ (X_i)_{1, n} \in \mathbb{C}\ /\ P(X) = a_n \prod_{i=1}^n (X - X_i) = \sum_{i=0}^n a_i X^i$ et que $\prod_{i=1}^n (X - X_i) = \sum_{J \subseteq [\![1, n]\!]} (-1)^{|J|} X^{n-|J|} \prod_{j \in J} X_j$ avec $\prod_{j \in \emptyset} X_j = 1$, on conclut par identification que : $\forall\ i \in [\![1, n]\!],\ a_i = a_n \sum_{\substack{J \subseteq [\![1, n]\!] \\ |J| = n-i}} (-1)^{n-i} \prod_{j \in J} X_j = (-1)^{n-i} \sum_{\substack{J \subseteq [\![1, n]\!] \\ |J| = n-i}} \prod_{j \in J} X_j$ [lecture incertaine — exposant noté $n_i$ / $n-i$],

ou encore $a_i = (-1)^{\dots} \sum_{1 \le i_1 < \dots < i_{n-i} \le n} \left(\prod_{j=1}^{\dots} X_{ij}\right) a_n$ [lecture incertaine — ligne biffée/surchargée].

App : Pour $n = 4$, on a : $P(X) = \sum_{i=0}^4 a_i X^i = a_4 \prod_{i=1}^4 (X - X_i)$ d'où $\begin{cases} a_4 = a_4 \\ a_3 = -(X_1 + X_2 + X_3 + X_4)\, a_4 \\ a_2 = (X_1X_2 + X_1X_3 + X_1X_4 + X_2X_3 + X_2X_4 + X_3X_4)\, a_4 \\ a_1 = -(X_1X_2X_3 + X_1X_2X_4 + X_1X_3X_4 + X_2X_3X_4)\, a_4 \\ a_0 = X_1X_2X_3X_4\, a_4 \end{cases}$

## Page 4

Corollaire (Proba) : Soient $(\Omega, \mathcal{E}, P)$ un esp probabilisé, $n \in \mathbb{N}^*$. $P(n)$ : « $\forall\ (A_i)_n \in \mathcal{E}$, $P(\dots)$ [lecture incertaine — amorce rognée à gauche] $(\overline{A_i})_n$ mutuellement indépendants $\iff$ $(A_i)_n$ mutuellement indépendantes » est vraie.

NB : $(A_i)_n$ mutuellement indépendant $\iff$ $\forall\ J \subseteq [\![1, n]\!]$ ($J \subseteq [\![1, n]\!] \iff (J \subseteq [\![1, n]\!] \land J \ne \emptyset)$), $P(\bigcap_{j \in J} A_j) = \prod_{j \in J} P(A_j)$.

Preuve : on montrera juste le sens $\implies$ car celui $\impliedby$ se déduit du $1^{er}$ en ce que $\forall\ i \in [\![1, n]\!],\ A_i = \overline{\overline{A_i}}$.

Soit donc $n \in \mathbb{N}^*$, $(A_i)_n \in \mathcal{E}$ / $(A_i)_n$ mutuellement indépendants.

Soit $J \subseteq^* [\![1, n]\!]$, on a : $J = \{j_1, \dots\}$ [lecture incertaine — ligne rognée].

Or : $P(\bigcap_{j \in J} \overline{A_j}) = P(\overline{\bigcup_{j \in J} A_j}) = 1 - P(\bigcup_{j \in J} A_j) = 1 - P(\bigcup_{j \in J} \dots)$ [lecture incertaine — fin rognée].

Lemme : Soient $(A_i)_n \in \mathcal{E}$ des évts mut ind d'un ep $(\Omega, \mathcal{E}, P)$. $P(\bigcup_{i=1}^n A_i) = 1 - \prod_{i=1}^n (1 - P(A_i)) \iff 1 - P(\bigcup_{i=1}^n A_i) = \prod_{i=1}^n (1 - P(A_i))$.

En effet $P(\bigcup_{i=1}^n A_i) = \sum_{J \subseteq^* [\![1, n]\!]} (-1)^{|J|+1} P(\bigcap_{j \in J} A_j)$ [lecture incertaine — symbole de sommation surchargé]

$$= -\sum_{J \subseteq [\![1, n]\!]} (-1)^{|J|} \prod_{j \in J} P(A_j)$$

$$= -\left(\sum_{J \subseteq [\![1, n]\!]} (-1)^{|J|} \prod_{j \in J} P(A_j) - 1\right)$$

$$= -\left(\prod_{i=1}^n (1 - P(A_i)) - 1\right) = 1 - \prod_{i=1}^n (1 - P(A_i))$$

d'où $P(\bigcup A_i) = \dots$ [lecture incertaine — renvoi]. Ainsi $P(\bigcap \overline{A_j}) = \prod_{j \in J} (1 - P(A_j)) = \prod_{j \in J} P(\overline{A_j})$. CQFD.

## Page 5

Appl. Étude de l'indicatrice de Euler $\varphi : \mathbb{N}^* \to \mathbb{N}$, $n \mapsto \varphi(n) =$ nbre de nbres inférieurs [lecture incertaine — « ou égaux » ?] à $n$ et premiers avec $n$ $= |\{m \in [\![1, n]\!]\ /\ m \land n = 1\}|$.

[raturé]. $\varphi(1) = |\{1 \land 1\}| = 1$.

$\varphi(n) = ?$ pour $n \ge 2$.

Soit l'expérience consistant à prélever un nbre dans $[\![1, n]\!]$. Considérons l'esp probabiliste associé $(\Omega, \mathcal{B}(\Omega), P)$ où $\Omega = [\![1, n]\!]$ et : $P : \mathcal{B}(\Omega) \to [0, 1]$, $\omega \mapsto P(\omega)$ vérifiant la condition d'équiprobabilité c-à-d $P(\omega) = \frac{|\omega|}{|\Omega|} = \frac{|\omega|}{n}$ [lecture incertaine — noté $P(\omega) = |w|/|Ω|$].

Soient $\{p_k\}_{1, m}$ les diviseurs $1^{ers}$ de $n$. Considérons $A$ : « le nbre prélevé est $1^{er}$ avec $n$ ». On a : $P(A) = \frac{\varphi(n)}{n}$. $A_k$ ($1 \le k \le m$) : « le nbre prélevé est multiple de $p_k$ ».

Or : $\bigcup_{k=1}^m A_k$ : « le nbre prélevé et $n$ admettent au moins un diviseur premier commun » $= \overline{A}$.

Ainsi on a encore $P(A) = P(\overline{\bigcup_{k=1}^m A_k}) = P(\bigcap_{k=1}^m \overline{A_k})$.

* Justifions que $A_k$ ($1 \le k \le m$) sont mutuellement ind. Soit $J \subseteq [\![1, m]\!] = \{i_j\}_p$, $p \in [\![1, |J|]\!]$ [lecture incertaine — bas de page rogné].

## Page 6

Or : $P(\bigcap_{j \in J} A_j) = P(\text{« le nbre prélevé est multiple de } P_{ij}\ \forall\ j \dots \text{ »})$ [lecture incertaine — rogné à droite]. Or $\mathrm{ppcm}\{P_{ij}\} = \prod_{j \in J} P_{ij}$ ainsi les multiples communs des $P_{ij}$ (entre $1$ et $n$) sont $\prod_{j \in J} P_{ij},\ 2\prod_{j \in J} P_{ij},\ \dots,\ q\prod_{j \in J} P_{ij}$ [lecture incertaine — noté avec accolade $\underbrace{\dots}_n$], d'où $|\bigcap_{j \in J} A_j| = q = \frac{n}{\prod_{j \in J} P_{ij}}$.

Ainsi $P(\bigcap_{j \in J} A_j) = \frac{n / \prod P_{ij}}{n} = \prod_{j \in J} \frac{1}{P_{ij}}$.

Or $\forall\ j \in [\![1, p]\!]$ les multiples de $P_{ij}$ entre $1$ et $n$ sont $P_{ij},\ 2P_{ij},\ \dots,\ q_j P_{ij}$ d'où $P(A_{ij}) = \frac{|A_{ij}|}{n} = \frac{q_j}{n} = \frac{n/P_{ij}}{n} = \frac{1}{P_{ij}}$.

D'où $P(\bigcap_{j \in J} A_j) = \prod_{j \in J} P(A_{ij})$. CQFD.

Car $A_k$ ($1 \le k \le m$) sont mutuellement indépendants, alors d'après le théo précédent $\overline{A_k}$ ($1 \le k \le m$) le sont aussi d'où $P(A) = P(\bigcap_{k=1}^m \overline{A_k}) = \prod_{k=1}^m P(\overline{A_k}) = \prod_{k=1}^m (1 - P(A_k)) = \prod_{k=1}^m \left(1 - \frac{1}{p_k}\right)$ où $\forall\ k \in [\![1, m]\!]$, [lecture incertaine — « $\dots P(A_k)$ » rogné].

Or $\frac{\varphi(n)}{n} = P(A) = \prod_{k=1}^m \left(1 - \frac{1}{p_k}\right)$. Donc en conclusion $\forall\ n \in \mathbb{N}$ (?), $\varphi(n) = n \prod_{k=1}^m \left(1 - \frac{1}{p_k}\right)$ où $p_{k_{1, m}}$ sont les diviseurs $1^{ers}$ de $n$.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée (date 16/10/2021, texte + équations) ; pp. 2–6 vérifiées S4 (récurrence, crible, indicatrice d'Euler — texte seul, sans schéma). Aucun script `reproduce_polynome_produit_somme_independance_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $I_n = [\![1, n]\!]$ ; $J \subseteq I_n$, $J \subseteq^* I_n$ = partie (non vide) ; $mtq$ = montrons que.
- $A_i$, $\overline{A_i}$ = événements/contraires ; $P$ = probabilité ; $ppcm$ = plus petit commun multiple.
- $\varphi$ = indicatrice d'Euler ; $p_k$ = diviseurs premiers de $n$ ; $CQFD$.
