# Crible de Poincaré — transcription fidèle

> 🧾 **Manuscrit original :** `crible-poincare.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`crible-poincare.pdf`](crible-poincare.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Soit $(\Omega, \mathcal{E}, P)$, un espace probabilisé. Soit $n \in \mathbb{N}^*$ et

$$P(n) : \forall (A_i)_{i=1}^n \in \mathcal{E}^n, P\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^n (-1)^{k-1} \sum_{1 \leq i_1 < \cdots < i_k \leq n} P\left(\bigcap_{j=1}^k A_{i_j}\right)$$

- Il est clair que $P(1)$ est vraie
- Mq $P(2)$ est vraie (ce sera utile dans la suite)

En effet : $P(A \cup B) = P\big(A \cup (B \setminus (A \cap B))\big) = P(A) + P(B \setminus (A \cap B))$ d'après le $3^{\text{e}}$ axiome de Kolmogorov vu que $A \cap (B \setminus (A \cap B)) = \emptyset$.

De plus car $(B \setminus (A \cap B)) \cap (A \cap B) = \emptyset$ on a de même

$$P\big((B \setminus (A \cap B)) \cap (A \cap B)\big) = P(B \setminus (A \cap B)) + P(A \cap B)$$

C-à-d $P(B) = P(B \setminus (A \cap B)) + P(A \cap B)$.

Donc $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ d'où $P(2)$ vraie.

- Soit $n \in \mathbb{N}$ ($n \geq 2$). Supposons $P(n)$ vraie et mq $P(n+1)$ l'est aussi. Posons $I_n = [\![1, n]\!] = \{1, \dots, n\}$.

Soient $(A_i)_{i=1}^{n+1} \in \mathcal{E}^{n+1}$. Remarquons tout d'abord que

$$\sum_{k=1}^n (-1)^{k-1} \sum_{1 \leq i_1 < \cdots < i_k \leq n} P\left(\bigcap_{j=1}^k A_{i_j}\right) = \sum_{k=1}^n (-1)^{k-1} \sum_{\substack{J \subseteq I_n \\ |J| = k}} P\left(\bigcap_{j \in J} A_j\right)$$

[flèche : tous sous les sous-ensembles à $k$ élts de $I_n$]

$$= \sum_{J \subseteq I_n} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right) = P\left(\bigcup_{i=1}^n A_i\right)$$

[tous les sous-ensembles possibles $\Rightarrow J \subseteq I_n$ de $I_n$]

## Page 2

En effet : $P\left(\bigcup_{i=1}^{n+1} A_{n+1}\right)$ [*sic* — lire $\bigcup_{i=1}^{n+1} A_i$] $= P\left(\left(\bigcup_{i=1}^n A_i\right) \cup A_{n+1}\right)$

$$= P\left(\bigcup_{i=1}^n A_i\right) + P(A_{n+1}) - P\left(\left(\bigcup_{i=1}^n A_i\right) \cap A_{n+1}\right) \text{ car } P(2) \text{ vraie}$$

$$= P(A_{n+1}) + \sum_{J \subseteq I_n} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right) - P\left(\bigcup_{i=1}^n (A_i \cap A_{n+1})\right) \text{ car } P(n) \text{ vraie}$$

[flèche verticale en marge droite remontant vers la ligne précédente]

$$= P(A_{n+1}) + \sum_{\substack{J \subseteq I_n \\ |J| = 1}} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right) + \sum_{\substack{J \subseteq I_n \\ |J| > 1}} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right)$$
$$- \sum_{J \subseteq I_n} (-1)^{|J|-1} P\left(\bigcap_{j \in J} (A_j \cap A_{n+1})\right) \text{ car [hypothèse } P(n) \text{ appliquée aux } A_i \cap A_{n+1} \text{]}$$

$$= \sum_{\substack{J \subseteq I_{n+1} \\ |J| = 1}} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right) + \sum_{\substack{J \subseteq I_{n+1} \\ |J| > 1 \\ n+1 \notin J}} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right)$$
$$- \left(\sum_{J \subseteq I_n} (-1)^{|J|-1} P\left(\left(\bigcap_{j \in J} A_j\right) \cap A_{n+1}\right)\right) \to \alpha$$

[le dernier terme entre parenthèses est entouré d'une ellipse]

$$\alpha = \sum_{\substack{J' \subseteq I_{n+1} \\ n+1 \in J'}} (-1)^{(|J'|-1)-1} P\left(\bigcap_{j \in J'} A_j\right) = -\sum_{\substack{J' \subseteq I_{n+1} \\ n+1 \in J'}} (-1)^{|J'|-1} P\left(\bigcap_{j \in J'} A_j\right)$$

[$J' = J \cup \{n+1\}$]

d'où $P\left(\bigcup_{i=1}^{n+1} A_{n+1}\right)$ [*sic* — lire $A_i$] $= \sum_{\substack{J \subseteq I_{n+1} \\ |J| = 1}} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right) + \sum_{\substack{J \subseteq I_{n+1} \\ |J| \geq 2 \\ n+1 \notin J}} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right)$

$$+ \sum_{\substack{J \subseteq I_{n+1} \\ n+1 \in J}} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right)$$

$$= \sum_{J \subseteq I_{n+1}} (-1)^{|J|-1} P\left(\bigcap_{j \in J} A_j\right) \text{ d'où } P(n+1) \text{ est vraie}$$

CQFD

---

## Figures

Aucune figure sur les 2 pages relues (N == pdfinfo) : démonstration seule ; les flèches marginales et l'ellipse entourant $\alpha$ (p.1–2) sont des annotations, pas des figures. P. 2 vérifiée visuellement au 2e passage le 2026-09-07 (rendu `/tmp/s9/crible-2.png`, r150) — les deux *sic* $\bigcup_{i=1}^{n+1} A_{n+1}$ (lire $A_i$) confirmés, $\alpha$ + $J' = J \cup \{n+1\}$ + CQFD confirmés.

## Vocabulaire

- **Espace probabilisé** : $(\Omega, \mathcal{E}, P)$.
- **$3^e$ axiome de Kolmogorov** : additivité sur disjoints.
- **$P(n)$** : formule du crible à $n$ ensembles ; $I_n = [\![1,n]\!]$.
- **Mq** : « montrer que ».
