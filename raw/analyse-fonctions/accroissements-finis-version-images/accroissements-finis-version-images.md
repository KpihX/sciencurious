# Accroissements finis (version images) — transcription fidèle

🧾 Source : [accroissements-finis-version-images.pdf](accroissements-finis-version-images.pdf)
🔍 Contenu : exercices manuscrits — pages 1–2 : théorème de Rolle et théorème des accroissements finis, étude de $f(x) = 1 - 2x\sqrt{1-x^2}$ (tableau de variations + courbe) ; pages 3–4 : calcul d'intégrale $\int \sqrt{4\theta^2-25}\,d\theta$ (changement de variable en $\mathrm{argsinh}$).
📄 Restauration : image restaurée Datas1 2026-09-07 — transcription fidèle, rien d'inventé.

## Page 1

[haut de page coupé — fin d'une ligne précédente avec « $g\ldots = 0$ »]

1/a) Cherchons $c \in ]-1, 0[$ tel que $g'(c) = 0$

On a : $g$ est $C^1$ sur $[-1, 2]$ comme somme de fonctions $C^1$ sur $[-1, 2]$

Car $g(1) = g(2)$

1/b) Cherchons $c \in ]-1, 0[$ tel que $g'(c) = 0$

On a : $g(-1) = 2(-1)^4 + (-1) +$ [lecture incertaine — un terme] $= 1$

$g(0) = 0$ ; $g(2) = 3$

On a : $g$ est continue sur $[-1, 2]$ comme somme de fonctions continues sur $[-1, 2]$

D'après le théorème des valeurs intermédiaires

- car $0{,}5 \in ]g(0), g(2)[$ [lecture incertaine — intervalles], $\exists\,c_1 \in ]-1, 0[$ tel que $g(c_1) = 0{,}5$
- car $0{,}5 \in ]g(0), g(1)[$ [lecture incertaine — intervalles], $\exists\,c_2 \in ]0, 1[$ tel que $g(c_2) = 0{,}5$

Ainsi $g(c_1) = g(c_2) = 0{,}5$. Car $g$ est $C^1$ sur $]c_1, c_2[$ [lecture incertaine — intervalle] comme somme de fonctions $C^1$, alors d'après le théorème de Rolle, $\exists\,c \in ]c_1, c_2[$ [lecture incertaine — intervalle] tel que $g'(c) = 0$ CQFD (souligné, flèche)

## Page 2

b) Montrons cela [lecture incertaine — début de ligne].

Cherchons $c \in ]0, 1[$ tel que $f'(c) = \overbrace{\ldots}^{\alpha} = \frac{1}{3}\left(f'(c_0) + f'(c_1)\right)$ [lecture incertaine — expression centrale et indices]

Car $f$ $C^1$ sur $[0, 1]$, $\exists\,c_1 \in ]0, 1[$ tel que $f'(c_1) = \frac{f(1)-f(0)}{1-0}$ [lecture incertaine — suite de l'égalité]

