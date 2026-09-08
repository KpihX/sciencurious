# Intégrale $\int_0^{+\infty}\frac{e^{-x^2}\sin x^2}{x^2}\,dx$ par dérivation sous le signe somme (Feynman) — transcription fidèle

> 🧾 **Manuscrit original :** `feynman-integrales.pdf` (scan, 4 pages) · ✍️ KpihX · texte en anglais
> 🔍 **Statut :** lisible (~85 %), transcrit fidèlement. Paramétrisation $I(a) = \int_0^{+\infty} e^{-x^2}\sin(ax^2)/x^2\,dx$, dérivation en $a$, gaussienne complexe via $\delta_a^2 = 1-ia$, constante fixée par $I(0) = 0$, positivité justifiée par découpage en arches de sinus puis généralisation et conclusion $I = \sqrt{\pi/(2(1+\sqrt{2}))}$.
> 📄 **Source scannée :** [`feynman-integrales.pdf`](feynman-integrales.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Paramétrisation et dérivée gaussienne complexe

$$I = \int_0^{+\infty} \frac{e^{-x^2}\sin x^2}{x^2}\,dx = \,?$$

Let's have $I(a) = \int_0^{+\infty} \frac{e^{-x^2}\sin(ax^2)}{x^2}\,dx$ for $a \in \mathbb{R}$ ; thus $I = I(1)$

We use this form in order to cancel $x^2$ with differentiating $I$ with respect to $a$. For $a \in \mathbb{R}$, let's have $f_a(x) = \frac{e^{-x^2}\sin(ax^2)}{x^2}$

Since $\lim_{x \to 0} f_a = a \in \mathbb{R}$ and $|f_a(x)| \underset{x \to \infty}{=} O\left(\frac{1}{x^2}\right)$, then $I(a) \in \mathbb{R}$

Hence $I'(a) = \int_0^{+\infty} e^{-x^2}\cos(ax^2)\,dx$

$$= \int_0^{+\infty} e^{-x^2}\mathrm{Re}\left(e^{iax^2}\right)\,dx$$

$$= \mathrm{Re}\left(\int_0^{+\infty} e^{-x^2(1-ia)}\,dx\right) \text{ since } \int_0^{+\infty} e^{-x^2}\cos(ax^2)\,dx \in \mathbb{R}$$

$$= \mathrm{Re}\left(\frac{1}{\delta_a}\int_0^{+\infty} \delta_a e^{-(\delta_a x)^2}\,dx\right) \text{ where } \delta_a \text{ is the root of } 1-ia \text{ for which } \mathrm{Re}\left(\frac{1}{\delta_a}\int_0^{+\infty} \delta_a e^{-(\delta_a x)^2}\,dx\right) > 0 \text{, [raturé] admitting that } I'(a) \geqslant 0 \text{, since } e^{-x^2}\cos(ax^2) \text{ tends rapidly towards } 0 \text{ (we'll justify at the end rigorously (12) [ainsi écrit — lire « (1),(2) »])}$$

$$= \mathrm{Re}\left(\frac{1}{\delta_a} \times \frac{\sqrt{\pi}}{2}\right)$$

So $I(a) = \int \mathrm{Re}\left(\frac{\sqrt{\pi}}{2} \times \frac{1}{\delta_a}\right)\,da$

$$= \frac{\sqrt{\pi}}{2}\mathrm{Re}\int \frac{1}{\delta_a}\,da$$

But $\delta_a = (\alpha+i\beta)$ with $(\alpha+i\beta)^2 = 1-ia$ meaning that $\begin{cases} \alpha^2-\beta^2 = 1 \\ \alpha^2+\beta^2 = \sqrt{1+a^2} \end{cases}$, $2\alpha\beta = -a$ [bas de page]

## Page 2 — Primitives, constante et formule de $I(a)$

Since we can write $\delta_a = (1-ia)^{1/2}$, we then have

