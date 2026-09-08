# Intégrales fiche 1 — $\int_0^\pi \frac{x^2}{1+\sin^2x}dx$ (série, Wallis, polylog) — transcription fidèle

> 🧾 **Manuscrit original :** `integrales-fiche-1.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** partiellement lisible (~65 %), transcrit fidèlement. Feuille pliée en deux (distorsions verticales au milieu), encre empâtée sur les calculs d'IPP complexes. Trois approches : développement en série géométrique $1/(1+\sin^2x) = \sum(-\sin^2x)^k$ avec coefficients $J_k(\pi)$, primitive polylogarithmique issue d'un CAS ($\mathrm{Li}_2$, $\mathrm{Li}_3$), sommes de Riemann. La série de Grandi $\sum(-1)^k = 1/2$ est admise sans justification (signalée).
> 📄 **Source scannée :** [`integrales-fiche-1.pdf`](integrales-fiche-1.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Série géométrique et coefficients $J_k(\pi)$

$I = \int_0^\pi \frac{x^2}{1+\sin^2x}\,dx = ?$ [haut de page partiellement rogné]

$\forall x \in ]-1,1[$ [lu « $\forall \dots \in ]-1,1[$ »], $\sum_{k=0}^n (-x^2)^k = \sum_{k=0}^n (-1)^k x^{2k} \xrightarrow[n\to+\infty]{}$

$$= \frac{1-(-x^2)^{\dots}}{1+x^2} = \frac{1}{1+x^2}$$ [exposant rogné — probablement $n+1$]

pour $x = -1$ ou $1$, $\sum_{k=0}^n (-1)^k = \sum_{k=0}^n (-1)^k = 1 + \sum_{k=1}^n (-1)^k = 1 + \sum_{k=0}^{n-1}(-1)^{k+1} = 1 - \sum_{k=0}^{n-1}(-1)^k$. D'où $\sum_{k=0}^{+\infty}(-1)^k = 1/2 = 1/(1+1^2)$ [*sic* — la série de Grandi diverge ; la valeur $1/2$ est un prolongement abusif, conservé tel quel]

Donc $\forall x \in [-1,1]$, $\sum_{k=0}^{+\infty}(-x^2)^k = \frac{1}{1+x^2}$

avec $\forall x \in \mathbb{R}$ comme $\sin x \in [-1,1]$, $\frac{1}{1+\sin^2x} = \sum_{k=0}^{+\infty}(-\sin^2x)^k$

avec $I = \int_0^\pi x^2\sum_{k=0}^{+\infty}(-\sin^2x)^k\,dx = \sum_{k=0}^{+\infty}(-1)^k J_k(\pi)$ où $J_k(\pi) = \int_0^\pi x^2\sin^{2k}x\,dx$

avec $J_k(\pi) = \int_0^\pi x^2\left(\frac{e^{ix}-e^{-ix}}{2i}\right)^{2k}\,dx$

$= \int_0^\pi \frac{x^2}{(2i)^{2k}}\sum_{j=0}^{2k} C_{2k}^j (e^{ix})^j(-1)^{2k-j}(e^{-ix})^{2k-j}\,dx$ [exposant du $(-1)$ peu lisible]

$= \frac{1}{(-4)^k}\sum_{j=0}^{2k} C_{2k}^j(-1)^j\int_0^\pi x^2 e^{2ix(j-k)}\,dx + \frac{1}{(-4)^k}\left(C_{2k}^k \int_0^\pi x^2\,dx\right)$, $j \ne k$ [séparation du terme $j = k$ : $\int_0^\pi x^2\,dx = \pi^3/3$]

$= A \times \frac{1}{2i(j-k)}\left(\left[x^2 e^{2ix(j-k)}\right]_0^\pi - 2\int_0^\pi x e^{2ix(j-k)}\,dx\right) + \frac{1}{(-4)^k}\left(C_{2k}^k\frac{\pi^3}{3}\right)$, $j \ne k$ [où $A = \frac{1}{(-4)^k}C_{2k}^j(-1)^j$ — restitution d'après le contexte]

$= \frac{A}{2i(j-k)}\left(\pi^2-\frac{2}{2i(j-k)}\right)\left(\left[\pi e^{2i\pi(j-k)}\right]_0^\pi - \int_0^\pi e^{2i\dots}\,dx\right) + \frac{1}{3}\left(\frac{4}{\pi}\right)^k C_{2k}^k \frac{\pi^3}{3}$ [ligne très empâtée — $j \ne k$]

$= \frac{1}{(-4)^k}\sum_{j=0, j\ne k}^{2k} C_{2k}^j(-1)^j \frac{\pi((j-k)\pi-1)}{-2(j-k)^2} + \dots$ [ligne empâtée]

Donc $J_k(\pi) = \frac{1}{4^k}\left(\pm\sum_{j=0, j\ne k}^{2k} C_{2k}^j(-1)^j \frac{\pi((j-k)\pi-1)}{(j-k)^2} + \frac{C_{2k}^k\pi^3}{3}\right)$ [signe de tête de la somme incertain]

Donc $J_k(\pi) = \frac{\pi}{4^k}\left(\frac{\pi^2 C_{2k}^k}{3} - \frac{1}{2}\sum_{j=0, j\ne k}^{2k} C_{2k}^j(-1)^j \frac{\pi((j-k)\pi-1)}{(j-k)^2}\right)$, $j \ne k$ [restitution d'après la reprise en page 2]

## Page 2 — Formule finale, primitive polylog et Riemann

avec $I = \sum_{k=0}^{+\infty} \frac{(-1)^k}{4^k}\left(\frac{\pi^2 C_{2k}^k}{3} - \frac{1}{2}\sum_{j=0, j\ne k}^{2k} C_{2k}^j(-1)^j \frac{\pi((j-k)\pi-1)}{(j-k)^2}\right)$, $j \ne k$

Donc $\boxed{I = \int_0^\pi \frac{x^2}{1+\sin^2x}\,dx = \pi\sum_{k=0}^{+\infty} \frac{1}{4^k}\left(\frac{(-1)^k\pi^2 C_{2k}^k}{3} - \frac{1}{2}\sum_{j=0}^{2k} C_{2k}^j(-1)^j \frac{\pi((j-k)\pi-1)}{(j-k)^2}\right)}$, $j \ne k$

Encore en remarquant que $\int \frac{x^2}{1+\sin^2x}\,dx = \frac{1}{4\sqrt{2}}i\big(-2i\pi\,\mathrm{Li}_2(|3-2\sqrt{2}|e^{2ix}) + 2i\pi\,\mathrm{Li}_2(|3+2\sqrt{2}|e^{2ix}) + \mathrm{Li}_3(|3-2\sqrt{2}|e^{2ix}) - \mathrm{Li}_3(|3+2\sqrt{2}|e^{2ix}) + 2i\log(1+(1+2\sqrt{2}-3)e^{2ix}) - 2i\log(1-(3+2\sqrt{2})e^{2ix})\big)$ [formule issue d'un CAS — parenthésage incertain par endroits, transcrite telle quelle]

$I = \frac{1}{4\sqrt{2}}i\big(-2i\pi\,\mathrm{Li}_2(|3-2\sqrt{2}|) + 2i\pi\,\mathrm{Li}_2(|3+2\sqrt{2}|) + \mathrm{Li}_3(|3-2\sqrt{2}|) - \mathrm{Li}_3(|3+2\sqrt{2}|) + 2i\pi\log|-2+2\sqrt{2}| - 2i\pi\log|-2-2\sqrt{2}| + 0 - 0 - \mathrm{Li}_3(3-2\sqrt{2}) + \mathrm{Li}_3(3+2\sqrt{2})\big)$ [transcrite telle quelle]

Donc [raturé] $I = \frac{\pi\sqrt{2}}{4}\left(\mathrm{Li}_2(3-2\sqrt{2}) - \mathrm{Li}_2(3+2\sqrt{2}) + i\pi\log\left(\frac{2\sqrt{2}-2}{-2-2\sqrt{2}}\right)\right)$

$= \frac{\pi\sqrt{2}}{4}\left(\mathrm{Li}_2(3-2\sqrt{2}) - \mathrm{Li}_2(3+2\sqrt{2}) + i\pi\log|e^{i\pi}(3-2\sqrt{2})|\right)$

$= \frac{\pi\sqrt{2}}{4}\left(\mathrm{Li}_2(3-2\sqrt{2}) - \mathrm{Li}_2(3+2\sqrt{2}) + \dots + i\pi\log|3-2\sqrt{2}|\right)$ [terme médian illisible]

ou encore simplement $I = \lim_{n\to+\infty} \frac{\pi}{n}\sum_{k=1}^n \frac{(\pi k/n)^2}{1+\sin^2(\pi k/n)} = \lim_{n\to+\infty} \frac{\pi^3}{n^3}\sum_{k=0}^n \frac{k^2}{1+\sin^2(\pi k/n)}$ [sommes de Riemann — le « $6$ » isolé après la première somme est un résidu de calcul]

---

## 📝 Notes de transcription (fidélité)

- Page 1 : l'extension de $\sum(-x^2)^k = 1/(1+x^2)$ à $x = \pm 1$ via $\sum(-1)^k = 1/2$ est mathématiquement abusive (série divergente) — le manuscrit l'admet pour appliquer la formule en $\sin x = \pm 1$.
- Les IPP de $J_k(\pi)$ séparent le mode $j = k$ (qui donne $C_{2k}^k\pi^3/3$) des modes $j \ne k$ (oscillants, intégrés deux fois par parties).
- Page 2 : la primitive en $\mathrm{Li}_2$/$\mathrm{Li}_3$ provient visiblement d'un système de calcul formel recopié à la main (valeurs absolues et arguments redondants conservés tels quels).
- Aucune figure ni schéma sur les 2 pages.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q09-fiche1-1.png`, r150) — feuille pliée en deux, distorsions verticales confirmées, aucune figure ; p. 2 vérifiée visuellement le 2026-09-07 (rendu `/tmp/s9/fiche1-2.png`, r150, 2e passage) — formule encadrée `Donc I = ∫₀^π …`, primitive polylog `Li₂/Li₃` + sommes de Riemann confirmées, « 6 » isolé déjà signalé, aucune figure. Aucun script `reproduce_integrales-fiche-1_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- Grandi = `Σ(−1)^k = 1/2` (prolongement abusif, série divergente — signalé `[*sic*]`).
- `J_k(π) = ∫₀^π x²sin^{2k}x dx` ; `Li₂/Li₃` = polylogarithmes (primitive issue d'un CAS) ; sommes de Riemann (3ᵉ approche).
