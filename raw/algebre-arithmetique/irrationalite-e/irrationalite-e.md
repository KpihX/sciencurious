# e est irrationnel — transcription fidèle

> 🧾 **Manuscrit original :** `irrationalite-e.pdf` (scan, 1 page) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`irrationalite-e.pdf`](irrationalite-e.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/e est irrationnel .pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

### Théo : $e$ est irrationnel

En effet il suffit de montrer que $\forall n \in \mathbb{N}^*,\ n!e \notin \mathbb{Z}$.

L'idée serait de tenter d'exploiter la relation $e = \sum_{k=0}^{+\infty} \frac{1}{k!}$ et ainsi de montrer que $\forall n \in \mathbb{N}^*,\ n!e \notin \mathbb{Z}$ ce qui serait suffisant car si par l'absurde $\exists (p, q) \in \mathbb{Z} \times \mathbb{N}^* \mid e = p/q$ on aurait $q!e = p(q-1)! \implies q!e \in \mathbb{Z}$ ce qui serait absurde !

Soit alors $n \in \mathbb{N}^*$, mq $n!e \notin \mathbb{Z}$.

On a : $n!e = x + y$ où $x = \sum_{k=0}^{n} \frac{n!}{k!} = \sum_{k=0}^{n} A_k \in \mathbb{N}$ et $y = \sum_{k=n+1}^{+\infty} \frac{n!}{k!} = \sum_{k=n+1}^{+\infty} \frac{1}{A_k}$.

D'où $0 < y < \sum_{k=n+1}^{+\infty} \frac{1}{(n+1)^{k-n}} = \frac{1}{n+1} \times \frac{1}{1 - \frac{1}{n+1}}$ car $0 < \frac{1}{n+1} \leq 1$ [*sic* — le manuscrit porte « car $0 < \frac{1}{n+1} \leq 1$ » (lu possiblement $n+2$, écriture ambiguë), l'encadrement fin est $= \frac{1}{n} \leq 1$].

$$= \frac{1}{n} \leq 1$$

Ainsi $x \in \mathbb{N}$ et $y \in {]0, 1[}$ d'où $n!e = x + y \notin \mathbb{Z}$. CQFD.

---

## Figures

Aucune figure à reproduire : 1 page texte, relue en entier, sans schéma.

## Vocabulaire / notions

- **Série** $e = \sum_{k=0}^{+\infty} 1/k!$ ; **factorielle** $n!$, $A_k = n!/k!$.
- **Découpage** $n!e = x + y$ : $x \in \mathbb{N}$, $y \in {]0, 1[}$ (série géométrique majorante $1/n \leq 1$).