Ainsi $f'(c_1) = \frac{1}{3}\left(f'(c_0) + f'(c_2) + f'(c_1)\right)$ [lecture incertaine — indices] (D'après le théo des Accroissements finis)

Car $\alpha$ est la moyenne arithmétique de $f'(c_0)$, $f'(c_2)$ et $f'(c_3)$ [lecture incertaine — indices] alors $\alpha$ est entre $f'(c_1)$ et $f'(c_3)$ [lecture incertaine — indices].

Car $f$ est $C^1$, alors $f'$ est continue sur $[0, 1]$ ; d'après le théo des valeurs intermédiaires $\exists\,c_2 \in ]c_1, \ldots[$ [lecture incertaine — borne] tel que $f'(c_2) = \alpha$

Car $]c_1, \ldots[ \subset ]0, 1[$ [lecture incertaine — intervalle] Il suffit alors de prendre $\underline{c = c_2}$

2/ $f(x) = 1 - 2x\sqrt{1-x^2}$

$D_f = [-1, 1]$. $f$ est dérivable sur $]-1, 1[$ comme somme et produit de fonctions dérivables sur $]-1, 1[$ [lecture incertaine — intervalle]

Ainsi $\forall x \in ]-1, 1[$, $f'(x) = -2\left(\sqrt{1-x^2} + x\frac{1-2x}{2\sqrt{1-x^2}}\right)$ [lecture incertaine — numérateur $1-2x$]

$$= \frac{2(2x^2-1)}{\sqrt{1-x^2}}$$

Tableau de variations (en bas à gauche) :

| $x$ | $-1$ | $-\frac{1}{\sqrt{2}}$ | $\frac{1}{\sqrt{2}}$ | $1$ |
| $f'(x)$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $f(x)$ | $1$ [lecture incertaine — valeur en $x=-1$ coupée] $\nearrow$ | $2$ $\searrow$ | $0$ $\nearrow$ | $1$ |

Figure (en bas à droite) : tracé manuscrit de la courbe (notée $C_f$, avec mention « $(g)$ » [lecture incertaine]) dans un repère $(O, x, y)$ : départ en $(-1, 1)$, maximum $2$, traversée de l'axe des ordonnées en $(0, 1)$, minimum $0$, remontée en $(1, 1)$ (voir ## Figures).

![Courbe (Cg) reproduite : f(x) = 1 - 2x√(1-x²), max 2, min 0](assets/courbe-cg.png)

## Page 3

[haut de page : fin d'un calcul précédent, hors champ — deux lignes « $\ldots/2$ » puis « $=$ »]

③ $I(\theta) = \int \sqrt{4\theta^2-25}\,d\theta \quad \theta \in ]-\infty, -\frac{5}{2}] \cup [\frac{5}{2}, +\infty[$

$$= 5\int \sqrt{\left(\frac{2}{5}\theta\right)^2-1}\,d\theta$$

[en marge, à droite : $= \ln\left|\frac{2}{5}\theta + \sqrt{\frac{4}{25}\theta^2-1}\right|$ — lecture incertaine]

• Pour $\theta \in [\frac{5}{2}, +\infty[$, posons $t = \mathrm{argsinh}\left(\frac{2}{5}\theta\right)$ qui est bien une bijection de $[\frac{5}{2}, +\infty[$ vers $[0, +\infty[$

On a : $t = \mathrm{argsinh}\left(\frac{2}{5}\theta\right) \Rightarrow \frac{2}{5}\theta = \cosh t \Rightarrow d\theta = \frac{5}{2}\sinh t\,dt$

Ainsi $I(\theta) = \frac{25}{2}\int \sqrt{\cosh^2 t - 1}\,\sinh t\,dt$

$= \frac{25}{2}\int \sinh^2 t\,dt$ car $\sqrt{\cosh^2 t - 1} = |\sinh t| = \sinh t$ car $t \ge 0$ [lecture incertaine — formulation exacte]

$= \frac{25}{2}\int \frac{\cosh 2t - 1}{2}\,dt$

$I(t) = \frac{25}{4}\left(\frac{1}{2}\sinh 2t - t\right) + c, \quad c \in \mathbb{R}$

## Page 4

$\theta \mapsto -I(\theta)$ (car $f$ étant paire, toutes ses [lecture incertaine — deux mots] sont impaires)

d'où [raturé] $I_1(\theta) = 5\int \sqrt{\left(\frac{2}{5}\theta\right)^2-1}\,d\theta = -\frac{25}{8}(\ldots)$ [lecture incertaine — début]

$I_1(\theta) = \frac{25}{8}\left(-2\,\mathrm{argsinh}\left(\frac{2}{5}\theta\right) + \sinh\left(2\,\mathrm{argsinh}\left(\frac{2}{5}\theta\right)\right)\right) + c, \quad c \in \mathbb{R}$

• Pour $\theta \in ]-\infty, -\frac{5}{2}]$, en posons [*sic* — « en posons »] $u = -\theta \in [\frac{5}{2}, +\infty[$, on a $I(\theta) = -5\int \sqrt{\left(\frac{2}{5}u\right)^2-1}\,du$

$= -\frac{25}{8}\left(-2\,\mathrm{argsinh}\left(\frac{2}{5}u\right) + \sinh\left(2\,\mathrm{argsinh}\left(\frac{2}{5}u\right)\right)\right) + c, \quad c \in \mathbb{R}$ (d'après ce qui précède)

$= -\frac{25}{8}\left(-2\,\mathrm{argsinh}\left(-\frac{2}{5}\theta\right) + \sinh\left(2\,\mathrm{argsinh}\left(-\frac{2}{5}\theta\right)\right)\right) + c, \quad c \in \mathbb{R}$

## Figures

Figure de la page 2 (bas-droite) : courbe $C_f$ de $f(x) = 1 - 2x\sqrt{1-x^2}$ (tableau de variations + tracé manuscrit). Reproduction en code :

![Courbe (Cg) reproduite : f(x) = 1 - 2x√(1-x²), max 2, min 0](assets/courbe-cg.png)

Reproduction (script `reproduce_accroissements-finis-version-images_1.py`, exécuté avec `uv run`) : courbe bleue $f(x) = 1 - 2x\sqrt{1-x^2}$ sur $[-1, 1]$, points rouges $(-1,1)$, $(-1/\sqrt{2},2)$, $(1/\sqrt{2},0)$, $(1,1)$, quadrillage bleu `#9db3d8`. PNG relu et conforme au croquis d'origine.

## Vocabulaire / notions

- Théorème de Rolle, théorème des accroissements finis, théorème des valeurs intermédiaires.
- Fonction $C^1$, continuité, moyenne arithmétique, tableau de variations, courbe $C_f$.
- Intégrale $\int \sqrt{4\theta^2-25}\,d\theta$, changement de variable $t = \mathrm{argsinh}(2\theta/5)$, $\cosh$/$\sinh$, parité.
