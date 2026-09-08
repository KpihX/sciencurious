# Séries entières factorielles — transcription fidèle

🧾 Source : [series-entieres-factorielles.pdf](series-entieres-factorielles.pdf) — 4 pages manuscrites, encre bleue.
🔍 Restauration : image restaurée Datas1 2026-09-07 (contraste/bleu atténués) ; lecture directe des pages, rien d'inventé.
📄 Contenu : question $\sum_{n \geq n_0} \frac{z^n}{(an+b)!}$, motivation, prérequis, évaluation par le critère de d'Alembert, calcul de $S_{a,b,n_0}(z)$ ramené à $S_{a,b}(z)$, cas $b = 0$ (conjecture racines de l'unité, démonstration), évaluation simplifiée pour $x \in \mathbb{R}$, cas $b \in \mathopen{]}0, a\mathclose{[}$, cas particuliers.

## Page 1

Soient $(a, b, n_0, z) \in \mathbb{N}^* \times \mathopen{[\![}0, a\mathclose{[\![} \times \mathbb{N} \times \mathbb{C}^*$ [lecture incertaine — la ligne du haut est partiellement coupée/raturée]

$$\sum_{n = n_0}^{+\infty} \frac{z^n}{(an+b)!} = ?$$

\* Motivation : Quand on s'intéresse à l'étude des séries et plus loin au calcul de leurs sommes, on rencontre très souvent la relation : « $\forall z \in \mathbb{C}^*$, $e^z = \sum_{n=0}^{+\infty} \frac{z^n}{n!}$ » et celle remarquable : « $e = \sum_{n=0}^{+\infty} \frac{1}{n!}$ ». Dans un souci d'extrapoler, on arrive à se demander ce qu'il en est des cas « $\sum_{n=0}^{+\infty} \frac{z^n}{(2n)!}$ », « $\sum_{n=0}^{+\infty} \frac{z^n}{(3n)!}$ » et plus généralement du cas présenté en amont.

\* Prérequis : - s'y connaître dans le domaine des nbres cplx et particulièrement dans le calcul des racines nièmes.

- s'y connaître en matière de séries de fonctions.

\* Évaluation de $\sum_{n \geq n_0} \frac{z^n}{(an+b)!}$ :

Considérons la série de fonctions $\sum_{n \geq n_0} \frac{z^n}{(an+b)!}$. Sot [raturé] Posons $u_n = \frac{z^n}{(an+b)!} = f_n(z)$, $\forall n \in \mathbb{N}$ ($n \geq n_0$).

On a : $\forall z \in \mathbb{C}^*$, $\left\lvert \frac{f_{n+1}(z)}{f_n(z)} \right\rvert = \frac{\lvert z \rvert}{(an+b+a) \times \dots \times (an+b+2) \times (an+b+1)} \xrightarrow[n \to +\infty]{} 0$ car $a \geq 1$

## Page 2

d'après le critère de D'Alembert, $\sum_{n \geq n_0} \frac{z^n}{(an+b)!}$ [lecture incertaine — début de ligne coupé par la reliure] converge.

\*\* Calcul de $S_{a,b,n_0}(z)$ :

On a : $S_{a,b,n_0}(z) = S_{a,b}(z) - \sum_{n=0}^{n_0-1} \frac{z^n}{(an+b)!}$ où $S_{a,b}(z) = \sum_{n=0}^{+\infty} \frac{z^n}{(an+b)!}$ ($\forall z \in \mathbb{C}$)

Le véritable tâche se résume alors à évaluer $S_{a,b}(z)$ plus simplement.

\*\*\* Calcul de $S_{a,b}(z)$

\*\*\*\* Cas $b = 0$

On a : $\sum_{n=0}^{+\infty} \frac{z^n}{n!} = e^z$, $\sum_{n=0}^{+\infty} \frac{z^{2n}}{(2n)!} = \frac{1}{2}\left(e^z + e^{-z}\right)$

on peut alors conjecturer que :

$\sum_{n=0}^{+\infty} \frac{(z)^{an}}{(an)!} = \frac{1}{a} \sum_{k=0}^{a-1} e^{z j_a^k}$ où $j_a^k$, $k \in \mathopen{[\![}0, a-1\mathclose{]\!]}$ sont les racines $a$-ième de l'unité (avec $j_a = e^{i\frac{2\pi}{a}}$)

Ainsi la conjecture s'étend à : $\sum_{n=0}^{+\infty} \frac{z^n}{(an)!} = \sum_{n=0}^{+\infty} \frac{(z^{1/a})^{an}}{(an)!} = \sum_{k=0}^{a-1} e^{z^{1/a} j_a^k}$ [*sic* — facteur $1/a$ manquant devant la somme, cf. formule démontrée p. 3] (où $z^{1/a} = r^{1/a} e^{i\theta/a}$ avec $r e^{i\theta} =$ écriture exponentielle de $z$)

\*\*\*\*\* Démonstration de la conjecture initiale

On a : $\frac{1}{a} \sum_{k=0}^{a-1} e^{z j_a^k} = \sum_{k=0}^{a-1} \sum_{n=0}^{+\infty} \frac{z^n j_a^{kn}}{n!} = \frac{1}{a} \sum_{n=0}^{+\infty} \frac{z^n}{n!} \sum_{k=0}^{a-1} (j_a^n)^k$

- Si $n \equiv 0 [a]$, $\sum_{k=0}^{a-1} (j_a^n)^k = \sum_{k=0}^{a-1} 1 = a$

- Sinon, $\sum_{k=0}^{a-1} (j_a^n)^k = \frac{1 - j_a^{na}}{1 - j_a^n} = 0$

## Page 3

$\frac{1}{a} \sum_{k=0}^{a-1} e^{z j_a^k} = \frac{1}{a} \sum_{m=0}^{+\infty} \frac{z^{am}}{(am)!} \times a = \sum_{m=0}^{+\infty} \frac{z^{am}}{(am)!}$ CQFD

$\sum_{k=0}^{+\infty} \frac{z^n}{(an)!} = e_a(z^{1/a}) = \frac{1}{a} \sum_{k=0}^{a-1} e^{z^{1/a} j_a^k}$ où $j_a = e^{i\frac{2\pi}{a}}$ [*sic* — indice $k$ au lieu de $n$ sous le $\sum$] [lecture incertaine — fin de ligne coupée : « si $z = r e^{i\theta}$ »]

\*\*\*\* Évaluation simplifiée de $e_a(x)$ pour $x \in \mathbb{R}$

Si $a \equiv 0 [2]$, $\{j_a^k\}_{k \in \mathopen{[\![}0, a-1\mathclose{]\!]}} = \{-1, 1, j_a^k, \bar{j}_a^k\}_{k \in \mathopen{[\![}1, \frac{a}{2}-1\mathclose{]\!]}}$ [lecture incertaine — ligne dense et raturée]

Ainsi $e_a(x) = \frac{1}{a}\left(e^x + e^{-x} + \sum_{k=1}^{\frac{a}{2}-1} e^{x \cos\frac{2k\pi}{a}} \times 2\cos\left(x \sin\frac{2k\pi}{a}\right)\right)$ [lecture incertaine — exposants/indices denses]

$$e_a(x) = \frac{1}{a}\left(e^x + e^{-x} + \sum_{k=1}^{\frac{a}{2}-1} e^{x \cos\frac{2k\pi}{a}} \times 2\cos\left(x \sin\frac{2k\pi}{a}\right)\right)$$

Si $a \equiv 1 [2]$, $\{j_a^k\}_{k \in \mathopen{[\![}0, a-1\mathclose{]\!]}} = \{1, j_a^k, \bar{j}_a^k\}_{k \in \mathopen{[\![}1, \frac{a-1}{2}\mathclose{]\!]}}$

Ainsi on obtient de même, $e_a(x) = \frac{1}{a}\left(e^x + \sum_{k=1}^{\frac{a-1}{2}} e^{x \cos\frac{2k\pi}{a}} \times 2\cos\left(x \sin\frac{2k\pi}{a}\right)\right)$

\*\*\*\* Cas particuliers

$\sum_{n=0}^{+\infty} \frac{(in)^n}{n!} = e_1(i e^{i\frac{\pi}{2}})$ [lecture incertaine — formule dense] $= \frac{1}{1}(e^{i\cdot 1} + 0) = e^{-1}$ [lecture incertaine — passage elliptique]

$\sum_{n=0}^{+\infty} \frac{1}{(3n)!} = e_3(e^{i\frac{0}{3}})$ [lecture incertaine] $= \frac{1}{3}\left(e + e^{-1 \times \cos\frac{2\pi}{3}} \times 2\cos(1 \times \sin\frac{2\pi}{3})\right) = \frac{1}{3}\left(e + e^{1/2} \times 2\cos\frac{\sqrt{3}}{2}\right)$ [lecture incertaine — reconstitution au mieux de l'écriture dense]

\*\*\*\*\* Rq : $e_1 = \exp$, $e_2 = \mathrm{ch}$

## Page 4

\*\*\*\* Cas $b \in \mathopen{]}0, a\mathclose{[}$

Considérons cette fois $e_{a,b}(z) = \frac{1}{a} \sum_{k=0}^{a-1} e^{z j_a^k} \times (j_a^k)^{-b}$ [lecture incertaine — exposant dense]

On a : $e_{a,b}(z) = \frac{1}{a} \sum_{k=0}^{a-1} (j_a^k)^{-b} \sum_{n=0}^{+\infty} \frac{(z j_a^k)^n}{n!} = \frac{1}{a} \sum_{n=0}^{+\infty} \frac{z^n}{n!} \sum_{k=0}^{a-1} j_a^{k(n-b)}$ [lecture incertaine]

on montre de même que $S$ est non nulle et vaut $a$ pour $n \in b[a]$ d'où $e_{a,b}(z) = \frac{1}{a} \sum_{n=0}^{+\infty} \frac{z^{an}}{(an+b)!} \times a = \sum_{n=0}^{+\infty} \frac{z^{an}}{(an+b)!}$.

Ainsi $S_{a,b}(z) = \sum_{n=0}^{+\infty} \frac{z^n}{(an+b)!} = \sum_{n=0}^{+\infty} \frac{(z^{1/a})^{an}}{(an+b)!} = e_{a,b}(z^{1/a}) = \frac{1}{a} \sum_{k=0}^{a-1} e^{z^{1/a} j_a^k} (j_a^k)^{-b}$ où $z^{1/a} =$ [coupé]

où $z^{1/a} = r^{1/a} e^{i\theta/a}$

\*\*\*\*\* Rq : $z^{1/a}$, $j_a^k$ ($k \in \mathopen{[\![}0, a-1\mathclose{]\!]}$) (où $j_a = e^{i\frac{2\pi}{a}}$) sont les racines $a$-ième de $z$ dans $\mathbb{C}$

\*\*\*\* Évaluation simplifiée de $e_{a,b}(x)$ pour $x \in \mathbb{R}$

- Si $a \equiv 0 [2]$, $e_{a,b}(x) = \frac{2}{a}\left(e^x + e^{-x} e^{i\pi b} + \sum_{k=1}^{\frac{a}{2}-1} e^{x \cos\frac{2k\pi}{a}} \times e^{-i\frac{2k\pi b}{a}} \times e^{x \cos\ldots} \times e^{\ldots}\right)$ [lecture incertaine — ligne très dense, partiellement masquée par le pouce]

$$= \frac{1}{a\, x^b}\left((e^x + (-1)^b e^{-x}) + 2\sum_{k=1}^{\frac{a}{2}-1} e^{x \cos\frac{2k\pi}{a}} \times 2\cos\left(x \sin\frac{2k\pi}{a} - \frac{2k\pi b}{a}\right)\right)$$ [lecture incertaine — reconstitution au mieux]

- Si $a \equiv 1 [2]$, $e_{a,b}(x) = \frac{1}{a x^b}\left(e^x + 2\sum_{k=1}^{\frac{a-1}{2}} e^{x \cos\frac{2k\pi}{a}} \cos\left(x \sin\frac{2k\pi}{a} - \frac{2k\pi b}{a}\right)\right)$ [lecture incertaine]

\*\*\*\*\* Cas particuliers

$\sum_{n=0}^{+\infty} \frac{(in)^n}{(2n+1)!}$ [lecture incertaine] $= e_{2,1}(-1) = \frac{1}{2i \cdot 1^1}(e^1 - e^{-1})$ ; $e_{2,1}(e^{i\frac{\pi}{2}}) = e_{2,1}(i)$

$= \frac{1}{2}\left(e^i e^{-i\pi/2} + e^{-i} e^{i\pi/2} \times i^{-(1+1)}\right)$ [lecture incertaine — formule très dense] $= i \cdot \frac{e - e^{-1}}{2} \sin 1$ [lecture incertaine]

$e^{i(b+1)\pi} + e^{i(b-1)\pi} \times (b-i)^{-2}$ [lecture incertaine — fragment isolé en bas de page]

## Figures

Aucune figure : 4 pages de texte manuscrit seul, sans schéma ni graphe (transcription : lecture directe, rien d'inventé ; confirmé p. 1 sur source le 2026-09-07 — question, Motivation, Prérequis — rendu `/tmp/qas/` ; p. 2–4 relues le 2026-09-07 — rendu `/tmp/s11/`, 0 figure à reproduire). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- $S_{a,b,n_0}(z) = \sum_{n \ge n_0} z^n/(an+b)!$ ; $S_{a,b}(z)$, $e_{a,b}(z)$ : sommes réduites.
- $j_a = e^{i2\pi/a}$ : racine $a$-ième de l'unité ; $z^{1/a} = r^{1/a}e^{i\theta/a}$.
- d'Alembert : critère utilisé ; cas $b = 0$, $b \in \mathopen{]}0,a\mathclose{[}$, $a$ pair/impair.
