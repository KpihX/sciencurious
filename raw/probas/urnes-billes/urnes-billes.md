# Des Urnes & Des Billes — transcription fidèle

> 🧾 **Manuscrit original :** [urnes-billes.pdf](urnes-billes.pdf) — 3 pages manuscrites, encre bleue.
> 🔍 **Restauration :** image restaurée Datas1 2026-09-07 ; lecture directe des pages, rien d'inventé. P.1 re-rendue à $r = 150$ et relue 2026-09-07.
> 📄 **Contenu :** énoncé (trois urnes, doubler le contenu d'une urne en prélevant dans une autre), solution par parité et descente (notations $[n]$, divisions par 2, invariant $a+b$), application $a = 2$, $b = 3$, $c = 7$, remarque finale, signature [raturé].

---

## Page 1

Des Urnes & Des Billes

Énoncé : Trois urnes contiennent des billes et sont suffisamment grandes pour contenir toutes les billes. La seule opération possible est de doubler le nbre de billes dans une urne en prélevant des billes dans une autre.

Démontrer que quel que soit la config init, il est tjrs possible d'arriver à une config où au moins l'une des urnes est vide

Solution

[0] L'opération décrite se fait tjrs avec 2 urnes. Sans nuire à la généralité, supp qu'elle se fasse avec 2 des 3 urnes contenant resp $a$ et $b$ billes (avec $a \leq b$. Ainsi en affectant les lettres de $'$ pour désigner le nbre de billes après l'opération resp dans les 2 urnes, ces dernières auront $a'$ et $b'$ billes avec $a' + b' = a + b$. Or $a < b$ alors $a' = 2a$ d'où $a' \equiv 2a\, [2nb]$ et aussi $b' = b - a$ d'où $b' - a \equiv (b - a) + a + b\, [2nb]$ c-à-d $b' \equiv 2b\, [2nb]$.

NB : $a' \equiv \beta\, [\delta] \Leftrightarrow a'$ est le reste de la DE de $\beta$ par $\delta$

Ainsi trouver $a'$, $b'$ revient à dét les restes des DE de $2a$, par $a+b$ et $2b$ [lecture incertaine — ligne raturée/surchargée].

[1] On désigne par $a, b$ et $c$ les nbres de billes dans les 3 urnes resp.

\* Si $a, b$ et $c$ sont impairs on fait l'opération sur 2 quelconques (on obtient 2 nbres pairs) et 1 impair et on recommence en [1].

\* Si 2 sont impairs on effectue l'opération sur eux (on obtient 3 nbres pairs) et on recommence en [1].

\* Si les 3 sont pairs tout se résume à démontrer que la proposition plus haut est vraie pour des urnes contenant $a/2$, $b/2$, $c/2$ billes car si la proposition est vraie pour $a/2$, $b/2$, $c/2$, $\exists n \in \mathbb{N}$ / après $n$ opérations(s) au moins l'une des urnes est vide i.e le cas $a'_n = 0$, $b'_n$, $c'_n \in \mathbb{N}$ (sans nuire à la généralité) ; il suffit de suivre le m processus, avec $a$, $b$, $c$ et après $n$ opération(s) on aura $a_n = 2 \times 0$, $b_n = 2b'_n$, $c_n = 2c'_n$ ; et donc la proposition est vraie pour $a, b$ et $c$.

## Page 2

Ainsi dans le cas $a, b$ et $c$ pairs on les divise par 2 et on recommence en 1.

\* Si 1 seul est impair on supp $c$ (sans nuire à la généralité) alors $a+b$ est pair. Or tout entier naturel peut se mettre sous l'unique forme $2^d f$, $d, f \in \mathbb{N}$ avec $f$ impair ou nul alors $\exists !$, $(c', d) \in \mathbb{N}^2$ / $a+b = 2^d c'$ avec $d \geq 1$ car $a+b$ pair.

- Si $a = 0$ ou $b = 0$, la démonstration est terminée.

- Sinon $d$ est impair [lecture incertaine — « impair » surchargé, le sens attendrait « $\geq 1$ »]. En effectuant $c$ fois l'opération sur $a$ et $b$ pour obtenir $a_c$ et $b_c$ d'après [0], $a'_c \equiv 2^c a\, [2^d c']$ et $b'_c \equiv 2^c b\, [2^d c']$. Or $a + b = a+b$ alors ; avec $\exists K, K' \in \mathbb{N}$ / $a_c = 2^c a + 2^d K$ et $b'_c = 2^c b + 2^d c' K'$ c-à-d $a_c = 2^c(a + dK)$ et $b'_c = 2^c(b + dK')$ c-à-d $a_c = 2^c e$ et $b'_c = 2^c f$ où $e = a + dK$ et $f = b + dK'$ avec $2^c d = 2^c(e + f) \Rightarrow e + f = d$ donc $e$ et $f$ sont de parités opposées. Sans nuire à la généralité supp $e$ impair et $f$ pair.

- Si $f = 0$ alors $b'_c = 0$ et la démonstration est terminée.

- Sinon $\exists !$, $(g, h) \in \mathbb{N}^{*2}$ / $f = 2^g h$ avec $h$ impair.

les urnes ont alors respectivement $a_c = 2^c e$, $b'_c = 2^{c+g} h$ et $c$ billes

