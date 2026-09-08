# Densité de la partie fractionnaire de racine — transcription fidèle

> 🧾 **Manuscrit original :** `densite-partie-fractionnaire-racine.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** écriture rapide à l'encre bleue, abréviations (« mtrer ») et calculs compacts en `[lecture incertaine — …]` ; deux ratures conservées ; aucune figure à reproduire. Transcrit mot à mot.
> 📄 **Source scannée :** [densite-partie-fractionnaire-racine.pdf](densite-partie-fractionnaire-racine.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Exo : $A = \{\sqrt{n} - E(\sqrt{n}),\ n \in \mathbb{N}\}$ est dense dans $[0, 1]$ pour la distance canonique $|.|$ sur $\mathbb{R}$.

Soit $x \in [0, 1]$.

Pour montrer cela il suffit de mtrer $\exists\, (a_n)_n \in A^{\mathbb{N}}$ / $a_n \longrightarrow x$, mieux encore que $\forall r > 0,\ \exists\, a_r \in A$ / $|x - a_r| < r$. Pour avoir ce dernier résultat, il suffit d'établir que $\forall x, y \in [0, 1],\ \exists\, a \in A$ / $x < a < y$ [raturé : « ou que »]. Soient alors $x, y \in [0, 1]$. Cherchons [raturé] $a \in A$ / $x < a < y$.

Notation : dans la suite, $\forall n \in \mathbb{N},\ d_n = \sqrt{n} - E(\sqrt{n})$.

Rq : $\forall n \in \mathbb{N},\ d_n = 0 \iff \sqrt{n} \in \mathbb{N}$.

• Soit $m \in \mathbb{N}$. $\forall n \in [\![m^2, (m+1)^2[\![,\ m = E(\sqrt{n}) \implies d_n = \sqrt{n} - m$.

d'où $(d_n)_n$ est croissante [raturé : « stricte »] sur $[\![m^2, m+1[\![$ [lecture incertaine — borne « $m+1$ », le contexte suggère « $(m+1)^2$ »].

On va alors chercher $a$ de la forme $\sqrt{n} - m$ où $m$ et $n$ sont à déterminer et doivent vérifier $m^2 \le n < (m+1)^2$.

Soient $m, n \in \mathbb{N}$ / $x < \sqrt{n} - m < y$ (I)

$$(I) \iff x + m < \sqrt{n} < y + m \iff (x+m)^2 < n < (y+m)^2.$$

Pour qu'il y ait [raturé : « ait … que »] que $n$ existe il faut et il suffit que $(y+m)^2 - (x+m)^2 > 1$ (I').

## Page 2

et si une telle condition est vérifiée on aura bien $m^2 \le (x+m)^2 < n < (y+m)^2 \le (m+1)^2$

d'où $m = E(\sqrt{n})$.

Il suffit alors juste de chercher $m$ vérifiant (I').

$$(I') \iff (y + x + 2m)(y - x) > 1 \iff m > \frac{1}{y-x} - (y+x) = \frac{1 + x^2 - y^2}{y-x} \ge 0.$$ [lecture incertaine — numérateur, le calcul donne « $1 + x^2 - y^2$ »] [*sic* — facteur $1/2$ omis dans le manuscrit].

En prenant alors $m = E\left(\frac{1}{y-x} - (y+x)\right) + 2$ [lecture incertaine — dernier chiffre, « $2$ » (p. 2 relue le 2026-09-07, rendu `/tmp/s10/`, « $1$ » peu probable)]

et $n$ l'un des entiers dans $](x+m)^2, (y+m)^2[$ qui existe bien car que $(y+m)^2 - (x+m)^2 > 1$ on a bien $m^2 \le n < (m+1)^2 \iff m = E(\sqrt{n})$ et au final $x < \sqrt{n} - m < y \iff d_n \in ]x, y[$.

Il suffit alors de prendre $a = d_n$.

Rq : $n = \begin{cases} E((y+m)^2) \text{ si } y \in ]0, 1[ \text{ où } m = E\left(\frac{1}{y-x} - (y+x)\right) + 1 \\ y + m - 1 \text{ sinon} \end{cases}$ [lecture incertaine — dernier chiffre, « $1$ » ou « $2$ »] [lecture incertaine — second cas]

[raturé : signature].

## Figures

Aucune figure : 2 pages de texte manuscrit seul, sans schéma ni graphe (transcription § Statut : « aucune figure à reproduire » ; confirmé p. 1 sur source le 2026-09-07, rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07, rendu `/tmp/s10/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- mtrer : montrer (graphie du manuscrit) ; Rq : remarque ; Exo : exercice.
- $E(x)$ : partie entière ; $d_n = \sqrt{n} - E(\sqrt{n})$ : partie fractionnaire ; $A = \{d_n\}$ : ensemble étudié.
- $(I)$ : encadrement $x < \sqrt{n}-m < y$ ; $(I')$ : condition d'écart $> 1$ garantissant l'existence de $n$.
