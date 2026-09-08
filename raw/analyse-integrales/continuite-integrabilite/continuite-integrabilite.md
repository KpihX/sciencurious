# Continuité et intégrabilité (Riemann) — transcription fidèle

> 🧾 **Manuscrit original :** `continuite-integrabilite.pdf` (scan, 3 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à ~90 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`continuite-integrabilite.pdf`](continuite-integrabilite.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Théo : Soit $f$ une fonction continue sur $I = [a, b]$. Alors $f$ est intégrable au sens de Riemann sur $[a, b]$ et $\forall x_0 \in I$, $F(x) = \int_{x_0}^x f(t)\,dt$ ($\forall x \in [a, b]$) est continue et dérivable sur $I$ avec $\forall x \in I$, $F'(x) = f(x)$.

En effet, supposons qu'on ait une fct° $f$ continue sur $I = [a, b]$.

$*$ Mtq $f$ est intégrable au sens de Riemann. Soit $\varepsilon > 0$. Cherchons 2 fonctions définies en escalier sur $[a, b]$ $f_g$ et $f_d$ / $\forall x \in [a, b]$, $f_g(x) \leq f(x) \leq f_d(x)$ et $\int_a^b (f_d(t) + f_g(t))\,dt < \varepsilon$ [*sic* — lire $f_d - f_g$, cf. page 2] (2).

[raturé : Prenons $n = E(\varepsilon) + 2$. Pour avoir (2) il suffit d'avoir $\frac{1}{n}\int (f_d(t) - f_g(t))\,dt < \varepsilon/n$.]

Soit $n \in \mathbb{N}^*$. Considérons la subdivision de $I$ : $(x_i)$ : $x_i = a + \frac{b-a}{n} \times i$, $0 \leq i \leq n$ et les fonctions $g_n$ : $\forall t \in I$, $g_n(t) = \min\{f(x_i), f(x_{i+1})\}$ pour $t \in [x_i ; x_{i+1}[$ ; $h_n$ : $\forall t \in I$, $h_n(t) = \max\{f(x_i), f(x_{i+1})\}$ pour $t \in [x_i ; x_{i+1}]$. Ainsi $\forall t \in I$, $g_n(t) \leq f(t) \leq h_n(t)$.

## Page 2

Cherchons alors $n$ pour réaliser ② et il suffira de prendre $f_g = g_n$ et $f_d = h_n$.

On a : $\underbrace{\int_a^b (h_n(t) - g_n(t))\,dt}_{J} = \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} (h_n(t) - g_n(t))\,dt = \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} |f(x_{i+1}) - f(x_i)|\,dt$

vu que $\forall a, b \in \mathbb{R}$, $\max(a, b) = \frac{a+b+|a-b|}{2}$ et $\min(a, b) = \frac{a+b-|a-b|}{2}$, ainsi $J = \sum_{i=0}^{n-1} |f(x_{i+1}) - f(x_i)| \times \frac{b-a}{n}$.

Car $f$ est continue sur $I$ qui est un compact de $\mathbb{R}$ alors $f$ y est [raturé : unifo] uniformément continue, ainsi [raturé : car $\varepsilon > 0$, $\exists N_2 \in \mathbb{N} \mid \forall n \in \mathbb{N}$, $n > N_2 \cdots$] car $\frac{\varepsilon}{b-a} > 0$ $\exists \eta_2 > 0 \mid$ [D'après le théo de Heine — mention marginale] $\forall x, y \in I$, $|x - y| < \eta_2 \Rightarrow |f(x) - f(y)| < \frac{\varepsilon}{b-a}$.

Soit $i \in [\![0, n-1]\!]$. Prenons $|x_{i+1} - x_i| < \eta_2 \iff \frac{b-a}{n} < \eta_2 \iff n > \frac{b-a}{\eta_2}$. Ainsi en prenant $n = E\left(\frac{b-a}{\eta_2}\right) + 2$, on a : $|f(x_{i+1}) - f(x_i)| < \frac{\varepsilon}{b-a}$. Alors $J < \sum_{i=0}^{n-1} \frac{\varepsilon}{b-a} \times \frac{b-a}{n} = \varepsilon$. Il suffit alors de prendre $f_g = g_n$ et $f_d = h_n$.

## Page 3

$*$ Mtq $\forall x_0 \in I$, $F_0$ : $x \in I$, $F_0(x) = \int_{x_0}^x f(t)\,dt$ est continue sur $I$. Soit $x_0 \in I$. Mtq $F_0$ est continue en $x_0$.

Soit $\varepsilon > 0$. Cherchons $\eta_3 > 0 \mid \forall x \in I$, $|x - x_0| < \eta_3 \Rightarrow |F_0(x) - F_0(x_0)| < \varepsilon$.

$\forall x \in I$, $|F_0(x) - F_0(x_0)| = \left|\int_{x_0}^x f(t)\,dt\right| \leq \int_{\min(x_0,x)}^{\max(x_0,x)} |f(t)|\,dt$.

- Si $f(x_0) \geq 0$. Car $1 > 0$ et $f$ continue en $x_0$, $\exists \eta' > 0 \mid \forall y \in I$, $|x - y| < \eta' \Rightarrow |f(y) - f(x_0)| < 1$ [lecture incertaine — borne lue d'après le contexte]. Posons $\eta'' = \min\left(\eta', \frac{\varepsilon}{1+f(x_0)}\right) \{> 0\}$. Soit $x_* \in I \mid |x - x_0| < \eta''$. Fixons $t$ entre $x$ et $x_0$. On a : $-1 + f(x_0) < f(t) < 1 + f(x_0) \Rightarrow |f(t)| < 1 + f(x_0)$. D'où $|F_0(x) - F_0(x_0)| < (1 + f(x_0))|x - x_0| < (1 + f(x_0)) \times \frac{\varepsilon}{1+f(x_0)} = \varepsilon$. Prendre $\eta_3 = \eta''$.

- Si $f(x_0) < 0$. Comme $-\frac{f(x_0)}{2} > 0$, $\exists \eta' > 0 \mid \forall y \in I$, $|x_0 - y| < \eta' \Rightarrow |f(y) - f(x_0)| < -\frac{f(x_0)}{2}$. Posons $\eta'' = \min\left\{\eta', \frac{\varepsilon}{5|f(x_0)|}\right\}$ [lecture incertaine sur le dénominateur — lu $\frac{\varepsilon}{5|f(x_0)|}$]. Soit $x_* \in I \mid |x - x_0| < \eta''$. Fixons $t$ entre $x$ et $x_0$. On a : $\frac{f(x_0)}{2} < f(t) < -\frac{f(x_0)}{2} \Rightarrow |f(t)| < \frac{5}{2}|f(x_0)|$ [*sic* — borne conservée telle que lue] $\Rightarrow |F_0(x) - F_0(x_0)| \leq \frac{5}{2}|f(x_0)||x - x_0| \leq \varepsilon$.

> ✅ Vérifié complet le 2026-09-07 (contrôle visuel p.2-3 : mention Heine en marge, dénominateur incertain conservé tel que lu, aucune figure ni marge omise).

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q01-continuite-1.png`, r150) — texte + équations, rature confirmée, aucune figure ; pp. 2–3 revérifiées visuellement au second passage le 2026-09-07 (rendus `/tmp/s8/cont-2.png` et `/tmp/s8/cont-3.png`, r150) — mention marginale Heine, équations, aucune figure. Aucun script `reproduce_continuite-integrabilite_N.py`, aucun PNG (aucun `assets/` créé, vérifié `uv run`).

---

## Vocabulaire

- `Mtq` = montrons que ; `fct°` = fonction ; `E(·)` = partie entière ; `Théo` = théorème.
- Heine = continuité uniforme sur compact ; encadrement par fonctions en escalier `f_g ≤ f ≤ f_d` ; `[*sic*]` = coquille conservée (`f_d − f_g` attendue p. 1).
