# Intégrales et arctan — transcription fidèle

> 🧾 **Manuscrit original :** `integrales-arctan.pdf` (scan, 5 pages) · ✍️ KpihX
> 🔍 **Statut :** partiellement lisible (~65 %), transcrit fidèlement. Cahier Seyès, encre bleue, nombreuses ratures. L'auteur écrit « arctan » d'une façon qui ressemble à « archan », et note $\tan^{-1}$ (lu « tg⁻¹ ») pour $\arctan$ à partir de la page 3. Décomposition en éléments simples de $\int dx/((x^2-2\alpha x+\beta)(x^2+2\alpha x+\beta))$, étude de $J$ ramenée par $x=\sqrt{t}$ à $I=\int_0^{+\infty} 2/(5+x^4)\,dx$ (convergence par la règle de Riemann, valeur exacte via factorisation de $5+x^4$), puis démonstration complète des formules d'addition $\arctan a \pm \arctan b$ avec discussion exhaustive des cas.
> 📄 **Source scannée :** [`integrales-arctan.pdf`](integrales-arctan.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Quelques propriétés, étude de $J$

[u](Quelques propriétés)

- $$I = \int \frac{dx}{(x^2-2\alpha x+\beta)(x^2+2\alpha x+\beta)} \quad \alpha,\beta \in \mathbb{R} \text{ [lecture incertaine — l'exposant après } \mathbb{R} \text{ est illisible]}$$

$$= \int \left( \frac{x+\alpha}{x^2+2\alpha x+\beta} - \frac{x-\alpha}{x^2-2\alpha x+\beta} \right) \times \frac{1}{[2\alpha\beta \text{ ? — lecture incertaine]}}\,dx$$

- $$I = \int \frac{1\,dx}{(x\pm\alpha)^2+\beta^2} = \frac{1}{\beta}\arctan\frac{1}{\beta}(x\pm\alpha) + C$$

- $$\forall a,b \in \mathbb{R}, \quad \arctan a \pm \arctan b = \arctan\left(\frac{a\pm b}{1\mp ab}\right) + k\pi \quad \text{[annotation marginale droite illisible]}$$

$$\arctan\frac{1}{a} = \frac{\pi}{2} - \arctan a$$

- [u](Étude de) $$J = \int_0^{+\infty} \frac{dt}{[\sqrt{t}\,(5+t^2) \text{ — lecture incertaine, dénominateur peu lisible, restitué grâce à la suite}]} = \int_0^{+\infty} \frac{[\ldots \text{ — illisible}]}{[\ldots \text{ — illisible}]}$$

Effectuons le changement de variable $x = \sqrt{t}$. Vu que [fonction — lecture incertaine] est strictement croissante de $\mathbb{R}_+^*$ vers $\mathbb{R}_+^*$ et que $x \mapsto \frac{2}{x^4+5}$ est continue sur $\mathbb{R}_+^*$ alors $I$ est [mot — lecture incertaine]

$$I = \int_0^{+\infty} \frac{2}{5+x^4}\,dx \text{ de même nature. Notons que } \forall x \in \mathbb{R}^*, \text{ [formule — lecture incertaine]}$$

$$\lim_{x\to+\infty} \frac{5+x^4}{x^4} = 1 \text{ ainsi } 5+x^4 \sim x^4 \Rightarrow f(x) \sim \frac{2}{x^4} = \frac{1}{x^4} \text{ [lecture incertaine — exposants et constantes peu lisibles]}$$

avec $[A > 0, \, \alpha \in \mathbb{R} \text{ — lecture incertaine]}$, car $\alpha > 1$ d'après la règle de Riemann $I$ est convergente (et il en est de même [fin de ligne coupée — probablement « de $J$ »])

## Page 2 — Valeur de $I$

pour $J$)

- Valeur de $I$
$$I = \lim_{X\to+\infty} \int_0^X \frac{2}{5+x^4}\,dx$$

Évaluons $G(x) = \int \frac{2}{5+x^4}\,dx \quad x \in \mathbb{R}$

$$= \int \frac{2}{(x^2-\sqrt{2\sqrt{5}}\,x+\sqrt{5})(x^2+\sqrt{2\sqrt{5}}\,x+\sqrt{5})}\,dx$$

$$= \frac{1}{2\sqrt{2\sqrt{5}}} \int \left( \frac{2x+2\sqrt{2\sqrt{5}}}{x^2+\sqrt{2\sqrt{5}}\,x+\sqrt{5}} - \frac{2x-2\sqrt{2\sqrt{5}}}{x^2-\sqrt{2\sqrt{5}}\,x+\sqrt{5}} \right)dx$$

$$= \frac{1}{2\sqrt{2\sqrt{5}}} \ln\left|\frac{x^2+\sqrt{2\sqrt{5}}\,x+\sqrt{5}}{x^2-\sqrt{2\sqrt{5}}\,x+\sqrt{5}}\right| + \sqrt{2\sqrt{5}}\left(\int \frac{1}{[\ldots]} + \frac{1}{[\ldots]}\right)dx \text{ [dénominateurs des formes canoniques — lecture incertaine]}$$

$$+ \frac{[\sqrt{2\sqrt{5}} \text{ — lecture incertaine}]}{[\ldots]} \left[ \arctan(\ldots) + \arctan(\ldots) \right]$$

$$+ 2\arctan \sqrt{\frac{2}{\sqrt{5}}} \left[ \frac{x}{1-\frac{x^2}{\sqrt{5}}} \right] + C \quad \text{[raturé — grand barré en croix]}$$

ou encore

$$+ 2[\ldots]\arctan\left| \sqrt{\frac{\sqrt{5}}{2}} \left( \frac{1}{x} - \frac{x}{\sqrt{5}} \right) \right| + C \quad \text{[raturé — barré en croix, lecture incertaine]}$$

ainsi $I = \frac{1}{2\sqrt{2\sqrt{5}}}\left(0 + 2\left(\frac{\pi}{2}+\frac{\pi}{2}\right) - 0 - 2(0+0)\right) = \frac{[\ldots]\pi}{[\ldots]} \text{ [résultat intermédiaire — lecture incertaine]}$

$$I = \frac{\pi}{\sqrt{10\sqrt{5}}} = \frac{\pi}{\sqrt{2} \times 5^{3/4}} \text{ [corrigé second passage — crop `/tmp/s8/crop-arctan2-bottom.png` : } \sqrt{10\sqrt{5}} \text{ confirmé, numérateur } \pi \text{ net]}$$

[annotation marginale droite : $5^{1/4}$ ? — lecture incertaine]

## Page 3 — Retour sur $\arctan a + \arctan b$

Retour sur $\arctan a + \arctan b = \arctan\left(\frac{a+b}{1-ab}\right) + k\pi$, $k \in$ [illisible]

Or $\arctan a + \arctan b \in ]-\pi, \pi[$

- Si $S \in ]-\pi/2, \pi/2[$, c-à-d $a \in \mathbb{R}$ et $-\frac{\pi}{2} - \tan^{-1}a < \tan^{-1}b < \frac{\pi}{2} - \tan^{-1}a$ [lecture incertaine] et $-\frac{\pi}{2} < \tan^{-1}b < \frac{\pi}{2}$

ainsi — si $a > 0 \Leftrightarrow \tan^{-1}a > 0$ [raturé], on a $-\frac{\pi}{2} < \tan^{-1}b < \frac{\pi}{2} - \tan^{-1}a$, d'où $-\infty < b < \tan\left(\frac{\pi}{2}-\tan^{-1}a\right) = \frac{1}{a}$ [lecture incertaine sur la fin]

- si $a < 0 \Rightarrow \tan^{-1}a < 0$ [raturé], on a $-\frac{\pi}{2}-\tan^{-1}a < \tan^{-1}b < \frac{\pi}{2}$, d'où $-\tan\left(\frac{\pi}{2}+\tan^{-1}a\right) < b < +\infty$ c-à-d $\frac{1}{a} < b$

- si $a = 0$ on a $b \in \mathbb{R}$. Ainsi $ab \neq 1$ ou $a \geq 0$ ou $b \geq 0$ [raturé — signe « $<$ » corrigé en « $\neq$ », lecture incertaine, confirmé sur crop `/tmp/s8/crop-arctan3-mid.png` au second passage]

Donc pour $a \geq 0$ ou $b \geq 0$ ou $ab > 1$ on a [*sic* — attendre $ab < 1$ pour le cas principal ; « $>$ » confirmé sur crop `/tmp/s8/crop-arctan3-mid.png` au second passage] : $$\arctan a + \arctan b = \arctan\left(\frac{a+b}{1-ab}\right)$$

- Si $S \in ]-\pi, -\pi/2[$, c-à-d [raturé] $-\pi-\tan^{-1}a < \tan^{-1}b < -\frac{\pi}{2}-\tan^{-1}a$ [lecture incertaine]

il faut que $-\frac{\pi}{2}-\tan^{-1}a > -\frac{\pi}{2} \Leftrightarrow a \in \mathbb{R}_-^*$ [lecture incertaine] et $-\frac{\pi}{2} < \tan^{-1}b < \pi$ [lecture incertaine]

dans ce cas $-\frac{\pi}{2} < \tan^{-1}b < -\frac{\pi}{2}-\tan^{-1}a$ c-à-d $-\infty < b < \frac{1}{a}$ c-à-d $ab > 1 \quad (a < 0)$

## Page 4 — Conclusion : lemme et théorème

Dans ce cas $\arctan a + \arctan b = \arctan\frac{a+b}{1-ab} - \pi$

- Si $S \in ]\pi/2, \pi[$ c-à-d $ab > 1$ et $a > 0$, on a $\arctan a + \arctan b = \arctan\frac{a+b}{1-ab} + \pi$

[u](Conclusion :)

Soit $a, b \in \mathbb{R}$, $\tan^{-1}a + \tan^{-1}b \in ]-\pi, \pi[$

[u](Lemme :) $\tan^{-1}a + \tan^{-1}b \in ]-\pi/2, \pi/2[ \Leftrightarrow$ [raturé] $ab < 1$

$\tan^{-1}a + \tan^{-1}b \in ]-\pi, -\pi/2[ \Leftrightarrow ab > 1$ et $a, b < 0$

$\tan^{-1}a + \tan^{-1}b \in ]\pi/2, \pi[ \Leftrightarrow ab > 1$ et $a, b > 0$

[u](Ainsi :) - Si $ab < 1 \quad \tan^{-1}a + \tan^{-1}b = \tan^{-1}\frac{a+b}{1-ab}$

[annotation marginale gauche : $ab < 1$]

- Si $ab > 1$ et $a, b < 0$, $\tan^{-1}a + \tan^{-1}b = \tan^{-1}\frac{a+b}{1-ab} - \pi$

- Si $ab > 1$ et $a, b > 0$, $\tan^{-1}a + \tan^{-1}b = \tan^{-1}\frac{a+b}{1-ab} + \pi$

on a de même $\tan^{-1}a + \tan^{-1}b \in \tan^{-1}a + \tan^{-1}(-b)$ [lecture incertaine — formule de transition vers la différence], ainsi

- Si $ab > -1 \quad \tan^{-1}a - \tan^{-1}b = \tan^{-1}\frac{a-b}{1+ab}$

- Si $ab < -1$ et $a > 0$, $b < 0 \quad \tan^{-1}a - \tan^{-1}b = \tan^{-1}\left(\frac{a-b}{1+ab}\right) - \pi$ [lecture incertaine — signe du $\pi$ peu lisible]

- Si $ab < -1$ et $a > 0$, $b < 0$ [*sic* — les deux dernières lignes portent les mêmes conditions ; lire probablement $a < 0$, $b > 0$ pour l'une d'elles] $\tan^{-1}a - \tan^{-1}b = \tan^{-1}\left(\frac{a-b}{1+ab}\right) + \pi$

## Page 5 — Cas particulier $a = b$

- R Cas particulier de $a = b$
- Si $a^2 < 1 \Leftrightarrow -1 < a < 1$, $2\tan^{-1}a = \tan^{-1}\frac{2a}{1-a^2}$
- Si $a^2 > 1$ et $a < 0 \Leftrightarrow a < -1$, $2\tan^{-1}a = \tan^{-1}\frac{2a}{1-a^2} - \pi$
- Si $a^2 > 1$ [raturé : $a^2 > 0$] et $a > 0 \Leftrightarrow a > 1$, $2\tan^{-1}a = \tan^{-1}\frac{2a}{1-a^2} + \pi$

[gribouillis — signature en bas de page]

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q07-arctan-1.png`, r150) — cahier Seyès, encre bleue, graphie « archan » pour arctan confirmée, aucune figure ; pp. 2–5 revérifiées visuellement au second passage le 2026-09-07 (rendus `/tmp/s8/arctan-2.png` à `/tmp/s8/arctan-5.png`, r150) — texte + équations uniquement, aucune figure. Aucun script `reproduce_integrales-arctan_N.py`, aucun PNG (aucun `assets/` créé, vérifié `uv run`).

---

## Vocabulaire

- `archan` = graphie de l'auteur pour `arctan` ; `tg⁻¹`/`tan⁻¹` = `arctan` (dès p. 3).
- Riemann = règle de convergence (`α > 1`) ; éléments simples = décomposition en éléments simples ; `[*sic*]` p. 4 : conditions dupliquées conservées.
