# Zêta de 4 — transcription fidèle

🧾 Source : [zeta-de-4.pdf](zeta-de-4.pdf) — 3 pages d'énoncé manuscrit (encre bleue, feuille perforée, photo).
🔍 Contenu : exercice (niveau Tle) — calcul de $\sum_{k=1}^{+\infty} 1/k^4 = \pi^4/90$ en trois parties : convergence d'une suite récurrente (A), lemme de Riemann-Lebesgue (B), intégrales $I_n$ et noyau de Dirichlet (C).
📄 Note : restauration Datas1 du 2026-09-07 — transcription à l'identique, sans correction ni ajout ; les erreurs du manuscrit sont signalées par [*sic*], les doutes de lecture par [lecture incertaine — …], les passages biffés par [raturé].

## Page 1

EXERCICE DE FOUELEF BRIOL. [lecture incertaine — nom propre]

LE CALCUL DU NOMBRE : $\sum_{k=1}^{+\infty} \frac{1}{k^4}$.

NIVEAU : Tle.

(Marge gauche : chiffres isolés « 695 », « 60 55 », « 86 » [lecture incertaine — chiffres isolés].)

EXERCICE.

Soit une suite $(U_n)_{n \ge 1}$ définie par son premier terme $U_1$, élément de $\mathbb{R}_+^*$ et par la relation de récurrence :

$\forall n \in \mathbb{N}^*$, $U_{n+1} = U_n + \dfrac{1}{(n+1)^4}$

PARTIE A : Consiste à vérifier la Convergence de $(U_n)$ et d'exprimer $(U_n)$ à l'aide du symbole $(\sum)$.

1) Étudier la monotonie de la suite $(U_n)_{n \ge 1}$.

2) Démontrer que $\forall n \in \mathbb{N}^*$, $U_n <$ [raturé — caractère biffé par surcharge] $\frac{4}{3}$

3) Conclure.

4) Exprimer $(U_n)$ à l'aide du symbole $(\sum)$

le but de l'exercice est donc de Démontrer que la limite de la suite $\left(\sum_{k=1}^{n} \frac{1}{k^4}\right)_{n \ge 1}$ Vaut $\frac{\pi^4}{90}$

PARTIE B : (le lemme de RIEMAN-LEBESGUE). [*sic* — RIEMANN]

Soit $a$ et $b$ deux réels et $\lambda \in \mathbb{R}_+^*$. Désignons par $f$ la fonction définie sur $[a,b]$ à valeurs réelles et de classe $C^1$ (c'est à dire fonction dérivable une fois et dérivée première continue).

## Page 2

le but de cette partie (B) est de Démontrer que : $\lim_{\lambda \to +\infty} \left[\int_a^b f(t)\sin(\lambda t)dt\right] = 0$

1) Démontrer que $\int_a^b f(t)\sin(\lambda t)dt = \int_a^b f'(t)\frac{\cos \lambda t}{\lambda}dt + \left[-\frac{\cos(\lambda t)}{\lambda}f(t)\right]_a^b$

2) a) Démontrer que $\left|\left[\frac{\cos(\lambda t)}{\lambda}f(t)\right]_a^b\right| \le \frac{1}{\lambda}(|f(a)| + |f(b)|)$

b) Sachant que pour toute fonction $g$, $|\int_a^b g(t)dt| \le \int_a^b |g(t)|dt$ Établir que $|\int_a^b f'(t)\frac{\cos(\lambda t)}{\lambda}dt| \le \frac{1}{\lambda}\int_a^b |f'(t)|dt$.

3) En Déduire que : $|\int_a^b f(t)\sin(\lambda t)dt| \le \frac{1}{\lambda}\left(|f(a)| + |f(b)| + \int_a^b |f'(t)|dt\right)$

4) Conclure.

PARTIE C : le but est d'exprimer $(U_n)$ en fonction de $n$ et Conclure.

Soit $(I_n)_{n \ge 0}$ la suite définie par : $I_n = \int_0^{\pi} t^n \cos(kt)dt$ où $k \in \mathbb{N}^*$.

1) Calculer $I_0$ et $I_1$ en fonction de $k$.

2) Établir une relation de récurrence entre $I_{n+2}$ et $I_n$

4) En déduire $I_2$, $I_3$ puis $I_4$ en fonction de $k$. [*sic* — numérotation : pas de 3)]

5) Trouver donc trois Réels $a, b$ et $c$ tous non nuls tels que : $\int_0^{\pi} (at^4 + bt^3 + ct^2)\cos(kt)dt = \frac{1}{k^4}$

## Page 3

6) soit $\forall n \in \mathbb{N}^*$ et $t \in \mathbb{R}$, $C_n(t) = \sum_{k=1}^{n} \cos(kt)$. Démontrer alors que : $C_n(t) = -\frac{1}{2} + \frac{\sin\left(\frac{2n+1}{2} \cdot t\right)}{2\sin\left(\frac{t}{2}\right)}$

7) Déduire de ce qui précède que : $\forall n \in \mathbb{N}^*$, $\sum_{k=1}^{n} \frac{1}{k^4} = \frac{\pi^4}{90} + \int_0^{\pi} g(t) \cdot \sin(\lambda t)dt$ [tranché au r250 (PDF p. 3, pas p. 2) — aucun facteur $1/\pi$ sur le manuscrit] où $\lambda = \frac{2n+1}{2}$ et $g$ une fonction définie et Continue sur $[0,\pi]$ que l'on précisera

8) a) montrer que $g$ est dérivable sur $]0,\pi[$. b) cette fonction $g$ est-elle de la classe $C^1$ ?

9) Déduire donc à l'aide du lemme de RIEMANN-LEBESGUE (Question 4 : partie B) que : [*sic* — Question 4 ?] $\lim_{n \to +\infty} \sum_{k=1}^{n} \frac{1}{k^4} = \frac{\pi^4}{90}$

10) Que Vaut donc le Nombre réel $\sum_{k=1}^{+\infty} \frac{1}{k^4}$.

par : F.B.L [lecture incertaine — initiales] (paraphe/signature)

## Figures

Aucune figure : 3 pages d'énoncé manuscrit seul (niveau Tle, exercice FOUELEF BRIOL), sans schéma ni graphe (transcription : questions 1)–10) ; confirmé p. 1 sur source le 2026-09-07 — PARTIE A/B, lemme de RIEMANN-LEBESGUE — rendu `/tmp/qas/` ; p. 2–3 relues le 2026-09-07 — rendu `/tmp/s11/`, 0 figure à reproduire). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- Tle : niveau Terminale ; PARTIE A : convergence de $(U_n)$ et expression en $\sum$ ; PARTIE B : lemme de RIEMANN-LEBESGUE.
- $U_{n+1} = U_n + 1/(n+1)^4$ ; $C_n(t) = \sum_{k=1}^n \cos(kt)$ ; $\lambda = (2n+1)/2$ ; $g$ : fonction auxiliaire $C^1$ par morceaux.
- $\sum_{k=1}^{+\infty} 1/k^4 = \pi^4/90$ : résultat visé ; F.B.L : initiales (paraphe).
