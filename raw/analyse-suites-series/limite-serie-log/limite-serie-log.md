# Limite de série log — transcription fidèle

> 🧾 **Manuscrit original :** `limite-serie-log.pdf` (photo, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** photo de cahier (doigts visibles en marge de la page 1), folio « (4) » entouré en bas de la page 1 : extrait d'un devoir plus long (question « b/ ») ; écriture à l'encre bleue, parenthésages compacts en `[lecture incertaine — …]` ; aucune figure à reproduire. Transcrit mot à mot.
> 📄 **Source scannée :** [limite-serie-log.pdf](limite-serie-log.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

b/ $U_n = \dfrac{1}{\ln n^{\ln n}}$ [lecture incertaine — parenthésage, « $(\ln n)^{\ln n}$ » ou « $\ln(n^{\ln n})$ », la suite du calcul donne « $(\ln n)^{\ln n} \ge n^2$ »], $S_n = \sum_{k=2}^{n} \dfrac{1}{\ln k^{\ln k}}$.

$\forall n \in \mathbb{N}$ / $n \ge 2000$, $\ln(\ln n) \ge \ln(\ln 2000) \ge 2$

càd $\ln n(\ln\ln n) \ge 2\ln n$

càd $e^{\ln n(\ln\ln n)} \ge e^{2\ln n}$

c-à-d $\ln n^{\ln n} \ge n^2$ [lecture incertaine — parenthésage, cf. ci-dessus]

c-à-d $U_n \le \dfrac{1}{n^2} \le \dfrac{1}{n\ln(n+1)}$ [lecture incertaine — « $n\ln(n+1)$ »].

(« (4) » entouré en bas à droite.)

## Page 2

ainsi $\forall k \in \mathbb{N}$ / $k \ge 2000$, $U_k \le \dfrac{1}{k\ln(k+1)}$ [lecture incertaine — « $k\ln(k+1)$ »].

d'où pour $n \in \mathbb{N}$ / $n \ge 2000$, $S_n = \underbrace{\sum_{k=2}^{2000} \dfrac{1}{\ln k^{\ln k}}}_{\alpha \in \mathbb{R}} + \sum_{k=2000}^{n} \dfrac{1}{\ln k^{\ln k}}$ [lecture incertaine — « $\alpha \in \mathbb{R}$ »]

$$\le a + \sum_{k=2000}^{n} \dfrac{1}{k(k-1)}$$ [tranché au r250+crop — dénominateur $k(k-1)$ confirmé ; sens $\le$ correct via p. 1 ($\le 1/k^2 \le 1/(k(k-1))$), aucun *sic* requis]
$$\le a + \sum_{k=2000}^{n} \left(\dfrac{1}{k-1} - \dfrac{1}{k}\right)$$
$$\le a + 1 - \dfrac{1}{n}$$
$$\le a + 1$$
$$\le \sum_{k=2}^{2000} \dfrac{1}{\ln k^{\ln k}} + 1.$$

$(U_n)$ [*sic* — le manuscrit porte « $(U_n)$ », le contexte (croissance de $S_n$) suggère « $(S_n)$ »] est $\nearrow$ et majorée par (flèche vers la borne ci-dessus) donc conver [lecture incertaine — mot coupé, « converge »].

## Figures

Aucune figure : 2 pages manuscrites seules (photo de cahier, doigts en marge p. 1), sans schéma ni graphe (transcription § Statut : « aucune figure à reproduire » ; confirmé p. 1 sur source le 2026-09-07, rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07, rendu `/tmp/s10/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- b/ : question d'un devoir plus long ; (4) entouré : folio ; càd/c-à-d : c'est-à-dire.
- $U_n = 1/\ln n^{\ln n}$ [parenthésage incertain] ; $S_n$ : sommes partielles ; $\alpha$/$a$ : constante $\sum_{k=2}^{2000}$.
- $\nearrow$ : croissante ; majorée : bornée supérieurement, d'où convergence.
