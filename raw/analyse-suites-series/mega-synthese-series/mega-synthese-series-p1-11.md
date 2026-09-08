# Mega-synthèse séries — transcription partielle p1-11 (partie 1/2)

🧾 Source : [mega-synthese-series.pdf](mega-synthese-series.pdf) — 22 pages au total, ici partie 1/2, p1-11 manuscrites (encre bleue).
🔍 Contenu : série alternée et corollaire (p. 1), nature de $\sum \frac{1}{n}(z/(2-z))^n$ selon $Re(z)$ (p. 2), série alternée $U_n=(-1)^n n^a(e^{1/n}-1)^b$ et monotonie de $f(x)=(e^x-1)/x$ (p. 3-4), Cauchy vs d'Alembert avec preuve $\varepsilon'$ (p. 5), contre-exemple à la réciproque + règle de Raabe-Duhamel cas ① (p. 6), fin cas ① + cas ② + application $\sum 1/k^\alpha$ (p. 7), fin application + équivalent de $H_n(\alpha)$ pour $0<\alpha<1$ (p. 8), comparaison intégrale-série à termes positifs (p. 9-10), intuition de Stirling $\int_1^n \ln x\,dx$ vs $\ln(n!)$ et suite $U_n$ associée (p. 10-11).
📄 Note : restauration Datas1 du 2026-09-07 — transcription à l'identique, sans correction ni ajout ; fichier partiel explicite : partie 1/2, p1-11 ; p12-22 non traitées. Les erreurs du manuscrit sont signalées par [*sic*], les doutes par [lecture incertaine — …], les passages biffés par [raturé], les complétions par [reconstruction — motif].

## Page 1

Un peu de Séries :

Soit $\sum (U_n)_{n \ge n_0}$ une série alternée $\iff \forall n \in \mathbb{N} \, (n \ge n_0)$

$U_n U_{n+2} \le 0$ [*sic* — alternée attend $U_n U_{n+1} \le 0$]

Cela est possible ssi $\exists \, (a_n)_{n \ge n_0}$ de signe constant /

$\forall n \in \mathbb{N}, \, U_n = (-1)^n a_n \quad (n \ge n_0)$

$\Rightarrow$ | Posons $\forall n \in \mathbb{N} \, (n \ge n_0), \, a_n = (-1)^n U_n \Rightarrow U_n = (-1)^n a_n$

On a : $U_n U_{n+2} \le 0 \Rightarrow (-1)^n a_n (-1)^{n+2} a_{n+2} \le 0 \Rightarrow a_n a_{n+2} \ge 0$

CQFD

$\Leftarrow$ | On a : $U_n U_{n+2} = (-1)^n a_n (-1)^n a_{n+2}$ [lecture incertaine — exposants] $= -a_n a_{n+2}$ [*sic* — $(-1)^n(-1)^{n+2}=+1$] ($n \in \mathbb{N}, n \ge n_0$)

or $(a_n)_{n \ge n_0}$ de signe constant $\iff \forall n \in \mathbb{N} \, (n \ge n_0), \, a_n a_{n+2} \ge 0$

d'où $U_n U_{n+2} \le 0$ CQFD

Corollaire : $\sum (U_n)_{n \ge n_0}$ est alternée $\iff \exists \, (a_n)_{n \ge n_0}$ [raturé — symbole biffé avant « positive »] positive /

$\forall n \in \mathbb{N}, \, U_n = (-1)^n a_n$ ou $(-1)^{n+2} a_n$ (① entouré, marge droite)

Convergence. Si $|U_n| \to 0$ alors $\sum_{n \ge n_0} U_n$ (série alternée)

converge. On va juste traiter le cas $U_n = (-1)^n a_n$

avec $a_n \ge 0$, car l'autre est similaire

Soit $N \in \mathbb{N}$,

$R_N = \sum_{n \ge N_0} (-1)^n a_n \le a_{N+2} \sum_{n \in N_0} (-1)^n \le a_{N+1} \times 1$ [lecture incertaine — bornes et indices repris par surcharge]

