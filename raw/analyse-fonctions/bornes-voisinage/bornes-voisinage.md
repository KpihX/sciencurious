# Bornes et voisinage (fonction continue sur $[a, b]$, notion de limite) — transcription fidèle

> 🧾 **Manuscrit original :** `bornes-voisinage.pdf` (scan, 5 pages, encre bleue sur papier quadrillé) · ✍️ KpihX
> 🔍 **Statut :** partiellement lisible (~65 %), transcrit fidèlement. Page 1 : fonction continue sur $[a, b]$ bornée (par l'absurde, Bolzano-Weierstrass). Page 2 : problème de la notion de limite en $0{,}5$ sur $\mathbb{R} \setminus \{0, 1\}$ (page très raturée ; fragments imprimés d'une page de livre adjacente visibles au bord gauche, non transcrits). Pages 3–4 : scans identiques (doublon) — limite finie $\implies$ bornée au voisinage, limite infinie $\implies$ non bornée. Page 5 : critère de convergence pour l'intégrale de Riemann (fonction définie au sens de Riemann $\implies$ bornée).
> 📄 **Source scannée :** [`bornes-voisinage.pdf`](bornes-voisinage.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — $f$ continue sur $[a, b] \implies f$ bornée sur $[a, b]$

Thm : $f$ continue sur $[a, b] \implies f$ bornée sur $[a, b]$

$\implies /$ Supposons par l'absurde $f$ non bornée.

Soit $M_0$. $\exists x_0 \in [a, b] / |f(x_0)| > M_0$

Soit $M_1 = \text{Max}(M_0+1, |f(x_0)|)$

$\exists x_1 \in [a, b] / |f(x_1)| > M_1$

on construit deux suites $(x_n)_N$ et $(|f(x_n)|)_N$ vérifiant

Pour $x_{n-1}$ donné $x_n$ est $(W_1)$ [lecture incertaine — l'étiquette entre parenthèses est empâtée] un réel tel que $|f(x_n)| > M_n$ où $M_n = \text{Max}(M_{n-1}+1, |f(x_{n-1})|)$

$(M_n)$ étant bornée on peut en extraire une sous suite $(x_{\varphi(n)})$ convergente [*sic* — lire « $(x_n)$ » au lieu de « $(M_n)$ », $(M_n)$ étant non bornée par construction]. Car $\lim |f(x_n)| = +\infty$ alors $\lim |f(x_{\varphi(n)})| = +\infty$

$f$ continue en $x = \lim_{n \to +\infty} x_{\varphi(n)}$

car $x \in [a, b]$ alors $f(\lim_{n \to +\infty} x_{\varphi(n)}) = +\infty$

c-à-d $|f(x)| \to +\infty$ A ! [*sic* — « A ! » : lire « Absurde » / contradiction]

---

## Page 2 — Problème de la notion de limite

[En marge gauche : fragments imprimés d'une page de livre adjacente partiellement visible (« …ES (OU GENERALIS… », « …I - Préliminaires : Fonct… », « …est dite bornée au vois… », « …$t f : A \to IR$ (ou… ») — page tronquée, non transcrite.]

Pb notion de limite

Considérons $f : IR \setminus \{0, 1\} \to IR$, $x \mapsto$ [raturé — la formule de $f$ est illisible] pour $x \ne 0$

$\lim_{x \to 0,5} f(x) = a \quad \forall a \in IR$

car $\forall \varepsilon > 0$, [raturé : « en prenant $n = a/\varepsilon$ »] on a bien $\forall x \in IR \setminus \{0, 1\}$, $|x - 0{,}5| < \varepsilon \iff |f(x) - a| < \varepsilon$ [lecture incertaine — toute la ligne est empâtée]

du fait que $Q$ est fausse et donc $P$ est vraie [lecture incertaine — la justification est empâtée]

le pb (celui qui nous plongeons [lecture incertaine — verbe empâté] en $0{,}5$) vient du fait que la defn ne s'assure pas de la définir [=*définir $f$*] au voisinage de $0{,}5$

Il serait mieux de dire [raturé — une ligne entièrement biffée : « pour $A \subset IR$, $x_0 \in \bar{A}$ et $l \in IR$, $\lim$ … »] pour $A \subset IR$ ◦ [lecture incertaine — la fin est empâtée]

le cul [lecture incertaine — mot empâté, lire probablement « le cœur » ?] de la notion de limite au voisinage de $x_0$ n'a de sens que ssi $x_0 \in \bar{A}$ en considérant $f : \bar{A} \to IR$ (ou $C$) $A \subset$ [phrase inachevée — la fin est rognée par la marge]

---

## Page 3 — Limite finie $\implies$ bornée au voisinage ; limite infinie $\implies$ non bornée

Soit $A \subset IR, x_0 \in \bar{A}$ $f : A \to IR$ (ou $C$) $\lim_{\substack{x \to x_0 \\ x \in A}} |f(x)| = l_0$

[Colonne droite : Puisque $\forall x \in$ [?] $, |x - x_0|, |x' - x_0| \le r$ [lecture incertaine] d'où $|f(x_0)| > M$ [lecture incertaine] De même on a $\forall |x - x_0| \le r$ car $x_0 \le r$ prendre $x_0 = x_1$ [lecture incertaine — toute la colonne est empâtée]]

Thm : si $l_0 \in IR$, alors $f$ bornée au voisinage de $x_0$ dans $A$

Prenons $M = |l| + 1 > 0$. Cherchons $r > 0 / \forall x \in A, |x - x_0| < r \implies |f(x)| < M$

car $\lim_{x \to x_0} |f(x)| = l$ et $M - l_0 - 1 > 0$ [=*?* — l'inégalité est empâtée]

donc $\exists \eta_0 > 0 / \forall x \in A, |x - x_0| < \eta_0 \implies ||f(x)| - l_0| < M - l_0 \implies ||f(x)| - l_0| \le M - l_0 \implies |f(x)| \le M$

Prendre $r = \eta$

Thm : si $l_0 = +\infty$, alors $f$ non bornée au voisinage de $x_0$ dans $A$

Soient [raturé — un mot illisible] $r > 0$ et $M \in IR^+$. Cherchons $x \in A / |x - x_0| < r$ et $|f(x)| > M$

[raturé : « $X$ … $x_0 \in \bar{A}$, pour $x = $ … » — une ligne entièrement biffée]

Car $\lim_{x \to x_0} |f(x)| = +\infty$ et que $M > 0, \exists \eta > 0 / \forall x \in A, |x - x_0| \le \eta \implies |f(x)| > M$

Vu que $x_0 \in \bar{A}$, pour $r_1 = \min(\eta, r)$, $\exists x_1 \in A \cap ]x_0 - r_1, x_0 + r_1[$.

---

## Page 4 — Doublon du scan de la page 3

[Le scan de la page 4 du PDF est identique à celui de la page 3 (même contenu, même cadrage, doublon dans le PDF) : « Soit $A \subset IR, x_0 \in \bar{A}$ … $\exists x_1 \in A \cap ]x_0 - r_1, x_0 + r_1[$. » — voir la transcription complète à la Page 3 ci-dessus, rien de nouveau à transcrire.]

---

## Page 5 — Critère de convergence pour l'intégrale de Riemann

Critère de [raturé — « (?) »] convergence [lecture incertaine — l'en-tête est raturé et empâté]

[En haut à gauche : « $(?)^2$ » — gribouillis illisible. En marge gauche : fragment imprimé adjacent (« …lles », « …C », « …larsen 1 », « …$-2x$… ») — page tronquée, non transcrite.]

Soit $I = \int_a^b f$ une intégrale définie au sens de Riemann

Considérons $I_x = \lim_{x \to a}$ [lecture incertaine — la variable de la limite est empâtée] $F_1(x)$ où $F_1 : ]a, b] \to IR$, $x \mapsto \int_x^b f$

et définissons aussi $F_2 : [a, b[ \to IR$, $x \mapsto \int_a^x f$ et $I_x = \lim_{x \to b^-} F_2(x)$

• Mtq [=*Montrons que*] $I = I_2$

[?] $\forall x \in ]a, b]$ $I - F_1(x) = \int_a^b f dx + \int_b^x f dx = \int_a^x f dx$

Ainsi $|I - F_1(x)| = |\int_a^x f dx| \le \int_a^x |f| dx$ [car $x > a$ — en marge droite]

$\implies f$ déf au sens de Riemann $\implies f$ borné sur $[a, b]$ avec $\exists M \in IR^+ / \forall x \in [a, b]$ $|f(x)| \le M$

Alors $|I - F_1(x)| \le (x - a)M$

or $\lim_{x \to a} (x - a)M = 0$ ainsi $I = I_2$ [?] Il en est de même pour $I_1$ [colonne droite]

---

## Figures

- Aucune figure pp. 1–5 vérifiées sur rendus `/tmp/faf1/r150/` (texte seul ; p. 4 = doublon du scan p. 3) — fragments imprimés adjacents (p. 2, p. 5) volontairement non transcrits, non comptés comme figures.

## Vocabulaire

bornée, voisinage, $[a,b]$, Bolzano-Weierstrass, limite finie/infinie, $x_0 \in \bar{A}$, intégrale de Riemann, $Mtq$ (= Montrons que), $A!$ (= Absurde).
