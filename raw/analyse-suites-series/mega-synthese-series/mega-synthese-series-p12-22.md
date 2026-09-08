# Mega-synthèse séries — transcription partielle p12-22 (partie 2/2)

🧾 Source : [mega-synthese-series.pdf](mega-synthese-series.pdf) — 22 pages au total, ici partie 2/2, p12-22 manuscrites (encre bleue).
🔍 Contenu : fin de Stirling + constante $K$ via Wallis (p. 12-13), série harmonique et constante d'Euler $\gamma$ (p. 14), permutations des séries : théorème absolu, contre-exemple semi-convergent (p. 15-18), produit de Cauchy : théorème, cas positif, cas contraire, contre-exemple semi-convergent (p. 19-22).
📄 Note : restauration Datas1 du 2026-09-07 — transcription à l'identique, sans correction ni ajout ; fichier partiel explicite : partie 2/2, p12-22 ; p1-11 traitées dans `mega-synthese-series-p1-11.md`. Les erreurs du manuscrit sont signalées par [*sic*], les doutes par [lecture incertaine — …], les passages biffés par [raturé], les complétions par [reconstruction — motif].

## Page 12 (suite p. 11)

Ainsi $\exists C \in \mathbb{R} \, / \, \lim_{n \to +\infty} \ln n! - (\frac{1}{2}+n)\ln n + n = C$

càd $\lim_{n \to +\infty}$ [raturé — « $\ln n!$ » repris par surcharge] $n! \times n^{-(\frac{1}{2}+n)} \times e^n = e^C \to K$ [lecture incertaine — parenthésage $(e^C)$]

càd $n! \underset{+\infty}{\sim} K\sqrt{n} \times (\frac{n}{e})^n$

. Mqy $K = \sqrt{2\pi}$ ! On pose par l'intégrale de wallis, $I_n = \int_0^{\pi/2} \sin^n t\,dt$ [lecture incertaine — $I_{n_2}$ ?]

Soit $n \in \mathbb{N}$ ($n \ge 2$) [raturé — « Soit » repris par surcharge]

$I_n = -\int_0^{\pi/2} \sin^{n-1} t\,d(\cos t) = -[\sin^{n-1} t \cos t]_0^{\pi/2} + \int_0^{\pi/2} (n-1)\cos^2 t \sin^{n-2} t\,dt$ [lecture incertaine — $d(\cos t)$]

$= (n-1)\left(\int_0^{\pi/2} \sin^{n-2} t\,dt - \int_0^{\pi/2} \sin^n t\,dt\right) = (n-1)I_{n-2} - (n-1)I_n$

d'où $I_n = \frac{n-1}{n} I_{n-2}$

. Si $n$ pair ($n = 2k, k \ge 1$), $I_{2k} = \frac{2k-1}{2k} I_{2k-2} = \frac{2k-1}{2k} \times \frac{2k-3}{2k-2} \times ... \times \frac{1}{2} \times I_0$ [lecture incertaine — fin du produit]

$I_{2k} = \frac{(2k-1)!!}{(2k)!!} \times \frac{\pi}{2} = \frac{(2k-1)!}{2k \times (2k-2)!!^2} \times \frac{\pi}{2} = \frac{(2k-1)!}{2k \times [2^{k-1} \times (k-1)!]^2} \times \frac{\pi}{2}$ [lecture incertaine — factorielles et doubles-factorielles]

$I_{2k} = \frac{(2k-1)!}{2^{2k} k! (k-1)!} \times \pi = \frac{\pi}{2^{2k}} C_{2k-2}^k$ [lecture incertaine — indice du coefficient binomial]

. Si $n$ impair ($n = 2k+1, k \ge 1$), $I_{2k+1} = \frac{2k}{2k+1} I_{2k-1} = \frac{2k}{2k+1} \times \frac{2k-2}{2k-1} \times ... \times \frac{2}{3} \times I_1$ [lecture incertaine — fin du produit]

d'où $I_{2k+1} = \frac{(2k)!!}{(2k+1)!!} \times 1 = \frac{[(2^k k)!]^2}{(2k+1)!}$ [lecture incertaine — $(2^k k!)^2$] $= \frac{2^{2k} (k!)^2}{(2k+1)!}$

Ainsi (suite p. 13)

## Page 13 (suite p. 12)

De plus $(I_n)_\mathbb{N}$ est décroissante d'où pour $p \ge 2$

