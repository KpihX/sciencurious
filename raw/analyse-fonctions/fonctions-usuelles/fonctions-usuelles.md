# Fonctions usuelles (cos, sin, ln) — transcription fidèle

> 🧾 **Manuscrit original :** `fonctions-usuelles.pdf` (manuscrit, 11 pages) · ✍️ KpihX
> 🔍 **Statut :** devoir d'informatique — écrire les fonctions cos, sin et ln à partir du théorème de Taylor avec reste ; principe, pseudo-code, dry running ($x = 0{,}5$ ; $x = 2$, $d = 1$), complexités ($O(1)$ / $O(x)$ pour cos et sin, $O(10^d)$ pour ln).
> 📄 **Source scannée :** [`fonctions-usuelles.pdf`](fonctions-usuelles.pdf) (restaurée Datas1, vérifiée `pdfinfo`, 2026-09-07)

## Page 1

En marge, en haut à gauche, vertical : AMDEN / OUOKAM / IVANN / HAROLD [lecture incertaine — début de ligne rogné, probablement « KAMDEM POUOKAM IVANN HAROLD »].

Mardi, 07 Décembre 2021

Informatique

Devoir : Écrire les fonctions cos, sin et ln en se basant sur les notions de cours et elles [*sic* — « et elles acquises », probablement « et celles acquises »] acquises

I/ Prérequis : théorème de Taylor avec reste $f^{(n+1)}(c)$

Soient $f : I \to \mathbb{R}$ ($I \subset \mathbb{R}$) de classe $C^n$ et telle que $f^{(n)}$ soit dérivable sur $I$, $x, a \in I$. Il existe $c \in \mathbb{R}$ entre $a$ et $x$ tel que

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k + \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1} \quad n \in \mathbb{N}$$

NB : Cette formule permettra non seulement d'approcher $f$ mais aussi d'évaluer la précision du résultat ceci en majorant $\left| \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1} \right| = \left| f(x) - \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k \right|$

II/ cos & sin

1/ Principe : (NB : on travaille en radian et on suppose l'existence du réel Pi $= \pi$)

\* Pour $x \geqslant 0$

. Si $x \in [0 ; \pi/4] \subset [0 ; 1]$, les erreurs dans le calcul du développement limité sont ignorables car insignifiantes [lecture incertaine — « ignorables car insignifiantes »]

D'après le prérequis, $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + \dots + \frac{\cos^{(n)}(0)}{n!}x^n + \frac{\cos^{(n+1)}(c)}{(n+1)!}x^{n+1}$, $c \in [0 ; x]$

$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} + \dots + \frac{\sin^{(n)}(0)}{n!}x^n + \frac{\sin^{(n+1)}(c)}{(n+1)!}x^{n+1}$, $c \in$ [0 ; $x$] [lecture incertaine — bas de page rogné]

## Page 2

(numéro manuscrit entouré en bas à gauche : 2)

avec des erreurs resp. $\left| \frac{\cos^{(n+1)}(c)}{(n+1)!}x^{n+1} \right| < \left| \frac{1 \times x}{(n+1)!} \right| < \frac{1}{(n+1)!}$

et $\left| \frac{\sin^{(n+1)}(c)}{(n+1)!}x^{n+1} \right| < \frac{1}{(n+1)!}$

NB : Dans la suite on donnera le résultat avec 3 chiffres exacts. Pour cela il suffit que $\frac{1}{(n+1)!} < 10^{-3} \Rightarrow n \geqslant$ 12 [lecture incertaine — « 12 », la valeur mathématique attendue serait 6] après la virgule

ainsi on prendra $\cos x = \sum_{i=0}^{6} \frac{(-1)^i x^{2i}}{(2i)!}$ pour avoir 3 chiffres exacts après la virgule

$$\sin x = \sum_{i=0}^{6} \frac{(-1)^i x^{2i+1}}{(2i+1)!}$$

