# Erdős–Selfridge (produit de trois entiers consécutifs) — transcription fidèle

> 🧾 **Manuscrit original :** [erdos-selfridge.pdf](erdos-selfridge.pdf) (photos de cahier, 12 pages) · ✍️ KpihX
> 🔍 **Statut :** transcrit à la main, page par page, sans rien inventer. Les maths sont en LaTeX ; les abréviations de l'auteur sont conservées telles quelles (`Mq`, `ona`, `SNALG`, `meth1`/`meth2`, `Thès`, `m̃`, `mtq`, `c-à-d`) ; les ratures, incertitudes et coquilles sont taggées `[raturé]`, `[lecture incertaine — …]`, `[*sic* — …]`.
> 📄 **Source scannée :** [erdos-selfridge.pdf](erdos-selfridge.pdf) (mention restaurée Datas1 2026-09-07, vérifiée `pdfinfo` : 12 pages, 515×720 pts, 2026-09-07). Les pages 9–12 sont une seconde prise photographique des pages 1–4 (même contenu).

---

## Page 1

Thès : Soient $K, a, b \in \mathbb{N}^*$ [lecture incertaine — le manuscrit porte ensuite un groupe de glyphes ressemblant à « $\forall n 1$ », sens obscur ; peut-être une condition sur $K$]. Ona : $(a-1)a(a+1) \neq b^K$

Supposons le contraire par l'absurde et posons

$(E1) : (a-1)a(a+1) = b^K$ [lecture incertaine — connecteur entre les deux formes : « et » ou « $\Leftrightarrow$ »] $a^3 - a = b^K$

• Mq tout [raturé — « diviseur commun à a et »] les diviseurs $1^{ers}$ de $a$ et $b \geq 5$ coïncident.

[raturé — « Soit » [lecture incertaine]] $a \mid b^K$, les diviseurs $1^{ers}$ de $a$ sont aussi ceux de $b$

– Soit $p$ un diviseur $1^{er}$ de $b$ mais pas de $a$.

ona : $(E1) \Rightarrow a^3 \equiv a [p] \Rightarrow a^2 \equiv 1 [p]$ car $a \wedge p = 1$

or $\exists n \in \mathbb{N} / a^n \equiv 1 [p]$ [lecture incertaine — le manuscrit porte ensuite un segment peu lisible ressemblant à « $= (p-1)\mathbb{N}$ »] ainsi $p-1 \mid 2 \Rightarrow p = 2$ ou $3$

Ainsi tout diviseur $1^{er}$ de $b$ autre que $2$ et $3$ (et donc [lecture incertaine — « $\geq 5$ »]) en est aussi un de $a$. d'où le résultat

• Car $a^3$ et $a$ sont de $\tilde{m}$ parité, $(E1) \Rightarrow b$ est pair et ce $3 \mid (a-1)a(a+1)$, $(E1) \Rightarrow 3 \mid b$

