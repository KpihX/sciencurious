# Probabilité d'un produit nul dans Z/nZ — transcription fidèle

> 🧾 **Manuscrit original :** `proba-nulle-zn.pdf` (OneNote imprimé, 4 pages paysage, encre noire + annotations rouges et titres bleus ; page 4 : deux photos de feuille manuscrite, encre bleue) · ✍️ KpihX. En-tête imprimé : « Probabilité d'avoir un produit nulle dans Z/nZ » [*sic* — « nul »], 23 Décembre 2024 20:34.
> 🔍 **Statut :** lisible (~75 %), transcrit fidèlement. Deux méthodes (I : diviseurs et DFPP ; II : minimums $m_a$ et somme des PGCD), extrapolation à un anneau quelconque, puis jonction des deux formules via le crible de Poincaré (photos p. 4, propos attribués à @briot). Les fins de lignes micro-écrites les plus douteuses sont balisées.
> 📄 **Source scannée :** [`proba-nulle-zn.pdf`](proba-nulle-zn.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

### Méthode I (colonne gauche)

Soit $N_n = \{(a,b) \in E^2 / ab = 0\}$.

En désignant par $P_n$ la probabilité recherchée, Ona : $P_n = \frac{|N_n|}{n}$ [*sic* — lire $n^2$, cf. méthode II et page 2]

Soient $(a,b) \in E^2$. $ab = 0 \Rightarrow n|ab \Rightarrow n \wedge a, n \wedge b > 1$ vu que $a,b < n$

Ainsi ni $a$, ni $b$ n'est inversible

le potentiels candidats pour $a$ et $b$ sont alors $0$ et ses diviseurs

Posons ainsi : $D$ = ens des diviseurs de $0$

. $I$ = ens des elts inversibles de $E = \{a \in E / a \wedge n = 1\}$

Pour $i \in E$, Posons $A_i = \{j \in E / ij = 0\}$

ona : $|N_n| = \sum_{i \in E} |A_i| = |A_0| + \sum_{i \in D} |A_i| + \sum_{i \in I} |A_i|$

Vu que $\forall i \in E$, $0 \cdot i = 0$ alors $|A_0| = n$

Soit $i \in I$. L'unique elt $j$ vérifiant $ij = 0$ est $0$

D'où $|A_i| = 1$

Et comme $|I| = \phi(n)$

Alors $|N_n| = n + \underbrace{\sum_{i \in D} |A_i|}_{|X_n|} + \phi(n)$

En vu d'évaluer $X$ on va s'intéresser à la DFPP de $n$

Càd $n = \prod p_i^{\alpha_i}$

En vu de simplifier le pb, remarquons déjà que $\mathbb{Z}/n\mathbb{Z} \cong \times_i \mathbb{Z}/p_i^{\alpha_i}\mathbb{Z}$

Il nous suffit donc d'évaluer $|N_{p^{\alpha_i}}|$ $\forall i$ et $|I_{\dots}|$ [fin de ligne peu lisible]

. de même que $N_C = N_A \times N_B$ si $C = A \times B$

$A, B, C$ étant des anneaux

et en posant $N_E = \{(a,b) \in E^2 / ab = 0\}$ pour un anneau $E$

\* Soit $n \in \mathbb{N}^*$. Evaluons $|N_{p^\alpha}|$.

Posons $n = p^\alpha$ et $E = \mathbb{Z}/n\mathbb{Z}$

On a : $|N_n| = n + X_n + \phi(n)$

Or $\phi(n) = p^\alpha - p^{\alpha-1}$

\*\* Evaluons $|X_n|$

Déjà remarquons que $X_n$ = les multiples stricts de $p$ dans $E$

D'où $X_n = \{p, 2p, \dots, (p^{\alpha-1}-1)p\}$

Pour un tel élément $x \in X_n$ dont la DFPP est de la forme $x = p^i \cdot s$

les elts $y$ / $xy = 0$ sont les multiples stricts de $p^{\alpha-i}$, $y$ compris $0$

Déjà posons $P_i$ cet ensemble

Et posons $M_i$ = multiples stricts de $p^i$

Il vient que $|X_n| = \sum_{i=1}^{\alpha-1} |P_i| \times (|M_{\alpha-i}|+1)$ [parenthésage peu lisible ; le $+1$ compte $y = 0$]

Or $M_i = \{p^i, 2p^i, \dots, (p^{\alpha-i}-1)p^i\} \Rightarrow |M_i| = p^{\alpha-i} - 1$ pour $i$ donné

D'où $|M_{\alpha-i}| = p^i - 1$

De plus $P_i$ = multiples stricts de $p^i$ hormis ceux de $p^{i+1}$

D'où $P_i = M_i \setminus M_{i+1} \Rightarrow |P_i| = p^{\alpha-i} - 1 - (p^{\alpha-i-1} - 1) = p^{\alpha-i} - p^{\alpha-i-1}$

Ainsi $|X_n| = \sum_{i=1}^{\alpha-1} (p^{\alpha-i} - p^{\alpha-i-1}) p^i = \sum_{i=1}^{\alpha-1} (p^\alpha - p^{\alpha-1})$ [le développement final en $(\alpha-1)(\dots)$ est peu lisible]

Il vient donc que $|N_n| = p^\alpha + p^\alpha - p^{\alpha-1} + (\alpha-1)(p^\alpha - p^{\alpha-1})$ [signe central peu lisible ; cohérent avec le rappel en tête de page 2]

### Méthode II (colonne droite)

Exo : Quelle est la probabilité qu'un 2-uplet $(a,b)$ vérifie $ab = 0$ dans $\mathbb{Z}/n\mathbb{Z}$ ($E$)

NB : Dans la suite, par abus […] $i \in \{0, \dots, n-1\}$ […] sera noté simplement $i$ $(n \ge 2)$ [ligne bleue peu lisible — identification de $E$ à ses représentants]

Soit $a \in E$. Posons $A_a = \{b \in E / ab = 0\}$

$0 \in A_a \Rightarrow A_a \neq \emptyset$ d'où $A_a$ admet un minimum non nul $m_a$

\* Soit $b \in A_a$. Mq $m_a | b$

$\exists! (q,r) \in \mathbb{N} \times [\![0, m_a-1]\!] / b = m_a q + r$

Or $a \cdot b = a \cdot m_a = 0 \Rightarrow a \cdot r = a \cdot (b - m_a q) = 0 \Rightarrow r \in A_a$

On a nécessairement $r = 0$. CQFD

Ainsi $A_a = \{m_a, 2m_a, \dots, \frac{n}{m_a}m_a\}$ vu que $n = 0 \in A_a$ et donc $m_a | n$

\* Explications $m_a$

Ona : $a \cdot m_a = 0 \Rightarrow \exists K \in \mathbb{N} / a \cdot m_a = n \cdot K$

Ainsi $a = \frac{n}{m_a} \cdot K$ (1)

On constate $\frac{n}{m_a} | n$ et $\frac{n}{m_a} | a$ au vu de (1)

Et comme $m_a$ est minimal $\frac{n}{m_a}$ est maximal

Il vient donc que $\frac{n}{m_a} = PGCD(a, n)$

D'où $m_a = \frac{n}{a \wedge n}$

En revenant au problème initial, en définissant $N_n$ et $P_n$ comme à la [encadré bleu : METHODE I]

Ona : $P_n = \frac{|N_n|}{n^2}$

Et $|N_n| = \sum_{a \in E} |A_a|$

$= \sum_{a \in E} \frac{n}{m_a}$

$= \sum_{a \in E} a \wedge n$

D'où $|N_n| = \sum_{K=0}^{n-1} K \wedge n$ (2) [en rouge ; annoté à droite : $\sum_{d|n} d \cdot \varphi(\frac{n}{d})$]

Or $\{K \wedge n, K \in [\![0, n-1]\!]\} = \{d \in [\![1, n]\!] / d|n\}$ ce qui s'établit aisément par inclusion réciproque

On peut ainsi regrouper dans la somme les $K$ ayant le m̃ $K \wedge n$

Soit $d|n$. Posons $M_d = \{K \in [\![0, n-1]\!] / K \wedge n = d\}$

Ona : $|N_n| = \sum_{d|n} d \cdot |M_d|$

\* Evaluons $|M_d|$ pour $d|n$

Posons $M'_d = \{d, 2d, \dots, \frac{n}{d}d\} = [\![1, n/d]\!] \cdot d$

Or pour qu'un elt $Kd$ de $M'_d$ ($1 \le K \le n/d$) appartienne à $M_d$ il faut que $Kd \wedge n = d \iff Kd \wedge (\frac{n}{d} \times d) = d \iff K \wedge \frac{n}{d} = 1$

---

## Page 2

### Méthode I — formule close et lemme de factorisation (colonne gauche)

[en rouge, rappel du bas de page 1 :] $|N_{p^\alpha}| = p^\alpha(\alpha+1) - p^{\alpha-1}\alpha$

En particulier $P_{p^\alpha} = \frac{p^\alpha(\alpha+1) - p^{\alpha-1}\alpha}{(p^\alpha)^2} = \frac{p(\alpha+1) - \alpha}{p^{\alpha+2}}$

\* Lemme 1 : Soient $A, B, C$, 3 anneaux / $A \cong B \times C$. Ona : $N_A = N_B \times N_C$

En effet, par abus on peut écrire : $A = \{(b,c), b \in B \text{ et } c \in C\}$. Ainsi $N_A = \{(a_1, a_2) \in A^2 / a_1 a_2 = 0\} = \{((b_1,c_1),(b_2,c_2)) \in (B \times C)^2 / \underbrace{(b_1,c_1) \cdot (b_2,c_2) = 0}_{\parallel} \}$

[$(b_1b_2, c_1c_2) = 0$, écrit sous l'accolade]

$= \{((b_1,c_1),(b_2,c_2)) \in (B \times C)^2 / b_1b_2 = 0 \text{ et } c_1c_2 = 0\}$

$= \{(b_1,b_2) \in B^2 / b_1b_2 = 0\} \times \{(c_1,c_2) \in C^2 / c_1c_2 = 0\}$

$= N_B \times N_C$

Ainsi en revenant au problème initial, Vu que $\mathbb{Z}/n\mathbb{Z} \cong \prod_K \mathbb{Z}/p_K^{\alpha_K}\mathbb{Z}$

Et d'après le lemme 1, qui peut facilement par récurrence se généraliser, Ona [en rouge :] $|N_E| = \prod_K p_K^{\alpha_K}(\alpha_K+1) - p_K^{\alpha_K-1}\alpha_K$

D'où [en rouge :] $P_E = \frac{\prod_K p_K^{\alpha_K}(\alpha_K+1) - p_K^{\alpha_K-1}\alpha_K}{n^2} = \prod_K \frac{p_K(\alpha_K+1) - \alpha_K}{p_K^{\alpha_K+2}}$

\* Essayons d'extrapoler ce résultat

Pour cela remplaçons $\mathbb{Z}/n\mathbb{Z}$ par un anneau quelconque $E$ non trivial (le cas trivial donnant $P_E = 1$). Posons $n = |E|$. Ona tjrs $P_E = \frac{|N_E|}{n^2}$.

Et $|N_E| = n + \sum_{i \in D} |A_i| + \sum_{i \in I} |A_i|$ avec ici $I = E \setminus (\{0\} \cup D)$ [lecture incertaine]

Posons $d = |D|$. Soit $i \in I$. Vu que $i \notin D$ alors le seul élément vérifiant $ij = 0$ est $j = 0$. D'où $|A_i| = 1$. Ainsi $|N_E| = n + \sum_{i \in D} |A_i| + |I| = n + \sum_{i \in D} |A_i| + (n-1-d)$.

\*\* Cas d'un anneau unitaire intègre

Dans ce cas $d = 0$ d'où $|N_E| = n + 0 + (n-1-0) = 2n-1$. D'où [en rouge :] $P_E = \frac{2n-1}{n^2} \underset{n \to +\infty}{\longrightarrow} 0$

\*\*\* Minorons ce résultat

$\forall i \in D$, $i \times 0 = 0$ et de plus $\exists j \neq 0 / ij = 0$, d'où $|A_i| \ge 2$. Ainsi $|N_E| \ge n + 2d + (n-1-d)$. D'où $|N_E| \ge 2n-1+d$. Et en particulier [en rouge :] $P_E \ge \frac{2n-1+d}{n^2}$ d'où $P_E \ge \frac{2n-1}{n^2}$

[bas de page rogné — la suite page 3]

### Méthode II — dénombrement des $M_d$ (colonne droite)

Ainsi $M_d = \{K \in [\![1, n/d]\!] / K \wedge \frac{n}{d} = 1\} \cdot d$

D'où $|M_d| = \varphi(n/d)$

Ainsi [en rouge :] $|N_n| = \sum_{d|n} d \cdot \varphi(n/d)$

$\bar{d} = \frac{n}{d}$ [changement de variable, en rouge :] $\sum_{\bar{d}|n} \frac{n}{\bar{d}}\varphi(\bar{d})$

Alors [en rouge :] $P_n = \frac{1}{n} \sum_{d|n} \frac{\varphi(d)}{d}$

Or on démontre au moyen d'un calcul de la probabilité que $K \wedge d = 1$ ($K \in [\![0, d-1]\!]$) ou encore par le dénombrement des valeurs distinctes de […] , $1 \le K \le d$ [fraction d'origine peu lisible] que $\frac{\varphi(d)}{d} = \sum_{d'|d} \frac{\mu(d')}{d'}$

Ainsi $\sum_{d|n} \frac{\varphi(d)}{d} = \sum_{d|n} \sum_{d'|d} \frac{\mu(d')}{d'} = \sum_{d'|n} \frac{\mu(d')}{d'} \sum_{\substack{d|n \\ d'|d}} 1$

[flèche vers le bas :] Ce qui n'aboutit à rien d'intéressant

Par conséquent [en rouge :] $P_n = \frac{1}{n} \sum_{d|n} \frac{\varphi(d)}{d}$

---

## Page 3

### Majoration et bilan (colonne gauche ; colonne droite vide)

\*\* Majorons ce résultat

Posons $M = \max_{i \in D} |A_i|$ [un « $d$ » parasite devant $|A_i|$ — lecture incertaine]

On a : $|N_E| \le n + d \cdot M + (n-1-d)$

Càd $|N_E| \le 2n + dM - d - 1$

Or $\forall i \in D$, $A_i$ est un idéal de $E$, d'où $|A_i| \mid n$ [lecture incertaine]

Ainsi $M \mid n$ d'où $M \le n/2$

Il vient que $|N_E| \le 2n + d \cdot (n/2) - d - 1$

Or vu que $0 \notin D$, $d \le n-1$. Alors $|N_E| \le 2n + (n-1)(n/2-1) - 1$

D'où $|N_E| \le \frac{n}{2}(n+2)$

Et donc [en rouge :] $P_E \le \frac{1}{2}(1 + \frac{2}{n})$, et donc $P_2 \le 1/2(1+1/2) = 3/4$

\*\*\* Cas particulier où $E$ est unitaire :

Dans ce cas $d \le n-2$ vu qu'aussi $1 \notin D$. Ainsi $|N_E| \le 2n + (n-2)(n/2-1) - 1$. Càd $|N_E| \le \frac{n^2}{2} + 1$.

Et donc [en rouge :] $P_E \le \frac{1}{2} + \frac{1}{n^2}$, d'où $P_2 \le 1/2 + 1/4 = 3/4$ [indice peu lisible]

\*\* Bilan :

Pour un anneau $E$, on a [en rouge :] $\frac{2n-1+d}{n^2} \le P_E \le \frac{1}{2}(1 + \frac{2}{n})$ $\left. \right\}$ d'où [en rouge :] $\frac{2n-1}{n^2} \le P_E \le \frac{3}{4}$

. En particulier, si $E$ est unitaire, [en rouge :] $\frac{2n-1+d}{n^2} \le P_E \le \frac{1}{2} + \frac{1}{n^2}$

. Si en particulier $E$ est intègre alors [en rouge :] $P_E = \frac{2n-1}{n^2} \underset{n \to +\infty}{\longrightarrow} 0$

Cas particulier : Si $p \in \mathbb{P}$ alors $P_{\mathbb{Z}/p\mathbb{Z}} = \frac{2p-1}{p^2}$ (1)

. Si $E = \mathbb{Z}/n\mathbb{Z}$, en partant de la DFPP de $n$ : $n = \prod_{K=1}^m p_K^{\alpha_K}$. Ona [en rouge :] $P_E = \prod_{K=1}^m \frac{p_K(\alpha_K+1) - \alpha_K}{p_K^{\alpha_K+2}}$

Cas particulier : Si $n = p^\alpha$ alors [en rouge :] $P_E = \frac{p(\alpha+1) - \alpha}{p^{\alpha+2}}$

Cas particulier : Si $\alpha = 1$, alors [en rouge :] $P_E = \frac{2p-1}{p^2}$ (2) qui coïncide bien avec (1)

Question : \* Peut on passer mathématiquement de $\frac{1}{n} \sum_{d|n} \frac{\varphi(d)}{d}$ à $\prod_{K=1}^m \frac{p_K(\alpha_K+1) - \alpha_K}{p_K^{\alpha_K+2}}$ et inversement ?

Eh oui ! Observons ce que nous a proposé @briot [en rouge]

avec $n = \prod_{K=1}^m p_K^{\alpha_K}$

[bas de page : deux photos collées — à gauche « Exercice : Soit $n \in \mathbb{N}^*$ on se fixe $1 \le k \le n$ … » (début, suite page 4) ; à droite « $\sum_{d|n} \frac{\varphi(d)}{d} = \sum_{p=1}^r \sum_{\dots} \sum (1-\frac{1}{P_{i_1}})\cdots(1-\frac{1}{P_{i_p}}) + 1$ » (début, suite page 4)]

---

## Page 4 — Deux photos : l'exercice (gauche) et la formule finale (droite)

### Photo gauche — comptage direct par $S_n$

on cherche $l \in [\![1,n]\!]$ tel que $n | kl$

pour cela on cherche d'abord le plus petit $q$ entier tel que $n | qk$, ie $qk = nq'$, posons $d = k \wedge n$, et écrivons $\begin{cases} k = dk' \\ n = dn' \end{cases}$ avec $k' \wedge n' = 1$

alors $qk' = n'q' \Rightarrow k' | n'q' \Rightarrow k' | q'$

la plus petite valeur de $q'$ est donc $q' = k'$

la valeur cherchée de $q$ est $q = \frac{nq'}{k} = \frac{nk'}{k} = \frac{n}{d} \in \mathbb{N}^*$

les couples cherchés sont donc $(k, q_k)$ avec $q_k \le n$ ie […] $\le d$ [fin de phrase peu lisible]

pour $k$ fixé $\in [\![1,n]\!]$ on a ainsi $d = k \wedge n$ couples.

Inutile de le vérifier, les couples ne permutent de manière autonome quand on fait varier $k \in [\![1,n]\!]$.

d'où la probabilité $P = \frac{\sum_{k=1}^n (k \wedge n)}{n^2}$ [un « $n$ » raturé/superposé au dénominateur]

Posons $S_n = \sum_{k=1}^n (k \wedge n)$ posons $d = k \wedge n$, on écrit : $\begin{cases} k = dk' \\ n = dn' \end{cases}$

$k \le n \Rightarrow k' \le \frac{n}{d}$ et $k' \wedge n' = k' \wedge \frac{n}{d} = 1$.

Ainsi $\forall k \in [\![1,n]\!]$, $d = k \wedge n \iff d|n$ et $\exists k' / k = dk', k' \wedge \frac{n}{d} = 1$

$S_n = \sum_{d|n} \sum_{\substack{k' \le n/d \\ k' \wedge n/d = 1}} d = \sum_{d|n} d\,\varphi(\frac{n}{d}) = \sum_{d|n} \frac{n}{d}\varphi(d)$ (car $dd' = n$)

### Photo droite — crible de Poincaré et « Sacrée formule »

[haut rogné — suite du calcul de la page 3 :] $= \sum_{p=1}^r \sum_{i_1 < \dots < i_p} (1-\frac{1}{P_{i_1}})\cdots(1-\frac{1}{P_{i_p}}) \times \alpha_{i_1}\cdots\alpha_{i_p} + 1$ [lecture incertaine — $\alpha$ ou $d$]

or $\prod_{i=1}^n (x+a_i) = x^n + \sum_{k=1}^n x^{n-k} \sum_{i_1 < i_2 < \dots < i_k} a_{i_1}\cdots a_{i_k}$ (formule du crible de Poincaré)

pour $x = 1$ et $a_i = \alpha_i(1-\frac{1}{P_i})$ $\forall i \in [\![1,r]\!]$,

on a $\sum_{d|n} \frac{\varphi(d)}{d} = \prod_{i=1}^r \left[1 + \frac{\alpha_i(P_i-1)}{P_i}\right] = \prod_{i=1}^r \left[\frac{P_i + \alpha_i(P_i-1)}{P_i}\right]$

d'où [encadré :] $P_n = \frac{1}{n}\sum_{d|n} \frac{\varphi(d)}{d} = \prod_{i=1}^r \left[\frac{P_i(\alpha_i+1)-\alpha_i}{P_i^{\alpha_i+1}}\right]$

Sacrée formule [souligné]

---

## 📝 Notes de transcription (fidélité)

- $a \wedge n$ = PGCD, $a \mid n$ = divisibilité, $\mathbb{P}$ = ensemble des nombres premiers, $DFPP$ = décomposition en facteurs premiers (produits), $\phi$/$\varphi$ = indicatrice d'Euler, $\mu$ = fonction de Möbius : notations d'origine conservées.
- Coquilles conservées telles quelles : « produit nulle » (titre imprimé), « le potentiels », « En vu » (×2), « Ona », « Mq », « ens », « elts », « tjrs », « Càd », « METHONE/METHODE ».
- Méthode I écrit $P_n = |N_n|/n$ [*sic*] ; partout ailleurs le dénominateur est $n^2$.
- Aucune figure à reproduire : les deux photos de la page 4 sont des dérivations textuelles (transcrites ci-dessus), pas des courbes ni des schémas ; les changements de variable

---

## Figures

Aucune figure à reproduire (aucun graphe/courbe/schéma) : p. 1 vérifiée (export OneNote, encre numérique, deux colonnes MÉTHODE I/II) ; pp. 2–3 vérifiées S4 (lemme de factorisation, bilan, majorations — texte seul, vignettes photos en bas de p. 3 = amorces déjà transcrites p. 4) ; p. 4 vérifiée (deux photos de dérivations manuscrites : comptage direct $S_n$ à gauche, crible de Poincaré + « Sacrée formule » encadrée à droite — texte transcrit, pas d'illustration). Aucun script `reproduce_proba_nulle_zn_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $N_n = \{(a,b) \in E^2 \mid ab = 0\}$, $P_n = |N_n|/n^2$ ; $M_d$, $S_n$ = sommes de comptage ; $m_a$ = minimum de $A_a$.
- $a \land n$ = PGCD ; $d \mid n$ = divisibilité ; $DFPP$ = décomposition en facteurs premiers.
- $\phi$/$\varphi$ = indicatrice d'Euler ; $Ona$, $Mq$, $ens$, $elts$, $tjrs$ = abréviations d'origine. ($\bar{d} = n/d$, $dd' = n$) sont notés en place.