car $\forall N, m \in \mathbb{N}, \, \sum_{n=N}^m (-1)^n \in \{-1, 1\}$ [lecture incertaine — ensemble d'arrivée]

Ainsi car $a_{N+n} \xrightarrow[n \to +\infty]{} 0$ alors [lecture incertaine — fin de ligne] d'où $\sum_{n \ge N} U_n$ cvge

[raturé — grand trait diagonal barrant tout le § « Convergence »]

## Page 2

Soit $z \in \mathbb{C}$. Nature de $\sum_{n \ge 1} \frac{1}{n} \left(\frac{z}{2-z}\right)^n$

Soit $n \in \mathbb{N}^*$. Posons $U_n = \frac{1}{n} \left|\frac{z}{2-z}\right|^n$ [lecture incertaine — $U_n$ ou $|U_n|$]

On a : $\left|\frac{U_{n+1}}{U_n}\right| = \frac{n}{n+1} \left|\frac{z}{2-z}\right| \xrightarrow[n \to +\infty]{} \left|\frac{z}{2-z}\right|$

Donc $|z| > |z-1|$ [lecture incertaine — membre de gauche ; manuscrit porte possiblement $|z|>|2-z|$] $\iff z\bar z > (z-1)(\bar z-1)$ [lecture incertaine — second facteur]

$\iff z\bar z > z\bar z - z - \bar z + 1$ [reconstruction — développement de $(z-1)(\bar z-1)$]

$\iff Re(z) > 1/2$ [lecture incertaine — $Re(z)$ ou $Re(1)$ ; *sic* — avec $|z|/|2-z|$ on attend $Re(z)>1$]

Ainsi, pour $Re(z) > 1/2$, $\sum_{n \ge 2} U_n$ dirge [*sic* — diverge]

- pour $Re(z) < 1/2$, $\sum_{n \ge 2} U_n$ cvge

- pour $Re(z) = 1/2$, $\exists b \in \mathbb{R} \,|\, z = 1/2 + ib$

on a : $\forall n \in \mathbb{N}, \, U_n = \frac{1}{n} \left(-\frac{z}{?}\right)^n = \frac{1}{n} (-1)^n \left(\frac{z}{|z|}\right)^n$ [lecture incertaine — base du second facteur]

Posons $\alpha = Arg\, z$. Comme $Re(z) = 1/2 > 0$, $\alpha = arctan\, \frac{b}{?} - arctan\,(2b)$ [lecture incertaine — arguments des $arctan$]

ainsi $U_n = \frac{1}{n} e^{i?n} \times e^{id?n} = \frac{1}{n} e^{in(?+2\alpha)} \equiv$ série trigonométrique,

Posons $?+2\alpha \in 2\pi\mathbb{Z} \iff \alpha \in \frac{\pi(2k-1)}{2} =$ [raturé — fin de ligne biffée]

$\iff \tan ? \to \pm\infty$ [lecture incertaine — argument]

$\iff 2b \to \pm\infty$ Absurde !

Ainsi on a tjrs $?+2\alpha \in \mathbb{R} \setminus 2\pi\mathbb{Z} \quad \forall b \in \mathbb{R}$ [lecture incertaine — membre de gauche]

Car $\frac{1}{n} \to 0$ alors $\sum_{n \ge 1} U_n$ cvge (③ entouré, bas droite)

## Page 3

. $\sum_{n \ge 1} U_n$ où $U_n = (-1)^n n^a (e^{1/n}-1)^b$

$\forall n \in \mathbb{N}^*, \, U_n = (-1)^n a_n$ où $a_n = \frac{1}{n^{b-a}} \left(\frac{e^{1/n}-1}{1/n}\right)^b = \frac{1}{n^{b-a}} f(1/n)$ [lecture incertaine — $f(1/n)\to 1$ en marge]

où $f : ]0,1] \to \mathbb{R}$

$x \mapsto f(x) = \frac{e^x-1}{x}$

. Car $\forall n \in ...$, $a_n \ge 0$ alors $U_n$ est alternée [lecture incertaine — quantificateur]

. Si $a \ge b$, $\lim_{n \to +\infty} a_{2n+2}$ [lecture incertaine — indice] $= \lim_{n \to +\infty} a_{2n} = +\infty \times 1 = +\infty$ (accolade « d'où $U_n \not\to 0$ »)

et $\lim_{n \to +\infty} U_{2n+1} = -\lim_{n \to +\infty} a_{2n+1} = -\infty$

donc $\sum_{n \ge 2} U_n$ dirge [*sic* — diverge]

. Sinon, $\lim_{n \to +\infty} a_n = 0$

Étudions $f$. $\forall x \in ]0,1], \, f'(x) = \frac{e^x x - e^x +1}{x^2} = \frac{g(x)}{x^2}$

