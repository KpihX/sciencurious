# Famille positivement génératrice — transcription fidèle

🧾 Source : [familles-positivement-generatrices.pdf](familles-positivement-generatrices.pdf) — 4 pages manuscrites sur cahier ligné, encre bleue.
🔍 Restauration : image restaurée Datas1 2026-09-07 ; lecture directe des pages, rien d'inventé.
📄 Contenu : soit $E$ un $\mathbb{R}$-ev [lecture incertaine] $\dim E = n$ et $\mathcal{F}$ une famille positivement génératrice / $|\mathcal{F}| = p$ ; \* $p \geq n+1$ ; \* s'il y a une telle famille à $2n+1$ elts, il y en a à moins de $p$ elts ; contre-exemple pour $p = 2n$.

## Page 1

Famille positivement Génératrice !

Soit $E$ un $\mathbb{R}$-ev [lecture incertaine — « $E \subset \mathbb{R}$-ev » ?] $\dim E = n$ et $\mathcal{F}$ une famille positivement génératrice / $|\mathcal{F}| = p$

\* $p \geq n+1$

\* S'il y a une telle famille à $2n+1$ elts, il y en a à moins de $p$ elts

En effet posons $\mathcal{F} = \{e_i\}_{i=1}^p$

On peut y extraire une base. SNALG fixons $B = \{e_i\}_{i=1}^n$ [lecture incertaine — indices] cette base.

$\forall x \in E$, $\exists ! (x_i)_{i=1}^n \in \mathbb{R}^n$ / $x = \sum_{i=1}^n x_i e_i$

c-à-d $x = \sum_{i \in I} x_i e_i + \sum_{j \in J} 0 e_j + \sum_{k \in K} x_k e_k$

où $I = \{i \in \mathopen{[\![}1, n\mathclose{]\!]} \,/\, x_i > 0\}$

$J = \{j \in \mathopen{[\![}1, n\mathclose{]\!]} \,/\, x_j = 0\}$

$K = \{k \in \mathopen{[\![}1, n\mathclose{]\!]} \,/\, x_k < 0\}$

On a alors $x = \sum_{i \in I} x_i e_i - \sum_{k \in K} y_k e_k$ où $\forall k \in K$, $y_k = -x_k > 0$

Posons $y_m = \max\{y_k\}_{k \in K} > 0$. Posons $e = -\sum_{i=1}^n e_i$ [lecture incertaine]

On a : $x = y_m e + \sum_{i \in I}(x_i + y_m) e_i + \sum_{j \in J} y_m e_j + \sum_{k \in K}(y_m - y_k) e_k$ [lecture incertaine — fin de ligne coupée par la reliure]

et on a bien tous les coef positifs.

## Page 2

Il ne reste plus qu'à essayer d'écrire $e$ en fonction des elts de $\mathcal{F}$ avec des coefs positifs mais sans faire intervenir tous les elts de $\mathcal{F}$

$\exists (d_i)_{i=1}^p \in \mathbb{R}_+^p$ [reconstruction — le manuscrit porte « $\in \mathbb{R}_+^p$ », précédemment transcrit $\in \mathbb{N}^{*p}$ par erreur] / $e = \sum_{i=1}^p d_i e_i$ (?) car $\mathcal{F}$ positivement génératrice

or la famille $\mathcal{B} = \{e_i\}_{i=1}^{n+2}$ [lecture incertaine — exposant] est liée car elle contient au moins $n+2$ elts d'où $\exists L \subset \mathopen{[\![}1, n+p\mathclose{]\!]}$ [lecture incertaine]

et $(p_\ell)_{\ell \in L} \in \mathbb{R}^*$ / $\sum_{\ell \in L} p_\ell e_\ell = 0$ (b)

Posons $M = \mathopen{[\![}1, n+p\mathclose{]\!]} \setminus L$ [lecture incertaine]

$\forall \lambda \in \mathbb{R}$, $(b) \Rightarrow \sum_{\ell \in L} \lambda p_\ell e_\ell = 0$

$(a) \Rightarrow e = \sum_{i=1}^n d_i e_i + \sum_{m \in M} d_m e_m + \sum_{\ell \in L}(d_\ell + \lambda p_\ell) e_\ell$

