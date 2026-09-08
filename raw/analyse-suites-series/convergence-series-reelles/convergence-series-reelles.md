# Convergence absolue et simple pour les séries réelles — transcription fidèle

> 🧾 **Manuscrit original :** `convergence-series-reelles.pdf` (scan, 1 page) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`convergence-series-reelles.pdf`](convergence-series-reelles.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/Convergence absolue et simple pour les series réelles.pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

### Critère de la cvge abs pour les séries réelles

Soit $\sum_{n \geq n_0} U_n$ une série réelle.

Théo : $\sum_{n \geq n_0} U_n$ cvge si $\sum_{n \geq n_0} |U_n|$ cvge ($\sum_{n \geq n_0} U_n$ cvge absolument).

En effet supposons que $\sum_{n \geq n_0} |U_n|$ cvge et mtq $\sum_{n \geq n_0} U_n$ cvge.

Soit $N \in \mathbb{N}\ (N \geq n_0)$. Posons $S_N = \sum_{n=n_0}^{N} U_n$, $AS_N = \sum_{n=n_0}^{N} |U_n|$, $S_{1N} = \sum_{\substack{n=n_0 \\ U_n \geq 0}}^{N} U_n$, $S_{2N} = \sum_{\substack{n=n_0 \\ U_n < 0}}^{N} U_n$. Ona : $S_{1N} + S_{2N} = S_N$.

De plus $\forall i \in \{1, 2\}$, $|S_{iN}| = \left|\sum_{\substack{n=n_0 \\ U_n \geq 0 \text{ ou } \leq 0 \text{ selon les cas}}}^{N} U_n\right| \leq \left|\sum_{n=n_0}^{N} U_n\right| \leq \sum_{n=n_0}^{N} |U_n| = AS_N$.

Or $\exists l \in \mathbb{R} \mid AS_N \xrightarrow[N \to +\infty]{} l$ et car $(AS_N)_{N \geq n_0}$ est croissante, $\forall N \in \mathbb{N}\ (N \geq n_0)$, $AS_N \leq l$. Ainsi $|S_{iN}| \leq l$.

Car $(S_{iN})_{N \geq n_0}$ est bornée et monotone (croissante pour $i = 1$ et décroissante pour $i = 2$) alors $(S_{iN})_{n \geq n_0}$ converge.

Donc $(S_N)_{N \geq n_0} = \sum_{i=1}^{2} (S_{iN})_{N \geq n_0}$ cvge.

## Figures

Aucune figure : 1 page de texte manuscrit seul, sans schéma ni graphe (transcription § Statut : page unique ; confirmé sur la page relue le 2026-09-07, rendu `/tmp/qas/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- cvge : converge ; mtq : montrons que ; Ona : on a ; Théo : théorème.
- $S_N$ : sommes partielles de $\sum U_n$ ; $AS_N$ : sommes partielles de $\sum |U_n|$ ; $S_{1N}$ ($U_n \ge 0$), $S_{2N}$ ($U_n < 0$).
- cvge absolument : $\sum |U_n|$ cvge.
