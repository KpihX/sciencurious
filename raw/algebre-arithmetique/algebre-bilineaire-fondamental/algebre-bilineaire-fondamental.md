# Algèbre bilinéaire fondamental — transcription fidèle

> 🧾 **Manuscrit original :** `algebre-bilineaire-fondamental.pdf` (scan, 3 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à ~95 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`algebre-bilineaire-fondamental.pdf`](algebre-bilineaire-fondamental.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

[En haut, fragment d'une autre feuille visible par transparence/chevauchement, non transcrit.]

Théo : Soit $E$ un $\mathbb{K}$-ev, $n \in \mathbb{N}^*$ ; $P(n)$ : $\forall (f_i)_n$, $f_i \in (E^*)^{n+1}$ [lecture incertaine — probablement $(f_i)_{1 \leq i \leq n} \in (E^*)^n$, $f \in E^*$]

$$
\bigcap_{i=1}^n \mathrm{Ker}\, f_i \subseteq \mathrm{Ker}\, f \Leftarrow f, \exists (\lambda_i)_{1 \leq n} \in \mathbb{K}^n \mid f = \sum_{i=1}^n \lambda_i f_i
$$
[ainsi que la réciproque, traitée en fin de page 2]

est vraie. En effet.

- Pour $n = 1$ : Soit $f, f_1 \in E^* \times E^*$ [lecture incertaine — probablement $f, f_1 \in E^*$], $f_1$ non nulle alors $\mathrm{Ker}\, f_1$ est un hyperplan de $E$ ainsi $\exists x_0 \in E \setminus \mathrm{Ker}\, f_1 \mid E = \mathrm{Ker}\, f_1 \oplus \mathbb{K}x_0$, d'où $\exists! (h, \alpha) \in \mathrm{Ker}\, f_1 \times \mathbb{K} \mid x = h + \alpha x_0$.
- Pour $\alpha \neq 0_{\mathbb{K}}$, cherchons $\lambda_1 \mid f(x) = \lambda_1 f_1(x)$ ($E$)

($E1 \Leftarrow$) $f_1(h) + \alpha f_1(x_0) = \lambda_1\big(\underset{\underset{\text{car } \mathrm{Ker}\, f_1 \subseteq \mathrm{Ker}\, f}{0_{\mathbb{K}}}}{f_1(h)} + \alpha f_1(x_0)\big)$ [lecture incertaine sur les indices $f/f_1$ de part et d'autre]

$\Rightarrow \lambda_1 = \dfrac{f(x_0)}{f_1(x_0)}$ car $\alpha \neq 0_{\mathbb{K}}$ et de plus $x_0 \notin \mathrm{Ker}\, f_1 \Rightarrow f_1(x_0) \neq 0_{\mathbb{K}}$

- Pour $\alpha = 0_{\mathbb{K}}$, $x \in \mathrm{Ker}\, f_1 \subseteq \mathrm{Ker}\, f$ d'où $f(x) = 0_{\mathbb{K}} = 0_{\mathbb{K}} \times \dfrac{f(x_0)}{f_1(x_0)}$

$$
= \frac{f(x_0)}{f_1(x_0)} f_1(x)
$$

Donc $\forall x \in E$, $f(x) = \dfrac{f(x_0)}{f_1(x_0)} f_1(x)$ CQFD

($\Leftarrow$) Soit $x \in \mathrm{Ker}\, f_1$. On a : $f(x) = \lambda_1 f_1(x) = \lambda_1 \cdot 0_{\mathbb{K}} = 0_{\mathbb{K}} \Rightarrow x \in \mathrm{Ker}\, f$. D'où $\mathrm{Ker}\, f_1 \subseteq \mathrm{Ker}\, f$. Ainsi $P(1)$ vraie.

- Hérédité. Soit $((f_i)_{1 \leq i \leq n+1}, f) \in (E^*)^{n+1} \times E^*$.
$\Rightarrow$ (?) Cherchons $(\lambda_i)_{1 \leq i \leq n+1} \in \mathbb{K}^{n+1} \mid f = \sum_{i=1}^{n+1} \lambda_i f_i \Leftarrow f - \sum_{i=1}^n \lambda_i f_i = \lambda_{n+1}f_{n+1} \Leftarrow f - \lambda_{n+1}f_{n+1} = \sum_{i=1}^n \lambda_i f_i$

## Page 2

[À droite, fine bande verticale d'une page adjacente, non transcrite.]

Considérons les restrictions $f' : \bigcap_{i=1}^n \mathrm{Ker}\, f_i \longrightarrow \mathbb{K}$, $x \longmapsto f_{n+1}(x)$ [lecture incertaine — probablement $x \longmapsto f(x)$] et $f_{n+1}' : F \longrightarrow \mathbb{K}$, $x \longmapsto f_{n+1}(x)$ [avec $F = \bigcap_{i=1}^n \mathrm{Ker}\, f_i$].

On a $f'$ et $f_{n+1}'$ sont des fl sur $F$.

- Si $f_{n+1}'$ nulle alors $\mathrm{Ker}\, f_{n+1} \supseteq \bigcap_{i=1}^n \mathrm{Ker}\, f_i$ d'où $\bigcap_{i=1}^{n+1} \mathrm{Ker}\, f_i = \bigcap_{i=1}^n \mathrm{Ker}\, f_i$, $f = \sum_{i=1}^n d_i f_i = \sum_{i=1}^{n+1} d_i f_i$ avec $d_{n+1} = 0_{\mathbb{K}}$. Prendre alors $\lambda_i = d_i$ $\forall i \in [\![1, n+1]\!]$ CQFD
- Sinon, ce $\mathrm{Ker}\, f_{n+1}' = \mathrm{Ker}\, f_{n+1} \cap \left(\bigcap_{i=1}^n \mathrm{Ker}\, f_i\right) = \bigcap_{i=1}^{n+1} \mathrm{Ker}\, f_i \subseteq \mathrm{Ker}\, f$, alors $\mathrm{Ker}\, f_{n+1}' \subseteq \mathrm{Ker}\, f \cap \left(\bigcap_{i=1}^n \mathrm{Ker}\, f_i\right) = \mathrm{Ker}\, f'$. Car $P(1)$ vraie, $\exists d_{n+1} \in \mathbb{K} \mid \forall x \in \bigcap_{i=1}^n \mathrm{Ker}\, f_i$, $f(x) = d_{n+1}f_{n+1}(x)$.

Posons $g = f - d_{n+1}f_{n+1}$. D'après ce qui précède, [raturé] $\bigcap_{i=1}^n \mathrm{Ker}\, f_i \subseteq \mathrm{Ker}\, g$ et ce $P(n)$ vraie, $\exists (d_i)_{1 \leq i \leq n} \in \mathbb{K}^n \mid g = \sum_{i=1}^n d_i f_i \iff f - d_{n+1}f_{n+1} = \sum_{i=1}^n d_i f_i \Rightarrow f = \sum_{i=1}^{n+1} d_i f_i$. Prendre alors $\lambda_i = d_i$ $\forall i \in [\![1, n+1]\!]$ CQFD

($\Leftarrow$) Soit $x \in \bigcap_{i=1}^n \mathrm{Ker}\, f_i$. On a : $f(x) = \sum_{i=1}^n \lambda_i f_i(x) = \sum_{i=1}^n \lambda_i \cdot 0_{\mathbb{K}} = 0_{\mathbb{K}}$ ainsi $x \in \mathrm{Ker}\, f$ d'où $\bigcap_{i=1}^n \mathrm{Ker}\, f_i \subseteq \mathrm{Ker}\, f$. CQFD

## Page 3

Théo : Soit $E$ un $\mathbb{K}$-ev. $(f_i)_n$ est une base de $E^*$ ssi $f_i$ non nulle $\forall i \in [\![1, n]\!]$ et $\bigcap_{i=1}^n \mathrm{Ker}\, f_i = \{0_E\}$.

Soit $(f_i)_n \in (E^*)^n$. $\mathcal{H}$

$\Rightarrow$ / lemme : $\bigcap_{H \in Hyp(E)} H = \{0_E\}$. [raturé — membre de phrase biffé]

Supp par l'absurde $\exists x \in \mathcal{H} \mid x \neq 0_E$ [lecture incertaine — probablement $\exists x \in E$].

- Si $\dim E = 1$, $\mathcal{H} = \{0_E\}$ car $\forall H \in Hyp(E)$, $\dim H = \dim E - 1 = 0$ ce qui est absurde ; d'où le résultat.
- Sinon, on que $\mathbb{K}x$ admet un supplément dans $E$ et qui est un hyperplan, $S \in Hyp(E)$ [raturé] $x \in S$. Absurde ! d'où CQFD

Soit $H \in Hyp(E)$. $\exists f_0 \in E^* \setminus \{0_{E^*}\} \mid \mathrm{Ker}\, f_0 = H$. ce $(f_i)_n$ génératrice, $\bigcap_{i=1}^n \mathrm{Ker}\, f_i \subseteq H$ (d'après le théo précédent) d'où $\bigcap_{i=1}^n \mathrm{Ker}\, f_i \subseteq \bigcap_{H \in Hyp(E)} H = \{0_E\}$.

D'où $\bigcap_{i=1}^n \mathrm{Ker}\, f_i = \{0_E\}$ [souligné, avec flèche Flutter].

Théo : (Il a été utilisé plus haut) Soit $E$ un $\mathbb{K}$-ev. Tout sev $F$ de $E$ admet au moins un supplément [page coupée — la fin manque].

---

## Figures

Aucune figure à reproduire : pages 1–3 relues visuellement (relecture 2026-09-07, texte et formules, sans schéma ; p. 3 : soulignés + flèche Flutter, pas de tracé).

## Vocabulaire / notions

- **Forme linéaire** $f \in E^*$, **noyau** $\mathrm{Ker}\,f$.
- **Hyperplan** : noyau d'une forme non nulle ; $\bigcap_{H \in Hyp(E)} H = \{0_E\}$.
- **Supplément** d'un sev ; **somme directe** $E = \mathrm{Ker}\,f_1 \oplus \mathbb{K}x_0$.
- **Famille génératrice de $E^*$** ; critère $\bigcap_i \mathrm{Ker}\,f_i = \{0_E\}$.
- **Abréviations d'auteur** : ratures `[raturé]`, lectures incertaines signalées.
