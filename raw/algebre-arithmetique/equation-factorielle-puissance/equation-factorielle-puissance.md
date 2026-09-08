# Eqn avec fac et puissance — transcription fidèle

> 🧾 **Manuscrit original :** `equation-factorielle-puissance.pdf` (2 pages : 1 carte-titre + 1 page de résolution) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`equation-factorielle-puissance.pdf`](equation-factorielle-puissance.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Eqn avec fac et puissance.pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

$$n! + n = n^n$$

[carte-titre sur fond marbré]

---

## Page 2

$(E_n)$ : $n! + n = n^n$. Contre-exemple : $n \neq 0$ disons $n \in \mathbb{N}^*$ [lecture incertaine sur le mot d'introduction].

$(E_{n0}) \iff (n-1)! + 1 = n^{n-1}$.

- Mq par récurrence que $P(n)$ : $\forall n \geq 3,\ (n-1)! + 1 < n^{n-1}$.
  - Pour $n = 3$, $(3-1)! + 1 = 3 < 9 = 3^{3-1}$. D'où $P(3)$ vraie.
  - Hérédité : $((n+1)-1)! + 1 = n(n-1)! + 1$. Or $(n-1)! + 1 \leq n^{n-1} \implies (n-1)! \leq n^{n-1} - 1$. Ainsi $((n+1)-1)! + 1 \leq n(n^{n-1} - 1) + 1 < n^n - n + 1 < n^n$ car $-n + 1 < 0 < (n+1)^n$. D'où $((n+1)-1)! + 1 < (n+1)^{n+1-1}$. Ainsi $P(n+1)$ vraie.
  - D'où $\forall n \geq 3,\ (n-1)! + 1 < n^{n-1}$.

Ainsi :
- Pour $n \geq 3$, $(n-1)! + 1 \neq n^{n-1} \implies S = \varnothing$.
- Pour $n = 1$, $(1-1)! + 1 \neq 1^{1-1} \implies S = \varnothing$.
- Pour $n = 2$, $(2-1)! + 1 = 2^{2-1} \implies S = \{2\}$.

Donc $S_{\mathbb{N}} = \{2\}$.

---

## Figures

Aucune figure manuscrite à reproduire : page 1 relue = carte-titre typographique « $n! + n = n^n$ » (fond marbré, pas un schéma) ; page 2 relue = résolution texte. Dossier relu en entier (2 pages).

## Vocabulaire / notions

- **Équation $(E_n)$** : $n! + n = n^n$ ; **réduite $(E_{n0})$** : $(n-1)! + 1 = n^{n-1}$.
- **Récurrence $P(n)$** : $\forall n \geq 3,\ (n-1)! + 1 < n^{n-1}$.
- **Ensemble solution** $S_{\mathbb{N}} = \{2\}$ ($S = \varnothing$ pour $n = 1$ et $n \geq 3$).