où $\forall x \in I_{0,1]}$, $g(x) = e^x (x-1)+1$ [lecture incertaine — $I_{0,1]}$ pour $]0,1]$]

$\forall x \in ]0,1], \, g'(x) = e^x (x-1) + e^x = x e^x > 0$

d'où $g \nearrow *$ et donc $\forall x \in ]0,1], \, g(x) \in ]\lim_{0^+} g, g(1)] = ]0,1]$

Ainsi $f'(x) = 0 \iff g(x) = 0 \iff x = 0$ [raturé — symbole biffé après « $x=0$ »] et comme

$g(x) \ge 0$ sur $]0,1]$, $f'(x) > 0$ d'où $f \nearrow *$ sur $]0,1]$ et

on a : $f(]0,1]) = ]1, e-1]$. (④ entouré, marge droite)

Ainsi que $(1/n)$ est décroissante et que $f$ est $\nearrow *$ alors

($f(1/n)$ est décroissante — suite p. 4)

## Page 4 (suite p. 3)

Car $(f(1/n))_N \downarrow$ et positive, de m̂ que $\left(\frac{1}{n^{b-a}}\right)_N$ alors [reconstruction — exposant $b-a>0$ car cas $a<b$]

$\frac{1}{n^{b-a}} f(1/n) \downarrow$

En définitive $a_n \downarrow^+ 0$ d'où $\sum_{n \ge 2} U_n$ cvge

Donc $\sum_{n \ge 2} U_n$ cvge ssi $a < b$

## Page 5

Un peu de séries

* Cauchy Vs D'Alembert

Soit $(U_n)_{n \ge n_0}$, une suite cxple. $\left|\frac{U_{n+1}}{U_n}\right| \to l \Rightarrow \sqrt[n]{|U_n|} \to l$

En effet supposons que $\left|\frac{U_{n+1}}{U_n}\right| \to l$

Soit $\varepsilon > 0$. Cherchons $N \,|\, \forall n \in \mathbb{N}, \, n > N \Rightarrow |\sqrt[n]{|U_n|}-l| < \varepsilon$

Soit $\varepsilon' > 0$. Car $\left|\frac{U_{n+1}}{U_n}\right| \to l$ alors $\exists N_1 \,|\, \forall n \in \mathbb{N}, \, n > N_1 \Rightarrow \left||\frac{U_{n+1}}{U_n}|-l\right| < \varepsilon'$

Soit $n > N_1'$ On a : $-\varepsilon'+l \le \left|\frac{U_{n+1}}{U_n}\right| \le l+\varepsilon'$

$\max(N_1,n_0)$ [lecture incertaine — mention sous la ligne]

càd $(-\varepsilon'+l) |U_n| \le |U_{n+1}| \le |U_n| (l+\varepsilon')$

