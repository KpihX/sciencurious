# Inéquation fonctionnelle $f(n+1) \geq f(f(n)) + 1$ — transcription fidèle

> 🧾 **Manuscrit original :** `inequation-fonctionnelle.pdf` (énoncé dactylographié 1 page + solution manuscrite 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à 100 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`inequation-fonctionnelle.pdf`](inequation-fonctionnelle.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Exercice 3 : Inéquation fonctionnelle [titre bleu]

On veut déterminer toutes les fonctions $f : \mathbb{N} \to \mathbb{R}$ telles que $\forall n \in \mathbb{N}$, $f(n+1) \geq f(f(n)) + 1$.

1. **Analyse** : Soit $f$ une telle fonction.
   (a) Montrer que $\forall n \in \mathbb{N}$, $\forall m \in \mathbb{N}$, $m \geq n \Rightarrow f(m) \geq n$.
   (b) En déduire que $f$ est strictement croissante : $\forall n \in \mathbb{N}$, $f(n+1) > f(n)$.
   (c) Montrer que $\forall n \in \mathbb{N}$, $f(n) < n + 1$, et conclure l'analyse.
2. Effectuer la synthèse du problème.

## Page 2

Ex : (If) $f : \mathbb{N} \to \mathbb{R} \mid \forall n \in \mathbb{N}$, $f(n+1) \geq f(f(n)) + 1$ (I)

Contraintes : Puisque $f$ définie sur $\mathbb{N}$ et que (I) fait intervenir $f(f(n))$ alors [raturé] (I) existe ssi $\forall n \in \mathbb{N}$ ($n \in \mathbb{N}$) $f(n) \in \mathbb{N}$.

A/ a) Soit $n \in \mathbb{N}$. Mt par rec $P(n)$ : $\forall m \in \mathbb{N}$, $m \geq n \Rightarrow f(m) \geq n$.

Pour $n = 0$, soit $m \in \mathbb{N}$. Vu que $f(m) \in \mathbb{N}$ alors $f(m) \geq 0$ d'où $P(1)$ vraie [*sic* — lire $P(0)$].

Supp que pour $n \in \mathbb{N}$, $P(n)$ est vraie et mtq que $P(n+1)$ l'est aussi. Soit $m \in \mathbb{N} \mid m \geq n+1$ ; (I) $\Rightarrow f(m) \geq f(f(m-1)) + 1$ car $m \geq 1$. Or $m-1 \geq n \Rightarrow f(m-1) \geq n$ d'après l'hypothèse de rec [d'où $m-1 \in \mathbb{N}$] $\Rightarrow f(f(m-1)) \geq n$ d'après cette même hypothèse et vu que $f(m-1) \in \mathbb{N}$ $\Rightarrow f(f(m-1)) + 1 \geq n+1$. Ainsi (I) $\Rightarrow f(m) \geq f(f(m-1)) + 1 \geq n+1 \Rightarrow f(m) \geq n+1$. D'où $P(n+1)$ vraie.

① : $\forall m, n \in \mathbb{N}$, $m \geq n \Rightarrow f(m) \geq n$.

b/ Déduction. Soit $n \in \mathbb{N}$. (I) $\Rightarrow f(n+1) \geq f(f(n)) + 1$. Or $f(n) \in \mathbb{N}$ et car $f(n) \geq f(n)$ [lecture incertaine — probablement $f(n) \geq n$] alors $f(f(n)) \geq f(n)$ d'après ①. Ainsi (I) $\Rightarrow f(n+1) \geq f(n) + 1 \Rightarrow f(n+1) > f(n)$. Ainsi $f$ strict croissante.

c/ $*$ Soit $n \in \mathbb{N}$. Mtq $f(n) < n+1$. On a : (I) $\Rightarrow f(n+1) > f(f(n)) \Rightarrow n+1 > f(n)$ car $f$ strict croissante.

$*$ Conclusion. Soit $n \in \mathbb{N}$. D'après ①, $m = n \Rightarrow f(n) \geq n$. D'après ②, $f(n) < n+1 \Rightarrow f(n) \leq n$. Donc $f(n) = n$ $\forall n \in \mathbb{N}$.

## Page 3

2/ Synthèse : En (1) on a montré que $f$ sol de (I) $\Rightarrow \forall n \in \mathbb{N}$, $f(n) = n$.

Réciproquement Pour toute fonction $g : \mathbb{N} \to \mathbb{R}$, $n \mapsto g(n)$ [lire $g(n) = n$], on a : $g(n+1) = n+1$ [raturé — caractère biffé] $= g(n) + 1 = g(g(n)) + 1$ d'où $g(n+1) \geq g(g(n)) + 1$. Ainsi $g$ sol de (I). Donc les solutions de (I) sont les fonctions $g : \mathbb{N} \to \mathbb{R}$, $n \mapsto n$.

---

## Figures

Aucune figure ni schéma : énoncé dactylographié + preuve textuelle (page 2 relue ; pages 1 et 3 non relues — limite des 20 pages).

## Vocabulaire

- Mt/mtq = montre/montrons que ; rec = récurrence ; ①② = jalons de preuve ; (I) = l'inéquation ; sol = solution.