$$I(a) = \frac{\sqrt{\pi}}{2}\mathrm{Re}\int (1-ia)^{-1/2}\,da$$

$$= \frac{\sqrt{\pi}}{2}\mathrm{Re}\left(2 \times i\,(1-ia)^{1/2} + C\right), \quad C \in \mathbb{C}$$

But $I(0) = 0 \Rightarrow \mathrm{Re}(2i+C) = 0 \Rightarrow C =$ [raturé] $\gamma i$, $\gamma \in \mathbb{R}$

Hence $I(a) = \frac{\sqrt{\pi}}{2}\mathrm{Re}\left(2i(1-ia)^{1/2}\right) + 0$

$$= -\sqrt{\pi}\,\mathrm{Im}(1-ia)^{1/2}$$

$$= -\sqrt{\pi}\,\mathrm{Im}(\delta_a)$$

Since $a \cdot I(a) \geqslant 0$ ((12) [ainsi écrit — lire « (1),(2) »] : we'll justify at the end), $\delta_a$ also verifies $\mathrm{Im}(\delta_a) \leqslant 0 \Rightarrow \beta = -\sqrt{\frac{\sqrt{1+a^2}-1}{2}} \cdot \frac{|a|}{a}$, for $a \neq 0$

Thus $I(a) = \sqrt{\frac{\pi}{2}\left(\sqrt{1+a^2}-1\right)} \cdot \frac{|a|}{a}$ for $a \neq 0$ ; $I(0) = 0$

[raturé : « And »] Therefore, $I = \int_0^{+\infty} \frac{e^{-x^2}\sin x^2}{x^2}\,dx = I(1) = \sqrt{\frac{\pi}{2}(\sqrt{2}-1)}$

Justification :

(1) : let's have $a \in \mathbb{R}$. Let's assume without loss of generality that $a > 0$ (since $I$ est odd [anglicisme conservé — lire « is »]) and let's show that $I(a) > 0$

$$I(a) = \int_{\substack{0 \\ t = x^2}}^{+\infty} \frac{\substack{e^{-t}\sin at \\ f_a(t)}}{2t\sqrt{t}}\,dt$$

## Page 3 — Positivité par arches de sinus

$$I(a) = \sum_{k \in \mathbb{N}} \underbrace{\int_{\frac{2k\pi}{a}}^{\frac{(2k+1)\pi}{a}} f_a(t)\,dt}_{I_{n1}(a)\ \text{[lecture incertaine — étiquette d'accolade peu lisible]}} + \underbrace{\int_{\frac{(2k+1)\pi}{a}}^{\frac{(2k+2)\pi}{a}} f_a(t)\,dt}_{I_{n2}(a)\ \text{[lecture incertaine — étiquette d'accolade peu lisible]}}$$

[raturé — deux lignes biffées :] Let's have $(t_1, x_1) \in \left[\frac{2k\pi}{a}, \frac{(2k+1)\pi}{a}\right] \times \left[\frac{(2k+1)\pi}{a}, \frac{(2k+2)\pi}{a}\right]$ for a certain $k \in \mathbb{N}$, in such a way that $x_1 =$ [fin illisible]

$$I_2(a) = \sum_{k \in \mathbb{N}} \int_{\frac{2k\pi}{a}}^{\frac{2(k+1)\pi}{a}} \frac{e^{-t}\sin at}{2t\sqrt{t}}\,dt \text{ let's set } u = t - \frac{\pi}{a}$$

$$I_2(a) = -\sum_{k \in \mathbb{N}} \int_{\frac{2k\pi}{a}}^{\frac{(2k+1)\pi}{a}} \frac{e^{-(u+\pi/a)}}{2\left|u+\frac{\pi}{a}\right|\sqrt{u+\frac{\pi}{a}}}\sin au\,du$$

We then have $I(a) = \sum_{k \in \mathbb{N}} \int_{\frac{2k\pi}{a}}^{\frac{(2k+1)\pi}{a}} \left(g(t) - g\left(t+\frac{\pi}{a}\right)\right)\sin(at)\,dt$

where : $g : t \mapsto \frac{e^{-t}}{2t\sqrt{t}}$ ↘* over $\mathbb{R}_+^*$ [l'astérisque suit la flèche de décroissance]

Hence $I(a) > 0$

(2) : we demonstrate it similarly by doing the replacements : $\frac{2k\pi}{a} \to -\frac{\pi}{2} + 2k\pi$, $\frac{(2k+1)\pi}{a} \to \frac{\pi}{2} + 2k\pi$, $\frac{2(k+1)\pi}{a} \to \frac{3\pi}{2} + 2k\pi$, $k \in \mathbb{Z}$ ; yes! here, we can show that $\int_{-\infty}^{+\infty} e^{-x^2}\cos(ax^2)\,dx > 0$ for $a \in \mathbb{R}$ and just considerate the case $a > 0$ since $a \mapsto \int_{-\infty}^{+\infty} e^{-x^2}\cos(ax^2)\,dx$ ist even [*sic* — lire « est », comme « $I$ est odd » page 2] ; and at the end $I'(a) = \frac{1}{2}\int_{-\infty}^{+\infty} e^{-x^2}\cos(ax^2)\,dx > 0$ [bas de page]

## Page 4 — Généralisation et conclusion

Generalisation : let's have $I(a) = \int_0^{+\infty} f(t)\sin(at)\,dt$ ; $J(a) = \int_{-\infty}^{+\infty} f(t)\cos at\,dt$ where $a \in \mathbb{R}^*$, $f$ is a strictly decreasing function over $\mathbb{R}_+$ (and is even on $\mathbb{R}$ for the case of $J$). We then have : $*\, a \cdot I(a) > 0$ ; $*\, J(a) > 0$

Conclusion : let's set $a \in \mathbb{R}$.

$$I(a) = \int_0^{+\infty} \frac{e^{-x^2}\sin(ax^2)}{x^2}\,dx = \sqrt{\frac{\pi}{2}\left(\sqrt{1+a^2}-1\right)} \times \frac{a}{|a|}$$

[raturé : formule intermédiaire biffée]

$$= a\sqrt{\frac{\pi}{2} \times \frac{1}{1+\sqrt{1+a^2}}}$$

And $I = \int_0^{+\infty} \frac{e^{-x^2}\sin x^2}{x^2}\,dx = \sqrt{\frac{\pi}{2(1+\sqrt{2})}}$

---

## 📝 Notes de transcription (fidélité)

- Le manuscrit est rédigé en anglais avec des gallicismes (« $I$ est odd », « ist even ») conservés tels quels.
- « (12) » pages 1–2 désigne les deux justifications (1) et (2) : (1) $I(a) > 0$ pour $a > 0$ (somme télescopique d'arches avec $g$ décroissante), (2) $I'(a) > 0$ par le même découpage translaté de $\pi/2$.
- Le choix de racine $\delta_a$ ($\mathrm{Im}(\delta_a) \leqslant 0$) est imposé par le signe $a \cdot I(a) \geqslant 0$.
- Aucune figure ni schéma sur les 4 pages.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q03-feynman-1.png`, r150) — texte anglais + équations, aucune figure ; pp. 2–4 revérifiées visuellement au second passage le 2026-09-07 (rendus `/tmp/s8/feynman-2.png` à `/tmp/s8/feynman-4.png`, r150) — texte + équations uniquement, aucune figure. Aucun script `reproduce_feynman-integrales_N.py`, aucun PNG (aucun `assets/` créé, vérifié `uv run`).

---

## Vocabulaire

- `I(a)` = paramétrisation de Feynman ; `δ_a` = racine de `1 − ia` (branche `Im ≤ 0`).
- Gallicismes conservés : « `$I$ est odd` », « `ist even` » ; `(12)` = justifications (1) et (2) ; `↘*` = décroissante.