càd $(-\varepsilon'+l) |U_{n-1}| \le |U_n| \le |U_{n-1}| (l+\varepsilon')$ ($n > N_1'+2$)

càd $(-\varepsilon'+l)^{n-N_1'} |U_{N_1'}| \le |U_n| \le |U_{N_1'}| (l+\varepsilon')^{n-N_1'}$ (1)

or $\lim_{n \to +\infty} (|U_{N_1'}| (l+\varepsilon')^{n-N_1'})^{1/n} = l+\varepsilon'$ ainsi $\exists N_{21} \in \mathbb{N} \,|\, \forall n \in \mathbb{N},$

$n > N_{21} \Rightarrow \left|(|U_{N_1'}| (l+\varepsilon')^{n-N_1'})^{1/n} - (l+\varepsilon')\right| < \varepsilon' \Rightarrow (|U_{N_1'}| (l+\varepsilon')^{n-N_1'})^{1/n} < l+2\varepsilon'$ [reconstruction — majoration]

. $\lim_{n \to +\infty} (|U_{N_1'}| (-\varepsilon'+l)^{n-N_1'})^{1/n} = -\varepsilon'+l$ ainsi $\exists N_{22} \in \mathbb{N} \,|\, \forall n \in \mathbb{N},$

$n > N_{22} \Rightarrow \left|(|U_{N_1'}| (-\varepsilon'+l)^{n-N_1'})^{1/n} - (l-\varepsilon')\right| < \varepsilon' \Rightarrow |U_{N_1'}| (-\varepsilon'+l)^{n-N_1'} > l-2\varepsilon'$ [lecture incertaine — exposants et $l-2\varepsilon'$]

pour $n > N_2' = \max\{N_1', N_{21}, N_{22}\}$,

$(1) \Rightarrow l-2\varepsilon' \le \sqrt[n]{|U_n|} \le l+2\varepsilon'$

En particulier, pour $\varepsilon' = \varepsilon/2$

$(1) \Rightarrow |\sqrt[n]{|U_n|}-l| \le \varepsilon$

Il suffit de prendre $N = N_2'$, CQFD

## Page 6

. $\sqrt[n]{|U_n|} = l \not\Rightarrow \left|\frac{U_{n+1}}{U_n}\right| = l$

exemple : Considérons $(U_n)_\mathbb{N}$ : $\forall n \in \mathbb{N}, \, U_n = \begin{cases} (2/3)^n \text{ si } n \text{ est pair} \\ (2/3)^n \times 1/5 \text{ si } n \text{ est impair} \end{cases}$

Soit $n \in \mathbb{N}$

- On a : $\sqrt[n]{|U_n|} = \begin{cases} 2/3 \xrightarrow[n \to +\infty]{} 2/3 \text{ si } n \text{ pair} \\ 2/3 \times 1/\sqrt[n]{5} \xrightarrow[n \to +\infty]{} 2/3 \text{ si } n \text{ impair} \end{cases} \Big\} \xrightarrow[n \to +\infty]{} 2/3$

- Mais $\left|\frac{U_{n+1}}{U_n}\right| = \begin{cases} 2/15 \xrightarrow[n \to +\infty]{} 2/15 \text{ si } n \text{ impair} \\ 10/3 \xrightarrow[n \to +\infty]{} 10/3 \text{ si } n \text{ impair} \end{cases} \Big\}$ et donc $\left|\frac{U_{n+1}}{U_n}\right| \not\to$ [lecture incertaine — parité et limite]

* Règle de Raabe-Duhamel : Soit $(U_k)_{k \ge K_0}$ une suite de nbres réels (tous pres) non nuls [lecture incertaine — « tous presque » ?]

- Si $\forall k > K_0, \, \left|\frac{U_{k+1}}{U_k}\right| \le 1 - \frac{\beta}{k}$ ($\beta>1$) alors $\sum_{k \ge K_0} U_k$ abs cvge (1)

- Si $\forall k > K_0, \, \left|\frac{U_{k+1}}{U_k}\right| \ge 1 - \frac{1}{k}$ alors $\sum_{k \ge K_0} U_k$ pas abs cvge (2)

En effet, [Cas ①]

Soit $K_0, K_0$. On a : $|U_{k+1}| k \le |U_k| (k-\beta)$ (a)

càd $|U_{k+1}| k < |U_k| (k-1)$ car $\beta > 1$ [lecture incertaine — manuscrit porte $\beta>2$ ?]

donc $(|U_k|(k-1))_{k > \max(K_0,1)}$ est décroissante strict décroissante [*sic* — redondance]

et minorée par $0$ d'où cvge

or $(a) \Rightarrow ... (\beta-1)|U_k| \le |U_k|(k-1) - |U_{k+1}| k$ [reconstruction — membre gauche]

Car la série télescopique $\sum_{k \ge K_0} |U_k|(k-1) - |U_{k+1}| k = |U_{K_0}|(K_0-1) - \lim_{k \to +\infty} k|U_k|$

## Page 7

cvge alors $\sum_{k \ge K_0} (\beta-1)|U_k|$ cvge et car $\beta>1 \Rightarrow (\beta-1) \ne 0$ [lecture incertaine — fin de ligne biffée], alors $\sum_{k \ge K_0} |U_k|$ cvge.

Cas ②

Soit $K_2, K_0$. On a : $k|U_{k+1}| \ge (k-1)|U_k|$ (a)

