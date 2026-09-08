# Cardinal de P(N) — transcription fidèle

> 🧾 **Manuscrit original :** `cardinal-parties-n.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** bijection $]0,1[ \leftrightarrow \mathcal{P}(\mathbb{N})$ par écriture binaire ; amorce et notations d'écritures en `[lecture incertaine — …]`. Transcrit mot à mot.
> 📄 **Source scannée :** [cardinal-parties-n.pdf](cardinal-parties-n.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Pourquoi $\aleph_1 = 2^{\aleph_0}$ [lecture incertaine — amorce « $\aleph_1 = 2^{\ldots}$ » peu lisible en haut du scan p.1 re-rendue à $r = 150$ (relue 2026-09-07) : le « $X_1$ » se lit comme $\aleph_1$ (hypothèse du continu en motivation), pas comme $|\mathcal{P}(\mathbb{N})|$]. $|\ldots| = |]0,1[|$ : construisons une bijection $f$ entre $]0,1[$ et l'ensemble des parties de $\mathbb{N}$.

Considérons d'abord la bijection $g$ entre les écritures $x^{10}$ et $x^2$, $x \in ]0,1[$ [lecture incertaine — exposants, lus comme écritures décimale (base 10) et binaire (base 2)] : $g$ associe à chaque réel $x \in ]0,1[$ donné en écriture décimale ce même réel $x$ donné en écriture binaire. C'est le changement de base $10 \to 2$ sur $]0,1[$, bijectif une fois fixée la convention d'écriture pour les dyadiques (voir note page 2).

Ensuite, à chaque $x$ pris en base 2, donc de la forme $x_{(2)} = 0,10100101\ldots$ [lecture incertaine — noté « $x^2$ » sur le scan, lu comme $x$ en base 2] [raturé : chiffres sous l'écriture — suite de petits chiffres (numérotation des positions) sous l'écriture binaire, illisibles à cette résolution], on le parcourt à partir du $1^{\text{er}}$ chiffre après la virgule de la gauche vers la droite.

Soit $q_n$ la $n$-ième décimale (binaire) ainsi parcourue : si $q_n = 0$, le sous-ensemble $A$ de $\mathbb{N}$ associé ne contient pas l'entier $n$ ; si $q_n = 1$, alors $n \in A$. C'est la correspondance $h$ entre écritures binaires de $]0,1[$ et parties de $\mathbb{N}$.

Ainsi $0,0101$ correspond de façon univoque au sous-ensemble de $\mathbb{N}$ égal à $\{1,3\}$ (les positions des $1$), et $0,111111$ correspond à $\{0,1,2,3,\ldots\} = \mathbb{N}$.

## Page 2

[raturé : « Il est clair que » en tête de page, biffé sur le scan] Pour $\{0,3,7,10\}$, le réel de $]0,1[$ associé est $x_{(2)} = 0,0001000100000001$ [chaîne confirmée p.2 r150 2026-09-07 (`/tmp/s9/cardinal-2.png`), 16 décimales ; *sic* — les $1$ lus sont en positions 3, 7, 15 (index 0), ce qui ne colle pas à $\{0,3,7,10\}$ selon la règle des $q_n$ : conservée telle quelle].

Résidu p.2 vérifié à $r = 150$ : aucune marge additionnelle exploitable (bord gauche coupé, seule la rature initiale déborde), aucun schéma ni figure sur la page, aucune mention marginale des cas dyadiques.

Il est clair que la correspondance $h$ ainsi construite (écriture binaire $\mapsto$ partie de $\mathbb{N}$ par la règle des $q_n$) est bien biunivoque : deux réels distincts diffèrent en au moins une décimale binaire, donc en l'appartenance d'au moins un entier ; et toute partie de $\mathbb{N}$ définit par sa fonction caractéristique une unique écriture binaire.

Prendre alors $f = h \circ g$ : $g$ (changement de base décimal $\to$ binaire sur $]0,1[$) suivie de $h$ (écriture binaire $\to$ partie de $\mathbb{N}$) donne la bijection cherchée entre $]0,1[$ et $\mathcal{P}(\mathbb{N})$.

> ⚠️ **Note — doubles écritures dyadiques :** le manuscrit ne traite pas explicitement le cas des réels admettant deux écritures binaires (par ex. $0,0111\ldots_{(2)} = 0,1000\ldots_{(2)}$) ; la bijectivité stricte de $g$ et de $h$ suppose une convention d'écriture fixée (par ex. exclure les écritures se terminant par une infinité de $1$), non précisée sur le scan.

> 🔎 **Relecture :** pages 1–2 re-rendues (`pdftoppm -png -r 150 -f 1 -l 2`), exemples et ratures relus ; $g$ explicitée ci-dessus comme décimal $\to$ binaire.

---

## Figures

Aucune figure sur les 2 pages relues (N == pdfinfo) : texte et exemples d'écritures binaires seuls, sans schéma ni tableau. P. 2 vérifiée visuellement au 2e passage le 2026-09-07 (rendu `/tmp/s9/cardinal-2.png`, r150) — rature « Il est clair que », bitstring `0,0001000100000001` + *sic* positions confirmés, $f = h \circ g$ confirmé.

## Vocabulaire

- **$2^{\aleph_0}$** : cardinal de $\mathcal{P}(\mathbb{N})$.
- **$g$ (changement de base)** : décimal $\to$ binaire sur $]0,1[$, à convention dyadique fixée.
- **$h$ (fonction caractéristique)** : écriture binaire $\mapsto$ partie de $\mathbb{N}$ par la règle des $q_n$.
- **Dyadique** : réel admettant deux écritures binaires (convention excluant les queues infinies de $1$).