$I_{2p+1} \le I_{2p} \le I_{2p-1}$ [tranché au r250+crop ×2 — le manuscrit porte 2p−1, pas 2p−2]

càd $1 \le \frac{I_{2p}}{I_{2p+1}} \le \frac{I_{2p-1}}{I_{2p+1}} = \frac{2p+1}{2p} \to 1$ [tranché au r250+crop ×2 — identité de Wallis exacte]

donc $\frac{I_{2p}}{I_{2p+1}} \to 1$ (formule de Stirling) [tranché au r250]

d'où $\frac{I_{2p}}{I_{2p-1}} = \frac{I_{2p}}{I_{2p+1}} \times \frac{I_{2p+1}}{I_{2p-1}} \to 1 \times 1$ [tranché au r250+crop ×2 — « 1×1 » lisible]

càd $\frac{(2k-1)!}{2^{2k} k! (k-1)!} \times \pi \times \frac{2^{2k-2} ((k-1)!)^2}{(2k-1)!}$ [lecture incertaine — produit] $\to 1$ $k = p$ [tranché au r250+crop — mention marginale « k=p »]

càd $\frac{(2k)! \,\pi\, k}{2k \times 2^{2k} \times k! \times k!} \times \frac{(2k)! \times k^2}{2k \times 2^{2k-2} \times k!^2}$ [lecture incertaine — produit télescopique] $\to 2$ [tranché au r250+crop — « →2 » lisible]

càd $\left(\frac{(2k)!}{k!^2}\right)^2 \times \frac{\pi}{2^{4k}} \times k \to 2$ [lecture incertaine — regroupement]

càd $\frac{\text{[raturé — membre biffé]}}{...} \frac{1}{...} \left(\frac{2^{2k} (k!)^2}{(2k)!}\right)^2$ [lecture incertaine — fraction inversée] $\to \pi$

or $\frac{1}{k}\left(\frac{2^{2k} (k!)^2}{(2k)!}\right)^2 \underset{+\infty}{\sim} \frac{?}{k} \left(2^{2k} \times \frac{K\sqrt{k}}{e^{\sqrt{2k}}} \left(\frac{k}{e}\right)^{2k} \times \left(\frac{e}{2k}\right)^{2k}\right)^2$ [lecture incertaine — substitution de Stirling, $K$ et exposants repris par surcharge]

$\underset{+\infty}{\sim} \frac{?^2}{k} \left(\frac{\sqrt{k}}{?}\right)^2$ [lecture incertaine — simplification]

donc $\lim_{k \to +\infty} \frac{C^2}{k} \sqrt{\frac{k}{2}}^2 = 6$ [tranché au r250+crop — le manuscrit porte bien « 6 » ; *sic* — on attend $\pi$] $\Rightarrow \lim_{k \to +\infty} \frac{C^2}{2} = 6$ [tranché au r250+crop — idem]

$\Rightarrow C = \sqrt{26}$ [tranché au r250+crop — tracé « √26 » ; *sic* — lapsus, la dernière ligne conclut $\sqrt{2\pi n}$]

Donc $n! \underset{+\infty}{\sim} \underline{\sqrt{2\pi n} \, (n/e)^n}$ CQFD (résultat souligné)

## Page 14

* Série Harmonique : comportement asymptotique

Soit $n \in \mathbb{N}^*$. Posons $V_n = \sum_{k=1}^n \frac{1}{k} - \ln n$

$(V_n)_\mathbb{N^*}$ est de m̂ nature que $\sum_{n \ge 2} U_n$ où $\forall n \in \mathbb{N}^*$,

$U_n = V_{n+1} - V_n = \frac{1}{n+1} - \ln(1+\frac{1}{n}) = \frac{1}{n+1} - \frac{1}{n} + \frac{1}{2n^2} + o(\frac{1}{n^2})$

càd $U_n = \frac{-1}{n(n+1)} + \frac{1}{2n^2} + o(\frac{1}{n^2})$

or $\frac{-1}{n(n+1)} \underset{+\infty}{\sim} \frac{-1}{n^2}$ et car $\sum_{n \ge 2} \frac{-1}{n^2}$ crge absolument car $\sum_{n \ge 1} \frac{-1}{n(n+1)}$ [lecture incertaine — second membre]

crge. De plus $\sum_{n \ge 2} \frac{1}{2n^2}$ crge. Enfin car $\sum_{n \ge 2} \frac{1}{n^2}$ crge absolu- [lecture incertaine — coupure de ligne]

