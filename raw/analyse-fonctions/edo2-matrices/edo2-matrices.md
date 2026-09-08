# EDO2 via matrices (exponentielle de matrice) — transcription fidèle

> 🧾 **Manuscrit original :** `edo2-matrices.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible (~90 %), transcrit fidèlement. Résolution de $y'' - 3y' + 2y = 0$ via $Y' = AY$ et $e^{At}$. Bas de page 1 très chargé (signes peu lisibles, signalés).
> 📄 **Source scannée :** [`edo2-matrices.pdf`](edo2-matrices.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Mise sous forme $Y' = AY$, éléments propres, $A^k$

$$y'' - 3y' + 2y = 0 \iff Y' = \begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix} Y \text{ où } Y = \begin{pmatrix} y' \\ y \end{pmatrix}$$

$$\iff Y = e^{\begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix}t} Y_0 \quad Y_0 = \begin{pmatrix} y'(0) \\ y(0) \end{pmatrix}$$

$$e^{\begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix}t} = \sum_{k=0}^{\infty} \frac{\begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix}^k t^k}{k!}$$

$$A = \begin{pmatrix} 3 & -2 \\ 1 & 0 \end{pmatrix} \quad P_A(\lambda) = \begin{vmatrix} 3-\lambda & -2 \\ 1 & -\lambda \end{vmatrix} = \lambda^2 - 3\lambda + 2$$

$$P_A(\lambda) = 0 \iff \lambda = 1 \text{ ou } \lambda = 2$$

. $E_1 =$ ? Soit $u = (x, y) \in \mathbb{R}^2$. $u \in E_1 \iff \begin{pmatrix} 2 & -2 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$

$$\iff x = y$$

D'où $E_1 = \langle (1, 1) \rangle$

. $\lambda = 2$ : Soit $u = (x, y) \in \mathbb{R}^2$. $u \in E_2 \iff \begin{pmatrix} 1 & -2 \\ 1 & -2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$

$$\iff x = 2y$$

D'où $E_2 = \langle (2, 1) \rangle$

Il vient que $A = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}^{-1}$

$\forall k \in \mathbb{N}$, $A^k = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & 2^k \end{pmatrix}\begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$ [le manuscrit fait précéder d'un signe biffé ; la dernière matrice est l'inverse de la première, lue telle quelle]

$$= \begin{pmatrix} 1 & 2^{k+1} \\ 1 & 2^k \end{pmatrix}\begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$$

$$A^k = \begin{pmatrix} 2^{k+1}-1 & 2-2^{k+1} \\ 2^k-1 & 2-2^k \end{pmatrix} \text{ [lecture incertaine sur les signes du bas de page — le premier coefficient est lu « } 2^{k+1}-1 \text{ » d'après le calcul, l'encre étant empâtée]}$$

## Page 2 — Exponentielle $e^{At}$ et solution $y(t)$

Alors $e^{At} = \sum_{k=0}^{\infty} \frac{t^k}{k!}\begin{pmatrix} 2^{k+1}-1 & 2-2^{k+1} \\ 2^k-1 & 2-2^k \end{pmatrix}$ [mêmes réserves de lecture qu'en page 1 pour les signes]

$$= \begin{pmatrix} \sum_{k=0}^{\infty}\frac{t^k}{k!}(2^{k+1}-1) & \sum_{k=0}^{\infty}\frac{t^k}{k!}(2-2^{k+1}) \\ \sum_{k=0}^{\infty}\frac{t^k}{k!}(2^k-1) & \sum_{k=0}^{\infty}\frac{t^k}{k!}(2-2^k) \end{pmatrix}$$

$$= \begin{pmatrix} 2e^{2t}-e^t & 2e^t-2e^{2t} \\ e^{2t}-e^t & 2e^t-e^{2t} \end{pmatrix}$$

D'où $Y(t) = \begin{pmatrix} y'(t) \\ y(t) \end{pmatrix} =$ [colonne $\begin{pmatrix} y \\ y' \end{pmatrix}$ raturée avant la matrice] $\begin{pmatrix} 2e^{2t}-e^t & 2e^t-2e^{2t} \\ e^{2t}-e^t & 2e^t-e^{2t} \end{pmatrix}\begin{pmatrix} y'(0) \\ y(0) \end{pmatrix}$

$$= \begin{pmatrix} e^{2t}(2y'(0)-2y_0) + e^t(-y'_0+2y_0) \\ e^{2t}(y'_0-y_0) + e^t(-y'_0+2y_0) \end{pmatrix} \quad [y_0 = y(0),\; y'_0 = y'(0)]$$

D'où $y(t) = \underbrace{(y'_0-y_0)}_{A}e^{2t} + e^t\underbrace{(2y_0-y'_0)}_{B}$

---

## Figures

- Aucune figure sur les 2 pages (vérifié p. 1–2, document complet).

## Vocabulaire

EDO2, $Y'=AY$, exponentielle de matrice $e^{At}$, polynôme caractéristique $P_A$, sous-espaces propres $E_1$/$E_2$, $y_0$/$y'_0$.

## 📝 Notes de transcription (fidélité)

- Le manuscrit note $P_A(\lambda)$ le polynôme caractéristique et $E_1$, $E_2$ les sous-espaces propres associés à $\lambda = 1$ et $\lambda = 2$.
- Page 1, bas : l'expression de $A^k$ est empâtée ; les signes ont été restitués d'après le calcul intermédiaire $\begin{pmatrix} 1 & 2^{k+1} \\ 1 & 2^k \end{pmatrix}\begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$ qui, lui, est net.
- Page 2 : une colonne $\begin{pmatrix} y \\ y' \end{pmatrix}$ placée avant la matrice $e^{At}$ a été raturée par l'auteur (ordre $y', y$ rétabli dans la version finale).
- Aucune figure ni schéma sur les 2 pages.