[passage barré d'une grande croix :] Ainsi [raturé — « $\exists !, d_1, p_1, (d_i)_{i \in \mathbb{N}}$ … $\ni n \in$ … » [lecture incertaine — texte partiellement lisible sous la rature]]. De plus $b$ a d'autres diviseurs $1^{ers}$ autres que $2$ et $3$ car sinon $(a-1)a(a+1)$ n'admet que $2$ et $3$ comme diviseurs $1^{ers}$, ce qui est absurde ! En effet il est à noter que $(a-1) \wedge a = 1, a \wedge (a+1) = 1$ [lecture incertaine — premier membre peu lisible sous la croix] d'où les diviseurs $1^{ers}$ de $a$ ne sont pas compris dans ceux de $a-1$ et $a+1$ et inversement.

## Page 2

[passage barré d'une croix :] Ainsi · si $2$ et $3 \mid a$, alors $a-1$ et $a+1$ n'ont aucun facteur $1^{er} \Rightarrow a-1 = a+1 = 1$ (Absurde !)

· si juste $2 \mid a$ alors le seul diviseur $1^{er}$ de $(a-1)(a+1)$ est $3 \Rightarrow \begin{cases} \text{soit } a-1 = 1 \text{ et } 3 \mid a+1 \text{ absurde car } 1 \times 2 \times 3 = \text{[coupé en bord de page — fin de ligne illisible]} \\ \text{ou alors } 3 \mid (a-1) \text{ et } a+1 \text{ ce qui est absurde car } (a+1)-(a-1) = 2 < 3 \end{cases}$

· si juste $3 \mid a$

Ainsi $\exists n \in \mathbb{N}$, [raturé — « $\exists \alpha, \alpha', \alpha_1, \dots, \alpha_n \in$ »] $\exists (p_i)_{i=1}^n \in \mathbb{P}^n$,

$\exists (\alpha, \alpha', (\alpha_i)_{i=1}^n) \in \mathbb{N}^* \times \mathbb{N}^* \times \mathbb{N}^{*n}$ (avec par exemple pour $n = 0$, $(p_i)_{i=0} = \emptyset$.) / $b^K = 2^\alpha \times 3^{\alpha'} \times \prod_{i=1}^n p_i^{\alpha_i}$ avec $\forall i \in [\![1,n]\!], p_i > 5$ et $\forall j \in [\![1,n]\!], p_j \neq p_i$ ssi $i \neq j$ (avec $\prod_{i=n}^{0} p_i^{\alpha_i} = 1$ [*sic* — le manuscrit porte $\prod_{i=n}^{0}$, produit vide])

• Vu que $a$ et $b$ ont $\tilde{m}$ diviseurs $1^{ers} \geq 5$, $\exists (\beta, \beta', (\beta_i)_{i=1}^n) \in \mathbb{N} \times \mathbb{N} \times \mathbb{N}^{*n} / a = 2^\beta \times 3^{\beta'} \times \prod_{i=1}^n p_i^{\beta_i}$ avec $\alpha K \geq \beta, \alpha' K \geq \beta', \forall i \in [\![1,n]\!], K\alpha_i \geq \beta_i$ (car $a \mid b^K$) (avec $\prod_{i=n}^{0} p_i^{\beta_i} = 1$ [*sic* — idem])

Ainsi $(E1) \Rightarrow (a-1)$ [raturé — lettre illisible] $(a+1) = 2^{K\alpha-\beta} \times 3^{K\alpha'-\beta'} \times \prod_{i=1}^n p_i^{K\alpha_i-\beta_i}$ [lecture incertaine — l'exposant de $2$ et le « $\times 3$ » sont peu lisibles : les glyphes ressemblent à « $2^{K\alpha+\beta K\alpha'-\beta'}$ »]

car $a \wedge (a-1) = a \wedge (a+1) = 1 \Rightarrow a \wedge (a-1)(a+1) = 1$ [lecture incertaine — le manuscrit porte « $= 1/p_i$ », probablement « $= 1$ » suivi de « $p_i$ »], alors $\forall i \in [\![1,n]\!]$, ce $p_i \mid a$ alors $(a-1)(a+1) \neq 0$ [raturé — probablement « $[p_i]$ »]

## Page 3

d'où $\forall i \in [\![1,n]\!], K\alpha_i - \beta_i = 0 \Rightarrow a = 2^\beta \times 3^{\beta'} \times \left(\prod_{i=1}^n p_i^{\beta_i}\right)^K$

d'où $(a-1)(a+1) = 2^{K\alpha+\beta}$ [lecture incertaine — « $+$ » ou « $-$ »] $\times 3^{K\alpha'-\beta'}$

[raturé — mot lourdement biffé, illisible]. Si $a$ est pair ($\beta \geq 1$) on a $K\alpha-\beta = 0$ [lecture incertaine — les glyphes ressemblent à « $K\alpha+\beta<0$ »] car $(a-1)(a+1) \wedge a = 1$

d'où $(a-1)(a+1) = 3^{K\alpha'-\beta'}$ ainsi car [lecture incertaine — « ainsi car »] le cas $a-1 = 1$ est absurde car $1 \times 2 \times 3 = 6$ n'est pas une puissance $K^{i\text{ème}}$) $3 \mid (a-1)$ et $(a+1)$ et qui est absurde car $(a+1)-(a-1) = 2 < 3$

d'où $a$ est impair

· Si $3 \mid a$ on a de $\tilde{m}$ $K\alpha'-\beta' = 0$ d'où $(a-1)(a+1) = 2^{K\alpha-\beta}$ d'où $a-1$ et $a+1$ sont des puissances de $2$ distantes de $(a+1)-(a-1) = 2$. On ne peut qu'avoir $a-1 = 2$ et $a+1 = 4$ ce qui est absurde vu que $2 \times 3 \times 4 = 24 \neq b^K$

d'où $a \neq 0 [3]$. Par conséquent $\beta = \beta' = 0$ d'où $a = \left(\prod_{i=1}^n p_i^{\beta_i}\right)^K$ et $(a-1)(a+1) = 2^{K\alpha} \times 3^{K\alpha'}$ et on a nécessairement $n \geq 1$ [lecture incertaine — « $\geq$ » ou « $>$ »] car sinon $a = 1$ (Absurde !)

Car l'un des entiers $(a-1), a, a+1$ est multiple de $3$ alors comme $a \neq 0 [3]$, ça ne peut qu'être $a-1$ ou $a+1$

## Page 4

meth 1 : (souligné)

SNALG supposons que c'est $a+1$ qui est multiple de $3$

ona : $(a-1)(a+1) = 2^{K\alpha} \times 3^{K\alpha'} \Rightarrow$ [raturé — mot illisible] $\exists \gamma \in \mathbb{N} / a+1 = 3^{K\alpha'} \times 2^\gamma$ et $a-1 = 2^{K\alpha-\gamma}$ et vu que $a-1 \neq 1$ ona : $K\alpha-\gamma \geq 1$.

[raturé — « Ainsi $a-1$ et $a$ »] Si $K\alpha-\gamma = 1$, alors $a-1 = 2$ Absurde ! car $2 \times 3 \times 4 = 24 \neq b^K$ d'où $K\alpha-\gamma \geq 2$

Ainsi $a-1 = 2^{K\alpha-\gamma}$ et $a = \left(\prod_{i=1}^n p_i^{\beta_i}\right)^K$ et comme $K\alpha-\gamma \geq 2$ et $K \geq 2$ [lecture incertaine — glyphes « $K\ldots,2$ »], $a-1$ et $a$ sont des puissances entières consécutives. D'après le théorème de Catalan [*sic* — le manuscrit porte « Catalan »] on ne peut qu'avoir $a-1 = 8 = 2^3$ et $a = 9 = 3^2$ Absurde ! car $8 \times 9 \times 10 = 720 \neq b^K$ (ce qui se vérifie aisément !). On aboutit alors à la fin à une absurdité, d'où le résultat !

Rappel du théo de Catalan (Mihăilescu) [*sic* — le manuscrit porte « Mihăilescu »] : les 2 seules puissances d'entiers consécutives sont 8 et 9. (souligné)

suite meth2 : (souligné) si c'est plutôt $a-1 \equiv 0 [3]$ on aboutit au $\tilde{m}$ résultat en permultant [*sic* — le manuscrit porte « permultant »] juste $a-1$ et $a+1$ dans le cas précédent

## Page 5

meth2 : (souligné) (l'on ne fera appel à aucun théorème de grande envergure comme celui de Catalan). On est arrivé aux relations $a = \left(\prod_{i=1}^n p_i^{\beta_i}\right)^K$, $(a-1)(a+1) = 2^{K\alpha}3^{K\alpha'}$ avec un seul des entiers $a-1$ et $a+1$, qui est $\equiv 0 [3]$

· Si c'est $a+1$ qui est $\equiv 0 [3]$, $\exists \gamma \in \mathbb{N} / a+1 = 3^{K\alpha'} \times 2^\gamma$ et $a-1 = 2^{K\alpha-\gamma}$ avec $K\alpha-\gamma \geq 1$.

