# Restes des séries à termes positifs — transcription fidèle

> 🧾 **Manuscrit original :** `restes-series-positives.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** écriture rapide, ratures conservées `[raturé]`, deux passages en `[lecture incertaine — …]` (notations des restes et un indice final). Transcrit mot à mot, le raisonnement s'interrompt en fin de Cas 2.
> 📄 **Source scannée :** [restes-series-positives.pdf](restes-series-positives.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Théo : Soient $\sum_{n \geq n_0} U_n$ et $\sum_{n \geq n_0} V_n$, 2 séries numériques à termes $\geq 0$.

Si $U_n \sim V_n$ alors $R_N^U \sim R_N^V$ [lecture incertaine — le scan porte « Rndu… Rndv… », interprété comme les restes $R_N$ des deux séries].

En effet, supp que $U_n \sim V_n$ et $\exists (\varepsilon_n)_{n \geq n_0} \to 0 \mid U_n = V_n(1 + \varepsilon_n)$.

Cas 1 : $V_n$ n'est pas stationnaire à 0 $\iff \forall n \in \mathbb{N}\ (n \geq n_0)$, $\exists m \in \mathbb{N}\ (m \geq n) \mid V_m \neq 0$. Dans ce cas [raturé : on peut extraire] une sous-suite $(V_{\varphi(n)})_{n \geq n_0}$ de $(V_n)$ à termes tous non nuls. Comme $U_n \sim V_n$ alors $U_{\varphi(n)} \sim V_{\varphi(n)}$ d'où ($U_\varphi$ [lecture incertaine — est à termes non nuls]) alors $\frac{U_{\varphi(n)}}{V_{\varphi(n)}} \to 1$.

[raturé : $\forall N \in \mathbb{N}\ (N \geq n_0)$, $R_N$ … $= \sum_{n \geq N+1} V_n \neq 0$ car … $\forall n \in \mathbb{N}$, $V_n \geq 0$.] Pour montrer que $R_N^U \sim R_N^V$ il suffit de mtr que $\frac{R_N^U}{R_N^V} \to 1$.

[raturé : Soit $\varepsilon > 0$. Cherchons $N_1 \in \mathbb{N}$ ($N_1$ … $N_2 \geq N_0$ …).]

$\exists N_2 \in \mathbb{N} \mid N_2 > N_1$. On a : $\frac{R_N^U}{R_N^V} = 1 + \frac{\sum_{n \in I_N} \varepsilon_n V_n}{\sum_{n \in I_N} V_n}$. Il suffit alors de mtr $W_N \to 0$. Soit $\varepsilon > 0$. Cherchons $N_1 \in \mathbb{N}\ (N_1 \geq N_0) \mid \forall N \in \mathbb{N},\ N \geq N_1 \implies |W_N| < \varepsilon$, avec $W_N = \frac{\sum_{n \in I_N} \varepsilon_n V_n}{\sum_{n \in I_N} V_n}$.

## Page 2

Comme $\varepsilon_n \to 0$, $\exists N_2 \in \mathbb{N}\ (N_2 \geq N_0) \mid \forall n \in \mathbb{N}\ (n \geq N_2) \implies |\varepsilon_n| < \varepsilon \implies \varepsilon_n < \varepsilon$ [raturé : car comme $U_n, V_n \geq 0\ (N \geq N_0)$] alors $\varepsilon_n \geq 0$.

Pour $N \geq N_2$, $W_N = \frac{\sum_{n \in I_N} \varepsilon_n V_n}{\sum_{n \in I_N} V_n}$ où $I_N = \{n \in \mathbb{N} \mid n \geq N+1 \text{ et } V_n \neq 0\}$. NB : $I_N \neq \emptyset$ car $(V_n)_{n \geq N_0}$ non stationnaire à 0.

Pour $n \in I_N$, comme $V_n > 0$ et $U_n \geq 0$ alors $\varepsilon_n \geq 0$, d'où $\varepsilon_n = |\varepsilon_n|$, et car $n \geq N+1 \geq N_2$ alors $\varepsilon_n = |\varepsilon_n| < \varepsilon$, d'où $|W_N| = \frac{\sum_{n \in I_N} \varepsilon_n V_n}{\sum_{n \in I_N} V_n} \leq \varepsilon \times 1$. Prendre $N_1 = N_2$ (car $V_n, \varepsilon_n \geq 0$, $n \in I_N$).

Cas 2 : $\exists N_1 \in \mathbb{N}\ (N_1 \geq n_0) \mid \forall n \in \mathbb{N},\ n \geq N_1 \implies V_n = 0$ (on choisit $N_1$ aussi petit que possible). Considérons $E_N$ : $\forall N \in \mathbb{N}\ (N \geq n_0)$ :

- Si $N \geq N_1$ alors $R_N = 0$.
- Si $N < N_1 - 1$ alors $R_N = \frac{R_{N_1-1}^U}{R_{N_1-1}^V} - 1$ qui est bien défini car ce $N_1$ est minimal : pour $n < N_1$, $V_n \neq 0$, d'où $R_{N_1-1} = \sum_{n} V_n \neq 0$ [lecture incertaine — borne inférieure de la somme coupée en bas de page], d'autant plus que $V_n \geq 0\ (n \geq n_0)$.

[Le manuscrit s'interrompt ici, fin du scan.]

## Figures

Aucune figure : 2 pages de texte manuscrit seul, sans schéma ni graphe (transcription § Statut : ratures conservées, raisonnement interrompu ; confirmé p. 1 sur source le 2026-09-07, rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07, rendu `/tmp/s10/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- supp : supposons ; mtr : montrer ; $R_N^U, R_N^V$ : restes des deux séries ; $I_N$ : indices utiles ($V_n \ne 0$) ; $W_N$ : quotient auxiliaire $\to 0$.
- stationnaire à 0 : nulle à partir d'un rang (Cas 2) ; $\sim$ : équivalence ; $\varepsilon_n \to 0$ : écart relatif.
