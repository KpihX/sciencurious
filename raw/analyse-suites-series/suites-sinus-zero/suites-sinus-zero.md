# Suites sinus nulles — transcription fidèle

> 🧾 **Manuscrit original :** `suites-sinus-zero.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** deux séries en $\sin$ étudiées ; bornes de sommes et congruences en `[lecture incertaine — …]`, bas de la page 2 coupé au scan (signalé). Transcrit mot à mot.
> 📄 **Source scannée :** [suites-sinus-zero.pdf](suites-sinus-zero.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

* $\sum_{n \geq 0} U_n$ où $U_n = \sin(\pi(2+\sqrt{3})^n)$.

$\forall n \in \mathbb{N},\ (2+\sqrt{3})^n + (2-\sqrt{3})^n = \sum_{k=0}^n C_n^k 2^{n-k}(\sqrt{3})^k + \sum_{k=0}^n C_n^k 2^{n-k}(-1)^k(\sqrt{3})^k$

$$= \sum_{0 \leq k \leq n/2} C_n^{2k} 2^{n-2k}3^k + \sum_{0 \leq k \leq (n-1)/2} C_n^{2k+1} 2^{n-2k-1}3^k \times \sqrt{3} \text{ [lecture incertaine — bornes supérieures des sommes]}$$
$$+ \sum_{0 \leq k \leq n/2} C_n^{2k} 2^{n-2k}3^k + \sum_{0 \leq k \leq (n-1)/2} C_n^{2k+1} 2^{n-2k-1} \times 3^k \times \sqrt{3}$$

$$= 2A_n \text{ où } A_n = \sum_{0 \leq k \leq n/2} C_n^{2k} 2^{n-2k}3^k \in \mathbb{N}.$$

Ainsi $U_n = \sin(2\pi A_n - \pi(2-\sqrt{3})^n) = -\sin(\pi(2-\sqrt{3})^n) \sim_{+\infty} -\pi(2-\sqrt{3})^n$.

Car $-1 \in \mathbb{R}^*$ et $0 \leq 2-\sqrt{3} \leq 1$ alors d'après la règle « $q^n$ » [lecture incertaine — nom de la règle entre guillemets], $\sum_{n \geq 0} U_n$ converge.

* $\sum_{n \geq 0} U_n$ où $U_n = \sin(\pi\underbrace{n!e^{-2}}_{V_n})$.

$\forall n \in \mathbb{N},\ V_n = \sum_{k=0}^n \frac{(-1)^k n!}{k!} + \underbrace{\sum_{k \geq n+2} \frac{(-1)^k n!}{k!}}_{W_n}$ car $e^{-2} = \sum_{k \geq 0} \frac{(-1)^k}{k!}$.

On a : $|W_n| \leq \sum_{k \geq n+2} \frac{n!}{A_k} = \frac{1}{n+1} + \sum_{k \geq n+2} \frac{1}{A_k}$ [lecture incertaine — dénominateurs notés $A_k$]

$$\leq \frac{1}{n+1} + \sum_{k \geq n+2} \frac{1}{k(k-1)} = \frac{1}{n+1} + \lim_{m \to +\infty}\sum_{k=n+2}^m\left(\frac{1}{k-1} - \frac{1}{k}\right)$$
$$\leq \frac{1}{n+1} + \frac{1}{n+1} - 0 = \frac{2}{n+1}.$$

Ainsi $\lim_{n \to +\infty} W_n = 0$.

## Page 2

Alors $V_n = \underbrace{\sum_{k=0}^n (-1)^k A_n}_{A_n \in \mathbb{Z}}\left(1 + W_n \times \underbrace{\frac{1}{n!\sum_{k=0}^n \frac{(-1)^k}{k!}}}_{d_n}\right)$ [lecture incertaine — factorisation et dénominateur].

Or $\lim_{n \to +\infty} d_n = 0 \times \frac{1}{0! \times e^{-2}} = 0$ [lecture incertaine — dénominateur], ainsi $V_n \sim_{+\infty} A_n\sum_{k=0}^n (-1)^k A^{n-k}$ [lecture incertaine — fin de formule].

Mieux encore, $U_n = \sin(\pi A_n + \pi W_n)$.

Or $A_n \equiv 1\ [2]$ pour $n$ pair car dans ce cas, $A_n^{n-n} \equiv 1\ [2]$ [lecture incertaine — modulo noté « $[?]$ », lu comme $[2]$], et $A_n^k \equiv 0\ [2]$, $\forall k \in [0;n[$.

Pour $n$ impair, $A_n \equiv \sum_{k=0}^{n-1}(-1)^k A_n^{n-k} + (-1)^n \times n + (-1)^n \times 1 \equiv 0\ [2]$ [lecture incertaine — indices et modulo].

Ainsi pour $n$ pair, $U_n = -\sin(\pi W_n)$ ; pour $n$ impair, $U_n = +\sin(\pi W_n)$. D'où $\forall n \in \mathbb{N},\ U_n = (-1)^{n+2}\sin(\pi W_n) \sim_{+\infty} \overbrace{(-1)^{n+2} \times \pi\sum_{k \geq n+2} \frac{(-1)^k n!}{k!}}^{B_n}$.

Or [bas de page coupé au scan — la fin du calcul (une fraction) n'est pas lisible].

## Figures

Aucune figure : 2 pages de calculs manuscrits seuls, sans schéma ni graphe (transcription : deux exercices $\sin(\pi(2+\sqrt3)^n)$ puis $\sin(\pi n!e^{-2})$ ; confirmé p. 1 sur source le 2026-09-07 — binôme, $A_n \in \mathbb{N}$, règle $\lambda^n$ — rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07 — rendu `/tmp/s11/`, 0 figure à reproduire). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- $A_n = \sum C_n^{2k}2^{n-2k}3^k \in \mathbb{N}$ ; $W_n$ : queue de série ($W_n \to 0$) ; $V_n = \pi n!e^{-2}$, $d_n$.
- règle « $\lambda^n$ » : convergence géométrique ($|2-\sqrt3| < 1$) ; $B_n$ : équivalent final.
- $U_n = (-1)^{n+2}\sin(\pi W_n)$ : forme réduite (parité de $A_n$ modulo 2).