- Approche 1 : Pour $k > K_2+2$, $(a) \Rightarrow |U_k| \ge \frac{K-1}{k-1} |U_{K+1}|$ [lecture incertaine — indices]

$\ge \frac{(K-1)(K-1-1)...K'(K'-1)}{(k-1)...} |U_k|$ [lecture incertaine — produit télescopique]

$\ge \frac{(K_2'+1)|U_{K_2'}|}{k-1}$ [lecture incertaine]

où $K' = \max(2, K_0)$ [lecture incertaine]

Car $\sum_{k > K'} \frac{(K_2'+1)|U_{K'}|}{k-1}$ diverge alors $\sum_{k > K'} |U_k|$ diverge d'où $\sum_{k \ge K_0} |U_k|$ diverge

- Approche 2 : $(a) \Rightarrow$ la suite $((k-1)|U_k|)_{k > K_0}$ est croissante

et comme $|U_k| \ne 0 \, \forall k > K_0$, pour $K_0' = \max(2, K_0)$ [raturé — « pour $K_2$ » biffé], pour $k > K_0' = \max(2, K_0)$, $(k-1)|U_k| \ge (K_0'-1)|U_{K_0'}| \Rightarrow |U_k| \ge \frac{K_0'-1}{k-1}|U_{K_0'}|$

et on conclut car en amont.

* Application : Nature de $\sum_{k \ge 1} \frac{1}{k^\alpha}$ avec $\alpha > 1$ [lecture incertaine — $\alpha>1$ ou $\alpha$ quelconque]

$\forall k \ge 1, \, \left|\frac{U_{k+1}}{U_k}\right| = \frac{k^\alpha}{(k+1)^\alpha} = (1+\frac{1}{k})^{-\alpha} = \frac{1}{(1+1/k)^\alpha}$ $\to$ pour $k > K_0$ où $K_0$ est à dét[erminer] [lecture incertaine — fin de ligne]

Cherchons $\beta>1 \,|\, \left|\frac{U_{k+1}}{U_k}\right| + \frac{\beta}{k} \le 1 \iff f(1/k) \le 1$ où

$f : \forall x \in [0,1], \, f(x) = \frac{1}{(1+x)^\alpha} + \beta x$

$f$ est $C^1$ d'où $\forall x \in [0,1], \, f'(x) = \frac{-\alpha}{(1+x)^{\alpha+1}} + \beta$.

## Page 8