c-à-d $\cos x = \sum_{i=0}^{6} (-1)^i \times \frac{x}{2i} \times \frac{x}{2i-1} \times \dots \times \frac{x}{\text{[raturé]}}$ et $\sin x = \sum_{i=0}^{6} (-1)^i \frac{x}{2i+1} \times \dots \times \frac{x}{2 \times 0 + 1}$ [lecture incertaine — produits télescopiques peu lisibles]

D'où l'utilisation par fonction de 2 boucles Pour, l'une pour faire le produit et l'autre pour sommer

. Si $x \in ]\pi/4 ; \pi]$, en posant $y = x/4 \in ]\pi/16 ; \pi/4] \subset [0 ; \pi/4]$ [confirmé second passage : $y = x/4 \in ]\pi/16 ; \pi/4]$ bien lisible]

alors $\cos x = \cos 4y = 2\cos^2 2y - 1 = 2(2\cos^2 y - 1)^2 - 1$

Si $x > \pi$, [confirmé second passage : bien « Si $x > \pi$, » souligné — *sic*, attendu « Si $x \in ]\pi/4 ; \pi]$ » pour la formule de $\sin$],

$\sin x = 2 \sin 2y \cos 2y = 4 \sin y \cos y (1 - 2\sin^2 y)$

- Si $x \in ]\pi/4 ; \pi/2]$, $\sin x = 4 \sin y \sqrt{1-\sin^2 y} (1-2\sin^2 y)$

- Si $x \in ]\pi/2 ; \pi]$, $\sin x = -4 \sin y \sqrt{1-\sin^2 y} (1-2\sin^2 y)$ [confirmé second passage : signe « $-$ » et bornes $]\pi/2 ; \pi]$ bien lisibles]

. Si $x > \pi$

