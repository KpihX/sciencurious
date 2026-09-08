# Double somme liée $\sum_{n\geq 1}\sum_{m\geq 1}\frac{1}{m^2n+mn^2+2mn}$ — transcription fidèle

> 🧾 **Manuscrit original :** `double-somme-liee.pdf` (scan, 3 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à ~95 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`double-somme-liee.pdf`](double-somme-liee.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

$$\sum_{n \geq 1} \sum_{m \geq 1} \frac{1}{m^2n+mn^2+2mn} = ? \mid \text{Soient } m, n \in \mathbb{N}^*, \text{ posons } U_{n,m} = \frac{1}{m^2n+mn^2+2mn}$$

$*$ Nature de $\sum_{n \geq 1} \sum_{m \geq 1} U_{n,m}$ :

On a : $\sum_{n \geq 1} \sum_{m \geq 1} U_{n,m} = \sum_{n \geq 1} U_n$ où $U_n = \sum_{m \geq 1} U_{n,m}$.

- Nature de [raturé — article biffé] la série $U_n = \sum_{m \geq 1} U_{n,m}$ pour $n$ fixé dans $\mathbb{N}^*$.

Soit $n \in \mathbb{N}^*$. Posons $U_m = U_{n,m}$. On a : $\sum_{m \geq 1} U_{n,m} = \sum_{m \geq 1} U_m$.

De plus $\forall m \in \mathbb{N}^*$, $U_m > 0$, $U_m \underset{m \to +\infty}{\sim} \frac{1}{m^2n}$ et ce $\sum_{m \geq 1} \frac{1}{m^2n}$ cvge (car série de Riemann) alors d'après le critère des équivalents, $\sum_{m \geq 1} U_m$ cvge d'où $U_n \in \mathbb{R}$ $\forall n \in \mathbb{N}^*$.

- Nature de la série $\sum_{n \geq 1} U_n$ : $\forall n \in \mathbb{N}^*$, on a $U_n \geq 0$.

De plus [raturé — majoration biffée] $U_n = \frac{1}{n}\sum_{m \geq 1} \frac{1}{m + \frac{2m+m^2}{n}}$ [lecture incertaine — forme intermédiaire].

Soit $n \in \mathbb{N}^*$. Évaluons $U_n$. On a : $U_n = \lim_{M \to +\infty} S_M$ où $S_M = \sum_{m=1}^M U_m$ ($M \in \mathbb{N}^*$).

Or $\forall m \in \mathbb{N}^*$, $U_m = \frac{1}{nm(m+n+2)} = \frac{1}{n(n+2)}\left(\frac{1}{m} - \frac{1}{m+n+2}\right)$.

## Page 2

Ainsi $S_M = \frac{1}{n(n+2)}\left(\sum_{m=1}^M \frac{1}{m} - \sum_{m=n+3}^{M+n+2} \frac{1}{m}\right)$

$$= \frac{1}{n(n+2)}\left(\sum_{m=1}^{n+2} \frac{1}{m} - \sum_{m=M+1}^{M+n+2} \frac{1}{m}\right)$$

$$= \frac{1}{n(n+2)}\left(\sum_{m=1}^{n+2} \frac{1}{m} - \left(\frac{1}{M+1} + \frac{1}{M+2} + \cdots + \frac{1}{M+n+2}\right)\right)$$

d'où $U_n = \lim_{M \to +\infty} S_M = \frac{1}{n(n+2)}\left(\sum_{m=1}^{n+2} \frac{1}{m} - 0\right) = \frac{1}{n(n+2)}\sum_{m=1}^{n+2} \frac{1}{m}$.

Ainsi en revenant à la nature de $\sum_{n \geq 1} U_n$. $\forall n \in \mathbb{N}$, on a : $U_n \geq 0$. De plus car $\sum_{m=1}^{n+2} \frac{1}{m} \underset{n \to +\infty}{\sim} \ln(n+2)$ ainsi $U_n \underset{+\infty}{\sim} \frac{\ln(n+2)}{n(n+2)}$. Comme $\lim_{n \to +\infty} n^{1.5}U_n = \lim_{n \to +\infty} \frac{\ln(n+2)}{n^{0.5}} = 0$ alors $\sum \frac{\ln(n+2)}{n(n+2)}$ cvge d'après la règle « $n^\alpha U_n$ » avec $\alpha = 1.5 > 1$ et par conséquent $\sum_{n \geq 1} U_n$ cvge d'après le critère des équivalents. Donc $\sum_{n \geq 1} \sum_{m \geq 1} U_{n,m} \in \mathbb{R}$.

$*$ Évaluation de cette somme. D'après ce qui précède, $\sum_{n \geq 1} \sum_{m \geq 1} U_{n,m} = \sum_{n \geq 1} U_n = \lim_{N \to +\infty} S_N$ où $S_N = \sum_{n=1}^N U_n$ ($N \in \mathbb{N}^*$).

## Page 3

Soit $N \in \mathbb{N}^*$, $S_N = \sum_{n=1}^N \frac{1}{n(n+2)}\sum_{m=1}^{n+2} \frac{1}{m}$

$$= \frac{1}{2}\sum_{n=1}^N \left(\frac{1}{n} - \frac{1}{n+2}\right)\sum_{m=1}^{n+2} \frac{1}{m}$$

$$= \frac{1}{2}\left(\sum_{n=1}^N \frac{1}{n}\sum_{m=1}^{n+2} \frac{1}{m} - \sum_{n=3}^{N+2} \frac{1}{n}\sum_{m=1}^{n} \frac{1}{m}\right)$$

$$= \frac{1}{2}\left(\sum_{n=1}^2 \frac{1}{n}\sum_{m=1}^{n+2} \frac{1}{m} - \sum_{n=N+1}^{N+2} \frac{1}{n}\sum_{m=1}^{n} \frac{1}{m} + \sum_{n=3}^N \frac{1}{n}\sum_{m=n+1}^{n+2} \frac{1}{m}\right)$$

$$= \frac{1}{2}\left(1\left(1+\frac{1}{2}+\frac{1}{3}\right) + \frac{1}{2}\left(1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}\right) - \frac{1}{N+1}\sum_{m=1}^{N+1} \frac{1}{m} - \frac{1}{N+2}\sum_{m=1}^{N+2} \frac{1}{m} + \sum_{n=3}^N \frac{1}{n}\left(\frac{1}{n+1}+\frac{1}{n+2}\right)\right)$$