Car $f(0) = 1$ on demanderait avoir un intervalle $[0,x_0[$ sur

$f$ y soit décroissante. Pour cela il est nécessaire que $f'(0) < 0$.

or $f'(0) = \beta - \alpha$. Ainsi prenons $\beta$ dans $]1,\alpha[$.

On a : $f'(0) < 0$ ainsi $\exists x_0 \in ]0,1] \,|\, f \searrow$ sur $[0,x_0]$

ainsi $\forall x \in [0,x_0]$, $f(x) \le f(0) = 1$

Pour $k \ge K_0 = E(1/x_0)+1$, car $1/k \le x_0$ alors $f(1/k) \le 1$

d'où $\left|\frac{U_{k+1}}{U_k}\right| \le 1 - \frac{\beta}{k}$ ainsi $\sum_{k \ge 1} \frac{1}{k^\alpha}$ est absolument cvge et donc cvge

* Équivalent de $\sum_{k=1}^n \frac{1}{k^\alpha} = H_n(\alpha)$ $\alpha \ne 1$

Soit $n \in \mathbb{N}^*$

$\forall k \in [1,n+1[$ [lecture incertaine — intervalle], $\frac{1}{(k+1)^\alpha} \le \int_k^{k+1} \frac{1}{t^\alpha} dt \le \frac{1}{k^\alpha}$

[raturé — ligne biffée entre les deux encadrements]

En passant $\sum_{k=1}^m$ puis $\sum_{k=1}^n$ on a :

$H_n(\alpha)-1 \le \int_1^n \frac{1}{k^\alpha} dt \le H_{m?}(\alpha)$ et [lecture incertaine — bornes]

$H_{m?}(\alpha)-1 \le \int_1^{m+1} \frac{1}{k^\alpha} dt \le H_n(\alpha)$ [lecture incertaine — indices]

ainsi $\frac{1}{1-\alpha} ((...)^{1-\alpha}-1) \le H_n(\alpha) \le 1 + \frac{1}{1-\alpha} (n^{1-\alpha}-1)$ [lecture incertaine — membre gauche]

d'où $\boxed{H_n(\alpha) = \sum_{k=1}^n \frac{1}{k^\alpha} \sim \frac{n^{1-\alpha}}{1-\alpha}}$ pour $0<\alpha<1$

## Page 9

* Comparaison ITS en $\infty$ et série à termes positifs

Soit $\sum_{n \ge n_0} U_n$ une série $|$ $\forall n \in \mathbb{N} \, (n \ge n_0), \, U_n \ge 0$.

Supposons $\exists g$ (décroissante) à valeurs positives sur $[n_0,+\infty[ \,|\, \forall n \in \mathbb{N} \, (n \ge n_0), \, U_n = f(n)$ [*sic* — $g$ annoncé puis $f$ utilisé]

On a : $I = \int_{n_0}^{+\infty} f(t)\,dt$ et $\sum_{n \ge n_0} U_n$ sont de m̂ nature.

En effet $\forall n \in \mathbb{N} \, (n_0, n_0+1)$ [lecture incertaine — quantificateur],

- $\forall t \in [n-1,n]$, Car $f \searrow$ alors $f(t) \ge f(n) = U_n$

d'où $\int_{n-1}^n f(t)\,dt \ge \int_{n-1}^n U_n\,dt = U_n$

- $\forall t \in [n,n+1]$, car $f \searrow$ alors $f(t) \le f(n) = U_n$ d'où

$\int_n^{n+1} f(t)\,dt \le \int_n^{n+1} U_n\,dt = U_n$

Ainsi $\int_n^{n+1} f(t)\,dt \le U_n \le \int_{n-1}^n f(t)\,dt$

En passant $\sum_{n=n_0+1}^N$ $\forall N \in \mathbb{N} \, (N \ge n_0+1)$, on a :

$\int_{n_0+1}^{N+1} f(t)\,dt \le \sum_{n=n_0}^N U_n - U_{n_0} \le \int_{n_0}^N f(t)\,dt$

càd $U_{n_0} + \int_{n_0+1}^{N+1} f(t)\,dt \le \sum_{n=n_0}^N U_n \le U_{n_0} + \int_{n_0}^N f(t)\,dt$

or $\forall t \in [n_0,n_0+1]$, $f(t) \le f(n_0) = U_{n_0}$ d'où $\int_{n_0}^{n_0+1} f(t)\,dt \le \int_{n_0}^{n_0+1} U_{n_0}\,dt = U_{n_0}$

ainsi on a : $\int_{n_0}^{N+1} f(t)\,dt \le \sum_{n=n_0}^N U_n \le U_{n_0} + \int_{n_0}^N f(t)\,dt$ (bas taché, encre pâle)

## Page 10

$\Rightarrow$ |Supp $\sum_{n \ge n_0} U_n$ cvge.

Soit $x \in [n_0,+\infty[$. Posons $N = E(x)+1 > x$

on a : $\int_{n_0}^x f(t)\,dt \le \int_{n_0}^{N+1} f(t)\,dt \le \sum_{n=n_0}^N U_n \le \sum_{n=n_0}^{+\infty} U_n$ car $U_n \ge 0$ ($n \in [n_0,+\infty[$)

Ainsi [raturé — « On passant aux limites » biffé], car $F(x) = \int_{n_0}^x f(t)\,dt$ est croissante

et majorée par $\sum_{n=n_0}^{+\infty} U_n$ alors $\int_{n_0}^{+\infty} f(t)\,dt \in \mathbb{R}$ CQFD

$\Leftarrow$ |Supp $I$ cvge. En particulier

On a : $\sum_{n=n_0}^N U_n \le U_{n_0} + \int_{n_0}^N f(t)\,dt \le U_{n_0} + \int_{n_0}^{+\infty} f(t)\,dt$ car $f \ge 0$ (sur $[n_0,+\infty[$)

($\forall N \in \mathbb{N}, N \ge n_0$)

Car $\forall n \in \mathbb{N} \, (n \ge n_0), \, U_n \ge 0$ alors $\sum_{n=n_0}^N U_n$ est croissante et

majorée d'où $\sum_{n=n_0}^{+\infty} U_n \in \mathbb{R}$ CQFD

Rq : On montre de m̂ que $\forall N \in \mathbb{N} \, (N \ge n_0)$,

$\int_{N+1}^{+\infty} f(t)\,dt \le R_N = \sum_{n=N+1}^{+\infty} U_n \le \int_N^{+\infty} f(t)\,dt$

* Approximation de Stirling :

Intuition : tentative de comparaison de

$\int_1^n \ln x\,dx = n\ln n - n +1$ et $\sum_{k=1}^n \ln k = \ln(n!)$

## Page 11

Hors? Par calcul, on y conjecture [lecture incertaine — premier mot]

$\int_1^n \ln x\,dx \approx \sum_{k=1}^n \ln k - \frac{1}{2}\ln n$

càd $n\ln n - n +1 \simeq \ln n! - \frac{1}{2}\ln n \Rightarrow n\ln n - n \simeq \ln n! - \frac{1}{2}\ln n$ pour $n$ très grand

Étudions pour ce fait la nature de la suite

$U_n = \ln n! - \frac{1}{2}\ln n - n\ln n + n -1/2$ [lecture incertaine — constante finale] $(n \in \mathbb{N}^*)$

$= -\ln n\,(n+\frac{1}{2}) + n -1 + \ln ... \ln n!$ [lecture incertaine — fin de ligne ; raturé — membre biffé]

$(U_n)_{N^*}$ est de m̂ nature que $\sum_{n \ge 2} V_n$

où $\forall n \in \mathbb{N}^*, \, V_n = U_{n+1} - U_n$

$= \ln(n+1)! - \frac{1}{2}\ln(n+1) - (n+1)\ln(n+1) + n+1 ...$ [lecture incertaine — constante]

$- \ln n! + \frac{1}{2}\ln n + n\ln n - n ...$ [lecture incertaine — constantes]

$= (n+\frac{1}{2})\ln(n+1)$ [lecture incertaine — signe] $+ (n+\frac{1}{2})\ln n +1$

$= -(n+\frac{1}{2})\ln(1+\frac{1}{n}) +1$

$= -(n+\frac{1}{2})(\frac{1}{n} - \frac{1}{2n^2} + \frac{1}{3n^3} + o(\frac{1}{n^3})) +1$

$= - ... - \frac{1}{12n^2} - \frac{1}{...} + o(\frac{1}{n^2})$ [raturé — premier terme biffé ; lecture incertaine — coefficients]

d'où $\sum_{n \ge 2} V_n$ cvge et donc $(U_n)_{N^*}$ converge

## Figures

Aucune figure en p1-11 : pages de texte manuscrit seul, sans schéma, sans capture, sans tableau. Aucun script `reproduce_mega_synthese_pXX.py` ni PNG généré pour cette plage — 0 PNG, motif : rien à reproduire.

## Vocabulaire

- cvge / crge / cnge : converge ; dirge / diryge / drge : diverge ; abs cvge : absolument convergente ; pas abs cvge : pas absolument convergente.
- cxple : complexe [lecture incertaine — « complexe »] ; nbres réels : nombres réels ; tous pres : [lecture incertaine — « tous presque » ?].
- m̂ / de m̂ : de même ; tjrs : toujours ; càd : c'est-à-dire ; or : or ; donc / d'où / ainsi : articulations.
- Supp : supposons / supposons que ; Mq : montrons que ; CQFD : ce qu'il fallait démontrer ; Rq : remarque.
- ITS : intégrale [lecture incertaine — « intégrale » ?] ; $E(x)$ : partie entière ; $\nearrow *$ / $\searrow$ / $\downarrow$ : (strictement) croissante / décroissante ; $\downarrow^+ 0$ : décroît vers $0$ par valeurs positives.
- $H_n(\alpha)=\sum_{k=1}^n 1/k^\alpha$ ; $R_N$ : reste ; $F(x)=\int_{n_0}^x f(t)dt$.
- [*sic*] garde les graphies d'origine : alternée, trichromie $a_n$/$f$/$g$, $U_nU_{n+2}$, $-\,a_na_{n+2}$, $\sum_{n\ge2}$ pour $\sum_{n\ge1}$.
