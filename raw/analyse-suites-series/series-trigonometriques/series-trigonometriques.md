# Séries trigonométriques — transcription fidèle

🧾 Source : [series-trigonometriques.pdf](series-trigonometriques.pdf) — 3 pages manuscrites, encre bleue.
🔍 Contenu : deux exercices — (1) série $\sum \cos^2(n\theta)\,x^{4n}$ selon $x$ et $\theta$ ; (2) somme de $\sum \ln\cos(a/2^n)$ par produit télescopique (page 2 : brouillon, page 3 : rédaction reprise et corrigée).
📄 Note : restauration Datas1 du 2026-09-07 — transcription à l'identique, sans correction ni ajout ; les erreurs du manuscrit sont signalées par [*sic*], les doutes de lecture par [lecture incertaine — …], les passages biffés par [raturé].

## Page 1

1b. $\sum_{n \ge 0} \cos^2(n\theta)\,x^{4n} \quad$ où $x \in \mathbb{R}$ et $\theta \in \mathbb{R}$

$= \frac{1}{2}\sum_{n \ge 0}\left(x^{4n} - x^{4n}\cos 2n\theta\right)$ [*sic* — signe : $\cos^2 = (1 + \cos 2)/2$]

Considérons : $S_1 = \sum_{n \ge 0} x^{4n} = \begin{cases} \dfrac{1}{1 - x^4} & \text{si } |x| < 1 \text{ [lecture incertaine — « ssi » ou « si »]} \\ +\infty & \text{si } |x| \ge 1 \end{cases}$

$S_2 = \sum_{n \ge 0} x^{4n}\cos 2n\theta = \sum_{n \ge 0} \mathrm{Re}\left((x^4 e^{i2\theta})^n\right)$

. Si $|x| < 1$, $\sum_{n \ge 0}(x^4 e^{i2\theta})^n$ cvge d'où $S_2 \in \mathbb{R}$ et on a

$S_2 = \mathrm{Re}\left(\sum_{n = 0}^{\infty}(x^4 e^{i2\theta})^n\right) = \mathrm{Re}\left(\dfrac{1}{1 - x^4 e^{i2\theta}}\right) = \dfrac{1 - x^4\cos 2\theta}{(1 - x^4\cos 2\theta)^2 + (x^4\sin 2\theta)^2}$

