# Démonstration proposition TANKEU Donald — Puissance de p dans n! — transcription fidèle

> 🧾 **Manuscrit original :** `valuation-p-factorielle.pdf` (scan, 2 pages) · 📅 06/07/2020 · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Même démonstration (Legendre) que `legendre-factorielle.md`, ici en cadrage plus serré avec la seconde page en partie vierge (verso en transparence). Les maths sont conservées telles quelles. Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`valuation-p-factorielle.pdf`](valuation-p-factorielle.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Démonstration proposition de TANKEU Donald _ Puissance de p dans n!.pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

**Exercice :** démontrer que la plus grande puissance de $p$ dans $n!$ est $\sum_{k=1}^{E\left(\frac{\ln n}{\ln p}\right)} E\left(\frac{n}{p^k}\right)$ où $p$ est un nombre $1^{er} \mid p \leq n$.

Soit $E = \{k \in \mathbb{N}^* \mid p^k \leq n\}$. Ona : $p^1 \leq n \implies 1 \in E \implies E \neq \varnothing$. De plus $\forall k \in E,\ k \leq \frac{\ln n}{\ln p} \implies E$ est majoré par $\frac{\ln n}{\ln p}$. Alors $E$ admet un plus grand élément $m \in \mathbb{N}^*$.

$\forall k \in E$, soit $E_k^0 = \{k' \in \mathbb{N}^* \mid k'p^k \leq n\}$. Ona : $1 \times p^k \leq n \implies 1 \in E_k^0 \implies E_k^0 \neq \varnothing$. De plus $\forall k' \in E_k^0$, [raturé : $k'\ln p \leq \ln n$] $k' \leq \frac{n}{p^k} \implies E_k$ est majoré par $\frac{n}{p^k}$. Alors $E_k$ admet un plus grand élément $m_k^0 \in \mathbb{N}^*$.

Ainsi les ($m_k$ nombres) $1 \times p^k, \dots, m_k p^k$ sont les seuls multiples non nuls de $p^k$ inférieurs (ou égaux) à $n$ qui interviennent dans l'écriture $n! = 1 \times \dots \times n$.

Or $m_k p^k \leq n \implies n - m_k p^k \geq 0$. De plus $n - m_k p^k < p^k$ car sinon $n - m_k p^k \geq p^k \implies n \geq (m_k+1)p^k \implies m_k+1 \in E_k$. Absurde !

Ainsi $0 \leq n - m_k p^k < p^k \implies 0 \leq \frac{n}{p^k} - m_k < 1 \implies m_k \leq \frac{n}{p^k} < m_k+1 \implies m_k = E\left(\frac{n}{p^k}\right)$.

De même les ($m$ nombres) $p^1, \dots, p^m$ sont les (seules) puissances (non unitaires) de $p$ à intervenir dans l'écriture $n! = 1 \times \dots \times n$. Or $p^m \leq n < p^{m+1}$ car $m = \mathrm{Max}(E)$ [raturé au-dessus]. De plus c-à-d $m\ln p \leq \ln n < (m+1)\ln p$, c-à-d $m \leq \frac{\ln n}{\ln p} < m+1$, c-à-d $m = E\left(\frac{\ln n}{\ln p}\right)$.

---

## Page 2

Par suite dans la décomposition en produit de facteurs $1^{ers}$ de $n!$, $p$ interviendra :

- $m_1$ fois dû au(x) multiple(s) $1 \times p^1, \dots, m_1 \times p^1$ de $p^1$ ;
- $m_2$ fois dû au(x) multiple(s) $1 \times p^{2-1}, \dots, m_2 \times p^{2-1}$ de $p$ non pris dans les $m_1$ premiers autres ;
- $m_3$ fois dû au(x) multiple(s) $1 \times p^{3-2}, \dots, m_3 \times p^{3-2}$ de $p$ non pris dans les $m_1 + m_2$ premiers autres ;
- $\vdots$
- $m_{m-1}$ fois dû au(x) multiple(s) $1 \times p^{(m-1)-[(m-1)-1]}, \dots, m_3 \times p^{(m-1)-[(m-1)-1]}$ de $p$ non pris dans les $m_1 + \dots + m_{m-2}$ premiers autres [*sic* — indices recopiés tels quels] ;
- $m_m$ fois dû au(x) multiple(s) $1 \times p^{m-(m-1)}, \dots, m_m \times p^{m-(m-1)}$ de $p$ restants.

Ainsi la puissance totale qu'aura $p$ dans cette décomposition est $P_1 = \sum_{k=1}^{m} m_k = \sum_{k=1}^{E\left(\frac{\ln n}{\ln p}\right)} E\left(\frac{n}{p^k}\right)$.

[bas de page vierge — verso en transparence]

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée (même démonstration Legendre que `legendre-factorielle.md`, cadrage plus serré, pliure de cahier visible) ; p. 2 = suite textuelle + bas vierge. Aucun script `reproduce_valuation_p_factorielle_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $E(\cdot)$ = partie entière ; $Ona$ = on a ; $m = \mathrm{Max}(E)$, $m_k$ = cardinaux associés.
- $P_1$ = puissance totale de $p$ dans $n!$ ; « nombres $1^{ers}$ » = nombres premiers.
- Titre d'origine : « Démonstration proposition TANKEU Donald » (nom cité tel quel).
