# Un K-ev sur un corps infini non dénombrable n'est pas réunion dénombrable de sev — transcription fidèle

> 🧾 **Manuscrit original :** `ev-reunion-denombrable.pdf` (scan, 1 page) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`ev-reunion-denombrable.pdf`](ev-reunion-denombrable.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Écriture impossible d_un ev cœur réunion dénombrable de sev.pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

### Théo : un $\mathbb{K}$-ev $(E, +, \cdot)$ où $\mathbb{K}$ est infini non dénombrable [*sic* — le manuscrit porte « où $\mathbb{K}$ n'est pas dénombra[ble] et infini non dénombrable », formule redondante conservée en ce sens] ne peut s'écrire comme réunion d'un nbre dénombrable de sev

Supposons par l'absurde $\exists (E_i)_{i \in \mathbb{N}} \equiv$ sev de $E \mid E = \bigcup_{i \in \mathbb{N}} E_i$.

Quitte à extraire de $\bigcup_{i \in \mathbb{N}} E_i$ les $E_j \mid E_j \subset \bigcup_{i \in \mathbb{N}, i \neq j} E_i$, supposons que $\forall j \in \mathbb{N},\ E_j \setminus \bigcup_{i \in \mathbb{N}, i \neq j} E_i \neq \varnothing$.

Soient $(x_0, x_1, \lambda) \in (E_0 \setminus \bigcup_{i \in \mathbb{N}^*} E_i) \times (E_1 \setminus \bigcup_{i \in \mathbb{N}, i \neq 1} E_i) \times \mathbb{K}$.

Posons $x(\lambda) = x_0 + \lambda x_1$ et considérons $F = \{x(\lambda),\ \lambda \in \mathbb{K}^*\}$.

Il est clair que $\forall \lambda \in \mathbb{K}^*,\ x(\lambda) \notin E_0$ ni $E_1$ d'où $x(\lambda) \in \bigcup_{i \geq 2} E_i$, car $x_0 \notin E_1$ et $x_1 \notin E_0$.

Considérons $f : \lambda \in \mathbb{K}^* \longmapsto E(\lambda)$ qui est l'indice tel que $x(\lambda) \in E(\lambda)$. Montrons $f$ est injective. Soit $\lambda_1, \lambda_2 \in \mathbb{K}^* \mid \lambda_1 \neq \lambda_2$. Supposons par l'absurde que $E(\lambda_1) = E(\lambda_2)$.

On a : $x_0 + \lambda_1 x_1,\ x_0 + \lambda_2 x_1 \in E(\lambda)$ d'où $x_1 = \dfrac{x(\lambda_1) - x(\lambda_2)}{\lambda_1 - \lambda_2} \in E(\lambda)$, ce qui est absurde, car que $x_1 \in E_1 \setminus \bigcup_{i \in \mathbb{N}, i \neq 1} E_i \implies x_1 \notin E(\lambda)$.

D'où $E(\lambda_1) \neq E(\lambda_2)$ et donc $f$ est injective.

Par conséquent, $\mathbb{K}^*$ est équipotent en terme de cardinal à un sous-ensemble de $E_{i, i \geq 2}$ et donc à un sous-ensemble de $\mathbb{N}$ d'où $\mathbb{K}^*$ est au plus dénombrable, ce qui est absurde ! CQFD.

---

## Figures

Aucune figure à reproduire : 1 page texte, relue en entier, sans schéma.

## Vocabulaire / notions

- **$\mathbb{K}$-ev**, **sev** $E_i$ ; **réunion dénombrable** $\bigcup_{i \in \mathbb{N}} E_i$.
- **Extraction** des $E_j \subset \bigcup_{i \neq j} E_i$ ; droite $x(\lambda) = x_0 + \lambda x_1$.
- **Injection** $f : \lambda \mapsto E(\lambda)$ ; **équipotence**, **au plus dénombrable**.
