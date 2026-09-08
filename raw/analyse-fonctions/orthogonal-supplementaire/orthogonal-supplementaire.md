# Orthogonal et supplémentaire (formes bilinéaires) — transcription fidèle

> 🧾 **Manuscrit original :** `orthogonal-supplementaire.pdf` (scan, 5 pages, encre bleue) · ✍️ KpihX
> 🔍 **Statut :** lisible (~80 %), transcrit mot à mot. Algèbre bilinéaire (orthogonalité, non-dégénérescence, supplémentaires) conservée telle quelle ; ratures et fins de lignes écrasées signalées. Aucune figure à reproduire (texte seul).
> 📄 **Source scannée :** [`orthogonal-supplementaire.pdf`](orthogonal-supplementaire.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Théorème (dimension de l'orthogonal) et lemme (matrice inversible)

Théo : Soit $E$ un $\mathbb{K}$-ev de dim finie $n$. Soit $\varphi \in L_2(E)$ [formes bilinéaires sur $E$]. Si $\varphi$ est non dégénérée alors $\dim F + \dim F^\perp = \dim E$ et $(F^\perp)^\perp$ [lecture incertaine — fin de ligne écrasée, lire probablement « $= F$ » d'après la page 3]

En effet,

considérons $B_p = (e_1, \dots, e_p)$ une base de $F$ que nous complétons en base de $E$ pnc $(e_1, \dots, e_p, e_{p+1}, \dots, e_n) = B$

Soit $v = \sum_{i=1}^n v_i e_i \in F^\perp$

$\forall j \in [\![1, p]\!]$, ona : $\varphi(v, e_j) = 0_{\mathbb{K}} \Leftrightarrow \sum_{i=1}^n v_i \varphi(e_i, e_j) = 0_{\mathbb{K}}$

Lemme : Si $\varphi$ non dégénérée [raturé — connecteur biffé] $M_B(\varphi) = [\varphi(e_i, e_j)]_{n \times n}$ est inversible

$\Rightarrow$/ona : $M_B(\varphi) = \begin{bmatrix} \varphi(e_1, e_1) & \dots & \varphi(e_1, e_n) \\ \vdots & & \vdots \\ \varphi(e_n, e_1) & \dots & \varphi(e_n, e_n) \end{bmatrix} \begin{matrix} L_1 \\ \vdots \\ L_n \end{matrix} \to M_B(\varphi)$ [flèche et colonnes $L_1 \dots L_n$ annotées en marge]

[raturé — amorce « $\varphi$ non inversible » biffée] Supp par l'absurde $\varphi$ non inversible ainsi $L_1 \dots L_n$ [les lignes] est liée. Ainsi $\exists j \in [\![1, n]\!]$, $\exists (d_i)_{i=1, i \neq j}^n$ / $L_j = \sum_{\substack{i=1 \\ i \neq j}}^n d_i L_i \Leftrightarrow$ (en particulier) $\varphi(e_j, e_k) = \sum_{\substack{i=1 \\ i \neq j}}^n d_i \varphi(e_i, e_k)$ $\forall k \in [\![1, n]\!]$

$$\Leftrightarrow \varphi(e_j - \underbrace{\sum_{\substack{i=1 \\ i \neq j}}^n d_i e_i}_{u}, e_k) = 0_{\mathbb{K}} \quad \forall k \in [\![1, n]\!]$$

Montrons que $u \in E^\perp$. Soit $v = \sum_{i=1}^n \alpha_i e_i$. Ona : $\varphi(u, v) = \sum_{i=1}^n \alpha_i \varphi(u, e_i) = \sum_{i=1}^n 0_{\mathbb{K}} = 0_{\mathbb{K}}$ [lecture incertaine — la conclusion « $\Rightarrow u \in E^\perp$, $u \neq 0_E$ » est écrasée en bas de page]

---

## Page 2 — Fin du lemme ($\varphi$ non dégénérée $\Leftrightarrow$ matrice inversible) et retour

Car $(e_i)_{i=1}^n$ est libre, $u = e_j - \sum_{\substack{i=1 \\ i \neq j}}^n d_i e_i \neq 0_E$ d'où $\varphi$ dégénérée A !

Donc $\varphi$ non dégénérée $\Rightarrow$ $M_B(\varphi)$ inversible

$\Leftarrow$/ Supp par l'Absurde $\varphi$ dégénérée alors $\exists u = \sum_{i=1}^n v_i e_i \in E$ / $\forall v \in E$, $\varphi(u, v) = 0_{\mathbb{K}}$.

En particulier $\forall j \in [\![1, n]\!]$, ona : $\varphi(u, e_j) = 0_{\mathbb{K}} \Rightarrow \sum_{i=1}^n v_i \varphi(e_i, e_j) = 0_{\mathbb{K}}$

$$\Rightarrow M_B(\varphi)[v]_B = 0_{\mathbb{K}^n}$$

$$\Rightarrow [v]_B = M_B(\varphi)^{-1} 0_{\mathbb{K}^n} \quad \text{car } M_B(\varphi) \text{ inversible}$$

$$\Rightarrow [v]_B = 0_{\mathbb{K}^n}$$

$\Rightarrow u = 0_E$ A !

Donc $\varphi$ non dégénérée $\Leftrightarrow$ $M_B(\varphi)$ inversible

. Revenons à notre démonstration

on avait $\forall j \in [\![1, p]\!]$, $\sum_{i=1}^n v_i \varphi(e_i, e_j) = 0_{\mathbb{K}}$

Ainsi comme $M_B(\varphi) = [\varphi(e_i, e_j)]_{n \times n}$ est inversible et qu'on a $p$ équations le système linéaire obtenu est de rang $p$ et ce $F^\perp$ correspond à l'espace des solutions de ce système, $F^\perp$ est donc de dimension $n - p$

d'où $\dim F + \dim F^\perp = \dim E$

---

## Page 3 — Double orthogonal, corollaire et contre-exemple dégénéré

[début rogné : fin de la preuve précédente] $F = (F^\perp)^\perp$

Car $F \subset (F^\perp)^\perp$ et que $\dim (F^\perp)^\perp = \dim E - \dim F^\perp$ car $F^\perp$ sev de $E$ $= \dim F$

alors $\underline{F = (F^\perp)^\perp}$

Corollaire : $\varphi$ non dégénérée $\Leftrightarrow$ $\forall F$ sev de $E$, $\underbrace{\dim F + \dim F^\perp = \dim E}_{\text{en dim finie}}$

. Car $\varphi$ dégénérée et $\dim F + \dim F^\perp \neq \dim E$

Considérons $E = \mathbb{R}^2$ et $\varphi : (\underbrace{(x_1, x_2)}_{x}, \underbrace{(y_1, y_2)}_{y}) \mapsto \varphi(x, y) = (x_1 + x_2)(y_1 + y_2)$ [au-dessous : $\mathbb{R}$-ev]

$\varphi \in L_2(E)$ et ona que pour $x = (1, -1)$ et $\forall y = (y_1, y_2)$ ona $\varphi(x, y) = 0_{\mathbb{R}}$ alors $\varphi$ dégénérée

considérons $F = \mathbb{K}\{x = (1, -1)^t\}$. $F^\perp = E$

or $\dim F + \dim F^\perp = 1 + 2 = 3 \neq \dim E$

Rq : ce constat peut permettre de démontrer le sens $\Leftarrow$ du corollaire précédent en raisonnant par l'absurde et en considérant $F =$ [raturé] $E^\perp \neq \{0_E\}$ puisque $\dim F + \dim F^\perp = \dim F + \dim E \neq \dim E$ car $\dim F \geqslant 1$

Théo : Soit $\varphi$ une fb non dégénérée sur $E$. Alors $\forall F$ sev de $E$, $F$ non dégénérée $\Leftrightarrow$ $F \oplus F^\perp = E$. ($\dim E$ finie)

$\Rightarrow$ car $\varphi$ non dégénérée, $\dim F + \dim F^\perp = \dim E$

De plus cherchons $v \in F \cap F^\perp$.

$v \in F^\perp \Leftrightarrow \forall v \in F$, $\varphi(v, v) = 0_{\mathbb{K}}$ [*sic* — même lettre $v$ liée et libre, attendu « $\forall w \in F$, $\varphi(v, w) = 0$ » ; confirmé second passage] et car $v \in F$ et que [non dégénérée — suite page 4]

---

## Page 4 — Fin du théorème ($F \oplus F^\perp$) et théorème d'isotropie

[suite :] … $v = 0_E$ d'où $F \cap F^\perp = \{0_E\}$. Par conséquent $F \oplus F^\perp \subset E$ / ona : $F \cap F^\perp = \{0_E\}$ et car $\varphi$ non dégénérée, $\dim F + \dim F^\perp = \dim E$ d'où $F \oplus F^\perp = E$.

* et $F^\perp$ est non dégénérée d'après ce même Théo appliqué à $F^\perp$.

Théo : Soit $\varphi$ une fb sur $E$ ($\dim E < +\infty$) et soit $F$ sev de $E$. $\varphi$ non isotrope $\Leftrightarrow$ $F \oplus F^\perp = E$

$\Leftarrow$/ Évident

$\Rightarrow$/ Moy $\dim F + \dim F^\perp = \dim E$.

Soit $B_p = (e_1, \dots, e_p)$ une base de $F$ que nous complétons en base de $E$ pnc $(e_1, \dots, e_n)$. Soit $v \in F^\perp$. J'écris $v$ [lecture incertaine] $v = \sum_{i=1}^n \alpha_i e_i$. Soit $j \in [\![1, p]\!]$

Ona : $\varphi(v, e_j) = 0_{\mathbb{K}} \Rightarrow \sum_{i=1}^n \alpha_i \varphi(e_i, e_j) = 0_{\mathbb{K}}$ car $v \in F^\perp$

En considérant le lemme précédent appliqué cette fois à $F$ et à la restriction $\varphi_F$ de $\varphi$ à $F$, ona : $M_{B_p}(\varphi_F) = [\varphi(e_i, e_j)]_{p \times p}$ est inversible, car [raturé] $F \cap F^\perp = \{0_E\}$, $\forall v \in F$ [lecture incertaine — passage écrasé : « … que $v \notin F^\perp$ on ne peut avoir $\varphi_F(v, \cdot) = 0$ »] $\forall v \in F$ ce qui entraîne $\varphi_F$ non dégénérée sur $F$ (d'où la possibilité d'appliquer ce lemme)

(Rq : $F$ non isotrope $\Leftrightarrow$ $\varphi_F$ non dégénérée)

---

## Page 5 — Système linéaire, conclusion et bloc biffé

… en revenant à notre démonstration, ona :

$$\sum_{i=1}^p \alpha_i \varphi(e_i, e_j) = -\sum_{i=p+1}^n \alpha_i \varphi(e_i, e_j)$$ [lecture incertaine — l'indice de départ de la seconde somme (« $p+1$ ») est écrasé]

en fixant les $(\alpha_i)_{i=p+1}^n$ [même incertitude] et ce $[\varphi(e_i, e_j)]_{i=1}^p$ est inversible le système d'inconnue $[\alpha_1 \dots \alpha_p]^T = [\alpha \dots \alpha_p]^T$ [lecture incertaine — second membre écrasé] admet un unique couple solutions (pour les $(\alpha_i)_{i=p+1}^n$ fixés).

En faisant parcourir ces $(\alpha_i)_{i=p+1}^n$, l'ens solution est un $\mathbb{K}$-ev de dim $n - (p+1) + 1 = n - p$. Et ce cet ens solution est isomorphe à $F^\perp$ alors $\dim F + \dim F^\perp = \dim E$.

Car $F^\perp \cap F = \{0_E\}$ et $\dim F + \dim F^\perp = \dim E$ alors $F \oplus F^\perp = E$

Cl : $\varphi \in L_2(E)$ et $E$ un $\mathbb{K}$-ev ($\dim E \in \mathbb{N}^*$). $F$ isotrope sot [lecture incertaine — mot de liaison illisible] $(F \cap F^\perp = \{0_E\}) \Leftrightarrow \varphi_F$ non dégénérée $\Leftrightarrow \begin{cases} \dim F + \dim F^\perp = \dim E \\ F \cap F^\perp = \{0_E\} \end{cases} \Leftrightarrow F \oplus F^\perp = E$.

[raturé — grand trait diagonal biffant un « Théo » et un « Lemme » intermédiaires :] Théo : Soit $\varphi \in L_2(E)$ ($\dim E < +\infty$). $\exists$ une base de $E$ formée de vecteurs 2 à 2 orthogonaux (caract $\mathbb{K} \neq 2$) / Lemme : Soit $F$ sev de $E$ de dim $F = p \in [\![1, m-2]\!]$ [lecture incertaine] … $\exists u \in F$ / $\varphi(u, u) \neq$ [suite illisible, biffée]

Lemme : $\exists v \in E$ / $\varphi(v, v) \neq 0_E$. (was $J_B$ ? $\neq 0_{L_2(E)}$) [lecture incertaine — parenthèse écrasée]

---

## Figures

Aucune figure ni schéma : texte seul (pages 1 et 5 relues + second passage pp. 2–4 le 2026-09-07, /tmp/s7/, pdftoppm -png -r 150, texte seul, pas de PNG requis). Le bloc biffé p. 5 (théorème + lemme) est transcrit, pas une figure.

## Vocabulaire

- Théo, pnc (= « que nous complétons »), ona, fb = forme bilinéaire, Moy (= « en moyenne »), Cl = conclusion, sev, $\mathbb{K}$-ev, A! = absurde.
- $L_2(E)$ = formes bilinéaires ; isotrope / non dégénérée ; rang ; $\mathrm{caract}\,\mathbb{K} \neq 2$.

---

## 📝 Notes de transcription (fidélité)

- Abréviations d'origine conservées : « Théo », « pnc » (pour « que nous complétons »), « ona » (pour « on a »), « fb » (forme bilinéaire), « Moy » (pour « moyen »/« en moyenne » — lire « en moyenne »), « Cl » (conclusion), « sev », « $\mathbb{K}$-ev », « A ! » (absurde !), « CQFD » implicite.
- Page 1 : l'énoncé du théorème se termine par une fin de ligne écrasée après $(F^\perp)^\perp$ (probablement « $= F$ », prouvé page 3) ; la matrice $M_B(\varphi)$ est annotée de ses lignes $L_1 \dots L_n$.
- Page 1 (bas) : la conclusion « $u \in E^\perp$, $u \neq 0_E$ » est écrasée — signalée, rien d'inventé.
- Pages 2–3 : l'équivalence « $\varphi$ non dégénérée $\Leftrightarrow$ $M_B(\varphi)$ inversible » est démontrée par double contraposée (les deux « A ! » sont d'origine).
- Page 3 : contre-exemple $\varphi(x,y) = (x_1+x_2)(y_1+y_2)$ sur $\mathbb{R}^2$ avec $x = (1,-1)$, $F = \mathbb{K}\{x\}$, $F^\perp = E$, $1 + 2 = 3 \neq 2$ ; la remarque « Rq » propose la contraposée du corollaire via $F = E^\perp$.
- Page 5 : l'indice de départ des sommes partielles ($p+1$) est écrasé mais cohérent avec la dimension $n-(p+1)+1 = n-p$ ; le second membre du système est illisible (signalé).
- Page 5 (bas) : un théorème (base de vecteurs 2 à 2 orthogonaux, $\mathrm{caract}\,\mathbb{K} \neq 2$) et un lemme intermédiaire sont biffés d'un grand trait diagonal ; seul le dernier « Lemme : $\exists v \in E$ / $\varphi(v,v) \neq 0_E$ » semble épargné.