[raturé — . Si $|x| < 1$, $|x^{4n}\cos 2n\theta|$ … (début de phrase biffé d'un trait horizontal)] d'où $S = \dfrac{1}{1 - x^4} - \dfrac{1 - x^4\cos 2\theta}{(1 - x^4\cos 2\theta)^2 + (x^4\sin 2\theta)^2}$ [*sic* — facteur $1/2$ manquant par rapport à la ligne d'attaque]

. Si $|x| \ge 1$, $(\cos^2(n\theta)\,x^{4n}) \not\to_{n \to +\infty} 0$ [lecture incertaine — liaison : « et car »] $\cos^2(n\theta)\,x^{4n} \ge 0$, $S \to +\infty$

. Si $\theta \in \pi\mathbb{Z}$

Calcul écrit à l'envers (page tournée à 180°, transcrit après rotation) :

$\left(1 - (x^4 e^{i2\theta})^{N+2}\right)\left(1 - x^4 e^{-i2\theta}\right)$

$1 - x^4 e^{-i2\theta} - (x^4 e^{i2\theta})^{N+2} + x^{4(N+2)} e^{i2\theta N}$ [lecture incertaine — dernier exposant]

$1 - x^4\cos 2\theta - x^{4(N+2)}\cos(2(N+2)\theta) + x^{4(N+2)} \times \cos 2N\theta$ [lecture incertaine — dernier terme]

## Page 2 (brouillon du second exercice)

Soit $a \in ]0, \pi/2[$

Posons $S = \sum_{n \ge 0} \ln\cos\left(\dfrac{a}{2^n}\right)$

$= \lim_{N \to +\infty} \ln\left(\prod_{n = 0}^{N} \cos\left(\dfrac{a}{2^n}\right)\right)$

Soit $N \in \mathbb{N}^*$. Posons $C_N = \prod_{n = 0}^{N} \cos\left(\dfrac{a}{2^n}\right)$ et $S_N = \prod_{n = 0}^{N} \sin\left(\dfrac{a}{2^n}\right)$ [raturé — indice sous chaque $\prod$ repris/corigé par surcharge]

On a : $C_N \times S_N = \prod_{n = 0}^{N} \dfrac{1}{2}\sin\left(\dfrac{a}{2^{n-1}}\right)$ [lecture incertaine — exposant : $2^{n-1}$] car $\forall x \in \mathbb{R}$, $\sin 2x = 2\cos x \sin x$

$= \dfrac{1}{2^{\cdots}}\left(\prod_{n = 0}^{N-1} \sin\left(\dfrac{a}{2^n}\right)\right) \times \sin(2a)$ [*sic* — exposant de $1/2$ incomplet dans le brouillon ; voir page 3 : $1/2^{N+1}$]

d'où $C_N \times S_N = \dfrac{1}{2} \times \dfrac{2aN}{\sin\left(\dfrac{a}{2^N}\right)}$ [lecture incertaine — numérateur] $\Rightarrow C_N = \dfrac{1}{2\sin\left(\dfrac{a}{2^N}\right)}$ vu que $S_N \ne 0$ [*sic* — facteur : la page 3 donne $C_N = \sin(2a)/(2^{N+1}\sin(a/2^N))$]

d'où $S = \lim_{N \to +\infty} \ln\left(\dfrac{1}{2\sin\left(\dfrac{a}{2^N}\right)}\right)$

(On distingue en marge droite, par transparence, le texte de la page 3.)

## Page 3 (rédaction reprise du second exercice)

Soit $a \in ]0, \pi/2[$

Posons $S = \sum_{n = 0}^{\infty} \ln\left(\cos\left(\dfrac{a}{2^n}\right)\right)$ qui est bien définie puisque

$0 < \dfrac{a}{2^n} < \pi/2 \ (\forall n \in \mathbb{N}) \Rightarrow \cos\left(\dfrac{a}{2^n}\right) > 0$

On a : $S = \lim_{N \to +\infty} \ln\left(\prod_{n = 0}^{N} \cos\left(\dfrac{a}{2^n}\right)\right)$

Soit $N \in \mathbb{N}^*$. Posons $C_N = \prod_{n = 0}^{N} \cos\dfrac{a}{2^n}$ et $S_N = \prod_{n = 0}^{N} \sin\dfrac{a}{2^n}$

On a : $C_N \times S_N = \prod_{n = 0}^{N} \dfrac{1}{2}\sin\left(\dfrac{a}{2^{n-1}}\right)$

$= \dfrac{1}{2^{N+1}} \times \sin(2a) \times \prod_{n = 1}^{N+1} \sin\left(\dfrac{a}{2^{n-1}}\right)$

$= \dfrac{\sin(2a)}{2^{N+1}} \times \prod_{n = 0}^{N-1} \sin\dfrac{a}{2^n}$

d'où $C_N \times S_N = \dfrac{\sin(2a)}{2^{N+1}} \times \dfrac{S_N}{\sin\left(\dfrac{a}{2^N}\right)} \Rightarrow C_N = \dfrac{\sin 2a}{2^{N+1}\sin\left(\dfrac{a}{2^N}\right)}$ vu que $S_N \ne 0$

ainsi $S = \lim_{N \to +\infty} \ln\left(\dfrac{\sin 2a}{2^{N+1}\sin\left(\dfrac{a}{2^N}\right)}\right)$

$= \lim_{N \to +\infty} \ln\left(\dfrac{\sin 2a}{2a} \times \dfrac{a/2^N}{\sin\left(a/2^N\right)}\right)$

$S = \ln\left(\dfrac{\sin 2a}{2a}\right)$ vu que $\ln$ est continue en $\dfrac{\sin 2a}{2a} \in \mathbb{R}_+^*$

## Figures

Aucune figure : 3 pages de calculs manuscrits seuls, sans schéma ni graphe (transcription : brouillon p. 2 puis rédaction reprise p. 3 ; confirmé p. 1 sur source le 2026-09-07 — exercice $\sum \cos^2(n\theta)x^{4n}$ — rendu `/tmp/qas/` ; p. 2–3 relues le 2026-09-07 — rendu `/tmp/s11/`, 0 figure à reproduire). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- 1b. : numéro d'exercice ; $S_1 = \sum x^{4n}$, $S_2 = \sum x^{4n}\cos 2n\theta$ ; Re : partie réelle.
- $C_N, S_N$ : produits télescopiques $\prod \cos(a/2^n)$, $\prod \sin(a/2^n)$ ; $a \in ]0,\pi/2[$.
- [*sic*] : signe $\cos^2$ conservé tel que lu ; brouillon/rédaction : double état p. 2–3.
