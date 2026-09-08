# Intégrale de Dirichlet $\int_0^{+\infty}\frac{\sin x}{x}dx = \frac{\pi}{2}$ — transcription fidèle

> 🧾 **Manuscrit original :** `integrale-dirichlet.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible (~85 %), transcrit fidèlement. Calcul de $I(u) = \iint_{[0,u]^2}\sin x\, e^{-xy}dxdy$ par doubles IPP, puis double passage à la limite $u \to +\infty$ (critère d'Abel, majorations exponentielles, trinôme $1+y^2-y$). Crochets d'IPP partiellement raturés (signalés).
> 📄 **Source scannée :** [`integrale-dirichlet.pdf`](integrale-dirichlet.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — L'intégrale double $I(u)$ et le calcul de $I_y$

$$I(u) = \iint_{[0,u]^2} \sin x\, e^{-xy}\,dxdy$$

1/ $\int_0^u \frac{\sin x}{x}(1-e^{-xu})\,dx = \int_0^u \frac{1-e^{-uy}(\cos u+y\sin u)}{1+y^2}\,dy$

2/ $\int_0^{+\infty} \frac{\sin u}{u}\,du = ?$ [en marge : calculs « $e^{\dots}$ » — brouillon]

1/ $\int_0^u \frac{\sin x}{x}(1-e^{-xu})\,dx = -\int_0^u \left[\frac{\sin x}{x}e^{-xy}\right]_{y=0}^u dx$ [signe de tête peu lisible] $= \int_0^u \int_0^u \sin x\, e^{-xy}\,dxdy$

$I_y = \int_0^u \sin x\, e^{-xy}\,dx = $ [crochet raturé]

$= -\int_0^u \cos x\, e^{-xy}\,dx$ [ligne empâtée — le crochet d'IPP est partiellement raturé]

$= -\left[\cos x\, e^{-xy}\right]_0^u + \int_0^u \cos x\,(-y)e^{-xy}\,dx$

$= -\cos u\, e^{-uy} + 1 - y\int_0^u \sin x\, e^{-xy}\,dx$

$= 1 - \cos u\, e^{-uy} - y\left\{[\sin x\, e^{-xy}]_0^u - \int_0^u \sin x\,(-y)e^{-xy}\,dx\right\}$ [accolade et second membre sur deux lignes dans le manuscrit]

$= 1 - \cos u\, e^{-uy} - y\sin u\, e^{-uy} - y^2 I_y$

d'où $I_y = \frac{1}{1+y^2}\left(1-e^{-uy}(\cos u+y\sin u)\right)$

## Page 2 — Double passage à la limite

2/. Mtr $I(u) = \int_0^u \frac{\sin x}{x}\,dx - \int_0^u \frac{\sin x}{x}e^{-xu}\,dx \xrightarrow[u\to+\infty]{} \int_0^{+\infty} \frac{\sin x}{x}\,dx$

On a : $\int_0^u \frac{\sin x}{x}\,dx \xrightarrow[u\to+\infty]{} \int_0^{+\infty} \frac{\sin x}{x}\,dx \in \mathbb{R}$ d'après le critère d'Abel pour les IIS en $+\infty$ [« IIS » lu tel quel]

De plus $\left|\int_0^u \frac{\sin x}{x}e^{-xu}\,dx\right| \leq \int_0^u 1\times e^{-xu}\,dx$ [facteur « $1\times$ » levé visuellement p.2 r150 2026-09-07 (`/tmp/s9/dirichlet-2.png`)]

$$\underset{xu=t}{\leq} \frac{1}{u}\int_0^{u^2} e^{-t}\,dt \leq -\frac{1}{u}(e^{-u^2}-1) \xrightarrow[u\to+\infty]{} 0$$

. Mtr $I(u) = \int_0^u \frac{1-e^{-uy}(\cos u+y\sin u)}{1+y^2}\,dy \xrightarrow[u\to+\infty]{} \int_0^{+\infty} \frac{1}{1+y^2}\,dy$ [« cqfd » au-dessus de la flèche] $= \frac{\pi}{2}$

On a : $\int_0^u \frac{1}{1+y^2}\,dy \xrightarrow[u\to+\infty]{} \frac{\pi}{2}$

De plus $\underbrace{\left|\int_0^u \frac{e^{-uy}(\cos u+y\sin u)}{1+y^2}\,dy\right|}_{A} \leq \int_0^u \frac{e^{-uy}(|\cos u|+|y||\sin u|)}{1+y^2}\,dy$

$$\leq \int_0^u e^{-uy}\left(\frac{1}{1+y^2}+\frac{|y|}{1+y^2}\right)dy$$

or en posant $p(y) = 1+y^2-y$, $\Delta_p = -3 < 0$ d'où $p(y) \geq 0 \implies \frac{y}{1+y^2} \leq 1$

Ainsi $A \leq \int_0^u 2e^{-uy}\,dy \leq -\frac{2}{u}(e^{-u^2}-1) \xrightarrow[u\to+\infty]{} 0$ [d'après le 1er cas]

En définitive $\boxed{\lim_{u\to+\infty} I(u) = \int_0^{+\infty} \frac{\sin x}{x}\,dx = \pi/2}$ CQFD

---

## 📝 Notes de transcription (fidélité)

- Les deux IPP de la page 1 dérivent l'exponentielle ($u = e^{-xy}$, $dv = \sin x\,dx$ puis $dv = \cos x\,dx$), d'où les facteurs $-y$ puis $-y^2$ et la résultante $I_y = (1-e^{-uy}(\cos u+y\sin u))/(1+y^2)$.
- Page 2 : la majoration $\frac{|y|}{1+y^2} \leq 1$ (pour $y \geq 0$) vient de $1+y^2-y \geq 0$ (discriminant $-3$), ce qui ramène $A$ à $\int_0^u 2e^{-uy}dy$.
- Aucune figure ni schéma sur les 2 pages.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q04-dirichlet-1.png`, r150) — texte + équations, brouillon marginal « `e^…` » confirmé, aucune figure ; p. 2 vérifiée visuellement le 2026-09-07 (rendu `/tmp/s9/dirichlet-2.png`, r150, 2e passage) — double passage à la limite, « cqfd » au-dessus de la flèche, « d'après le 1er cas » et CQFD confirmés, aucune figure. Aucun script `reproduce_integrale-dirichlet_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- `Mtr` = montrer ; `IIS` = intégrale impropre ; `IPP` = intégration par parties (doubles, p. 1).
- Abel = critère de convergence des IIS en `+∞` ; `p(y) = 1+y²−y`, `Δ_p = −3` ; `cqfd`.