Et d'après un résultat de la meth1 (souligné), $K\alpha-\gamma \geq 2$. (en marge droite)

Ainsi $2a = a-1 + a+1 = 3^{K\alpha'} \times 2^\gamma + 2^{K\alpha-\gamma}$ d'où $a = 3^{K\alpha'} \times 2^{\gamma-1} + 2^{K\alpha-\gamma-1}$ car [raturé — « $K\alpha-\gamma \geq 2$ »] $K\alpha-\gamma-1 \geq 1$ ce qui contraint $\gamma \geq 1$

Car [raturé — segment illisible] on doit necessairement avoir $\gamma-1 = 0$ car sinon on pourrait factoriser [*sic* — le manuscrit porte « factoriser »] au moins par $2^1$ et avoir $a$ pair, ce qui est absurde

Ainsi $a-1 = 2^{K\alpha-1}$ et $a+1 = 3^{K\alpha'} \times 2$. De plus $2 = (a+1)-(a-1) = 2 \times 3^{K\alpha'} - 2^{K\alpha-1}$ d'où $1 = 3^{K\alpha'} - 2^{K\alpha-2}$ avec $K\alpha-\gamma \geq 2 \Rightarrow K\alpha-2 \geq 1$

[paraphe en bas à droite]

## Page 6

Lemme 1 : Soit $n, m \in \mathbb{N}^*$. $3^m - 2^n = 1 \Leftrightarrow (m,n) \in \{(1,1), (2,3)\}$

Rq : on pourrait utiliser le théo de Catalan pour rapidement se sortir d'affaire.

Posons $(E1)$ [*sic* — le manuscrit réutilise l'étiquette « $(E1)$ », déjà employée page 1] : $3^m - 2^n = 1 \Rightarrow 3^m \equiv 1 [2^n]$

Or $3^m \wedge 2^n = 1$, un résultat d'algèbre classique (facile à vérifier) énonce que $\exists m_0 \in \mathbb{N} / 3^m \equiv 1 [2^n] \Leftrightarrow m \in m_0\mathbb{N}$ pour un certain $m_0$ (appelé [raturé — mot illisible] valeur de l'indica[lecture incertaine — « indicatrice » ?] de Carmichaël pour $2^n$). ($m_0 \in \mathbb{N}^*$)

Dans la suite on désignera $m_0$ par $\lambda(n)$

Lemme 2 : $\forall n \in [\![3, +\infty[\![, \lambda(n) = 2^{n-2}$.

[barré d'une croix — première rédaction :] · pour $n = 3$, $2^{3-2} = 2$. Or : $3^1 \equiv 3 [8] \not\equiv 1 [8]$, $3^2 = 9 \equiv 1 [8]$ d'où $\lambda(3) = 2^{3-2}$

· Soit $n \in$ [raturé — chiffre biffé, illisible [lecture incertaine]] et vu $\exists K_n \in \mathbb{N} / 3^{\lambda(n)} - 1 = 2^n \times K_n$ on a $K_n \in 2\mathbb{N}+1$

· Pour $n = 3$, $2^{3-2} = 2$, or : $3^1 \equiv 3 [8] \not\equiv 1 [8]$, $3^2 = 9 \equiv 1 [8]$ d'où $\lambda(3) \leq 2^{3-2}$ [lecture incertaine — « $\leq$ », « $<$ » ou « $=$ »]. De plus $\frac{3^2-1}{2^3} = 1 = K_3$ [lecture incertaine — « $K_3$ » ou « $K_1$ »] $\in 2\mathbb{N}+1$ d'où le lemme est vrai pour $n = 3$

## Page 7

· Soit $n \in [\![4, +\infty[\![$ [lecture incertaine — borne exacte]. Supposons que le lemme 2 est vérifié pour $n-1$ et mtq qu'il l'est aussi pour $n$.

Ona : $3^{\lambda(n-1)} \equiv 1 [2^{n-1}] \Rightarrow 3^{\lambda(n)} \equiv 1 [2^{n-1}] \Rightarrow \lambda(n) \in \lambda(n-1)\mathbb{N} \Rightarrow \exists K \in \mathbb{N}^* / \lambda(n) = K\lambda(n-1)$

Par hypothèse, $\lambda(n-1) = 2^{n-3}$ d'où $\lambda(n) = K \times 2^{n-3}$

· Si $K = 1$ alors $3^{\lambda(n)} \equiv 1 [2^n] \Rightarrow \exists K_n \in \mathbb{N} / 3^{\lambda(n)} - 1 = 2^n \times K_n \Rightarrow$ [raturé — calcul biffé] Or : $3^{\lambda(n)} - 1 = \left(3^{\cdots}\right)^2 - 1$ [lecture incertaine — exposant illisible]

· Si $K = 1$ alors $3^{2^{n-3}} \equiv 1 [2^n]$ d'où $\exists K_n \in \mathbb{N} / 3^{2^{n-3}} - 1 = K_n \times 2 \times 2^{n-1}$ or comme $\lambda(n-1) = 2^{n-3}$ on a de $\tilde{m}$ $3^{2^{n-3}} - 1 = K_{n-1} \times 2^{n-1}$ d'où $K_{n-1} = 2K_n \Rightarrow K_{n-1} \in 2\mathbb{N}$ Absurde par hypothèse d'où $K \geq 2$.

Pour $K = 2$, $3^{2^{n-2}} - 1 = \left(3^{2^{n-3}} - 1\right)\left(3^{2^{n-3}} + 1\right) = K_{n-1} \times 2^{n-1} \left(3^{2^{n-3}} + 1\right)$ or $3^{\cdots} - 1 = K_{n-1} \times 2^{\cdots}$ [lecture incertaine — exposants] $\Rightarrow 3^{2^{n-3}} + 1 = 2\left(1 + K_{n-1} \times 2^{n-2}\right)$ ainsi $3^{2^{n-2}} - 1 = K_{n-1}\left(1 + K_{n-1} \times 2^{n-2}\right) \times 2^{\cdots}$ [lecture incertaine — exposant] $\quad (1)$

[tache brune en bas de page]

## Page 8

$(1) \Rightarrow 3^{2^{n-2}} - 1 \equiv 0 [2^n]$ et de plus $K_n = K_{n-1}(1 + K_{n-1} \times 2^{n-2}) \in 2\mathbb{N}+1$ car $K_{n-1} \in 2\mathbb{N}+1$ par hypothèse d'où le résultat.

Ainsi en revenant au lemme 1 [raturé — segment biffé], ona · pour $n \geq 3$, $3^m \equiv 1 [2^n] \Rightarrow m \in 2^{n-2}\mathbb{N}$ car $\lambda(n) = 2^{n-2} \Rightarrow \exists K \in \mathbb{N}^* / m = K \times 2^{n-2}$

or pour avoir $3^m - 2^n = 1$ il faut que $n > m$ c-à-d $K \times 2^{n-2}$ [lecture incertaine — comparateur illisible] $n \Rightarrow n \geq 2^{n-2}$

or le cas $n < 2^{n-2}$ est réalisé pour $n \geq 5$. Ainsi on a alors $n \leq 4$ d'où $n \in \{3, 4\}$.

On vérifie aisément qu'il n'y a que le cas $n = 3$ qui donne un entier $m = 2$

· pour $n \in \{1, 2\}$ il n'y a de $\tilde{m}$ que le cas $n = 1$ qui donne un entier $m = 1$. CQFD

En revenant alors au théorème on qu'on avait [*sic* — « on qu'on »] $1 = 3^{K\alpha'} - 2^{K\alpha-2}$ et comme $K \geq 2 \Rightarrow K\alpha' \geq 2$ car $\alpha' \geq 1$ [lecture incertaine — « car … $\geq 1$ »] on ne peut qu'avoir $K\alpha' = 2$ et $K\alpha-2 = 3 \Leftrightarrow K = 2, \alpha' = 1, \alpha = 5/2$ [raturé — quelques glyphes biffés]. or $\alpha \in \mathbb{N}^*$. On aboutit ainsi à une absurdité d'où le résultat.

## Page 9

Seconde prise photographique de la page 1 : contenu identique (voir transcription de la Page 1 ci-dessus). Différences visibles : cadrage et angle légèrement différents, luminosité plus faible, tache sombre au bord droit (doigt ?). Aucun ajout ni retrait de texte constaté.

## Page 10

Seconde prise photographique de la page 2 : contenu identique (voir transcription de la Page 2 ci-dessus). Différences visibles : cadrage légèrement différent ; la dernière ligne $(a-1)(a+1) \neq 0$ [raturé] est tronquée en bas exactement comme sur la page 2. Aucun ajout ni retrait de texte constaté.

## Page 11

Seconde prise photographique de la page 3 : contenu identique (voir transcription de la Page 3 ci-dessus). Différences visibles : cadrage et contraste légèrement différents. Aucun ajout ni retrait de texte constaté.

## Page 12

Seconde prise photographique de la page 4 : contenu identique (voir transcription de la Page 4 ci-dessus), sauf la dernière ligne « et $a+1$ dans le cas précédent », coupée à mi-hauteur en bas de page (seul le haut des glyphes est visible). Différences visibles : cadrage légèrement différent. Aucun ajout de texte constaté.

---

*Figures : aucune — le document est un manuscrit texte (démonstration) sans schéma ni tracé ; pas de script de reproduction ni d'image en `assets/`.*

---

## Figures

Aucune figure signalée par la transcription (démonstration texte, 12 pages dont 9–12 = seconde prise des pages 1–4) ; confirmé par relecture visuelle 2026-09-07 (pp. 1–12 relues, aucun schéma ni tracé ; pp. 9–12 identiques à pp. 1–4 : mêmes ratures, mêmes croix, cadrage/luminosité seuls différents).

Vérification 2026-09-08 (FAUX-POSITIF) : source `erdos-selfridge.pdf` re-rendue en intégralité (12/12 pages, r150, `/tmp/fmf/erdos-r150-*.png`) et relue visuellement — aucun schéma, tracé, courbe ni construction géométrique sur aucune page (texte manuscrit + ratures + tache brune p. 7–8 + paraphe p. 5, rien de codable) ; pp. 9–12 = seconde prise des pp. 1–4 (même contenu, cadrage/luminosité seuls différents). Le mot « figure » du dossier désigne uniquement la section générique `## Figures` ci-dessus : aucune figure manquante, donc aucun script `lab/scripts/`, aucun PNG `assets/`, aucun embed à créer.

## Vocabulaire / notions

- **Produit de trois entiers consécutifs** (Erdős–Selfridge).
- **Abréviations d'auteur** : `Mq`, `ona`, `SNALG`, `meth1`/`meth2`, `Thès`, `m̃`, `mtq`, `c-à-d`.
- **Doublons** : pages 9–12 = seconde prise photographique des pages 1–4 (même contenu).