ment, $\sum_{n \ge 2} O(\frac{1}{n^2})$ crge donc $\sum_{n \ge 2} U_n$ crge d'où $(V_n)_\mathbb{N^*}$ crge

. Équivalent de $(H_n)_\mathbb{N^*}$ : $\forall n \in \mathbb{N}^*, H_n = \sum_{k=1}^n \frac{1}{k}$

$\forall n \in \mathbb{N}^*, \frac{H_n}{\ln n} = \frac{V_n + \ln n}{\ln n} = \frac{V_n}{\ln n} + 1 \longrightarrow \frac{\lim_{+\infty} V_n}{+\infty} + 1 = 1$ car $\lim_{+\infty} V_n \in \mathbb{R}$

donc $H_n \underset{+\infty}{\sim} \ln n$.

Note : le réel $\gamma = \lim_{n \to +\infty} V_n = \lim_{n \to +\infty} \sum_{k=1}^n \frac{1}{k} - \ln n = \lim_{N \to +\infty} \sum_{n=1}^N \frac{1}{n} - \ln(1+\frac{1}{n})$ [lecture incertaine — dernier membre]

(car $\sum_{n \ge 1} V_{n+1} - V_n = \gamma - V_1 \Rightarrow \sum_{n=1}^{+\infty} \frac{1}{n+1} - \ln(1+\frac{1}{n}) = \gamma - 1$ [lecture incertaine — bornes et second membre]

d'où $\gamma = 1 + \sum_{n=1}^{+\infty} \frac{1}{n+1} - \frac{1}{n} + \sum_{n=1}^{+\infty} \frac{1}{n} - \ln(1+\frac{1}{n})$ [lecture incertaine — découpage]

càd $\gamma = 1 + 0 - \frac{1}{1} + \sum_{n=1}^{+\infty} \frac{1}{n} - \ln(1+\frac{1}{n}) = \sum_{n=1}^{+\infty} \frac{1}{n} - \ln(1+\frac{1}{n})$ [lecture incertaine — télescopage]),

est conventionnellement appelé : la constante d'Euler-Mascheroni et vaut $\gamma \simeq 0,577$

## Page 15

* Permutation :

