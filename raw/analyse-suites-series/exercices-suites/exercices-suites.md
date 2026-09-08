# Exercices suites — transcription fidèle

> 🧾 **Manuscrit original :** `exercices-suites.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** énoncés à l'encre bleue, écriture rapide et formules compactes en `[lecture incertaine — …]` ; marges rognées avec fragments de feuilles voisines (non transcrits) ; « 1000 » en haut à droite de la page 2 ; aucune figure à reproduire. Transcrit mot à mot.
> 📄 **Source scannée :** [exercices-suites.pdf](exercices-suites.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

[fragments d'une feuille voisine en marge gauche (« 2000 », « il suffit », « $1/n$ », …), non transcrits ; marge droite rognée (« $\pi/4 = 1\ldots$ », « Étude… »), non transcrits]

Ex : le but de l'exercice est de donner une méthode simple permettant d'avoir de bonnes approximations de $\pi$.

On va alors dq $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \ldots + \frac{(-1)^k}{2k+1} + \ldots = \sum_{k=1}^{+\infty} \frac{(-1)^k}{2k+1}$ [lecture incertaine — borne « $k = 1$ »].

On considère $S(x) = \sum_{n=1}^{+\infty} \frac{\sin nx}{n}$, $x \in \mathbb{R}$. On va calculer $S(\pi/2)$ de 2 façons.

1/ Mq $S(\pi/2) = \sum_{k=1}^{+\infty} \frac{(-1)^k}{2k+1}$ [raturé ; lecture incertaine — borne « $k = 1$ »].

2/ a/ En remarquant que $\sin x = \mathrm{Im}\left(e^{ix}\right)$ ($x \in \mathbb{R}$), mtq $S(x) = \mathrm{Im}\left(\sum_{n=1}^{+\infty} \frac{e^{inx}}{n}\right)$.

b/ En admettant que $\forall x \in \mathbb{R}$, $\sum_{n=1}^{+\infty} \frac{x^n}{n} = -\ln(1-x)$, mtq $S(x) = -\mathrm{Im}\ln(1-e^{ix})$.

c/ Écrire $1-e^{ix}$ sous la forme $ae^{ib}$, $a, b \in \mathbb{R}$ (on prendra $-i = e^{-i\pi/2}$). Préciser $a$ et $b$.

d/ Écrire $\ln(1-e^{ix})$ sous la forme $c+id$ (Préciser $c$ et $d$).

e/ Déduire une autre expression de $S(x)$.

3/ En remplaçant $x$ par $\pi/2$ dans la précédente expression de $S(x)$, déduire que $\underline{\frac{\pi}{4} = 1 - \frac{1}{3} + \ldots + \frac{(-1)^k}{2k+1} + \ldots}$.

## Page 2

[« 1000 » en haut à droite]

Ex : pour évaluer $S_m(n) = 1^m + 2^m + \ldots + n^m = \sum_{k=0}^{n} k^m$ [lecture incertaine — « $S_m(n)$ »], $m, n \in \mathbb{N}$ (et profiter pour faire la rq $(1+\ldots+n)^2 = 1^3+\ldots+n^3$ et justifier).

1/ Que valent $S_0(n)$ et $S_1(n)$ ?

On considère $R_m(n) = \sum_{k=1}^{n} (k+1)^{m+1} - k^{m+1}$, $n \ge 1$ (p. 2 relue le 2026-09-07, rendu `/tmp/s10/`).

2/ En remarquant que c'est une somme télescopique, simplifier $R_m(n)$.

3/ En appliquant le binôme de Newton sur $(k+1)^{m+1}$, mtq $R_m(n) = \sum_{k=0}^{m} C_{m+1}^k S_k(n)$ [lecture incertaine — indices du binôme].

4/ Déduire des questions précédentes une relation de récurrence liant $S_m(n)$ à $S_{m-1}(n) \ldots S_0(n)$.

5/ Évaluer alors $S_2(n)$ puis $S_3(n)$. Conclure alors que $\underline{(1+\ldots+n)^2 = 1^3+\ldots+n^3}$.

Ex : On désire évaluer en fonction de $n$ le terme général d'une suite linéaire d'ordre 2 définie par récurrence. Soit $(U_n)$ : $\begin{cases} U_0, U_1 \text{ connus} \\ \forall n \in \mathbb{N},\ U_{n+2} = aU_{n+1} + bU_n,\ a, b \in \mathbb{R} \end{cases}$.

1/ Chercher des solutions canoniques de la forme $r^n$ où $r$ est à déterminer. Remplacer dans la relation de récurrence pour aboutir au polynôme caractéristique $p(r)$ (à préciser) vérifiant $p(r) = 0$.

2/ Résoudre suivant les valeurs de $a$ et $b$, l'éqn $p(r) = 0$.

a/ Dans le cas où on a 2 solutions $r_1 \ne r_2$, mtq $\forall n \in \mathbb{N},\ U_n = \alpha r_1^n + \beta r_2^n$, $\alpha, \beta \in \mathbb{R}$.

b/ Dans le cas où on a une racine double $r_0$, mtq $\forall n \in \mathbb{N},\ U_n = (\alpha n + \beta) r_0^n$.

c/ Dans le cas où on a 2 solutions complexes $r \pm iw$ mtq $U_n = r^n(\alpha \cos wn + \beta \sin wn)$, $\alpha, \beta \in \mathbb{R}$ (on pourra s'aider du principe d'induction).

d/ Dans chaque cas, déterminer $\alpha$ et $\beta$ en fonction de $U_0$ [fin de ligne rognée — « en fonction de $U_0$ [et $U_1$] »].

## Figures

Aucune figure : 2 pages d'énoncés manuscrits seuls, sans schéma ni graphe (transcription § Statut : « aucune figure à reproduire » ; confirmé p. 1 sur source le 2026-09-07 — approximation de $\pi/4$, rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07, rendu `/tmp/s10/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- Mtq : montrons que ; Ex : exercice ; 1/–5/, a/–d/ : numérotation des questions.
- $S_m(n) = \sum_{k=1}^n k^m$ ; $R_m(n)$ : somme télescopique auxiliaire ; $C_{m+1}^k$ : coefficients du binôme.
- $r^n$ : solutions canoniques ; $p(r)$ : polynôme caractéristique ; $r_0$ : racine double.
