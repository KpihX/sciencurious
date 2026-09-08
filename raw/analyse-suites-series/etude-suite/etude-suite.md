# Étude de suite — transcription fidèle

> 🧾 **Manuscrit original :** `etude-suite.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** écriture rapide à l'encre bleue, haut de la page 1 et bord droit rognés ; calculs compacts par endroits en `[lecture incertaine — …]` ; une rature conservée ; aucune figure à reproduire. Transcrit mot à mot.
> 📄 **Source scannée :** [etude-suite.pdf](etude-suite.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

[haut de page rogné] TD : $(U_n)_{n \in \mathbb{N}^*}$ : $\begin{cases} U_1 = 3 \\ U_{n+1} = \dfrac{(n+2)U_n + 2(n^2+n-1)}{(n+1)^2} \end{cases}$ [lecture incertaine — indice du terme initial ($U_1 = 3$)] [lecture incertaine — l'indice « $n \ge 1$ » supposé, haut de page rogné].

1/ $(U_n) \searrow$.

$\forall n \in \mathbb{N}^*,\ U_{n+1} - U_n = \dfrac{(n+2)U_n + 2(n^2+n-1) - (n+1)^2 U_n}{(n+1)^2}$

$$= \dfrac{U_n(n^2-n+1) + 2(n^2+n-1)}{(n+1)^2}$$ [lecture incertaine — coefficient de $U_n$, « $n^2-n+1$ »]
$$= \dfrac{(n^2+n-1)(2-U_n)}{(n+1)^2}.$$ [lecture incertaine — « $n^2+n-1$ » ou « $n^2-n-1$ »]

[bord droit rogné — « Donc … » coupé]

$*$ Mq $\forall n \in \mathbb{N}^*,\ U_n - 2 > 0$.

— $U_1 = 3 > 2$.

— Si pour $n \in \mathbb{N}^*$, $U_n - 2 > 0$ alors $U_{n+1} - 2 = \dfrac{(n+2)U_n + 2(n^2+n-1)}{(n+1)^2} - 2$

$$= \dfrac{(n+2)U_n - 2n - 4}{(n+1)^2} = \dfrac{(n+2)(U_n-2)}{(n+1)^2} > 0.$$

Donc $\forall n \in \mathbb{N}^*,\ U_n > 2$.

ainsi $U_{n+1} - U_n < 0$. Donc [bord droit rogné — fin de ligne coupée].

2/ $(U_n)$ est $\searrow$ et minorée par $2$ donc elle converge.

3/ Car $U_n \to l$ alors la sous-suite $U_{n+1} \to l$.

on a alors [raturé] $U_{n+1} - U_n = \dfrac{(n^2+n-1)(2-U_n)}{(n+1)^2}$ [lecture incertaine — « $n^2+n-1$ » ou « $n^2-n-1$ »] $\implies \lim(U_{n+1} - U_n) = \lim \dfrac{(n^2+n-1)(2-U_n)}{(n+1)^2}$

$$\implies l - l = 1 \times (2 - l) \implies \underline{l = 2}.$$

## Page 2

4/ $U_n = f(n)$ (question 4, p. 2 relue le 2026-09-07, rendu `/tmp/s10/`).

$\forall n \in \mathbb{N}^*$, d'après ① [lecture incertaine — renvoi], $U_{n+1} - 2 = \dfrac{(n+2)(U_n-2)}{(n+1)^2}.$

[raturé : « donc »]

ainsi $\forall n \in \mathbb{N}^*$ [lecture incertaine — parenthèse « $(n \ge 1)$ »], $U_n - 2 = \dfrac{(n+1)(U_{n+1}-2)}{n^2}$ [lecture incertaine — « $U_{n+1}$ », le sens de la récurrence suggère « $U_{n-1}$ »]

$$= \dfrac{(n+1)}{n^2} \times \dfrac{(n)}{(n-1)^2} (U_{n+1}-2)$$ [lecture incertaine — « $U_{n+1}$ », cf. ci-dessus]
$$= \dfrac{(n+1) \times n \times \ldots \times (2+1)}{n^2 (n-1)^2 \times \ldots \times 2^2} (U_{2-1}-2)$$ [lecture incertaine — « $2+1$ » ou « $2-1$ », la ligne suivante porte « $U_1-2$ »]
$$= \dfrac{(n+1)!\ (U_1-2)}{2 \times n!^2}.$$

Donc $\forall n \in \mathbb{N}^*$ [lecture incertaine — parenthèse], $U_n = 2 + \dfrac{(n+1)!}{2n!^2}$ [raturé : fraction résiduelle en « $\frac{\ldots}{2n!}$ »] (souligné).

## Figures

Aucune figure : 2 pages de texte manuscrit seul, sans schéma ni graphe (transcription § Statut : « aucune figure à reproduire » ; confirmé p. 1 sur source le 2026-09-07, rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07, rendu `/tmp/s10/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- TD : travail dirigé ; $\searrow$ : décroissante ; minorée par $2$ ; $l = 2$ : limite (soulignée).
- ① : renvoi interne du manuscrit ; $f(n)$ : intitulé de question [lecture incertaine].
- $U_n - 2$ : écart à la limite, formule télescopée en factorielles.
