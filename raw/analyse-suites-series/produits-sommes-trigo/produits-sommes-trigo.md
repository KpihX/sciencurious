# Produits et sommes trigonométriques — transcription fidèle

> 🧾 **Manuscrit original :** `produits-sommes-trigo.pdf` (scan, 7 pages manuscrites, encre bleue, sans énoncé dactylographié) · ✍️ KpihX
> 🔍 **Statut :** transcrit fidèlement ; les passages biffés sont signalés par [raturé], les doutes de lecture par [lecture incertaine — …], les erreurs du manuscrit par [*sic* — …] ; rien d'inventé ni corrigé.
> 📄 **Source scannée :** [`produits-sommes-trigo.pdf`](produits-sommes-trigo.pdf) (restaurée Datas1, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

* $\boxed{P = \prod_{k \ge 0} \cos\left(\frac{\pi}{2^{k+2}}\right) = ?}$ [encadré, souligné]

$P = \lim_{n \to +\infty} P_n$ où $P_n = \prod_{k=2}^{n} U_k$ où $U_n = \cos \frac{\pi}{2^n}$ $\forall n \in [\![2, +\infty[\![$ [lecture incertaine — crochets d'intervalle d'entiers]

$\forall n \in [\![2, +\infty[\![$, posons $V_n = \sin \frac{\pi}{2^n}$ et $Q_n = \prod_{k=2}^{n} V_k$ [indice sous $\prod$ lu $k=2$ par le contexte]

On a : $P_n Q_n = \prod_{k=2}^{n} \left(\cos \frac{\pi}{2^k}\right)\left(\sin \frac{\pi}{2^k}\right)$

$= \prod_{k=2}^{n} \frac{1}{2}\sin \frac{\pi}{2^{k-1}}$ car $\forall x \in \mathbb{R}$, $\sin 2x = 2\sin x \cos x$

$= \frac{1}{2^{n-1}} \times \sin \frac{\pi}{2^2} \times \left(\prod_{k=3}^{n} \sin \frac{\pi}{2^{k-1}}\right) \times \frac{1}{\sin \frac{\pi}{2^n}}$

$= \frac{1}{2^{n-1}\sin \frac{\pi}{2^n}} \times \prod_{k=2}^{n} \sin \frac{\pi}{2^n}$ [lu tel quel — *sic*, attendre $\prod_{k=2}^{n} \sin \frac{\pi}{2^k}$]

d'où $P_n Q_n = \frac{1}{2^{n-1}\sin \frac{\pi}{2^n}} \times Q_n \Rightarrow P_n = \frac{1}{2^{n-1}\sin \frac{\pi}{2^n}}$ car $Q_n \ne 0$ $\forall n \in [\![2, +\infty[\![$

Ainsi $P = \lim_{n \to +\infty} \frac{\pi/2^n}{\sin \frac{\pi}{2^n}} \times \frac{2}{\pi} = \frac{2}{\pi}$ car posons $x = \frac{\pi}{2^n} \xrightarrow[n \to +\infty]{} 0$ ; $\lim_{x \to 0} \frac{[x]}{\sin x} = 1$ [numérateur raturé/surchargé — lu par le contexte]

Donc $\boxed{\prod_{k \ge 0} \cos \frac{\pi}{2^{k+2}} = \frac{2}{\pi}}$ [encadré, souligné]

* $Q = \frac{\sqrt{2}}{2} \times \frac{\sqrt{2+\sqrt{2}}}{2} \times \frac{\sqrt{2+\sqrt{2+\sqrt{2}}}}{2} \times \cdots = ?$

Soit $(W_n)_{n \in \mathbb{N}, \, (n \ge 2)}$ : $\begin{cases} W_2 = \sqrt{2}/2 \\ W_{n+1} = \frac{\sqrt{2+2W_n}}{2} = \sqrt{\frac{1+W_n}{2}} \end{cases}$

---

## Page 2

Montrons que $W_n = U_n$ $\forall n \in [\![2, +\infty[\![$

- Pour $n = 2$, $W_2 = \cos \frac{\pi}{2^2} = \frac{\sqrt{2}}{2} = U_2$

- Hérédité. $W_{n+1} = \sqrt{\frac{1+W_n}{2}}$

$= \sqrt{\frac{1+\cos(\pi/2^n)}{2}}$ car d'après l'hypothèse de récurrence $W_n = U_n$ $\forall n \in [\![2, +\infty[\![$

$= \sqrt{\cos^2\left(\frac{\pi}{2^{n+1}}\right)}$

$= \left\lvert\cos \frac{\pi}{2^{n+1}}\right\rvert$

$= \cos \frac{\pi}{2^{n+1}}$ car $\forall n \in [\![2, +\infty[\![$, $\frac{\pi}{2^{n+1}} \in \left]0, \frac{\pi}{2}\right[$ d'où $\cos \frac{\pi}{2^{n+1}} > 0$

ainsi $W_{n+1} = U_{n+1}$

CQFD

Par conséquent, car $Q = \lim_{n \to +\infty} \prod_{k=2}^{n} W_k = \lim_{n \to +\infty} \prod_{k=2}^{n} U_k = P$ alors $\boxed{Q = \frac{2}{\pi}}$ [encadré, souligné]

* De façon générale, évaluons, pour $\theta \in \left]0, \frac{\pi}{2}\right[$, $U_n = \cos \frac{\theta}{2^n}$, $V_n = \sin \frac{\theta}{2^n}$ ($n \in \mathbb{N}$), les expressions $P_n = \prod_{k=0}^{n} \cos \frac{\theta}{2^k} \times U_k$ [lu tel quel — *sic*, le facteur $U_k$ semble de trop], $Q_n = \prod_{k=0}^{n} V_k$ et $P = \lim P_n$, $Q = \lim Q_n$.

- $P_n Q_n = \prod_{k=0}^{n} \cos \frac{\theta}{2^k} \sin \frac{\theta}{2^k} = \prod_{k=0}^{n} \frac{1}{2}\sin \frac{\theta}{2^{k-1}}$ [fin de ligne : exposant raturé/surchargé]

$= \frac{1}{2^{n+1}} \times \left(\prod_{k=1}^{n+1} \sin \frac{\theta}{2^{k-1}}\right) \times \frac{\sin 2\theta}{\sin \frac{\theta}{2^n}}$ [lu par le contexte]

---

## Page 3

car ca [lu tel quel — lire « car »] $\theta \in \left]0, \frac{\pi}{2}\right[$, $\frac{\theta}{2^n} \in \left]0, \frac{\pi}{2}\right[$ $\Rightarrow \sin \frac{\theta}{2^n} \ne 0$

ainsi $P_n Q_n = \frac{\sin 2\theta}{2^{n+1}\sin \frac{\theta}{2^n}} \times \prod_{k=0}^{n} \sin \frac{\theta}{2^n} = \frac{\sin 2\theta}{2^{n+1}\sin \frac{\theta}{2^n}} \times Q_n$

d'où $\boxed{P_n = \frac{\sin 2\theta}{2^{n+1}\sin \frac{\theta}{2^n}}}$ [encadré]

- Ainsi $P = \lim P_n = \frac{\sin 2\theta}{2\theta} \times \frac{\theta/2^n}{\sin \frac{\theta}{2^n}} \Rightarrow \boxed{P = \lim P_n = \frac{\sin 2\theta}{2\theta}}$ [encadré]

- $\forall n \in \mathbb{N}$, car $\frac{\theta}{2^n} \in \left]0, \frac{\pi}{2}\right[$, $0 \le V_n \le \frac{\theta}{2^n}$ [membre de gauche raturé/surchargé — lu par le contexte]

d'où $0 < Q_n < \prod_{k=0}^{n} \frac{\theta}{2^k} = \frac{\theta^{n+1}}{2^{n(n+1)/2}} = \left(\frac{\theta}{2^{n/2}}\right)^{n+1} = e^{(n+1)\ln \frac{\theta}{2^{n/2}}} \xrightarrow[n \to +\infty]{} 0$ [passage central lu par le contexte — lecture incertaine]

d'où $\underline{Q = \lim Q_n = 0}$ [souligné]

* Cas de $T = \lim_{n \to +\infty} T_n$ où $T_n = \prod_{k=0}^{n} t_k$ où $t_k = \tan \frac{\theta}{2^k}$, $n \in \mathbb{N}$ [lu par le contexte]

$\forall n \in \mathbb{N}$, $t_n = \frac{V_n}{U_n}$ d'où $T_n = \frac{Q_n}{P_n} \xrightarrow[n \to +\infty]{} \frac{0}{\sin 2\theta / 2\theta} = 0$

Donc $\boxed{\lim_{n \to +\infty} T_n = 0}$ [encadré, souligné]

---

## Page 4

Soient $\theta_k$, $i = \ldots \in \mathbb{R}^n$ [lecture incertaine — « Soient $\theta_k \in \mathbb{R}$ »], $\cos\left(\sum_{k=1}^{n} \theta_k\right) = \Sigma ?$ | $\sin\left(\sum_{k=1}^{n} \theta_k\right) = \Sigma ?$ [lus tels quels]

$\cos \sum_{k \in I_n} \theta_k = \mathrm{Re}\left(\prod_{k \in I_n} e^{i\theta_k}\right) = \mathrm{Re}\left(\prod_{k \in I_n} (\cos \theta_k + i\sin \theta_k)\right)$

$\cos \sum_{k} \theta_k =$ [raturé — « on … de $P_n$ … » biffé] or [lu tel quel]

$\prod_{k \in I_n} (\cos \theta_k + i\sin \theta_k) = \sum_{K=0}^{n/2} \sum_{\substack{J \subseteq I_n \\ |J| = 2K}} \left(\prod_{j \in J} (i\sin \theta_j)\right)\left(\prod_{j \in \bar{J}} \cos \theta_j\right)$ [avec $\bar{J} = I_n \setminus J$, $\forall J \subseteq I_n$] $+ \sum_{K=0}^{\ldots} \sum_{\substack{J \subseteq I_n \\ |J| = 2K+1}} \prod_{j \in J} (i\sin \theta_j)\left(\prod_{j \in \bar{J}} \cos \theta_j\right)$

où $I_n = [\![1, n]\!]$ [lu par le contexte]

où $(i)^{2K} = (-1)^K$, $(i)^{2K+1} = (-1)^K i$ [lu par le contexte — écriture très cursive]

$= \sum_{K=0}^{\ldots} (-1)^K \sum_{\substack{J \subseteq I_n \\ |J| = 2K}} \prod_{j \in J} \sin \theta_j \prod_{j \in \bar{J}} \cos \theta_j + i\left(\sum_{K=0}^{\ldots} (-1)^K \sum_{\substack{J \subseteq I_n \\ |J| = 2K+1}} \prod_{j \in J} \sin \theta_j \prod_{j \in \bar{J}} \cos \theta_j\right)$

Car $\mathrm{Re}(P_n) = \cos\left(\sum_{k \in I_n} \theta_k\right)$ et $\mathrm{Im}(P_n) = \sin\left(\sum_{k \in I_n} \theta_k\right)$,

Alors $\boxed{\cos\left(\sum_{k \in I_n} \theta_k\right) = \sum_{K=0}^{n/2} (-1)^K \sum_{\substack{J \subseteq I_n \\ |J| = 2K}} \prod_{j \in J} \sin \theta_j \prod_{j \in \bar{J}} \cos \theta_j}$ et $\sin\left(\sum_{k \in I_n} \theta_k\right) = \sum_{K=0}^{(n-1)/2} (-1)^K \sum_{\substack{J \subseteq I_n \\ |J| = 2K+1}} \prod_{j \in J} \sin \theta_j \prod_{j \in \bar{J}} \cos \theta_j$ [bornes supérieures lues par le contexte p. 4 relue le 2026-09-07, rendu `/tmp/s10/` — cohérentes avec la spécialisation p. 5]

---

## Page 5

En particulier lorsque $\theta_k = \theta \in \mathbb{R}$ $\forall k \in [\![1, n]\!]$, on a :

$\cos n\theta = \sum_{K=0}^{n/2} (-1)^K C_n^{2K} \sin^{2K}\theta \cos^{n-2K}\theta$ et $\sin n\theta = \sum_{K=0}^{(n-1)/2} (-1)^K C_n^{2K+1} \sin^{2K+1}\theta \cos^{n-2K-1}\theta$ [encadré — bornes et exposants lus par le contexte, lecture incertaine]

Application :

- $\cos(\theta_1+\theta_2+\theta_3) = \cos\theta_1\cos\theta_2\cos\theta_3 - ($[raturé — mot biffé] $\sin\theta_1\sin\theta_2\cos\theta_3 + \sin\theta_1\sin\theta_3\cos\theta_2 + \sin\theta_2\sin\theta_3\cos\theta_1)$

- $\sin(\theta_1+\theta_2+\theta_3) = \sin\theta_1\cos\theta_2\cos\theta_3 + \sin\theta_2\cos\theta_1\cos\theta_3 + \sin\theta_3\cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2\sin\theta_3$

- $\cos(4\theta) = \cos^4\theta - 6\sin^2\theta\cos^2\theta + \sin^4\theta$

- $\sin(4\theta) = 4\sin\theta\cos^3\theta - 4\sin^3\theta\cos\theta$ [le premier $\cos$ porte un exposant peu lisible — lu $3$ par le contexte, la formule standard l'exige]

* $\boxed{\text{Soit } n \in \mathbb{N}^*, \, \theta \in \mathbb{R}, \, \cos^n\theta = \Sigma ?, \, \sin^n\theta = \Sigma ?}$ [encadré]

$\cos^n\theta = \left(\frac{e^{i\theta}+e^{-i\theta}}{2}\right)^n = \frac{1}{2^n}\left(\sum_{K=0}^{\ldots} C_n^K e^{iK\theta} \times C_n^{n-K} e^{i\theta(n-K)} \times e^{-i\theta K} \times e^{-i\theta(n-K)} + C_n^{n/2} e^{\frac{in\theta}{2}} \times e^{\frac{-in\theta}{2}}\right)$ [formule confuse, termes intermédiaires surchargés — lus tels quels]

où $C_n^{n/2} = 0$ pour $n \equiv 1\,[2]$

$= \frac{1}{2^n} \sum_{K=0}^{\ldots} C_n^K \left(e^{-i\theta(n-2K)} + e^{i\theta(n-2K)}\right) + C_n^{n/2}$ [le $+ C_n^{n/2}$ est lu tel quel]

---

## Page 6

Donc $\boxed{\cos^n\theta = \frac{1}{2^{n-1}}\left(\left(\sum_{K=0}^{\ldots} C_n^K \cos\theta(n-2K)\right) + \frac{C_n^{n/2}}{2}\right)}$ [encadré]

De même $\sin^n\theta = \frac{1}{(2i)^n}\left(\sum_{K=0}^{\ldots} C_n^K e^{-i\theta(n-2K)} \times (-1)^K + C_n^{n-K} e^{i\theta(n-2K)} \times (-1)^K + (-1)^{n/2}C_n^{n/2}\right)$ [terme central raturé — non reconstitué]

- Si $n \equiv 0\,[2]$, $\sin^n\theta = \frac{(-1)^{n/2}}{2^{n-1}}\left(\text{[raturé]} \frac{C_n^{n/2}}{2} + \sum_{K=0}^{\ldots} C_n^K (-1)^K \cos\theta(n-2K)\right)$ [« $0$ pour $n \equiv 1\,[2]$ » annoté sous la rature]

- Si $n \equiv 1\,[2]$, $\sin^n\theta = \frac{(-1)^{(n-1)/2}}{2^{n-1}} \sum_{K=0}^{(n-1)/2} C_n^K (-1)^K \sin(\theta(n-2K))$ [exposant de $-1$ lu par le contexte]

Application :

$\cos^2\theta = \frac{1}{2}(\cos 2\theta + 1)$ , [lecture incertaine — second membre de la ligne : « $\cos\theta = \frac{1}{2^2}\lvert\cos\theta\rvert$ » lu tel quel, sens obscur]

$\cos^3\theta = \frac{1}{4}(\cos 3\theta + 3\cos\theta)$ [dernier signe lu par le contexte]

$\sin\theta = \frac{(-1)^0}{2^0}(\sin\theta)$ , $\sin^2\theta = \frac{(-1)^1}{2}(-1 + \cos 2\theta) = \frac{1-\cos 2\theta}{2}$ [*sic* — le $-1$ intermédiaire est compensé dans le résultat final ; p. 6 relue le 2026-09-07, rendu `/tmp/s10/` : le manuscrit porte bien « $-1+\cos 2\theta$ »]

$\sin^3\theta = \frac{-1}{4}(\sin 3\theta + 3\sin\theta) = \frac{1}{4}(3\sin\theta - \sin 3\theta)$

---

## Page 7

Commentaires : . Dans l'ensemble $\sum_{k_2, k_1} f(k) = \sum_{\substack{k_1 \le k \le k_2 \\ k \in \mathbb{N}}} f(k)$ [lu par le contexte]

- $C_n^{n/2}$ a été pris pour $0$ pour $n \equiv 1\,[2]$

---

## 📝 Notes de transcription (fidélité)

- P. 1–7 : corrigé manuscrit à l'encre bleue sur papier bleu-vert ; aucun énoncé dactylographié — la page 1 commence directement par le calcul de $P = \prod_{k \ge 0} \cos(\pi/2^{k+2})$.
- Aucune figure géométrique ni graphe : les « figures » du manuscrit sont des formules encadrées ; aucune reproduction par script n'a donc été produite.
- P. 1 : la ligne $= \frac{1}{2^{n-1}\sin\frac{\pi}{2^n}} \times \prod_{k=2}^{n} \sin\frac{\pi}{2^n}$ est lue telle quelle (indice intérieur suspect).
- P. 2 (bas) : $P_n = \prod_{k=0}^{n} \cos\frac{\theta}{2^k} \times U_k$ — le facteur $U_k$ est lu tel quel (*sic*, semble de trop).
- P. 4 : écriture très cursive (niveaux d'indices $J \subseteq I_n$, $|J| = 2K$ / $2K+1$) ; bornes supérieures des $\sum_K$ lues $n/2$ et $(n-1)/2$ par le contexte (p. 4 relue le 2026-09-07, rendu `/tmp/s10/`).
- P. 5 : $\sin(4\theta)$ — l'exposant du premier $\cos$ est lu $3$ par le contexte (formule standard).
- P. 6 (Application) : la fin de la ligne $\cos^2\theta$ (« $\cos\theta = \frac{1}{2^2}\lvert\cos\theta\rvert$ ») est transcrite telle quelle, sens obscur — relecture à haute résolution effectuée sans lever le doute.

## Figures

Aucune figure géométrique ni graphe : 7 pages de calculs manuscrits seuls ; les « figures » du manuscrit sont des formules encadrées (transcription § Notes ; confirmé p. 1 sur source le 2026-09-07, rendu `/tmp/qas/` ; pp. 2–7 relues le 2026-09-07, rendu `/tmp/s10/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire (encadrés conservés en LaTeX `\boxed{}`).

## Vocabulaire

- $P = \prod \cos(\pi/2^{k+2}) = 2/\pi$ ; $Q$ : produit de radicaux emboîtés ; $W_n$ : suite auxiliaire ($W_2 = \sqrt{2}/2$).
- $P_n, Q_n, U_k$ : produits partiels et facteur [*sic*] ; $J \subseteq I_n$ : parties d'indices (p. 4, cursive).
- $\boxed{}$ : formules encadrées du manuscrit ; [*sic*] : erreurs conservées (signe $\cos^2$, facteur $U_k$).