On pourra toujours retrancher au moins $K \in \mathbb{N}$ fois $2\pi$ dans [lecture incertaine — « $2\pi$ dans … jusqu'à ce que »] $x \in ]0 ; \pi]$ [reconstruction — borne basse lue « $0$ » au second passage ; le premier passage lisait « $]\pi ; \pi]$ » impossible — *sic*] et $x_0$ trouvé est sa mesure principale ainsi $\cos(x) = \cos(x_0 + 2K\pi) = \cos x_0$

$$\sin(x) = \sin(x_0 + 2K\pi) = \sin x_0$$

Le cas $x < 0$ sera traité plus bas.

\* Pour $x < 0$, puisque $-x > 0$, $\cos(|x|) = \cos(-x)$ [confirmé second passage : bien $|x|$, redondant car $|x| = -x$]

$$\sin(|x|) = -\sin(-x)$$
[confirmé second passage : bien $|x|$ — *sic*, attendu $\sin(x) = -\sin(-x)$ car $|x| = -x$]

## Page 3

(numéro manuscrit entouré en bas à gauche : 3)

2/ Pré-estimation des complexités

Dans le cas principal $x \in [0 ; \pi/4]$ pour chaque $i = \overline{0,6}$ [lecture incertaine — « pour chaque $i = 0,6$ »]

il faudra faire - $2i$ multiplications et par multiplication une [raturé — « modtilliplication »] multiplication par 2 et une division (cas cos) soit à peu près $\sum_{i=0}^{6} i(1+1) = 2 \times 21 = 42$ opérations [lecture incertaine — le manuscrit porte « $2 \times$ [raturé] $= 42$ opérations »]

- $2i+1$ multiplications et par multiplication, une somme une multiplication par 2 et une division (cas sin) soit à peu près $\sum_{i=0} i(1+1+1) = 63$ opérations [lecture incertaine]

Dans l'ensemble, on a toujours un nombre fini d'opérations soit une complexité d'ordre $O(1)$ pour $x \in [0 ; \pi/4]$ et un cas plus complexe le cas échéant (on déterminera à la fin)

3/ Rédaction des fonctions

\* Fonction cos (x : réel par valeur) : réel

Début

Var $i, j$ : entier ;

$p, s, b, c$ : réel ;

Si $x \geqslant 0$ Alors

Si $0 \leqslant x \leqslant$ Pi/4 Alors

$s \leftarrow 1$ ; // pour $i = 0$, $s = 1$

Pour $i$ allant de 1 à 6 Faire

$p \leftarrow 1$ ;

Pour $j$ allant de 1 à $2i$ Faire

[raturé — « Si $j > 0$ Alors »]

$p \leftarrow (p \times x) /$ ([lecture incertaine — dénominateur biffé, probablement $j$]) $j$ ;

FinPour [écrit « Fin Pour »]

Si $i$ mod $2 = 0$ Alors

$s \leftarrow s + p$ ; // car $(-1)^i = 1$

## Page 4

(numéro manuscrit entouré en bas à gauche : 4)

Sinon

$s \leftarrow s - p$ ;

FinSi

FinPour

renvoyer $s$ ;

[raturé — « FinSi » / « Finsoin »]

Si [lecture incertaine — borne gauche biffée, probablement $\pi/4 <$] $x \leqslant$ Pi Alors

$b \leftarrow \cos(x/4)$ ;

$c \leftarrow 2 \times b \times b - 1$ ;

renvoyer $2 \times c \times c - 1$ ;

FinSi

Si $x > \pi$ Alors

Répéter

$x \leftarrow x - 2 \times$ Pi ;

Jusqu'à $x \leqslant \pi$ ;

renvoyer $\cos(x)$ ;

FinSi

Sinon

renvoyer $\cos(-x)$ ;

FinSi

Fin

## Page 5

(numéro manuscrit entouré en bas à gauche : 5)

\* Fonction sin (x : réel par valeur) : réel

Début

Var $i, j$ : entier ;

$p, s, b$ : réel ;

Si $x >= 0$ Alors

Si $0 \leqslant x \leqslant$ Pi/4 Alors

$s \leftarrow x$ ; // pour $i = 0$, $s = x$

Pour $i$ allant de 1 à 6 Faire

$p \leftarrow 1$ ;

Pour $j$ allant de 1 à $2i+1$ Faire

$p \leftarrow (p \times x) /$ ([raturé] $j$ [raturé]) ;

FinPour

Si $i$ mod $2 = 0$ Alors

$s \leftarrow s + p$ ; // car $(-1)^i = 1$

Sinon

$s \leftarrow s - p$ ;

FinSi

FinPour

renvoyer $s$ ;

FinSi

Si [lecture incertaine — borne gauche, probablement $\pi/4 <$] $x \leqslant$ Pi Alors

$b \leftarrow \sin(x/4)$ ;

[raturé — « renvoyer »]

Si $x \leqslant$ Pi/2 Alors

renvoyer $4 \times b \times$ sqrt$(1 - b \times b) (1 - 2b \times b)$ ;

Sinon

renvoyer $-4 \times b \times (1 - 2 \times b \times b) \times$ sqrt$(1 - b \times b)$ ;

FinSi

## Page 6

(numéro manuscrit entouré en bas à gauche : 6)

Si $x >$ Pi Alors

Répéter

$x \leftarrow x - 2 \times$ Pi ;

Jusqu'à $x \leqslant$ Pi ;

renvoyer $\sin(x)$ ;

[raturé — « FinSi » avec un « R » suscrit]

Sinon

renvoyer $-\sin(-x)$ ;

FinSi

Fin

4/ Preuve de Fonctionnement

- Sur le plan théorique, les formules de sin et cos avec le développement limité sont valides

- Pratique : on prend $x = 0{,}5$ [tableau de suivi barré d'une grande croix, colonnes $x$, $i$, $j$, $p$, $s$, $b$, $c$, Conclusion ; lignes « $0{,}5$ », « $0{,}5$ 1 », « $0{,}5$ 1 1 $0{,}25$ 1 » [reconstruction second passage — colonnes $j = 1$, $p = 0{,}25$ ; lu « $10{,}25$ » au premier passage], « $0{,}5$ 2 2 » et mention « Pour $i = 2$ à la fin » [confirmé second passage, marge gauche] ; Conclusion : « $x = 0 \to V$ », « $0 < x \leqslant$ Pi/4 $\to V$ » [confirmé second passage]]

- Dry running on prend $x = 0{,}5$

## Page 7

(pas de numéro visible)

\* $\cos(0{,}5) = ?$ — tableau de suivi, colonnes $x$ | $i$ | $j$ | $p$ | $s$ | $b$ | $c$ | condition. Transcription des lignes lisibles (les cellules vides sont notées « / » comme dans le manuscrit) :

| $x$ | $i$ | $j$ | $p$ | $s$ | $b$ | $c$ | condition |
|---|---|---|---|---|---|---|---|
| 0,5 | / | / | / | / | / | / | 0,5 $? = 0 \to V$ [lecture incertaine] |
| 0,5 | / | / | / | 1 | / | / | $0 < 0{,}5 \leqslant$ Pi/4 $\to V$ [lecture incertaine] |
| 0,5 | 1 | / | / | 1 | / | / | / |
| 0,5 | 1 | / | 1 | 1 | / | / | / |
| 0,5 | 1 | 1 | 1 | 1 | / | / | / |
| 0,5 | 1 | 1 | 0,5 [lecture incertaine] | 1 | / | / | / |
| 0,5 | 1 | 2 | 0,5 | 1 | / | / | / |
| 0,5 | 1 | 2 | 0,125 | 1 | / | / | / |
| 0,5 | 1 | 2 | 0,125 | 1 | / | / | $1$ mod $2 = 0 \to F$ |
| 0,5 | 1 | 2 | 0,125 | 0,875 | / | / | / |
| 0,5 | 2 | 4 | $2{,}604166669 \times 10^{-3}$ [lecture incertaine] | 0,877604166 | / | / | / |
| … [lignes intermédiaires peu lisibles] | | | | | | | / |
| 0,5 | 6 | 12 | $5{,}03626449 \times 10^{-13}$ [lecture incertaine] | 0,877582561 | / | / | / |

$\Rightarrow \cos(0{,}5) = 0{,}877582561$ avec les 3 chiffres exacts [« avec les 3 chiffres exacts » en marge à droite avec une flèche]

\* $\sin(0{,}5) = ?$ — tableau de suivi, colonnes $x$ | $i$ | $j$ | $p$ | $s$ | $b$ | condition. Lignes lisibles :

| $x$ | $i$ | $j$ | $p$ | $s$ | $b$ | condition |
|---|---|---|---|---|---|---|
| 0,5 | / | / | / | 0,5 | / | / |
| 0,5 | 1 | 3 | 0,02083333 | 0,47916666 | / | / |
| … [lignes intermédiaires peu lisibles] | | | | | | |
| 0,5 | 6 | 13 | $1{,}0505\dots \times 10^{-14}$ [lecture incertaine] | 0,479425538 | / | / |

$\Rightarrow \sin(0{,}5) = 0{,}479425538$

## Page 8

(numéro manuscrit entouré en bas à gauche : 9)

\* cos Au pire des cas

- pour $x \in [0 ; \pi/4]$, $C(x) = O(1)$ car le développement limité appliqué à un nbre d'opérations ne dépendant pas de $x$ est toujours fini

- pour $x \in$ [raturé — borne gauche, probablement $]\pi/4$] $; \pi]$, le résultat (l'observation) est le même $C(x) = O(1)$

- pour $x > \pi$, $C(x) = O(E(\frac{x}{2\pi})) + C(x - E(x/2\pi) \times 2\pi)$ [lecture incertaine — le manuscrit porte « $E(\frac{x}{2\pi})$ » avec $E$ = partie entière]

↑ il faut effectuer à peu près ce nombre d'opérations pour ramener $x$ dans $]0 ; \pi]$ (soustractions) ; ↑ on calcule alors … [lecture incertaine — annotations à flèches]

Et … de la mesure principale de $x$ : $x - E(\frac{x}{2\pi}) \times 2\pi \in ]0 ; \pi]$