$$= \frac{29}{16} + \frac{1}{2}\left(-\frac{1}{N+1}\sum_{m=1}^{N+1} \frac{1}{m} - \frac{1}{N+2}\sum_{m=1}^{N+2} \frac{1}{m} + \frac{1}{3} - \frac{1}{N+2} + \frac{1}{2}\left(\frac{1}{3}+\frac{1}{4}-\frac{1}{N+1}-\frac{1}{N+2}\right)\right)$$ [raturé — valeur biffée, calcul repris]

$$= \frac{7}{4} - \frac{1}{2}\left(\frac{1}{N+1}\sum_{m=1}^{N+1} \frac{1}{m} + \frac{1}{N+2}\sum_{m=1}^{N+2} \frac{1}{m} + \frac{3}{2(N+1)} + \frac{1}{2(N+2)}\right)$$

En remarquant que $\sum_{n=1}^N \frac{1}{n} \underset{N \to +\infty}{\sim} \ln N$ alors on aboutit à $\lim_{N \to +\infty} \frac{1}{N+1}\sum_{m=1}^{N+1} \frac{1}{m} = 0$, $\lim_{N \to +\infty} \frac{1}{N+2}\sum_{m=1}^{N+2} \frac{1}{m} = 0$, d'où $\sum_{n \geq 1}\sum_{m \geq 1} \frac{1}{m^2n+mn^2+2mn} = \frac{7}{4} - \frac{1}{2}(0+0+0+0) = \boxed{\frac{7}{4}}$.

## Figures

Aucune figure : 3 pages de texte manuscrit seul, sans schéma ni graphe (transcription § Statut : ratures notées, pas de figure ; confirmé p. 1 sur source le 2026-09-07, rendu `/tmp/qas/` ; pp. 2–3 relues le 2026-09-07, rendu `/tmp/s10/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- cvge : converge ; Ona : on a ; mtq implicite : natures de séries.
- $U_{n,m} = 1/(m^2n+mn^2+2mn)$ ; $U_n = \sum_m U_{n,m}$ ; $S_M, S_N$ : sommes partielles.
- série de Riemann ; critère des équivalents ; règle « $n^\alpha U_n$ » ($\alpha = 1{,}5 > 1$).