On montre en algèbre que $A = \{m \in \mathbb{N}^* \,/\, 2^m \equiv 1\, [b' + c]\}$ admet un plus petit elt non nul $n$ et que $A = n\mathbb{N}$ ainsi $\exists m \in \mathbb{N}$ / $2^m \equiv 1\, [b' + c]$ et $m > g$.

On fait alors $r = g$ fois l'opération sur $b'_c$ et $c$ pour obtenir $b'_{c+g} \equiv 2^g \cdot 2^c \times 2^{c+g} h\, [b'_{r+c}]$ [lecture incertaine — indices très surchargés] $\equiv 2^h h\, [b' + c]$ et $c_{m+g} \equiv c_{m+g} \times 2^{m+g}\, [b' + c]$

or $b < f$ alors $2^h h < 2^g f \Rightarrow b'_{r} < b' + c$ avec $0 \leq 2^h h < b' + c$ d'où $b'_{m+g} = 2^{c} h$ [lecture incertaine]

De plus $c_{mg}$ est impair car $c_{mg} = (b' + c) - b'_{mg}$ [lecture incertaine — « impair » sur « pair » raturé]

On pose à nouveau $a = a_c = 2^c e$, $b = b'_{m+g} = 2^h h$ [lecture incertaine — exposants] et $c = c_{mg}$ et on recommence en [2]. On a aussi $a + b = 2^d(e + f)$, $e+h$ étant pair (car $e, h$ sont impairs) en mettant $a+b$ sous la forme $2^{d'} f'$ le nouveau $c'$ sera plus grand que l'ancien car $(e+h)$ pair. Or la somme arithm reste tjrs invariante et cet $c'$ croit après chaque fois qu'on refait [2] et $d$ doit nécessairement décroître pour que $2^d d = a+b$ ne dépasse jamais $a+b+c$ : de cet impair [lecture incertaine] donc $d$ ne décroîtra jusqu'à 1. En refaisant 2 on aura $a'_c = 2^c e'_1$ et $b_0 = 2^g f$ avec $e + f = d = 1$ ; $e$ et $f$ sont de parités opposées l'un vaut 0 et l'autre

## Page 3

vaut 1 et ainsi, si ou $g$ [raturé] alors $e = 1$ et $f = 0$ (car $f$ est supposé pair sans nuire à la généralité) et donc $b = 0$ et la démonstration est achevée.

Application $a = 2$, $b = 3$, $c = 7$ (en suivant le processus démontré plus haut)

- $b, c$ impairs on fait l'opération sur $b$ et $c$ et on a : $2 \quad 6 \quad 4$

- $a, b, c$ impairs [sic — $a = 2$ est pair, lire plutôt « on traite d'abord le cas $a = 1$, $b = 3$, $c = 2$ »] on traite d'abord le cas $a = 1$, $b = 3$, $c = 2$

- $a$ et $b$ impairs on fait l'opération sur eux et on a : $2 \quad 2 \quad 2$

- $a, b, c$ impairs [sic — $2$ est pair] on traite d'abord le cas $a = 1$, $b = 1$, $c = 1$

- $a, b, c$ impairs [sic] on fait l'opération sur $a$ et $b$ et on a : $2 \quad 0 \quad 1$

- ainsi pour $a = 2$, $b = 2$, $c = 2$ on fait l'opération sur $a$ et $b$ et on a : $4 \quad 0 \quad 2$

- ainsi pour pour $(a, b, c) = (2, 6, 4)$ et suivant le m processus que pour $1, 3, 2$, on a successivement $2 \quad 6 \quad 4$ ($= 2(1 \quad 3 \quad 2)$)

$4 \quad 4 \quad 4$ ($= 2(2 \quad 2 \quad 2)$)

$8 \quad 0 \quad 4$ ($= 2(4 \quad 0 \quad 2)$)

Rq : Il existe pour ce cas des procédés bien plus simples. L'avantage avec celui utilisé (dont la validité a été démontrée plus haut) est qu'il permet d'arriver à la configuration où au moins l'une des urnes est vide quelque soit le cas de départ !

[signature raturée]

---

## Figures

Aucune figure sur les 3 pages (p.1 re-rendue à $r = 150$ et relue ; p.2 vérifiée visuellement au 2e passage le 2026-09-07 — rendu `/tmp/s9/urnes-2.png`, r150 — « $d$ est impair » surchargé, indices surchargés, « $c_{mg}$ impair car $(b'+c)-b'_{mg}$ » (« impair » sur « pair » raturé) confirmés, sans schéma ni tableau ; p.3 vérifiée visuellement au 2e passage le 2026-09-07 — rendu `/tmp/s16/urnes-p3-3.png`, r150 — « vaut 1 et ainsi, si ou $g$ [raturé] », application $a = 2$, $b = 3$, $c = 7$ ($2\;6\;4$, $2\;2\;2$, $2\;0\;1$, $4\;0\;2$, $4\;4\;4$, $8\;0\;4$), doubles « pour pour » conservés tels quels, remarque finale et signature raturée confirmés, sans schéma ni tableau) : énoncé et démonstration seuls.

## Vocabulaire

- **DE** : division euclidienne ($a' \equiv \beta\,[\delta] \Leftrightarrow a'$ reste de la DE de $\beta$ par $\delta$).
- **Invariant** : $a'+b' = a+b$ (puis $a+b+c$ sur les trois urnes).
- **Descente** : divisions par 2 et décroissance de $d$ (cas « 3 pairs » et « 1 impair »).
- **[0] / [1] / [2]** : étapes de la démonstration (notations du manuscrit).