or $C(-x) = O(C(x))$ [raturé — suite biffée] ainsi $\forall x \in ]0 ; \pi]$, $C(x) = O(1)$ d'où $C(x) = O(x) + O(1) = O(x)$

- pour $x < \pi$ [*sic* — probablement $x < 0$], $C(-x) = O(\cos) = O(x)$ [lecture incertaine]

ainsi au pire des cas $\begin{cases} C(x) = O(1) \text{ pour } x \in ]0 ; \pi] \\ C(x) = O(x) \text{ sinon} \end{cases}$

\* sin

Cet algorithme étant similaire à celui de cos, on montre que $\begin{cases} C(x) = O(1) \text{ pour } x \in ]0 ; \pi] \\ C(x) = O(x) \text{ sinon} \end{cases}$

## Page 9

(pas de numéro visible)

II/ Fonction ln

1/ Principe

\* Pour $x \in [1 ; 2]$, $1 - x \in [-1 ; 0]$ Les erreurs des calculs de puissance dans le développement limité sont insignifiantes [lecture incertaine — « insignifiantes » ou « négligeables »]

D'après le prérequis, $\ln x = \sum_{k=1}^{n} \frac{(-1)^{k-1}(x-1)^k}{k} + \frac{(\ln)^n}{(n+1)c^{n+1}}$ [lecture incertaine — reste peu lisible] $c \in \mathbb{R}$ ou $c \in [1 ; x]$ [lecture incertaine]

