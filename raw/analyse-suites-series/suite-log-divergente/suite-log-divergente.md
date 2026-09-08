# Suite log divergente — transcription fidèle

> 🧾 **Manuscrit original :** `suite-log-divergente.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** écriture rapide à l'encre bleue, définition récursive initiale et tour d'exponentielles en `[lecture incertaine — …]` (détails peu lisibles) ; une rature conservée. Transcrit mot à mot.
> 📄 **Source scannée :** [suite-log-divergente.pdf](suite-log-divergente.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Nature de $(U_n)_{\mathbb{N}^*}$ : $\forall n \in \mathbb{N}^*$, $U_n = \begin{cases} \ln n = 0 \\ \ln|\ln(\ln(2 + \ldots + \ln|n + \ln|n|\ldots|))| \text{ sinon} \end{cases}$ [lecture incertaine — définition récursive emboîtée, condition et bornes peu lisibles].

Approche 1 : Car $\ln \nearrow^*$ et $\forall x \in \mathbb{R}_+^*,\ \ln x = \ln 10 \times \log x > \log x$ (pour $n \geq 1$).

Ainsi $\forall n \in \mathbb{N}^*,\ U_n > \ln|\ln(\ln(2 + \ldots + \ln|n-1 + \ln n|\ldots))|$ [raturé : un fragment] $> \ln|\ln(|\ln|\ldots + \ln|n-1 + \ln n|\ldots|)|$

$$\vdots$$
$$> \underbrace{\ln|\ln|\ldots\ln}_{n \text{ fois}}(n-1 + \ln n)\ldots|)$$

$$> \underbrace{\ln|\ln|\ldots\ln(n)}_{n \text{ fois}}\ldots|)$$

$$> \underbrace{\log|\log|\ldots\log(n}_{n \text{ fois}}\ldots|).$$

Considérons la sous-suite $(U_{\ell(n)})_{\mathbb{N}^*}$ où $\ell : \mathbb{N}^* \to \mathbb{N},\ n \mapsto 10^{10^{\cdot^{\cdot^{10}}}}$ ($n$ fois) [lecture incertaine — tour d'exponentielles itérée, hauteur « $n$ fois »].

$\forall n \in \mathbb{N}^*,\ U_{\ell(n)} > \underbrace{\log(\ldots\log}_{n \text{ fois}}|10^{10^{\cdot^{\cdot^{10}}}}|\ldots)$

$$> \underbrace{\log(\ldots\log}_{(n-1) \text{ fois}}(10^{\overbrace{10^{\cdot^{\cdot^{10}}}}^{m \text{ fois}}})\ldots)$$

$$\vdots$$
$$> \log(10^n),$$

car $U_{\ell(n)} > n \implies U_{\ell(n)} \xrightarrow[n \to +\infty]{} +\infty$, d'où $(U_n)_{\mathbb{N}^*}$ diverge.

## Page 2

Approche 2 :

— Justifions que $(U_n) \nearrow^*$.

$\forall n \in \mathbb{N}^*,\ \ln(n+2) > 0 \implies n + \ln(n+2) > n$

$$\implies \ln(n + \ln(n+2)) > \ln n$$
$$\implies \ln(n-1 + \ln(n + \ln(n+2))) > \ln(n-1 + \ln n)$$
$$\vdots$$
$$\implies \ln(1 + \ldots + \ln(n-1 + \ln(n + \ln(n+2)))\ldots) > \ln(1 + \ldots + \ln(n-1 + \ln n)\ldots)$$
$$\implies U_{n+2} \geq U_n, \text{ d'où } (U_n) \nearrow^*.$$

— Justifions que $(U_n)_{\mathbb{N}^*}$ non majorée.

Soit $M > 0$ (Rq : Car $(U_n) \nearrow^*$ , $\forall n \in \mathbb{N}^*,\ U_n > U_1 = \ln(1) = 0$ [lecture incertaine — le scan porte « $U_1 = \ln(1\ldots2 = 0)$ », valeur $0$ lisible]).

En s'inspirant de la démarche faite dans l'approche 1, pour $n = 10^{10^{\cdot^{\cdot^{10}}}}$ ($\underbrace{\phantom{10}}_{E(M)+2 \text{ fois}}$, tour de hauteur $E(M)+2$) [lecture incertaine — hauteur de la tour notée « $E(M)+2$ » avec « $n$ fois »], on a : $U_n >$ [raturé : log] $E(M)+2 > M$, d'où $(U_n)_{\mathbb{N}^*}$ non majorée.

Au vu des 2 résultats précédents, $U_n \to +\infty$.

## Figures

Aucune figure : 2 pages de texte manuscrit seul, sans schéma ni graphe (transcription : approches 1–2, tours de logarithmes ; confirmé p. 1 sur source le 2026-09-07 — Approche 1, sous-suite $V_{e(n)}$ — rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07 — rendu `/tmp/s11/`, 0 figure à reproduire). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- Approche 1 / (approche 2, p. 2) : deux preuves de divergence ; $\nearrow^*$ : strictement croissante.
- $U_n$ : logarithmes itérés emboîtés ; $V_{e(n)}$ : sous-suite test ($e(n)$ : tour de $10$ de hauteur $n$) ; $\log$ vs $\ln$.
- $E(M)+2$ : hauteur de tour ; $U_1 = 0$ [lisible] ; $U_n \to +\infty$ : conclusion.
