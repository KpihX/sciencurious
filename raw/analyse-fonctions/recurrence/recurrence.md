# Récurrence (bon ordre de ℕ et principe d'induction) — transcription fidèle

> 🧾 **Manuscrit original :** `recurrence.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible (~85 %), transcrit fidèlement. Partie I : toute partie non vide de $\mathbb{N}$ admet un plus petit élément (avec dénombrement des entiers entre $n_1$ et $n_2$) ; partie II : justification du principe de récurrence forte par l'absurde. Lignes raturées et réécrites en partie II (signalées).
> 📄 **Source scannée :** [`recurrence.pdf`](recurrence.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — I. Bon ordre de $\mathbb{N}$

I/ Montrons que toute partie non vide de $\mathbb{N}$ admet un plus petit élément [titre souligné]

[en haut à droite : notes « $\mathbb{N}^* = \mathbb{N}\setminus\{0\}$ » et calculs — lecture incertaine]

\* On part de la définition de $\mathbb{N}$ : $0 \in \mathbb{N}$ [?] et du fait que $\forall n \in \mathbb{N}$, $n+1 \in \mathbb{N}$ [le symbole du successeur est peu lisible]

— ainsi pour tout élément $n \in \mathbb{N}$, $n+1 \in \mathbb{N}$ et donc tout élément de $\mathbb{N}$ [lu « de n »] a un successeur

— Entre $n_1, n_2 \in \mathbb{N}$ / $n_2 > n_1$ les seuls entiers sont $v_i = n_1 + i$ où $i = \overline{0, n_2-n_1}$ car — $0 \leq i \leq n_2-n_1 \implies n_1 \leq v_i \leq n_2$ et de plus $n_1 \in \mathbb{N} \implies n_1+1 \in \mathbb{N} \implies n_1+\underbrace{1+\cdots+1}_{i \text{ fois}} \in \mathbb{N} \implies n_1+i \in \mathbb{N}$

— Pour $i < 0$ on a : $v_i < n_1$ et donc $v_i \notin [n_1, n_2]$

— Pour $i > n_2-n_1$ on a : $v_i > n_2$ et donc $v_i \notin [n_1, n_2]$

Ainsi comme on a : $1 + (n_2-n_1)$ valeur(s) de $i$ on a $n_2-n_1+1$ terme(s) entre $n_1$ et $n_2$ et entiers

\* Soit alors $A \subseteq \mathbb{N}$ / $A \neq \emptyset$

Soit $n \in A$, d'après ce qui [précède] : on a au plus $n+1$ éléments de $A$ entre $0$ et $n$. Soit alors $a_0, a_1, \dots, a_m$ ces éléments $m = \overline{0,n}$ [la formule de l'indice est peu lisible]

NB : Pour $m = 0$ on a juste $a_0 = \dots$ [fin illisible]

On pose alors $a_{\min} = \min\{a_0, a_1, \dots, a_m\}$ et ainsi $\forall a \in A$ [lu « $\forall n \in A$ »]

— Si $n \in \{a_0, \dots, a_m\}$ alors $a_{\min} \leq n$

— sinon $n > a_m$ [lecture incertaine] d'où $a_{\min} \leq n$

Donc $A$ admet un plus petit élément à savoir $a_{\min}$.

En conclusion toute partie non vide de $\mathbb{N}$ admet un plus petit élément [interligne : « admet un minimum »].

\* Corollaire : Toute suite décroissante de $\mathbb{N}$ est … [mot peu lisible — probablement « stationnaire »]. Pour prouv[er …] il suffit de considérer cette suite comme une partie de $\mathbb{N}$

## Page 2 — II. Principe de récurrence

II/ Justification du principe d'Induction / de récurrence [titre souligné]

Énoncé dudit principe : Soit $P(n)$ une proposition portant sur $n \in \mathbb{N}$. $n_0 \in \mathbb{N}$ … [formule empâtée : $n \geq n_0$]. On suppose que

— $P(n_0)$ est vraie

— si, pour $n \in \mathbb{N}$ [$\geq n_0$], $P(i)$ est vraie ($i = \overline{n_0,n}$), alors $P(n+1)$ est vraie [ligne raturée et réécrite — restitution d'après le contexte : récurrence forte]

[raturé : « Montrons que : »] Alors $P(n)$ est vraie $\forall n \in \mathbb{N} \cap [n_0, +\infty[$

\* Supposons par l'absurde $\exists A \subseteq \mathbb{N} \cap [n_0, +\infty[$ ($A \neq \emptyset$) / $\forall a \in A$, $P(a)$ est fausse. [avec insertions raturées]

D'après I, $A$ admet un minimum $a_m \geq n_0$.

[Or :] — $P(n_0)$ est vraie d'où $a_m > n_0$ cad $a_m \geq n_0+1$

— $p-1 \geq n_0$ et $p-1 \notin A$ d'où $P(p-1)$ est vraie [la lettre $p$ désigne le minimum $a_m$]

— $P((p-1)+1)$ est vraie car tous les entiers entre $n_0$ et $p-1$ ne sont pas dans $A$ et donc $P$ est vraie pour eux

— $P(p)$ est vraie d'où $p \notin A$. Absurde !

Alors $A = \emptyset$

Par conséquent sous les hypothèses en amont, $\forall n \in \mathbb{N} \cap [n_0, +\infty[$, $P(n)$ est vraie

---

## Figures

Aucune figure ni schéma (page 2 relue ; page 1 non relue — limite des 20 pages). Le script `reproduce_recurrence-justification_1.py` appartient au dossier hors périmètre `tableau-noir/recurrence-justification`, pas à celui-ci.

## Vocabulaire

- $P(n)$ = proposition portant sur $n$ ; $[n_0, +\infty[$ ; bon ordre ; récurrence (forte) ; « en amont » (habitude d'auteur).

---

## 📝 Notes de transcription (fidélité)

- Page 1 : le comptage « $n_2-n_1+1$ termes entre $n_1$ et $n_2$ » sert à borner le nombre d'éléments de $A$ entre $0$ et $n$ (au plus $n+1$), ce qui ramène le minimum de $A$ au minimum d'un ensemble fini $\{a_0, \dots, a_m\}$.
- Page 2 : l'hypothèse de récurrence est forte ($P(i)$ vraie pour tout $i$ de $n_0$ à $n$) ; la preuve applique cette hypothèse à $n = p-1$ (tous les entiers de $n_0$ à $p-1$ sont hors de $A$ par minimalité de $p$).
- Aucune figure ni schéma sur les 2 pages.