Thos : Soit $\sum_{k \ge K_0} U_k$ une série abs crgte, soit $\sigma : [\![K_0,+\infty[\! \to [\![K_0,+\infty[\!$ [raturé — fin biffée] une permutation (bijection)

alors $\sum_{k \ge K_0} U_{\sigma(k)}$ est abs crgte

En effet Soit $n \in \mathbb{N}$ ($n \ge K_0$) $\le \sum_{k=K_0}^{+\infty} |U_k|$ [lecture incertaine — majoration]

$\sum_{k=K_0}^n |U_{\sigma(k)}| \le \sum_{k=K_0}^m |U_k|$ où $m = \max\{\sigma(k)\}_{k \le n}$ [lecture incertaine — $m = \max \sigma(k), k \le n$]

Car $\left(\sum_{k=K_0}^n |U_{\sigma(k)}|\right)_{n \ge K_0}$ est croissante et [raturé — « crge » biffé] majorée

alors elle crge CQFD

dreemple : (cas où $\sum_{k \ge K_0} U_k$ est juste semi-convergente

et $\exists \, \sigma \, / \, \sum_{k \ge K_0} U_{\sigma(k)}$ est divergente)

Considérons $\sum_{n \ge 1} \frac{(-1)^n}{n}$ de somme $S = \ln 2$ [lecture incertaine — $(-1)^n$ ou $(-1)^{n+1}$]

Considérons $\sigma : \mathbb{N}_{>0} \to \mathbb{N}_{>0}$ [raturé — première définition biffée d'une grande croix]

$n \mapsto \sigma(n)$ [raturé — formules $2k+1$ si $n = 2k+1$ etc. biffées]

Il est clair que $\sigma$ est une bijection de $\mathbb{N}_{>0}$ vers $\mathbb{N}_{>0}$ (encadré, marge gauche)

$\sigma(n) = \begin{cases} 2k+1 \text{ si } n = 2k+2, k \in \mathbb{N} \\ 4k+2 \text{ si } n = 3k+2, k \in \mathbb{N} \\ 4k \text{ si } n = 3k \quad k \in \mathbb{N}^* \end{cases}$ [lecture incertaine — conditions et accolade]

## Page 16 (suite p. 15)

Pour tout $n \in \mathbb{N}$,

$S'_{3n} = \sum_{k=1}^{3n} \frac{(-1)^{\sigma(k)-1}}{\sigma(k)}$ [lecture incertaine — exposant $\sigma(k)-1$]

$= \sum_{k=0}^{n-1} \frac{(-1)^{\sigma(3k+3)-1}}{\sigma(3k+3)}$ [raturé — première somme biffée] $+ (-1)^{\sigma(3n)} $ [lecture incertaine — exposant]

$= \sum_{k=0}^{n-1} \frac{(-1)^{\sigma(3k+1)-1}}{\sigma(3k+1)} + \frac{(-1)^{\sigma(3k+2)-1}}{\sigma(3k+2)} + \frac{(-1)^{\sigma(3k+3)-1}}{\sigma(3k+3)}$ [lecture incertaine — indices]

$= \sum_{k=0}^{n-1} \frac{(-1)^{2k+2-1}}{2k+2} + \frac{(-1)^{4k+4-1}}{4k+2} + \frac{(-1)^{4k+4-1}}{4k+4}$ [lecture incertaine — exposants]

$= \sum_{k=0}^{n-1} \frac{1}{2k+2} - \frac{1}{2(2k+2)} - \frac{1}{4k+4}$ [lecture incertaine — décomposition]

$= \sum_{k=0}^{n-1} \frac{1}{2(2k+2)} - \frac{1}{2(2k+2)}$ [raturé — premier membre biffé] $\frac{1}{2(2k+2)} - \frac{1}{2(2k+2)}$ [lecture incertaine — simplification]

$= \text{[raturé — somme biffée]} \sum_{k=0}^{n-1} \frac{1}{...} $ [raturé — ligne biffée]

$= \frac{1}{2} \left( \sum_{k=0}^{n-1} \frac{(-1)^{2k+2-1}}{2k+2} + \frac{(-1)^{2k+2-1}}{2k+2} \right)$ [lecture incertaine — regroupement]

$= \frac{1}{2} \left( \sum_{k=1}^{2n} \frac{(-1)^{k-1}}{k} \right)$ [lecture incertaine — bornes]

d'où $S'_{3n} = \frac{1}{2} S_{2n}$. On s'attendrait à ce que $S'_{3n}$ crge [lecture incertaine — « crge »]

crge vers la m̂ limite que $S_n$ et donc que $\ln 2 = \frac{1}{2}\ln 2$

ce qui est Absurde !

## Page 17 (suite p. 15)

Suite thos : En plus en posant $S = \sum_{k \ge K_0}^{+\infty} U_k$ on a $\sum_{k \ge K_0}^{+\infty} U_{\sigma(k)} = S$

En effet. Cas où $U_k \ge 0 \, \forall k \in \mathbb{N}$ ($k \ge K_0$)

Soit $n \in \mathbb{N}$. Posons $S_n = \sum_{k=K_0}^n U_k$ et $S'_n = \sum_{k=K_0}^n U_{\sigma(k)}$

Considérons $\varphi : [\![K_0,+\infty[\![ \to \mathbb{N}$ [raturé — définition biffée d'une grande croix]

$m \mapsto \varphi(m) = \max\{\sigma(k)\}_{k=K_0}^n$ [lecture incertaine — variable]

$\varphi$ est une strict croissan [raturé — ligne biffée]

Posons $m_n = \max\{\sigma(k)\}_{k=K_0}^n \ge n$ [lecture incertaine — $m_n \ge n$]

et $m'_n = \max\{\sigma^{-1}(k)\}_{k=K_0}^n \ge n$ [lecture incertaine — $\sigma^{-1}$]

or $S_n \le \text{[raturé — membre biffé]} S'_{m'_n}$ car $(S_n)$ ? [lecture incertaine — inégalité]

Donc $S_n = \sum_{k=K_0}^n U_{\sigma(k)}$ [lecture incertaine — $S_n$ ou $S'_n$] $\le \sum_{k=K_0}^{m_n} U_k$ car $\forall k \in [\![K_0,n]\!]$, $U_{\sigma(k)} \in \{U_k\}_{k=K_0}^{m_n}$ [lecture incertaine — appartenance]

d'où $S'_n \le S_{m_n}$

d'où $S' \le S$ où $S' = \lim S'_n$ et $S = \lim S_n$ [raturé — « d'où $S' \le S$ où $S' = \lim S'_n$ » repris par surcharge]

d'où $\lim_{n \to +\infty} S'_n \le \lim_{n \to +\infty} S_{m_n}$ posons $S' = \lim S'_n$ [lecture incertaine — limites]

$S = \lim S_n$

d'où $S' \le S$ car lorsque $n \to +\infty$, $m_n \ge n \to +\infty$

De plus $S'_{m'_n} = \sum_{k=K_0}^{m'_n} U_{\sigma(k)} \ge \sum_{k=K_0}^n U_k$ [lecture incertaine — $m'_n$]

car $\forall k \in [\![K_0,n]\!]$, [raturé — « car que $\sigma^{-1}(k) \le m'_n$ alors » biffé] $k \le \sigma(m'_n)$ [lecture incertaine — majoration]

## Page 18 (suite p. 17)

en posant $k' = \sigma^{-1}(k) \le m'_n$, donc : $U_k = U_{\sigma(k')} \in \{U_{\sigma(l)}\}$ [lecture incertaine — appartenance]

$\text{[raturé — « } K_0 \le i \le m'_n \text{ » biffé]}$ dans $S'_{m'_n} \ge S_n$

càd $S' \ge S$ car lorsque $n \to +\infty$, $m'_n \ge n \to +\infty$

En conclusion $S = S'$

. Cas général

Soit $n \in \mathbb{N}$ ($n \ge K_0$)

$|S_{m_n} - S'_n| = \left|\sum_{k=K_0}^{m_n} U_k - \sum_{k=K_0}^n U_{\sigma(k)}\right|$ [lecture incertaine — $S_{m_n}$]

$= \left|\sum_{\substack{k=K_0 \\ k \notin \Sigma}}^{m_n} U_k\right|$ où $\Sigma = \{\sigma(k)\}_{k=K_0}^n$ [lecture incertaine — ensemble $\Sigma$]

$\le \sum_{\substack{k=K_0 \\ k \notin \Sigma}}^{m_n} |U_k|$ [raturé — symbole biffé devant la somme]

$\le \sum_{\substack{k=K_0 \\ ...}}^{...} |U_k| +$ [raturé — indices repris] $\sum_{\substack{k=K_0 \\ k \in \Sigma}}^{m_n} |U_k|$ [lecture incertaine — découpage]

$\le \sum_{k=K_0}^{m_n} |U_k| - \sum_{k=K_0}^n |U_{\sigma(k)}| \to 0$ d'après le cas précédent [lecture incertaine — différence des sommes partielles]

ainsi comme quand $n \to +\infty$, $m_n \to +\infty$ alors $S_{m_n} \to S$ d'où $\underline{S = S'}$ (résultat souligné)

## Page 19

* Produit de Cauchy = série produit

Soit $\sum_{i \ge i_0} a_i$, $\sum_{j \ge j_0} b_j$, 2 séries cplexes. On appelle (),

la série $\sum_{k \ge K_0} c_k$ où $K_0 = i_0 + j_0$ et $\forall k \in \mathbb{N}$ ($k \ge K_0$),

on a : $c_k = \sum_{i=i_0}^{k-j_0} a_i b_{k-i} = \sum_{\substack{i+j=k \\ i,j \ge i_0,j_0}} a_i b_j$ [lecture incertaine — bornes]

Thos : Si $\sum_{i \ge i_0} a_i$, $\sum_{j \ge j_0} b_j$ sont abs crgte alors la série produit $\sum_{k \ge i_0+j_0 = K_0} c_k$ est absolument crgte et

on a : $\sum_{k \ge K_0}^{+\infty} c_k = \left(\sum_{i \ge i_0}^{+\infty} a_i\right)\left(\sum_{j \ge j_0}^{+\infty} b_j\right)$

En effet Supp $\sum_{i \ge i_0} a_i$ et $\sum_{j \ge j_0} b_j$ = abs crgte

. Mqy $\sum_{k \ge K_0} c_k$ est abs crgte

Soit $n \in \mathbb{N}$ ($n \ge K_0$). Posons $A_n = \sum_{i=i_0}^n a_i$, $B_n = \sum_{j=j_0}^n b_j$,

$C_n = \sum_{k=K_0}^n c_k$, $A'_n = \sum_{i=i_0}^n |a_i|$, de m̂ pour $B'_n$ et $C'_n$

on a : $C'_n = \sum_{k=K_0}^n \left|\sum_{i=i_0}^{k-j_0} a_i b_{k-i}\right| \le \sum_{k=K_0}^n \sum_{i=i_0}^{k-j_0} |a_i||b_{k-i}|$ [lecture incertaine — majoration ; mention « car $|i_0| \le i \le k-j_0 \le n-j_0$ »]

$\le \sum_{i=i_0}^n |a_i| \sum_{...} |b_{k-i}|$ [lecture incertaine — factorisation ; raturé — indices repris]. Posons $j = k-i$

$\le \sum_{i=i_0}^{n-j_0} |a_i| \sum_{j=j_0}^{n-i} |b_j| \le \sum_{i=i_0}^n |a_i| \sum_{j=j_0}^n |b_j| = A'_n \times B'_n$ [lecture incertaine — bornes]

## Page 20 (suite p. 19)

Posons $A = \lim A_n$, $A' = \lim A'_n$. On définit de m̂ $B, B', C$ etc.

on a : $C'_n \le A'_n B'_n \le A' \times B'$ car $A'_n$ et $B'_n$ ? [lecture incertaine — fin de ligne]

Car $C'_n$ est ? et majorée alors elle crge CQFD [lecture incertaine — « croissante »]

(dans la suite on montrera m̂ que $C'_n \to A' \times B'$ [raturé — membre biffé]

dans un cadre plus général)

. Mqy $C = A \times B$

— Cas $\forall (i,j) \in [\![i_0,+\infty[\![ \times [\![j_0,+\infty[\![$, $a_i, b_j \ge 0$.

Vu que $\forall (i,j) \in [\![i_0,+\infty[\![ \times [\![j_0,+\infty[\![$, $|a_i|, |b_j| = a_i, b_j$ [lecture incertaine — égalité]

d'après ce qui précède, $C_n \le A_n \times B_n$ $\forall n \in \mathbb{N}$ ($n \ge K_0$) (1)

De plus $\forall n \in \mathbb{N}$ ($n \ge K_0$),

$C_{2n} = \sum_{k=K_0}^{2n} \sum_{i=i_0}^{k-j_0} a_i b_{k-i}$ [lecture incertaine — $C_{2n}$]

$= \sum_{i=i_0}^{2n-j_0} \sum_{k=i+j_0}^{2n} a_i b_{k-i}$ [lecture incertaine — permutation des sommes]

$= \sum_{i=i_0}^{2n-j_0} \sum_{j=j_0}^{2n-i} a_i b_j$ où $j = k-i$ [lecture incertaine — changement de variable]

$\ge \sum_{i=i_0}^n \sum_{j=j_0}^{2n-i} a_i b_j$ [raturé — « $\sum_{i=i_0}^n \sum_{j=j_0}^{2n-1}$ » repris] $+ \sum_{i=n+1}^{2n-j_0} \sum_{j=j_0}^{2n-i} a_i b_j$ [lecture incertaine — découpage ; mention diagonale « $\ge 0$ car $2n-i \ge n$ et $a_i b_j \ge 0$, $j \le ...$ »]

$\ge \sum_{i=i_0}^n \left( \sum_{j=j_0}^n a_i b_j + \sum_{j=n+1}^{2n-i} a_i b_j \right)$ [lecture incertaine — regroupement]

## Page 21 (suite p. 20)

or pour $i \in [\![i_0,n]\!]$, $2n-i \ge 2n-n \ge n$ et car $\forall i,j$, $a_i b_j \ge 0$

alors $\sum_{j=n+1}^{...} a_i b_j \ge 0$ [lecture incertaine — borne supérieure]

d'où $C_{2n} \ge \sum_{i=i_0}^n \sum_{j=j_0}^n a_i b_j = A_n \times B_n$ (2)

ainsi (1) $\Rightarrow C \le A \times B$ } $\Rightarrow \underline{C = A \times B}$ (résultat souligné)

et (2) $\Rightarrow C \ge A \times B$

— cas contraire

Soit $n \in \mathbb{N}$ ($n \ge K_0$).

[raturé — « $\sum_{i=i_0}^n \sqrt{...}$ » biffé]

on a : $|A_n B_n - C_n| = A_n B_n - C_n$ d'après (1) [lecture incertaine — valeur absolue]

$= \sum_{i=i_0}^n \sum_{j=j_0}^n a_i b_j - \sum_{k=K_0}^n \sum_{\substack{i \ge i_0 \\ j \ge j_0 \\ i+j=k}} a_i b_j$ [lecture incertaine — sommes]

$= \text{[raturé — « } \sum_{i=i_0}^n \text{ » biffé]} \sum_{\substack{i \ge i_0, j \ge j_0 \\ i+j \ge n+2}} a_i b_j$ [lecture incertaine — domaine de sommation]

$\le \sum_{\substack{i \ge i_0, j \ge j_0 \\ i+j \ge n+2}} |a_i||b_j|$

$\le |A'_n B'_n - C'_n| \longrightarrow 0$ d'après le cas précédent [lecture incertaine — majoration]

d'où $A_n B_n \longrightarrow C_n$ (Rq : Ne pas oublier que $A_n, B_n$ et $C_n$ sont abs crgte) [lecture incertaine — parenthèse]

## Page 22

( drexple : (Cas où $\sum_{i \ge i_0} a_i$, $\sum_{j \ge j_0} b_j$ sont semi-convergentes

, mais que la série produit $\sum_{k \ge i_0+j_0} c_k$ diverge)

( Posons $i_0 = j_0 = 1$ et $\forall i \ge 1$, $a_i = b_i = \frac{(-1)^i}{\sqrt{i}}$ [lecture incertaine — exposant]

D'après le critère de Leibniz sur les séries alternées,

$\sum_{i \ge 1} a_i$, $\sum_{i \ge 1} b_i$ sont semi-convergentes.

$\forall k \in \mathbb{N}$ ($k \ge 2$), on a : $|c_k| = \left|\sum_{i=1}^k \frac{(-1)^i}{\sqrt{i}} \times \frac{(-1)^{k-i}}{\sqrt{k-i}}\right|$ [tranché au r250+crop — le manuscrit porte bien $i=1..k$ ; *sic* — borne correcte $1..k-1$]

$= \sum_{i=1}^k \frac{1}{\sqrt{i(k-i)}}$ [lecture incertaine — valeur absolue sortie]

$\ge \sum_{i=1}^k \frac{1}{\sqrt{\frac{k}{2} \times \frac{k}{2}}}$ [lecture incertaine — majoration du dénominateur]

$\ge \sum_{i=1}^k \frac{2}{k}$

$\ge 2$ [lecture incertaine — somme télescopée ; manuscrit porte « $\ge 2$ »]

donc $c_k \not\to 0$ d'où $\sum_{k \ge 2} c_k$ diverge

[raturé — calcul $\frac{(-1)^k}{k}$ biffé en bas de page]

## Figures

Aucune figure en p12-22 : pages de texte manuscrit seul, sans schéma, sans capture, sans tableau. Aucun script `reproduce_mega_synthese_pXX.py` ni PNG généré pour cette plage — 0 PNG, motif : rien à reproduire.

## Vocabulaire

- crge : converge ; abs crgte / abs crge : absolument convergente ; semi-convergente : convergente mais pas absolument ; diverge / diryge : diverge.
- Mqy : montrons que ; Thos : théorème ; drexemple / dreemple : exemple [*sic* — graphie] ; CQFD : ce qu'il fallait démontrer ; càd : c'est-à-dire ; m̂ / de m̂ : de même ; or : or ; d'où / donc / ainsi / càd : articulations.
- $I_n$ : intégrale de Wallis $\int_0^{\pi/2}\sin^n t\,dt$ ; $K$ : constante de Stirling ($K=\sqrt{2\pi}$) ; $H_n=\sum_{k=1}^n 1/k$ ; $V_n$ : suite $H_n-\ln n$ ; $\gamma$ : constante d'Euler-Mascheroni $\simeq 0{,}577$.
- $\sigma$ : permutation (bijection) de $\mathbb{N}$ ; $S_n$, $S'_n$, $S_{3n}'$, $m_n$, $m'_n$, $\Sigma$ : sommes partielles et Césaro des réarrangements.
- $a_i$, $b_j$, $c_k$ : produit de Cauchy ; $A_n$, $B_n$, $C_n$ (sommes partielles) ; $A'_n$, $B'_n$, $C'_n$ (modules) ; cplexes : complexes [*sic*].
- [*sic*] garde les graphies d'origine : wallis, leibniz, Mqy, Thos, crge, $C=\sqrt{2\pi}$ souligné, $S=S'$ souligné, $C=A\times B$ souligné.
