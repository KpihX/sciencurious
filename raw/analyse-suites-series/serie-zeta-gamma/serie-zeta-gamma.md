# Série Zêta-Gamma — transcription fidèle

> 🧾 **Manuscrit original :** `serie-zeta-gamma.pdf` (scan, 6 pages) · ✍️ KpihX · restaurée Datas1 2026-09-07
> 🔍 **Statut :** lisible (~90 %), transcrit fidèlement. Encre légère par endroits (p. 4), ratures et notes marginales conservées.

📄 **Source scannée :** [`serie-zeta-gamma.pdf`](serie-zeta-gamma.pdf)

---

## Page 1 — Relation $\zeta(u)\Gamma(u)$, nature de l'intégrale

[En tête, souligné : $\forall u \in ]1,+\infty[,\ \zeta(u)\,\Gamma(u) = \int_0^{+\infty} \dfrac{x^{u-1}}{e^x-1}\,dx$.]

En effet. Posons $I(u) = \int_0^{+\infty} \dfrac{x^{u-1}}{e^x-1}\,dx$ $\forall u \in \mathbb{R}$ [lecture incertaine — ensemble raturé].

✳ Nature de $I(u)$ $\forall u \in \mathbb{R}$.

• $I \equiv$ I.I en $+\infty$ (et en $0$ ssi $u < 2$ [lecture incertaine — « $<$ » ou « $\leqslant$ » ?]).

• $\forall u \in \mathbb{R}$, $\lim_{x \to +\infty} x^2\,\dfrac{x^{u-1}}{e^x-1} = \lim_{x \to +\infty} x^{u+1} e^{-x} \times \dfrac{e^x}{e^x-1} = 0$, d'où $\int_1^{+\infty} \dfrac{x^{u-1}}{e^x-1}\,dx \in \mathbb{R}$.

• $\forall u \in \mathbb{R}$, $\dfrac{x^{u-1}}{e^x-1} \underset{0^+}{\sim} \dfrac{1}{x^{2-u}}$ d'où comme $\forall x \in \mathbb{R}_+^*$, $\dfrac{x^{u-1}}{e^x-1} > 0$, alors $\int_0^1 \dfrac{x^{u-1}}{e^x-1}\,dx \in \mathbb{R}$ ssi $2-u < 1 \iff u > 1$.

D'où $D_I = ]1,+\infty[$.