On approchera ainsi $\ln x$ par $\sum_{k=1}^{n} \frac{(-1)^{k-1}(x-1)^k}{k}$ avec une erreur $\left| \frac{(x-1)^n}{(n+1)c^{n+1}} \right| \leqslant \frac{1}{(n+1) \times 1^{n+1}}$

NB : on prendra en entrée le nombre exact de décimales voulues dans le résultat ($d$) et pour avoir cela, il suffit que $\frac{1}{n+1} < 10^{-d} \Rightarrow n > 10^d - 1$ il suffit d'avoir $n = 10^d$

on prendra alors $\ln x = \sum_{k=1}^{n} \frac{(-1)^{k-1}}{k} \times \frac{(x-1)^x \times (x-1)^n}{x \text{ fois}}$ [*sic* — passage peu lisible] avec $n = 10^d$ pour $d$ chiffres exacts.

d'où l'utilisation de 2 boucles Pour, l'une pour le produit et l'autre la somme

\* Pour $x \in ]0 ; 1[$, $\exists! n \in \mathbb{N} \mid 2^{-n} < x < 2^{-n+1}$ et ainsi en posant $y = 2^n x \in ]1 ; 2[$, $\ln x = \ln(y \times 2^{-n}) = \ln y - n \ln 2$

\* Pour $x \in ]2 ; +\infty[$, $\exists! n \in \mathbb{N} \mid 2^n < x < 2^{n+1}$ et ainsi en posant $y = 2^{-n} x \in ]1 ; 2[$, $\ln x = \ln(y \times 2^n) = \ln y + n \ln 2$

2/ Pré-estimation de la complexité

- Pour $x \in [1 ; 2]$, le nombre d'opérations du développement limité dépend juste de $n = 10^d$ et on aura un nombre fini d'opérations pour $k = \overline{1, 10^d}$ ainsi $C(x, d) = O(10^d) = O(10^d)$ [le manuscrit porte « $C(x, d) = O(\text{[raturé]}) = O(10^d)$ »]

- Pour les autres cas un peu plus complexe, on reviendra à la fin

## Page 10

(numéro manuscrit entouré en bas à gauche : 11 [confirmé second passage])

3/ Rédaction de la fonction

Fonction ln (x : réel par valeur, d : entier par valeur) : réel

Début

Var $i, j, n$ : entier ;

$s, p, y$ : réel ;

Si $1 \leqslant x \leqslant 2$ Alors

$s \leftarrow 0$ ;

Pour $i$ allant de 1 à $10 \wedge d$ Faire

$p \leftarrow 1$ ;

Pour $j$ allant de 1 à $i$ Faire

$p \leftarrow (x-1) \times p$ ;

FinPour

Si $i$ mod $2 = 0$ Alors

$s \leftarrow s - p/i$ ;

Sinon

$s \leftarrow s + p/i$ ;

FinSi

FinPour

renvoyer $s$ ;

FinSi

[raturé — « Si $0 < x < 1$ Alors »]

$y \leftarrow x$ ;

$n \leftarrow 0$ ;

Si $0 < x < 1$ Alors

Répéter

$y \leftarrow y \times 2$ ;

$n \leftarrow n + 1$ ;

Jusqu'à $1 \leqslant y \leqslant 2$ ;

## Page 11

(numéro manuscrit entouré en bas à gauche : 12)

4/ Preuve de fonctionnement

- théoriquement, la méthode du développement limité est valide

- En pratique, prenons $x = 2$ et $d = 1$

En exécutant l'algorithme on a

$\ln 2 = \sum_{k=1}^{10} \frac{(-1)^{k-1}(x-1)^k}{k}$

$\ln 2 = 0{,}64563492$ avec au plus un chiffre exact après la virgule

5/ Calcul de la complexité

- Pour $x \in [1 ; 2]$, le développement limité n'est que fonction de $d$ [raturé — « $n$ ($x \in R$) »] comme justifié en 2/ d'où $C(x, d) = O(n) = O(10^d)$ où $n = 10^d$

- Pour $x \in ]0 ; 1[$, $\ln x = \ln y - n \ln 2$ où $y = 2^m x \in [1 ; 2]$ ainsi $C(x, d) = O(C(y, d) + m \times C(2, d))$ [raturé — « où $m = \log_2 y$ »] $= O(10^d) + O(10^d)$ [lecture incertaine] $1 \leqslant 2^m x \leqslant 2 \Rightarrow \log_2 \frac{1}{x} \leqslant m \leqslant \log_2 \frac{2}{x}$ ainsi au pire des cas $m = 1 - \log_2 x$ ainsi $C(x, d) = O(10^d) + O((1 - \log_2 x)10^d)$ $C(x, d) = O(10^d(2 - \log_2 x)) = O(10^d \log_2(\frac{4}{x}))$

[raturé — « $\approx O(10^d)$ »]

- Pour $x > 2$, $\ln x = \ln y + n \ln 2$ où $y = x2^{-m}$ [*sic* — « $x2^{-m}$ », probablement $y = x \cdot 2^{-m}$] De même que pour le cas précédent $1 \leqslant y \leqslant 2 \Rightarrow \log_2$ [suite peu lisible] et on obtient en raisonnant de même $C(x, d) = O(10^d) + O(10^d \times \log_2 \frac{1}{x})$ [lecture incertaine] $(C(x, d) = O(10^d \log_2(2x)))$

---

## Figures

Aucune courbe ni schéma sur les pages relues (1, 7 + second passage 2–6, 8–11 le 2026-09-07, /tmp/s7/, pdftoppm -png -r 150) : les tableaux de suivi (dry running de $\cos(0{,}5)$, $\sin(0{,}5)$, p. 6–7) sont transcrits en markdown ci-dessus, pas de PNG requis.

## Vocabulaire

- DL = développement limité ; $O(\cdot)$ = complexité ; $E(\cdot)$ = partie entière ; Pi = $\pi$ ; mod = modulo.
- dry running = exécution à la main (tableau de suivi $x, i, j, p, s, b, c$) ; $d$ = nombre de décimales voulues ; $n = 10^d$.
