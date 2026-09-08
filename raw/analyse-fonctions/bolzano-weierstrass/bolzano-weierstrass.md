# Bolzano-Weierstrass dans ℝ — transcription fidèle

> 🧾 **Manuscrit original :** `bolzano-weierstrass.pdf` (scan, 5 pages, encre bleue sur papier blanc) · ✍️ KpihX
> 🔍 **Statut :** lisible (~80 %), transcrit fidèlement. Page 1 : 1ère formulation (sous-ensemble infini borné de ℝ) et début de la construction de $(M_n)$. Page 2 : fin de la construction, cas fini/infini, exemples et remarque Sup/Inf. Pages 3–5 : 2e formulation (suite réelle bornée), lemme du point d'accumulation privé d'un point, extraction de la sous-suite convergente, cas des suites finies et caractérisation séquentielle du point d'accumulation.
> 📄 **Source scannée :** [`bolzano-weierstrass.pdf`](bolzano-weierstrass.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — 1ère formulation et construction de $(M_n)$

Thor [lecture incertaine — « Thor » : abréviation de « Théorème » ?] de Bolzano-Weierstrass dans IR :

1ère Formulation (1P1) : Tout sous-ens infini borné de IR admet au moins un pt d'accumulation

En effet soit $E$ un tel sous ens.

Construisons la suite $(M_n)_N$ de IR de la façon suivante

① Car $E$ est borné, [et non vide — inséré au-dessus de la ligne] $E$ admet une borne inf. on fixe $M_0 = \inf E$. Si $M_0$ est un pt d'accumulation de $E$, on arrête la construction ; sinon, $\exists \varepsilon_0 > 0 / \forall x \in E \setminus \{M_0\}, x > M_0 + \varepsilon_0$ [lecture incertaine — le membre « $x > M_0 + \varepsilon_0$ » est empâté]

Rq : dans ce cas on a nécessairement $x_0 \in E$ [lecture incertaine — on lit aussi bien « $M_0 \in E$ »].

on [raturé : « fixe »] par la suite $E_0 = E \setminus \{M_0\} = E \cap [M_0 + \varepsilon_0, +\infty[ \ne \emptyset$ car $E$ est infini, et on poursuit la construction en ②

② Soit $n \in IN^*$. Pour $M_{n-1}$ déjà construit / $M_{n-1}$ n'est pas un pt d'accumulation de $E$, car $E_{n-1} = E \cap [M_{n-1} + \varepsilon_{n-1}, +\infty[ = E \setminus \{M_k, k \in [\![0, n-1]\!]\}$ [lecture incertaine — l'égalité ensembliste est empâtée] est non vide et borné (car $E_{n-1} \subset E$), $E_{n-1}$ admet [raturé : « un pt d'accumu »] une borne inf. on fixe $M_n = \inf E_{n-1}$. Si $M_n$ est un pt d'accumulation de $E$, on arrête la construction ; sinon, $\exists \varepsilon_n > 0 / \forall x \in E_{n-1} \setminus \{M_n\}, x > M_n + \varepsilon_n$ (dans ce cas on a nécessairement $M_n \in E$).

on pose $E_n = E_{n-1} \setminus \{M_n\} = E \setminus \{M_k, k \in [\![0, n]\!]\} = E \cap [M_n + \varepsilon_n, +\infty[$ et on poursuit la construction en ②

---

## Page 2 — Suite finie ou infinie, exemples, remarque Sup/Inf

Rq : la construction aboutit soit à une suite finie soit à une suite infinie

. $(M_n)$ est strict croissante $(P^*)$ [lecture incertaine — l'étiquette « $(P^*)$ » est empâtée]

\* Si [raturé — quelques mots illisibles] $(M_n)$ est finie, c-à-d $\exists N \in IN / (M_{n1} = (M_n)_{0, N}$ [lecture incertaine — la notation de la suite finie est empâtée], alors $M_N$ est un pt d'accumulation de $E$ d'où le résultat

\* Sinon, $(M_n) = (M_n)_N$ est une suite infinie, [$P^*$ — exposant ajouté/raturé] et majorée par $\Sup E$ (car $E$ étant borné, $E$ admet une borne sup, et de surcroît, $\forall n \in IN, M_n \in E$).

Ainsi $(M_n) \longrightarrow \Sup\{M_n, n \in IN\}$ et par ce fait $\Sup\{M_n\}$ est un pt d'accumulation de $E$ car limite d'une suite strict monotone d'elts de $E$, d'où le résultat

Ex : $]2, 3[$ [lecture incertaine — le « $3$ » de droite est empâté ; rendu p. 2 lu « $]2,3[$ », l'ancienne lecture « $], 2[$ » est écartée] admet $2$ comme pt d'accumulation ; dans ce cas $(M_n) = ?$ $M_0 = 2$ ? [lecture incertaine — la suite extraite est illisible]

. $\{ \frac{(-1)^n}{n}, n \in IN^* \}$ [reconstruction — motif : rendu p. 2 lisible « $(-1)^n/n$ », l'ancienne lecture « $60^n$ » venait du « $(-1)$ » empâté] admet $0$ comme pt d'accumulation ; dans ce cas $(M_n) = \{ M_n = \frac{(-1)^{2n+1}}{2n+2}, n \in IN \} \longrightarrow 0$ [lecture incertaine — l'exposant $2n+1$ est empâté mais cohérent avec $(-1)^n/n$]

NB : Pour $E \subset IR$, $\Sup E, \Inf E \equiv$ pt adhérent de $E$. Ils sont pts d'accumulation de $E$ ssi $\exists (M_n) \subset E \longrightarrow \Sup E$ ($\Inf E$) avec $\forall N \in IN / \exists n \in IN, n > N$ et $M_n \ne \Sup E$ ($\Inf E$)

Rq : Il suffit de chercher $(M_n)$ [raturé — « ? (resp ?) »] pour $\Sup E$ (resp $\Inf E$)

---

## Page 3 — 2e formulation et lemme

$2^e$ Formulation $(2P)$ : De toute suite réelle bornée, [infinie — ajouté en marge à droite] on peut extraire une sous suite crgte [=*convergente*].

On va en fait mtq [=*montrer que*] $(1P1) \iff (2P)$

$\implies /$ Soit une telle suite $(S_n)_{IN}$.

D'après $(1P1)$, $\{S_n, n \in IN\}$ admet au moins un pt d'accumulation. Soit $x$ l'un d'eux.

Lemme : Soit $A \subset IR$, $a \equiv$ pt d'accumulation de $A$. Soit $a' \in A$. $a \equiv$ pt d'accumulation de $A \setminus \{a'\}$.

Supp par l'absurde que l'on n'ait pas cette dernière assertion. donc $\exists \varepsilon > 0 / A \cap (]a-\varepsilon, a+\varepsilon[ \setminus \{a\}) = \emptyset$. Si $A' = A \setminus \{a'\}$ car $a \equiv$ pt d'accumulation de $A$, on a nécessairement $a' \in A \cap (]a-\varepsilon, a+\varepsilon[ \setminus \{a\})$.

• Si $a' = a$, cela est impossible, ce qui conduit à une absurdité

• Sinon, en posant $\varepsilon' = |a' - a|$, d'après ce qui précède, $A \cap (]a-\varepsilon', a+\varepsilon'[ \setminus \{a\}) = \emptyset$ ce qui est encore absurde d'où le résultat

Rq : le résultat reste vrai si on remplace la notion d'accumulation par celle d'adhérence, mais à condition que $a' \ne a$.

---

## Page 4 — Extraction de la sous-suite convergente

D'après ce lemme $x \equiv$ pt d'accumulation de $\{x_n, n \in IN / n > N\}, \forall N \in IN$.

Considérons l'application $\varphi : IN \to IN$ définie comme suit, $n \mapsto \varphi(n)$

① car $x \equiv$ pt d'accum de $\{x_n, n \in IN\}, \exists n \in IN / x_n \in ]x-1, x+1[ \setminus \{x\}$. on fixe alors $\varphi(0) = n$ et on poursuit la construction de $\varphi(n), n \in IN^*$ en ②

② pour $n \in IN^* / \varphi(n-1)$ ait déjà été construit, car $x \equiv$ pt d'accumulation de $\{x_{n'}, n' \in IN / n' > \varphi(n-1)\}$, $\exists n' \in IN / x_{n'} \in ]x-1/n, x+1/n[$. on fixe alors $\varphi(n) = n'$ ($n \mapsto \varphi(n-1)$) (Rq : $\varphi(n) = n' > \varphi(n-1)$.) et on poursuit la construction en ②

Au bout de ce processus il est clair que $\varphi$ est [raturé — un mot illisible] bien définie et [$\nearrow^*$ — exposant raturé] et que $\forall n \in IN^*, |x - x_{\varphi(n)}| < 1/n$ alors $x_{\varphi(n)} \longrightarrow x$ ; d'où le résultat

$\impliedby /$ Soit $E$, un ens infini borné de IR. Car $E$ infini, d'après l'axiome du choix, on peut construire une suite d'elts deux à deux distincts de $E$. construisons en une $(S_n)_{IN}$. $\exists$ une sous suite $(x_{\varphi(n)}) \longrightarrow x$. (car $(S_n)$ est infinie) Car $\forall n, m \in IN$, $x_n \ne x_m$, on a aussi $x_{\varphi(n)} \ne x_{\varphi(m)}$ et par conséquent $\forall N \in IN$ [raturé : « $m, n > N \implies$ »] $x_{\varphi(n)} \ne x$, d'où $x \equiv$ pt d'accum de $E$ [lecture incertaine — la fin de la phrase est empâtée]

---

## Page 5 — Suites finies et caractérisation séquentielle

Rq : $(2P)$ reste valable si on tient aussi en compte les suites finies. Dans ce cas on pourra en extraire une sous suite stationnaire et donc convergente.

En effet soit $(S_n)_N$, une telle suite. $\{S_n, n \in IN\} = \{a_1, \dots, a_m\}$ $\exists k \in [\![1, m]\!] / A_k = \{n \in IN / x_n = a_k\}$ soit infini car $IN = \bigcup_{k=1}^{m} A_k$ est infini [lecture incertaine — le signe entre « $IN$ » et « $\bigcup A_k$ » est raturé]

Considérons $\varphi : IN \longrightarrow IN$, $n \mapsto \varphi(n) = \min \{A_k \setminus \{\varphi(i)\}_{i=0}^{n-1}\}$ [lecture incertaine — la fin de la définition est empâtée] et $\varphi(0) = \min A_k$ [lecture incertaine — le début de la ligne est empâté]

Il est clair que $\varphi$ est $\nearrow^*$ ainsi $(x_{\varphi(n)})$ est une sous suite de $(x_n)$.

De plus $\forall n \in IN$, car $\varphi(n) \in A_k$, $x_{\varphi(n)} = a_k$ et ainsi $(x_{\varphi(n)})$ est stationnaire et donc crgte. $x_{\varphi(n)}$ est une des sous suites cherchées.

• Soit $(x_n)$, une suite réelle. / $(x_n) \longrightarrow x \iff x \equiv$ pt d'accum de $\{x_n, n \in IN\}$ [? — un connecteur raturé] $(\exists N \in IN / \forall n, m \in IN, n, m > N \implies x_n \ne x_m) \iff (\exists N \in IN / \forall n \in IN, n > N \implies x_n \ne x) \iff \forall N \in IN, \exists n \in IN / n \ge N$ et $x_n \ne x \iff \forall N \in IN, \exists n, m \in IN / n, m > N$ et $x_n \ne x_m$ [lecture incertaine — les trois dernières équivalences sont empâtées]

---

## Figures

- Aucune figure pp. 1–5 vérifiées sur rendus `/tmp/faf1/r150/` (texte seul, sans schéma).

## Vocabulaire

Bolzano-Weierstrass, pt d'accumulation, $\inf$/$\sup$, suite $(M_n)$ strict croissante, sous-suite convergente, axiome du choix, $1P1$/$2P$, $crgte$ (= convergente), $mtq$ (= montrer que), $\nearrow^*$.
