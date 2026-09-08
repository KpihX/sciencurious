# Proba-ensembles — transcription fidèle

> 🧾 **Manuscrit original :** `proba-ensembles.pdf` (cahier + feuilles volantes, 5 pages) · ✍️ KpihX
> 🔍 **Statut :** partiellement lisible, transcrit mot à mot. Page 1 : formulaire (Bayes, proba composée, Poincaré). Pages 2–4 : théorème de Poincaré généralisé au triplet $(\Omega, \mathcal{E}, f)$ avec démonstration par induction, applications à $\mathrm{Card}$ et $P$, mention de $!n$ ; la page 4 est un doublon de la page 3 (même feuille photographiée deux fois). Page 5 : complémentaire d'une intersection. Les maths sont conservées telles quelles ; les passages douteux sont signalés `[lecture incertaine — …]`, les erreurs apparentes `[*sic* — …]`, les ratures `[raturé]`.
> 📄 **Source scannée :** [proba-ensembles.pdf](proba-ensembles.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

[haut de page coupé — fin d'une formule de la page précédente :]

$$= P(A_n \setminus \bigcap A_i) \times \ldots$$ [lecture incertaine — ligne tronquée en haut de la photo]

- Théo de Bayes : Pour un système complet d'evts $(A_i)_n$ et $B \subseteq E$ où $(\Omega, \mathcal{E}, P)$ est un e-p,

$$P(A_i/B) = \frac{P(B/A_i) \times P(A_i)}{\sum_j P(B/A_j) \times P(A_j)}, \quad i = \overline{1,n} \quad (n \geq 2)$$

[en marge droite : $i = \overline{1,n}$, $(n \geq 2)$ ; sigle « W$\Delta$ » [lecture incertaine]]

- Proba composée : $P(\bigcap_{i=1}^n A_i) = P(A_1) \times P(A_2/A_1) \times P(A_3/A_1 \cap A_2) \times \ldots \times P(A_n/\bigcap_{i=1}^{n-1} A_i)$ [en marge droite : « bn » [lecture incertaine]]

$$P\left(\bigcap_{i=1}^n A_i\right) = P(A_1) \times \prod_{i=2}^n P\left(A_i \Big/ \left(\bigcap_{j=1}^{i-1} A_j\right)\right)$$

- Formule de Poincaré : $P(\bigcup_{i=1}^n A_i) = \sum_{I \in \mathcal{P}(\{1,2,\ldots,n\})} (-1)^{|I|+1} P(A_I)$

où $P(\emptyset) = 0$ et $P(A_I) = \prod_{j \in I} P(A_j)$, $I \neq \emptyset$ [*sic* — en général $P(A_I) = P(\bigcap_{j \in I} A_j)$ ; le produit ne vaut que sous indépendance mutuelle]

[en marge droite, notes verticales à 90° (calculs $P(A_1) \times P(A_2)$, $P(A_1 \cap A_2)$, $P(B_1 \cup \ldots)$, $\sum P(B_1 \cap \ldots)$) [lecture incertaine — écriture verticale, partiellement hors cadre]]

[bas de page coupé]

## Page 2

Théorème de Poincaré : Soit $(\Omega, \mathcal{E}, f)$ un triplet vérifiant [en haut à droite : date « 20/05/20… » [lecture incertaine — coupée]]

- $\Omega$ est un ens non vide
- $\mathcal{E} \subseteq \mathcal{P}(\Omega)$ vérifiant : $\cdot$ Si $A_1, A_2 \in \mathcal{E}$ alors $A_1 \cup A_2 \in \mathcal{E}$ (1)
$\cdot$ $\Omega \in \mathcal{E}$ (2)
$\cdot$ Si $A \in \mathcal{E}$ alors $\overline{A} = C_\Omega^A \in \mathcal{E}$ (3)
$\Big\}$ $(\Omega, \mathcal{E})$ est dit probabilisable

- $f : \mathcal{E} \longrightarrow G$ (où $(G, +)$ est un groupe) est une application vérifiant : $\forall A_1, A_2 \in \mathcal{E}$, $A_1 \cap A_2 = \emptyset \Rightarrow f(A_1 \cup A_2) = f(A_1) + f(A_2)$ (4)

Soient $(A_i)_n \in \mathcal{E}^n$ ($n \in [\![2, +\infty[\![ = \{2, \ldots\} \cap \mathbb{N}$) [lecture incertaine — « $wll = \{2, \ldots\} \cap \mathbb{N}$ »]. Mt $P(n)$ : $f(\bigcup_{i=1}^n A_i) = \sum_{I \subseteq^* [\![1,n]\!]} (-1)^{|I|+1} f(\bigcap_{i \in I} A_i)$

Nota : $I \subseteq^* [\![1,n]\!] \Rightarrow I \in (\mathcal{P}([\![1,n]\!]) \setminus \{\emptyset\})$

* Rq : $f(\bigcup_{i=1}^n A_i)$ est bien défini car qu'on montre par récurrence que $\bigcup_{i=1}^n A_i \in \mathcal{E}$

- Justifions que $f(\bigcap_{i \in I} A_i)$ bien défini c-à-d $\bigcap_{i \in I} A_i \in \mathcal{E}$. On se limitera juste à montrer que $\forall A_1, A_2 \in \mathcal{E}$, $A_1 \cap A_2 \in \mathcal{E}$, le cas général en découle par récurrence

Soient donc $A_1, A_2 \in \mathcal{E}$, Ona : $\overline{A}_1, \overline{A}_2 \in \mathcal{E}$ (d'après ③) $\Rightarrow \overline{A}_1 \cup \overline{A}_2 \in \mathcal{E}$ (d'après ①) $\Rightarrow$ [formule de Morgan] $\Rightarrow A_1 \cap A_2 = \overline{\overline{A}_1 \cup \overline{A}_2}$ [lecture incertaine — surcharges] $\in \mathcal{E}$ (d'après ③)

- $\sum_{I \subseteq^* [\![1,n]\!]} (-1)^{|I|+1} g(I)$ (dans un cadre général où $g : \mathcal{P}([\![1,n]\!])^* \to G$ [raturé — « $\mathcal{P}$ » réécrit] est une application) est défini par $\left\{ \sum_{I \subseteq^* [\![1,n]\!]} (-1)^{|I|+1} g(I) = \left\{ \begin{array}{l} g(J) + \sum_{\substack{I \subseteq^* [\![1,n]\!] \\ I \neq J}} (-1)^{|I|+1} g(I) \text{ si } \ldots \in 2\mathbb{N}+1 \text{ [lecture incertaine]} \\ -g(J) + \text{—//— si } \ldots \in 2\mathbb{N}^* \text{ [lecture incertaine]} \end{array} \right. \right.$ avec $J$ quelconque dans $\mathcal{P}([\![1,n]\!])^*$ ou $\mathcal{P}([\![1,n]\!]) \setminus \{\emptyset\}$ [« ou $\mathcal{P}([\![1,n]\!]) \setminus \{\emptyset\}$ » confirmé p.2 r150 2026-09-07 ; parités « si $|I| \in 2\mathbb{N}+1$ » / « si $|I| \in 2\mathbb{N}^*$ » levées visuellement (`/tmp/s9/ens-2.png`)] : lorsqu'il ne reste plus qu'un elt non prélevé à prélever dans $\mathcal{P}([\![1,n]\!])^*$ $\sum$ renvoie cet elt.

* Démontrons $P(n)$ (on utilisera le principe d'induction)

- Pour $n=2$, $\left. \begin{array}{l} A_1 \cap (A_2 \setminus A_1) = \emptyset \\ A_1 \cup (A_2 \setminus A_1) = A_1 \cup A_2 \end{array} \right\} \Rightarrow f(A_1 \cup A_2) = f(A_1) + f(A_2 \setminus A_1)$
or $\left. \begin{array}{l} (A_2 \setminus A_1) \cap (A_1 \cap A_2) = \emptyset \\ (A_2 \setminus A_1) \cup (A_1 \cap A_2) = A_2 \end{array} \right\} \Rightarrow f(A_2) = f(A_2 \setminus A_1) + f(A_1 \cap A_2)$
$\left. \vphantom{\begin{array}{l} . \\ . \end{array}} \right\} \Rightarrow f(A_1 \cup A_2) = f(A_1) + f(A_2) - f(A_1 \cap A_2)$

d'où $P(2)$ vraie

- hérédité : On suppose $P(n)$ vraie jusqu'à un rang $n \in [\![2, +\infty[\![$ et montrons $P(n+1)$ vraie

## Page 3

$$f\left(\bigcup_{i=1}^{n+1} A_i\right) = f\left(\left(\bigcup_{i=1}^n A_i\right) \cup A_{n+1}\right) = f\left(\left. \bigcup_{i=1}^n A_i \right| A_{n+1} \cap A_{n+1}\right)$$ [lecture incertaine — surcharges]

$$= f\left(\bigcup_{i=1}^n A_i\right) + f(A_{n+1}) - f\left(A_{n+1} \cap \left(\bigcup_{i=1}^n A_i\right)\right) \text{ car } P(2) \text{ vraie or que } 2 \leq n$$ [lecture incertaine — « rus que 2 $\in$ n »]

$$= \sum_{I \subseteq^* [\![1,n]\!]} (-1)^{|I|+1} f\left(\bigcap_{i \in I} A_i\right) + f(A_{n+1}) - \sum_{I \subseteq^* [\![1,n]\!]} (-1)^{|I|+1} f\left(\bigcap_{i \in I} (A_i \cap A_{n+1})\right) \text{ car } P(n) \text{ vraie}$$

$$= \sum_{\substack{I \subseteq^* [\![1,n+1]\!] \\ 1 \notin \Delta}} (-1)^{|I|+1} f\left(\bigcap_{i \in I} A_i\right) + \sum_{\substack{I \subseteq^* [\![1,n+1]\!] \\ 2 \leq |I| \leq n \\ n+1 \notin I}} (-1)^{|I|+1} f\left(\bigcap_{i \in I} A_i\right) - \sum_{\substack{I \subseteq^* [\![1,n+1]\!] \\ 2 \leq |I| \leq n+1 \\ n+1 \in I}} (-1)^{|J|} f\left(\bigcap_{i \in J} A_i\right) = \sum \ldots$$ [lecture incertaine — premier sous-ensemble : « $1 \notin \Delta$ »] [raturé — terme barré ; en marge : car $|J| = |I|+1$]

$$= \sum_{\substack{I \subseteq^* [\![1,n+1]\!] \\ |I| = 1}} (-1)^{|I|+1} f\left(\bigcap_{i \in I} A_i\right) + \sum_{\substack{I \subseteq^* [\![1,n+1]\!] \\ 2 \leq |I| \leq n \\ n+1 \notin I}} (-1)^{|I|+1} f\left(\bigcap_{i \in I} A_i\right) + \sum_{\substack{I \subseteq^* [\![1,n+1]\!] \\ 2 \leq |I| \leq n \\ n+1 \in I}} (-1)^{|I|+1} f\left(\bigcap_{i \in I} A_i\right) + \sum_{\substack{I \subseteq^* [\![1,n+1]\!] \\ |I| = n+1}} (-1)^{|I|+1} f\left(\bigcap_{i \in I} A_i\right)$$

$$f\left(\bigcup_{i=1}^{n+1} A_i\right) = \sum_{I \subseteq^* [\![1,n+1]\!]} (-1)^{|I|+1} f\left(\bigcap_{i \in I} A_i\right) \text{ d'où } P(n+1) \text{ vraie}$$

CQ : $\forall n \in [\![2, +\infty[\![$, $\forall (A_i)_n \in \mathcal{E}$, $\boxed{f\left(\bigcup_{i=1}^n A_i\right) = \sum_{I \subseteq^* [\![1,n]\!]} (-1)^{|I|+1} f\left(\bigcap_{i \in I} A_i\right) = \sum_{k=1}^n \sum_{1 \leq i_1 < \cdots < i_k \leq n} f\left(\bigcap_{j=1}^k A_{i_j}\right)}$

* Rq : Une telle somme a $\sum_{k=1}^n C_n^k = 2^n - 1$ termes (nbre de Mersenne)

* Application : Vu que $\mathrm{Card} : \mathcal{E} \to \mathbb{N} \subseteq \mathbb{Z}$ et $P : \mathcal{E} \to [0,1] \subseteq \mathbb{R}$ (pour $(\Omega, \mathcal{E}, P)$ un espace probabilisé) alors on déduit $\forall n \in [\![2, +\infty[\![$, $\forall (A_i)_n \in \mathcal{E}$, $\boxed{\mathrm{Card}\left(\bigcup_{i=1}^n A_i\right) = \sum_{I \subseteq^* [\![1,n]\!]} (-1)^{|I|+1} \mathrm{Card}\left(\bigcap_{i \in I} A_i\right) \text{ et } P\left(\bigcup_{i=1}^n A_i\right) = \sum_{I \subseteq^* [\![1,n]\!]} (-1)^{|I|+1} P\left(\bigcap_{i \in I} A_i\right)}$

* Cette même formule avec les cardinaux aide à établir une expression explicite de $!n$.

Rq : Fondamentalement, on retient que $(\Omega, \mathcal{E}, f)$ doit satisfaire aux axiomes ①, ②, ③ et ④.

## Page 4

[doublon CONFIRMÉ visuellement au 2e passage le 2026-09-07 (`/tmp/s9/ens-3.png` vs `/tmp/s9/ens-4.png`, r150) : même contenu — hérédité, CQ encadré, Mersenne $2^n-1$, applications Card/$P$, $!n$, axiomes ①②③④ — angle et lumière légèrement différents (md5 distincts) ; voir la transcription de la Page 3]

## Page 5

Soient $n \in \mathbb{N}$ et $(A_i)_n \subseteq \mathcal{E}$, On note $\overline{A}_i = C_{B_i}^{A_i}$ $\forall i \in [\![1,n]\!]$ [lecture incertaine — le complémentaire est noté $C_{B_i}^{A_i}$]

$$\overline{\left(\bigcap_{i=1}^n A_i\right)} = \bigcup_{I \subseteq^* [\![1,n]\!]} \left[ \left(\bigcup_{i \in I} \overline{A}_i\right) \cup \left(\bigcup_{i \in C_{[\![1,n]\!]}^I} A_i\right) \right]$$ [lecture incertaine — l'opérateur sous la barre (membre de gauche) ressemble à $\bigcap$]

Note : $I \subseteq^* [\![1,n]\!] \Leftrightarrow$ [lecture incertaine — $\Leftrightarrow$ ou $\Rightarrow$] $I \in \mathcal{P}([\![1,n]\!]) \setminus \{\emptyset\}$

$= \bigcup_{k=1}^n \left(\bigcup_{1 \leq i_1 < \cdots < i_k \leq n} \overline{A_{i_j}}\right) \cup \left(\bigcup_i \ldots \right.$ [raturé — toute la ligne est barrée d'une grande croix]

$$= \bigcup_{k=1}^n \left[ \bigcup_{1 \leq i_1 < \cdots < i_k \leq n} \left( \left(\bigcup_{j=1}^k \overline{i_j}\right) \cup \left(\bigcup_{\substack{j \in [\![1,n]\!] \setminus \ldots \\ j_i \notin i_k}} j_S \right) \right) \right]$$ [lecture incertaine — exposants du sous-ensemble] [lecture incertaine — bas de feuille shaping, écriture empâtée]

---

## Figures

Aucune figure sur les 5 pages relues (p.1 et p.5 re-rendues à $r = 150$ et relues ; pp.2–4 vérifiées visuellement au 2e passage le 2026-09-07 — rendus `/tmp/s9/ens-2.png`, `/tmp/s9/ens-3.png`, `/tmp/s9/ens-4.png`, r150 — parités $2\mathbb{N}+1$/$2\mathbb{N}^*$ levées, surcharges et ratures confirmées, doublon p.3=p.4 CONFIRMÉ ; N == pdfinfo) : formulaires et démonstration seuls, notes marginales verticales (p.1) sans schéma.

## Vocabulaire

- **Probabilisable** : $(\Omega, \mathcal{E})$ vérifiant ①②③ (stabilité union, $\Omega \in \mathcal{E}$, stabilité complémentaire).
- **$f : \mathcal{E} \to G$** : additive sur disjoints (④) ; Poincaré généralisé à $(\Omega, \mathcal{E}, f)$.
- **$I \subseteq^* [\![1,n]\!]$** : $I \in \mathcal{P}([\![1,n]\!]) \setminus \{\emptyset\}$.
- **$!n$** : dérangements (application annoncée p.3) ; **$2^n-1$** : nombre de Mersenne (termes de la somme).
