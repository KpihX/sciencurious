# Minimum de $a^2+b^2+c^2+d^2$ sous $a+b+c+d = 1$ — transcription fidèle

> 🧾 **Manuscrit original :** `minimum-somme-carres.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible (~90 %), transcrit fidèlement. Page 1 : preuve par les six inégalités $x^2+y^2 \geq 2xy$ (avec $T = 2\sum xy$) ; page 2 : reprise au propre par Cauchy-Schwarz ($M_q$ = « montrer que »). Ratures locales (signalées).
> 📄 **Source scannée :** [`minimum-somme-carres.pdf`](minimum-somme-carres.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Preuve par les inégalités deux à deux

Soient $a, b, c, d \in \mathbb{R}$

Supp $a+b+c+d = 1$. Posons $S = a^2+b^2+c^2+d^2$

Or : $S = \underbrace{(a+b+c+d)^2}_{1^2} - \underbrace{2(ab+ac+ad+bc+bd+cd)}_{T}$

or $\left.\begin{aligned} a^2+b^2 &\geq 2ab \\ a^2+c^2 &\geq 2ac \text{ [le premier a^2 porte une surcharge]} \\ a^2+d^2 &\geq 2ad \\ b^2+c^2 &\geq 2bc \\ b^2+d^2 &\geq 2bd \\ c^2+d^2 &\geq 2cd \end{aligned}\right\}$ du fait que $a^2+b^2-2ab = (a-b)^2 \geq 0$

$\implies 3(a^2+b^2+c^2+d^2) \geq T$

$\implies$ [raturé : « $3S$ »] $-T \geq -3S$

[mot de liaison peu lisible — probablement « donc »] $S = 1-T \geq 1-3S$ d'où $S \geq 1/4$ [souligné]

## Page 2 — Reprise par Cauchy-Schwarz

$a, b, c, d \in \mathbb{R}$

Mq : si $a+b+c+d = 1$ alors $a^2+b^2+c^2+d^2 \geq 1/4$ [« Mq » = montrer que]

Soit $A = (a,b,c,d)$ et $B = (1,1,1,1)$ [« $(1,1,1,1)$ » net p.2 r150 2026-09-07 (`/tmp/s9/minimum-2.png`) — doute levé] deux vecteurs de $\mathbb{R}^4$.

D'après l'inégalité de Cauchy-Schwarz [orthographe d'origine : « Cauchy-schwarz » (s minuscule), confirmé p.2 r150 2026-09-07] $|A \cdot B| \leq \|A\| \times \|B\|$

$\implies |(a,b,c,d) \cdot (1,1,1,1)| \leq \sqrt{a^2+b^2+c^2+d^2} \times \sqrt{1^2+1^2+1^2+1^2}$

$\implies |a+b+c+d| \leq \sqrt{a^2+b^2+c^2+d^2} \times \sqrt{4}$

$\implies \boxed{\sqrt{a^2+b^2+c^2+d^2} \geq \frac{|1|}{\sqrt{4}} = \frac{1}{\sqrt{4}}}$

$\implies a^2+b^2+c^2+d^2 \geq \frac{1}{4}$. Car la fonct[ion] $x \mapsto x^2$ est croissante sur $\mathbb{R}_+$

---

## 📝 Notes de transcription (fidélité)

- Page 1 : $T$ désigne le bloc $2(ab+ac+ad+bc+bd+cd)$ tout entier, d'où $S = 1-T$ et $3S \geq T$ (chaque carré apparaît dans trois des six inégalités), puis $S \geq 1-3S$, soit $S \geq 1/4$.
- Page 2 : la dernière étape explicite que $t \mapsto t^2$ est croissante sur $\mathbb{R}_+$ pour passer de $\sqrt{S} \geq 1/2$ à $S \geq 1/4$.
- Aucune figure ni schéma sur les 2 pages.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q13-minimum-1.png`, r150) — six inégalités `x²+y² ≥ 2xy`, ratures confirmées, aucune figure ; p. 2 vérifiée visuellement le 2026-09-07 (rendu `/tmp/s9/minimum-2.png`, r150, 2e passage) — `B = (1,1,1,1)` net, `Cauchy-schwarz` (s minuscule) et `fonct° … croissante sur R₊` confirmés, aucune figure. Aucun script `reproduce_minimum-somme-carres_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- `Mq` = montrer que ; `S = a²+b²+c²+d²`, `T = 2Σxy` ; Cauchy-Schwarz (p. 2, reprise au propre).
- ⚠️ Hors sujet « intégrales » : optimisation algébrique pure (voir rapport : nom trompeur, sans agir).