✳ Valeur de $I(u)$ $\forall u \in ]1,+\infty[$. Soit $u \in ]1,+\infty[$.

$$I(u) = \int_0^{+\infty} \frac{e^{-x} x^{u-1}}{1-e^{-x}}\,dx = \int_0^{+\infty} \sum_{k=0}^{+\infty} e^{-x} x^{u-1} \times e^{-kx}\,dx = \int_0^{+\infty} \sum_{k \geqslant 0} e^{-x(k+1)} x^{u-1}\,dx.$$

• Étudions $\sum_{k \geqslant 0} f_k$ où $\forall k \in \mathbb{N}$, $\forall x \in \mathbb{R}_+^*$, $f_k(x) = x^{u-1} e^{-x(k+1)}$.

— $\forall k \in \mathbb{N}$, $f_k$ est continue sur $\mathbb{R}_+^*$.

---

## Page 2 — Convergence uniforme sur $[a,b]$

— Mtq $\sum_{k \geqslant 0} f_k$ CVU sur tout $[a,b] \subset \mathbb{R}_+^*$. Soit $[a,b] \subset \mathbb{R}_+^*$. Soit $n \in \mathbb{N}$.

$\forall x \in [a,b]$, $R_n(x) = \sum_{k \geqslant n+1} x^{u-1} e^{-x(k+1)}$

$$= \frac{x^{u-1} e^{-x} \times e^{-x(n+1)}}{1-e^{-x}} = \frac{x^{u-1}}{e^x-1}\,e^{-x(n+2)}.$$

[*sic* — exposant : $e^{-x(n+1)}$ attendu après $1/(1-e^{-x}) = e^x/(e^x-1)$ ; majorant aval cohérent avec l'exposant transcrit, conclusion CU inchangée]

— Trouvons $\sup_{[a,b]} |R_n(x)|$. Étudions $g(x) = \dfrac{x^{u-1}}{e^x-1}$ $\forall x \in [a,b]$.

$\forall x \in [a,b]$, $g'(x) = \dfrac{(u-1)x^{u-2}(e^x-1) - e^x x^{u-1}}{(e^x-1)^2}$

$$= \frac{e^x x^{u-2}(u-1-x) \ldots}{(e^x-1)^2} \to \frac{(u-1)x^{u-2}}{\ldots} \quad \text{[lecture incertaine — ligne de simplification]}.$$

[raturé — tout le calcul de $g'(x)$ biffé d'un grand trait diagonal sur la source]

d'où $|R_n(x)| \leqslant \dfrac{b^{u-1}\,e^{-a(n+2)}}{e^a-1}$ [lecture incertaine — numérateur],

d'où $\sup_{[a,b]} |R_n(x)| \leqslant \dfrac{b^{u-1}\,e^{-a(n+2)}}{e^a-1} \underset{n \to +\infty}{\longrightarrow} 0$, d'où la CU.

Par conséquent $I(u) = \sum \int\ldots = \int \sum\ldots$

---

## Page 3 — Lemme $J_{u,k}$ et conclusion

Ainsi $I(u) = \sum_{k \geqslant 0} \int_0^{+\infty} e^{-x(k+1)} x^{u-1}\,dx = \sum_{k \geqslant 1} \int_0^{+\infty} e^{-xk} x^{u-1}\,dx$.

Lemme : $\forall k \in \mathbb{N}^*$, $\forall u > 1$, $J_{u,k} = \int_0^{+\infty} e^{-xk} x^{u-1}\,dx = \dfrac{\Gamma(u)}{k^u}$. Soit $k \in \mathbb{N}^*$ et $u \in ]1,+\infty[$. • Pour $u \in \mathbb{N}^*$.

Ona : $J_{u,k} = -\dfrac{1}{k}\left(\left[e^{-xk} x^{u-1}\right]_0^{+\infty} - \int_0^{+\infty} e^{-xk}(u-1)x^{u-2}\,dx\right)$, $J_u = \dfrac{u-1}{k}\,J_{u-1}$ [pour $u \geqslant 2$].

• $J_1 = \int_0^{+\infty} e^{-xk} x^{1-1}\,dx = \dfrac{1}{k} = \Gamma(1) \times \dfrac{1}{k}$.

• Si pour $u \in \mathbb{N}^*$ [raturé — mot barré], $J_{u-1} = \dfrac{\Gamma(u-1)}{k^{u-1}}$ [lecture incertaine — exposant du dénominateur], alors $J_u = \dfrac{u-1}{k} \times \dfrac{\Gamma(u-1)}{k^{u-1}} = \dfrac{\Gamma(u)}{k^u}$.

• Pour le cas général, $u \in ]1,+\infty[$, $J_u =_{t = xk} \int_0^{+\infty} e^{-t}\left(\dfrac{t}{k}\right)^{u-1}\dfrac{dt}{k} = \dfrac{1}{k^u}\int_0^{+\infty} e^{-t} t^{u-1}\,dt = \dfrac{\Gamma(u)}{k^u}$.

D'où $I(u) = \sum_{k=1}^{+\infty} \dfrac{\Gamma(u)}{k^u} = \Gamma(u)\,\zeta(u)$.

[encadré : Cl : $\forall u \in ]1,+\infty[,\ \Gamma(u)\,\zeta(u) = \int_0^{+\infty} \dfrac{x^{u-1}}{e^x-1}\,dx$.]

---

## Page 4 — Intégrale $I_n = \int_0^{+\infty} x^n e^{-x^{2n+2}}\,dx$

$$I_n = \int_0^{+\infty} x^n e^{-x^{2n+2}}\,dx = ? \quad \forall n \in \mathbb{N}.$$

$\forall n \in \mathbb{N}$,

$$I_n =_{t = x^{2n+2}} \int_0^{+\infty} t^{\frac{n}{2n+2}} \times e^{-t} \times \frac{dt}{2n+2} \times t^{-\frac{2n+1}{2n+2}}\,dt$$
$$= \frac{1}{2n+2}\int_0^{+\infty} e^{-t} \times t^{\frac{-n-1}{2n+2}}\,dt$$
$$= \frac{1}{2n+2}\int_0^{+\infty} e^{-t} \times t^{-1/2}\,dt$$
$$= \frac{1}{2n+2}\,\Gamma(1/2).$$

[souligné : $I_n = \dfrac{\sqrt{\pi}}{2n+2}$.] Ce résultat reste valable $\forall n \in \mathbb{R}_+^*$ [raturé — la fin de la ligne est raturée].

---

## Page 5 — Intégrale $I = \int_0^{+\infty} \dfrac{x}{e^x-1}\,dx$ (mise en série)

$$I = \int_0^{+\infty} \frac{x}{e^x-1}\,dx = ?$$
$$= \int_0^{+\infty} \frac{x\,e^{-x}}{1-e^{-x}}\,dx = \int_0^{+\infty} x\,e^{-x} \sum_{k \geqslant 0} e^{-xk}\,dx = \int_0^{+\infty} \sum_{k \geqslant 0} x\,e^{-x(k+1)}\,dx.$$

$$I = \sum_{k \geqslant 0} \int_0^{+\infty} x\,e^{-x(k+1)}\,dx.$$

En effet considérons la série de fcts $\sum_{k \geqslant 0} f_k(x)$ où $\forall k \in \mathbb{N}$, $\forall x \in \mathbb{R}_+^*$, $f_k(x) = x\,e^{-x(k+1)}$. Ona : $\sum_{k=0}^{+\infty} f_k(x) = \dfrac{x}{e^x-1} \in \mathbb{R}$ $\forall x \in \mathbb{R}_+^*$, donc $\sum_{k \geqslant 0} f_k(x) \xrightarrow[\mathbb{R}_+^*]{\text{CVS}} f(x) = \dfrac{x}{e^x-1}$.

De plus $\forall n \in \mathbb{N}$, $\forall x \in \mathbb{R}_+^*$, $|R_n(x)| = \sum_{k \geqslant n+1} x\,e^{-x(k+1)} = \dfrac{x\,e^{-x(n+2)}}{e^x-1}$ [*sic* — même exposant que p. 2 : $e^{-x(n+1)}$ attendu après simplification, majorant aval cohérent, CU inchangée].

• Mtq $\sum_{k \geqslant 0} f_k(x) \xrightarrow[[a,b]]{\text{CU}} f$ $\forall [a,b] \subset \mathbb{R}_+^*$. Soit $[a,b] \subset \mathbb{R}_+^*$. Trouvons pour $n \in \mathbb{N}$, $\sup_{[a,b]} |R_n(x)|$.

— Étudions $g(x) = \dfrac{x}{e^x-1}$ $\forall x \in [a,b]$. $\forall x \in [a,b]$, $g'(x) = \dfrac{e^x-1-e^x x}{(e^x-1)^2} = \dfrac{e^x(1-x)-1}{(e^x-1)^2}$ [lecture incertaine — signe dans la seconde forme].

— Étudions $h(x) = e^x(1-x)-1$ [lecture incertaine — signe], $\forall x \in \mathbb{R}_+$.

---

## Page 6 — Convergence uniforme et $I = \pi^2/6$

$\forall x \in \mathbb{R}_+$, $h'(x) = -x\,e^x < 0$ car $x > 0$, d'où $\forall x \in [a,b]$, $h(x) < h(a) = 0$ car $a > 0$ [*sic* — $h(a) < 0$ pour $a > 0$, c'est $h(0) = 0$], d'où $g'(x) < 0 \implies g(x) \leqslant g(a) = \dfrac{a}{e^a-1}$, et comme $e^{-x(n+2)} \leqslant e^{-a(n+2)}$, alors $\sup_{[a,b]} |R_n(x)| \leqslant \dfrac{a\,e^{-a(n+2)}}{e^a-1} \underset{n \to +\infty}{\longrightarrow} 0$, d'où $\sum_{k \geqslant 0} f_k \xrightarrow[[a,b] \subset \mathbb{R}_+^*]{\text{CU}} f$.

• Comme $\mathbb{R}_+^*$ est d'intérieur [lecture incertaine] : $]a,b[ \subset \ldots \neq \varnothing$ et que $f_n$ est continue sur $\mathbb{R}_+^*$ $\forall k \in \mathbb{N}$, alors on a bien $I = \sum \int\ldots = \int \sum\ldots$

d'où $I = \sum_{k \geqslant 0} -\dfrac{1}{k+2}\left(\left[x\,e^{-x(k+2)}\right]_0^{+\infty} - \int_0^{+\infty} e^{-x(k+2)}\,dx\right)$

$$= \sum_{k \geqslant 0} +\frac{1}{k+2} \times -\frac{1}{k+2}\,\left[e^{-x(k+2)}\right]_0^{+\infty} = \sum_{k \geqslant 1} \frac{1}{k^2}.$$

d'où [souligné : $I = \dfrac{\pi^2}{6} \iff \int_0^{+\infty} \dfrac{x}{e^x-1}\,dx = \dfrac{\pi^2}{6}$].

---

## 📝 Notes de transcription (fidélité)

- p. 1 : l'ensemble de $u$ dans « Posons $I(u) = \ldots$ » est raturé ; la parenthèse « (et en 0 ssi $u < 2$) » est de lecture incertaine.
- p. 2 : la ligne de simplification de $g'(x)$ et le numérateur du majorant sont de lecture incertaine ; la conclusion CU est en revanche nette.
- p. 3 : mot barré dans l'hérédité (« Si pour $u \in \mathbb{N}^*$… ») ; exposant du dénominateur de $J_{u-1}$ incertain (transcrit $k^{u-1}$, cohérent avec la conclusion).
- p. 4 : encre légère ; fin de la dernière ligne raturée (« Ce résultat reste valable $\forall n \in \mathbb{R}_+^*$… »).
- p. 5–6 : signe de $h(x) = e^x(1-x)-1$ confirmé a posteriori par $h'(x) = -xe^x$ (p. 6) ; la justification « intérieur non vide » de l'échange $\sum\int = \int\sum$ est de lecture incertaine.
- Aucune figure à reproduire (formules manuscrites uniquement).

## Figures

Aucune figure géométrique ni graphe : 6 pages de calculs manuscrits seuls (transcription § Notes ; confirmé p. 1 sur source le 2026-09-07 — relation $\zeta(u)\Gamma(u)$ — rendu `/tmp/qas/` ; p. 2–6 relues le 2026-09-07 — rendu `/tmp/s11/`, 0 figure à reproduire). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- CU : convergence uniforme ; DI : domaine d'intégrabilité ($]1,+\infty[$) ; $I(u)$ : intégrale auxiliaire.
- $\zeta(u)\Gamma(u)$ ; $J_{u,k}$ : lemme d'intégration ; $f_k$ : termes de la série de fonctions.
- $I_n = \int_0^{+\infty} x^n e^{-x^{2n+2}}dx$ ; $I = \int_0^{+\infty} x/(e^x-1)dx = \pi^2/6$ (souligné).
