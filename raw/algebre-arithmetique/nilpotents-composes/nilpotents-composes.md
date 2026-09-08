# Nullité de la composition de n endomorphismes nilpotents — transcription fidèle

> 🧾 **Manuscrit original :** `nilpotents-composes.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** transcrit mot à mot depuis les rendus. Les maths sont conservées telles quelles ;
> les passages raturés ou elliptiques sont signalés. Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`nilpotents-composes.pdf`](nilpotents-composes.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Nullité de la composition de n endomorphismes nilpotents.pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

[cartouche en haut : « 2439 » — lecture incertaine]

En étudiant le cas $n = 2$, on obtient $u_2 = 0_{L(E)}$. Montrons plus généralement que $u_n^2 \dots \circ u_n = 0_{L(E)}$ [formule d'objectif partiellement illisible — lue telle quelle].

Pour cela montrons que $\mathrm{Ker}\,u_5 = E$ [indice lu tel quel — probablement $\mathrm{Ker}\,u_n$].

Il suffira de mq $\forall k \in [\![2; n]\!]$, $\mathrm{Ker}\,u_{k-2} \subsetneq \mathrm{Ker}\,u_k$ et ($\forall k \in [\![2; n]\!]$, $\mathrm{Ker}\,u_k \neq \{0_E\}$) et [raturé : « ne que … car »] car $\dim\mathrm{Ker}\,u_n \geq 1 + \dim\mathrm{Ker}\,u_{n-2} \geq \dots \geq n-2 + \dim\mathrm{Ker}\,u_2 \geq n-2+1 = n$. D'où $\mathrm{Ker}\,u_n = E$.

- Soit $k \in [\![2; n]\!]$. Mq $\mathrm{Ker}\,u_k \neq \{0_E\}$. Supp par l'absurde que $\mathrm{Ker}\,u_k = \{0_E\}$. Ainsi $\forall x \in E \setminus \{0_E\}$, $u_k(x) \neq 0_E$. Or $u_k$ est nilpotent d'où $\exists m \in \mathbb{N}^* \mid u_k^m = 0_{L(E)}$. Il vient que $u_k^m(x) = 0_E$. Or $x \neq 0_E \implies u_k(x) \neq 0_E \implies u_k \circ u_k(x) \neq 0_E \implies \dots \implies u_k^m(x) \neq 0_E$. [!] D'où $\mathrm{Ker}\,u_k \neq \{0_E\}$.

---

## Page 2

Soit $k \in [\![2; n]\!]$. Mq $\mathrm{Ker}\,u_{k-2} \subsetneq \mathrm{Ker}\,u_k$.

Ona : $u_k = u_k \circ u_{k-2}$. Ainsi $\forall x \in \mathrm{Ker}\,u_{k-2}$, $u_k(x) = u_k(0_E) = 0_E \implies \mathrm{Ker}\,u_{k-2} \subset \mathrm{Ker}\,u_k$.

De plus $\mathrm{Ker}\,u_k =$ [raturé] $= u_{k-2}^{-1}(\mathrm{Ker}\,u_k)$ [membre de gauche raturé puis réécrit].

Supposons par l'absurde que $\mathrm{Ker}\,u_k = \mathrm{Ker}\,u_{k-2}$. Ona : $\mathrm{Ker}\,u_{k-2} = u_k^{-1}(\mathrm{Ker}\,u_{k-2}) = u_{k-2}^{-1}(\mathrm{Ker}\,u_k)$ [lue telle quelle]. D'où $u_{k-2}^{-1}(\mathrm{Ker}\,u_{k-2}) = \mathrm{Ker}\,u_k$, c-à-d $\{0_E\} = \mathrm{Ker}\,u_k$. Absurde ! CQFD.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée (texte + équations sur papier quadrillé, cartouche « 2439 » en haut) ; p. 2 = suite textuelle d'après la transcription. Aucun script `reproduce_nilpotents_composes_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $\mathrm{Ker}\,u_k$ = noyau ; $0_{L(E)}$, $0_E$ = endomorphisme/vecteur nuls ; $u_k^m$ = itérée $m$-ième.
- $Mq$ = montrons que ; $Ona$ = on a ; $Supp$ = supposons ; $\subsetneq$ = inclusion stricte.
