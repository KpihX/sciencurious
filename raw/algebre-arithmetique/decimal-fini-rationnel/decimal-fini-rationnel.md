# Tout rationnel a une partie décimale périodique (et réciproquement) — transcription fidèle

> 🧾 **Manuscrit original :** `decimal-fini-rationnel.pdf` (démonstration manuscrite au stylo bleu, 6 pages) · ✍️ KpihX
> 🔍 **Statut :** écriture manuscrite globalement lisible, transcrite au plus près ; les passages ambigus sont signalés `[lecture incertaine — …]`, les ratures `[raturé]`, les coquilles `[*sic* — …]`. Rien n'est inventé.
> 📄 **Source scannée :** [`decimal-fini-rationnel.pdf`](decimal-fini-rationnel.pdf) (restaurée Datas1, 2026-09-07)
> ✅ Vérifié complet le 2026-09-07 (contrôle visuel p. 6).

---

## Page 1

**Théo :** tout rationnel a une partie décimale périodique, c-à-d qu'à partir d'un certain rang après la virgule, il y a une suite de chiffres qui se répète indéfiniment et inversement

**Preuve :**

**Prérequis :**

- On définit $l$ : $\forall A \equiv \overline{a_n \dots a_0}^{10} \in \mathbb{N}$, $l(A) = n$
- Dans la suite $\overline{a_n \dots a_0}^{10}$ se notera simplement $a_n \dots$ [lecture incertaine — fin de ligne illisible ; l'auteur semble convenir d'omettre la barre et la base]
- $\forall A, B \in \mathbb{N}$, l'écriture $AB$ ne signifiera non pas $A \times B$ mais le résultat de la concaténation des chiffres de $A$ et de $B$ dans cet ordre