on va maintenant choisir $\lambda$ de sorte à avoir tous les coefficients $(d_\ell + \lambda p_\ell)_{\ell \in L}$ positifs avec au moins 1 nul. Pour cela, $\forall \ell \in L$ on doit avoir $d_\ell + \lambda p_\ell \geq 0$ c-à-d $\lambda p_\ell \geq -d_\ell$ (4)

On prend $\lambda \geq 0$ pour $\ell \in L$ / $p_\ell > 0$ $d_\ell + \lambda p_\ell \geq 0$

Soit maintenant $\ell \in L$ / $p_\ell < 0$

$(4) \Rightarrow \lambda \leq -\frac{d_\ell}{p_\ell}$. Vu qu'on veut annuler au moins un terme en prenant $\lambda =$ [raturé]

Vu qu'on veut annuler au moins un terme, en prenant $\lambda = \min\{-\frac{d_\ell}{p_\ell}, \ell \in L\}$ [lecture incertaine] on aura bien annulé un certain terme d'indice $l_m$ et le reste sera juste positif

## Page 3

Il vient que $(a) \Rightarrow e = \sum_{i=1}^n d_i e_i + \sum_{m \in M} d_m e_m + \sum_{\ell \in L \setminus \{l_m\}} (d_\ell + \lambda p_\ell) e_\ell$

$e$ s'écrit ainsi en fct des $e_i$, $i \in \mathopen{[\![}1, p\mathclose{]\!} \setminus \{l_m\}$ [reconstruction — le manuscrit porte $p$, précédemment transcrit $n$ par erreur] à coef positifs

Considérons le sous-ensemble $N$ de $\mathopen{[\![}1, p\mathclose{]\!} \setminus \{l_m\}$ / le coef devant $e_n$ ($n \in N$) dans l'écriture de $e$ soit non nul

Il vient que $e = \sum_{n \in N} \delta_n e_n$ pour certains $(\delta_n) \in \mathbb{R}_+^*$

en remplaçant $e$ dans l'expression de $x$ il vient que la famille $\{e_i\}_{i \in N} \neq \mathcal{F}$ est positivement génératrice. CQFD

\* contre-exemple pour $p = 2n$

Considérons $\mathcal{G} = \{e_i, -e_i\}_{i=1}^n$ pour $B = \{e_i\}_{i=1}^n$ une base de $E$

elle est positivement génératrice à $2n$ elts.

- Soit une sous-famille stricte $\mathcal{G}'$, $\exists i \in \mathopen{[\![}1, n\mathclose{]\!]}$ / $e_i$ ou $-e_i \notin \mathcal{G}'$.

Supp que $\mathcal{G}'$ est positivement génératrice,

- Si c'est $e_i \notin \mathcal{G}'$, alors $\exists (d_j)_{j \in \mathopen{[\![}1, n\mathclose{]\!} \setminus \{i\}}$, $(\beta_j)_{j \in 1}^n$ [lecture incertaine] tous positifs / $e_i = \sum_{j \neq i} d_j e_j + \sum_{j=1}^n \beta_j (-e_j)$

## Page 4

c-à-d $\sum_{j \neq i} (d_j - \beta_j) e_j - (\beta_i + 2)$ [lecture incertaine — « $+ 2$ » ?] $e_i = 0$

or $B$ étant libre car $\equiv$ base, il vient que $\beta_i + 2 = 0 \Rightarrow \beta_i = -2$ [*sic* — $\beta_i \geq 0$ par hypothèse, contradiction voulue]

- Si c'est $-e_i \notin \mathcal{G}'$ ; un raisonnement similaire aboutit tjrs à une A! [lecture incertaine — abréviation de « Absurde », précédemment transcrit « $1!$ » par erreur]

CQFD

---

## Figures

Aucune figure à reproduire : pages 1–4 relues visuellement (relecture 2026-09-07, texte et formules sur cahier ligné, sans schéma ni tracé).

## Vocabulaire / notions

- **Famille positivement génératrice** : tout $x$ = combinaison à coefficients $\geq 0$.
- **Base extraite** $B = \{e_i\}_{i=1}^n$ ; **SNALG** ; vecteur auxiliaire $e = -\sum e_i$.
- **Contre-exemple $p = 2n$** : $\mathcal{G} = \{e_i, -e_i\}_{i=1}^n$, minimale.