$\Rightarrow$ Soit alors $r \in \mathbb{Q}$. $\exists (p, q) \in \mathbb{Z} \times \mathbb{N}^* / r = p/q$. SNALG [*sic* — l'auteur écrit « SNALG »] on va supposer que $p > 0$ car le cas $p = 0$ donne $r = 0,0 \dots 0 = 0,\bar{0}$ qui est bien une partie décimale périodique et le cas $p < 0$ est similaire à celui $p > 0$ en affectant juste les résultats de $-$.

NB : $\forall A \in \mathbb{N}$ (pouvant éventuellement commencer par des $0$), $\bar{A} = AAA \dots$ Ex : $\overline{003} = 003003 \dots$ Rq : $\bar{A} = A\bar{A} = AA\bar{A} \dots$

Pour montrer que $r$ a une partie décimale périodique il suffit de trouver $A, C, B \in \mathbb{N}$ et [raturé — « $A \in \mathbb{N}$ » barré] (où $A$ et $B$ peuvent éventuellement commencer par des $0$) / $r = C,B\bar{A}$ ($\Leftrightarrow r = CB,\bar{A} \times 10^{-l(B)}$ ; Il suffit alors de montrer $\exists D \in \mathbb{N}$ et $n \in \mathbb{N}$ / $r = D,\bar{A} \times 10^{-n}$ (1)

Rq : $B$ peut ne même pas exister dans l'écriture $r = C,B\bar{A}$ et dans ce cas $l(B) = 0$.

(1) se justifie par le fait qu'il suffira de prendre $B$ comme la suite des $n$ derniers chiffres [lecture incertaine — passage très raturé] de $D$ et [lecture incertaine] comme la suite du reste des chiffres [lecture incertaine — fin de page coupée]

## Page 2

**Lemme :** Il vise à établir une équivalence entre les écritures $D,\bar{A}$ et $p/(1)$ [lecture incertaine — référence illisible]

(a) : Soit $D, A \in \mathbb{N}$ (où $A$ peut éventuellement commencer par des $0$) On a : $D,\bar{A} = \dfrac{DA - D}{10^{l(A)} - 1}$

*En effet* $D,\bar{A} = D,A\bar{A} \Rightarrow 10^{l(A)} D,\bar{A} = DA + 0,\bar{A} = DA + D,\bar{A} - D$ $\Rightarrow D,\bar{A} = \dfrac{DA - D}{10^{l(A)} - 1}$ (NB : $DA \neq D \times A$ ici ! CQFD)

(b) : Soit $E, n \in \mathbb{N}$. $\exists D, A \in \mathbb{N}$ (où $A$ peut éventuellement commencer par des $0$) / [raturé — « le tout » barré] $\dfrac{E}{10^n - 1} = D,\bar{A}$

*Cherchons de tels $D$ et $A$.* D'après (a), $\dfrac{E}{10^n - 1} = D,\bar{A} \Leftrightarrow \dfrac{E}{10^n - 1} = \dfrac{DA - D}{10^{l(A)} - 1}$ [raturé — symbole barré]

- Si $l(E) \le n$, il suffit de prendre $D = 0$ et $A = \underbrace{0 \dots 0}_{n - l(E) \text{ fois}} E$ et on a bien $n = l(A)$ et $E = A = OA - O$ [lecture incertaine] NB : $OA \neq O \times A$
- Sinon, $l(E) > n$, d'après l'algorithme de la div Eucl, $\exists ! (q, r) \in \mathbb{N} \times [\![0, 10^n - 1]\!]$ / $E = (10^n - 1) \times q + r$. Ainsi $\dfrac{E}{10^n - 1} = \dfrac{(10^n - 1)q + r - q}{10^n - 1} = \dfrac{DA - D}{10^{l(A)} - 1}$ où $D = q$ et $A = \underbrace{0 \dots 0}_{n - l(r)} r$ et car $r < 10^n - 1$ on a bien $l(r) < n$ [accolade : et $DA = \underbrace{q0 \dots 0}_{n - l(r) \text{ fois}} r$] CQFD

## Page 3

Ainsi d'après le lemme précédent pour avoir (1) il suffit de montrer $\exists (E, n) \in \mathbb{N}^2$ / $r = \dfrac{E}{10^n - 1} \times 10^{-n}$ et $n \in \mathbb{N}$ (en exploitant le (b) de ce lemme)

Pour établir le théo il suffit alors de montrer $\exists a, b, m \in \mathbb{N}$ / $r = \dfrac{a}{10^n (10^m - 1)}$ (2)

Rq : Cette écriture lorsqu'elle sera justifiée entraînera le fait que tout rationnel est le quotient d'un décimal relatif (1 nbre de la forme $a/10^n$, $a, n \in \mathbb{N}$) par $10^m - 1$ pour un certain $m \in \mathbb{N}$)

Et comme un nbre décimal a un nbre fini de chiffres après la virgule, il en découlera que les rationnels avec une partie décimale repetitive infinie ne stationnant pas à $0$, sont dus à la division par un certain $10^m - 1$

Ex : $\dfrac{7}{10^3 - 1} = \dfrac{7}{99}$ [lecture incertaine — dénominateur lu « 99 » au lieu du « 999 » attendu] $= 0,\overline{007}$ ; $\dfrac{3}{10^1 - 1} = 0,\bar{3}$ [lecture incertaine — fin de ligne coupée]

- **Justification de (2) :** On a : $r = p/q$. (l'on essaye de faire ressortir $10^n$ en remarquant que $10 = 2 \times 5$) Soit $m$ et $n_2$ resp les plus gdes puissances de $2$ et $5$ dans la décomposition en produit de facteurs $1^{ers}$ de $q$. Ainsi $\exists q' \in \mathbb{N}^* / q = 2^m \times 5^{n_2} \times q'$ avec $q'$ non multiple ni de $2$ ni de $5$. Ainsi $r = \dfrac{p}{2^m \times 5^{n_2} \times q'} = \dfrac{p \times 2^{\max-m} \times 5^{\max-n_2}}{10^{\max} \times q'}$ où $\max = \max$ de $m, n_2$ [lecture incertaine — l'auteur note « $\max$ de $m, n_2$ »]. Prenons $n = \max$ et posons $p' = p \times 2^{\dots} \times 5^{n-m}$ [lecture incertaine — exposants raturés]

## Page 4

on a $r = \dfrac{p'}{10^n \times q'}$. On route pour se rapprocher davantage de (2), il suffirait qu'on puisse trouver $K \in \mathbb{N}$ et $K' \in \mathbb{N}$ / $Kq' = 10^{K'} - 1 \Leftrightarrow 10^{K'} \equiv 1 [q']$ (3)

**Lemme 2 :** (on va généraliser le résultat (3) qu'on souhaite avoir, en un résultat plus général pouvant être utile ultérieurement) Soit $a, b \in \mathbb{N}^* / a \wedge b = 1$ (cad $pgcd(a, b) = 1$) $\exists n \in \mathbb{N}$ / $a^n \equiv 1 [b]$

**Notation :** l'écriture $r \underset{r}{\equiv} d[\beta] \Leftrightarrow r = \text{reste de la div Eucl de } d / \beta$ [lecture incertaine — l'indice sous le $\equiv$ est peu lisible]

Considérons l'ens $E = \{r_n \underset{r}{\equiv} a^n[b], n \in \mathbb{N}\}$. On a : $E \subseteq [\![0, b-1]\!]$. Comme $|E| < +\infty$, à partir d'un certain rang la suite $(r_n)_{\mathbb{N}}$ va commencer à se répéter.

- Mq la $1^{\text{ère}}$ valeur à se répéter est $r_0 \underset{r}{\equiv} a^0[b] \Rightarrow r_0 = 1$. Supp par l'absurde que la $1^{\text{ère}}$ valeur à se répéter est $r_\alpha$ ($\alpha \in \mathbb{N}$, $\alpha > 1$). Soit $\beta$ le tout $1^{er}$ rang où on observe la répétition de $r_\alpha$. On a : $r_\beta = r_\alpha \Rightarrow a^\beta \equiv a^\alpha[b]$ (avec $\beta > \alpha \ge 1$) $\Rightarrow a^{\beta-1} \equiv a^{\alpha-1}[b]$ car $a \wedge b = 1$ $\Rightarrow r_{\beta-1} = r_{\alpha-1}$ $\Rightarrow r_{\alpha-1}$ est le $1^{er}$ reste à se répéter ce qui est absurde ! vu que $\alpha - 1 < \alpha$. Donc $\alpha = 0$. Ainsi il existe un rang $m \in \mathbb{N}^*$ minimal / $r_m = r_0 = 1 \Rightarrow a^m \equiv 1[b]$. Il suffit de prendre $n = m$.

## Page 5

Rq : on montrera que $\{n \in \mathbb{N} / a^n \equiv 1[b]\} = m\mathbb{N}$ en justifiant que $E$ est cyclique d'ordre $m$ ou en réduisant le reste de $n$ par $m$ pour $n \in \mathbb{N} / a^n \equiv 1[b]$.

- On ne pourrait pas juste s'arrêter au fait que la suite $dr_n$ [lecture incertaine] $_{\mathbb{N}}$ va se répéter car sans les $a \wedge b \neq 1$ [lecture incertaine — l'auteur écrit « sans les $a \wedge b \neq 1$ », comprendre « sans $a \wedge b = 1$ »] il peut arriver qu'elle boucle sur une valeur autre que $1$. Ex : $\forall n \in \mathbb{N}$, $10^n \equiv 0[2] \Rightarrow 10^n \not\equiv 1[10]$ ce qui se justifie bien car que $2 \,|\, 10$ [raturé — gribouillis]

En revenant à (3) comme ni $2$ ni $5$ ne divise $q'$ alors $q' \wedge 10 = 1$ et d'après le lemme précédent $\exists K' \in \mathbb{N}$ / $10^{K'} \equiv 1[q'] \Rightarrow \exists K \in \mathbb{N}$ / $Kq' = 10^{K'} - 1$. Prenons $m = K'$. On a : $r = \dfrac{q' \times K}{10^n(10^m - 1)}$ [lecture incertaine — numérateur lu « $q' \times K$ », l'auteur écrirait plutôt $p' \times K$]. Prenons enfin $a = q' \times K$ [lecture incertaine — même remarque]. on vient ainsi de construire $a = q' \times K$, $n = \max$ et $m = K'$ et donc de démontrer (2). Comme (2) suffit à établir le théorème initial, on peut alors conclure que tout rationnel a une partie décimale périodique

**Théo :** (Vers une autre définition de $\mathbb{Q}$) Si un réel a une partie décimale périodique, alors c'est un rationnel

## Page 6

En effet soit $x \in \mathbb{R}$, de partie décimale périodique (SNALG [*sic* — l'auteur écrit « SNALG »] on va prendre $x > 0$). En s'inspirant des $1^{ers}$ résultats du théo précédent, son justifie [raturé — « justifie » barré, le verbe est réécrit par-dessus] qui étaient des équivalences, on a $\exists n, D, A \in \mathbb{N}$ ($A$ pouvant éventuellement commencer par des $0$) / $x = D,\bar{A} \times 10^{-n}$. D'après le tout $1^{er}$ lemme (point (a)) on a : $x = \dfrac{DA - D}{10^{l(A)} - 1}$ [lecture incertaine — dénominateur partiellement masqué par une tache]. Comme $DA - D \in \mathbb{N}$ et $10^{l(A)} - 1 \in \mathbb{N}^*$ alors $x \in \mathbb{Q}$. CQFD

**Conséquence :** Un nbre réel est rationnel ssi il a un développement décimal périodique.

Rq : Ce résultat est valable en n'importe quelle base $b \in \mathbb{N}^* \setminus \{1\}$ en remplaçant juste $10$ par $b$, $2$ et $5$ par les diviseurs [raturé] de $b$ premiers [raturé — mot griffonné en marge droite, illisible]

RM : (Théo initial) Comme $1 = D,\bar{A} = \dfrac{E}{10^{l(A)} - 1} \times 10^{-n} \in \mathbb{Q}$ [lecture incertaine] alors la longueur de la portion qui se répète pour un rationnel $r = p/q = \dfrac{p}{2^m \times 5^n \times q'}$ la période est $n$ où $m$ [lecture incertaine — fin très raturée et pliure de page] $m \in \mathbb{N}^* / 10^m \equiv 1[q']$.

---

## Figures

Aucune figure à reproduire : pages 1–6 relues (S2 le 2026-09-07 : pp. 2–4 confirmées ; S4 : p. 5 confirmée — texte et formules seuls, sans schéma).

## Vocabulaire / notions

- **Développement décimal périodique** : $r = C,B\bar{A}$, $\bar{A} = AAA\dots$.
- **Longueur** $l(A)$ d'un entier, **concaténation** $AB \neq A \times B$.
- **Lemme** $D,\bar{A} = \dfrac{DA-D}{10^{l(A)}-1}$ ; **congruence** $10^{K'} \equiv 1[q']$ ($q' \wedge 10 = 1$).
- **SNALG** [*sic* — abréviation d'auteur] ; généralisation en base $b$ quelconque.
