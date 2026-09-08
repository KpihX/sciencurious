# Carnet équations-inéquations — transcription fidèle

🧾 Source : [carnet-equations-inequations.pdf](carnet-equations-inequations.pdf) — document restauré Datas1, 2026-09-07.
🔍 Transcription : fidèle, page à page, sans correction ni ajout ; les doutes sont balisés.
📄 Contenu : 3 pages manuscrites — résolutions d'équations (trigonométrie, logarithmes, exponentielles, arctan, ch/sh, intégrales).

## Page 1

a) $(E1 \iff) \cos^2 \ln x + \frac{\sqrt{2}}{2} \sin(\ln x^2) - \frac{1}{2} = \frac{1}{\sqrt{2}} \quad (\text{avec } x > 0)$

[raturé] $$\iff \cos^2 \ln x + \frac{\sqrt{2}}{2} \sin(2\ln x) = \frac{1+\sqrt{2}}{2}$$

$$\iff \cos^2 \ln x + \sqrt{2} \sin \ln x \, (\cos \ln x) = \frac{1+\sqrt{2}}{2}$$

$$(\iff) \, 2\cos \ln x \left(\frac{1}{2}\cos \ln x + \frac{\sqrt{2}}{2}\sin \ln x\right) = \frac{1+\sqrt{2}}{2}$$

$$\iff 2\cos \ln x \, \cos(\ln x - \pi/3) = \frac{1+\sqrt{2}}{2}$$

$$\Rightarrow \cos(2\ln x - \pi/3) + \cos(\pi/3) = \frac{1+\sqrt{2}}{2} \quad \text{car } 2\cos a \cos b = \cos(a+b) + \cos(a-b)$$

$$\iff \cos(2\ln x - \pi/3) = \frac{\sqrt{2}}{2} = \cos \frac{\pi}{4}$$

$$\iff \left\{\begin{array}{l} 2\ln x - \pi/3 = \pi/4 + 2k\pi \\ \text{ou} \\ 2\ln x - \pi/3 = -\pi/4 + 2k\pi \end{array}\right., k \in \mathbb{Z}$$

$$\iff \left\{\begin{array}{l} x = e^{\frac{7\pi}{24} + k\pi}, \, k \in \mathbb{Z} \\ \text{ou} \\ x = e^{\frac{\pi}{24} + k\pi} \end{array}\right. \qquad S_{\mathbb{R}} = \left\{ e^{\frac{7\pi}{24} + k\pi}, \, e^{\frac{\pi}{24} + k\pi}, \, k \in \mathbb{Z} \right\}$$

b) $(\log_2 x)^{\log_2 x} = 1 \iff x^y = 1, \text{ où } y = \log_2 x \quad (x > 0) \quad (y \ne 0)$

$$\iff y \ln y = 0$$

$$\iff y = 0 \text{ ou } \ln y = 0$$

$$\iff \log_2 x = 0 \text{ (entouré, avec la note marginale : discute en } y \ne 0\text{, flèche vers la zone entourée) ou } \log_2 x = 1$$

$$S_{\mathbb{R}} = \{ 2^1 = 2 \}$$ [raturé : $2^0 = 1$ biffé dans le membre de gauche]

c) $16^x + 16^{1-x} = 10 \iff (16^x)^2 + 16 = 10 \times 16^x$

$$\iff y^2 - 10y + 16 = 0 \text{ où } y = 16^x > 0$$

$$\iff y^2 - (8+2)y + 2 \times 8 = 0$$

$$\iff 16^x = 2 \text{ ou } 8$$

$$S_{\mathbb{R}} = \left\{ \frac{\ln 2}{\ln 16} = \frac{1}{4} \, ; \, \frac{\ln 8}{\ln 16} \right\}$$

## Page 2

d) $(E1 \iff) \arctan(1-x) + \arctan x = \pi/3 \quad (x > 0)$

$$\iff \tan(\arctan(1-x) + \arctan x) = \tan \pi/3 = \sqrt{3}$$

$$\iff \frac{(1-x)+x}{1-(1-x)\times x} = \sqrt{3} \quad \text{car } \forall a,b \in ]-\pi/2, \pi/2[, \, \tan(a+b) = \frac{\tan a + \tan b}{1 - \tan a \tan b}$$

$$\iff x^2 - x + \frac{3-\sqrt{3}}{3} = 0$$

$$\Delta = \frac{-9+4\sqrt{3}}{3} < 0$$

[lecture incertaine — parenthésage]

$$S_{\mathbb{R}_{+}^{*}} = \varnothing$$

e) travail (Polynôme 2nd degré)

f/ $\cosh x + \cos \alpha = 2\sinh x + \sin \alpha \iff \frac{e^x+e^{-x}}{2} - 2\left(\frac{e^x-e^{-x}}{2}\right) = \sin \alpha - \cos \alpha = \sqrt{2}\sin(\alpha-\pi/4)$ (accolade sous le membre de droite : [lecture incertaine — intervalle, vraisemblablement $\in [-\sqrt{2}, \sqrt{2}]$])

([raturé] en marge gauche, sous « f/ »)

$$\iff -e^x + 3e^{-x} = 2\alpha$$

$$\iff (e^x)^2 + 2\alpha(e^x) - 3 = 0$$

$$\Delta = 4 \times 2\sin^2(\alpha-\pi/4) + 12 > 0$$

$$e^x = \frac{-2\sqrt{2}\sin(\alpha-\pi/4) \pm 2\sqrt{3+2\sin^2(\alpha-\pi/4)}}{2}$$ [raturé : « 2 » corrigé devant la racine]

$$\text{or } \forall \alpha \in \mathbb{R}, \quad 3+2\sin^2(\alpha-\pi/4) > 2\sin^2(\alpha-\pi/4) \iff \sqrt{3+2\sin^2(\alpha-\pi/4)} > \sqrt{2}\sin(\alpha-\pi/4)$$ [raturé : symbole $\iff$ corrigé]

$$\Rightarrow \left\{\begin{array}{l} -\sqrt{2}\sin(\alpha-\pi/4) + \sqrt{3+2\sin^2(\alpha-\pi/4)} > 0 \\ -\sqrt{2}\sin(\alpha-\pi/4) - \sqrt{3+2\sin^2(\alpha-\pi/4)} < 0 \end{array}\right.$$

[raturé : mot biffé] $$S_{\mathbb{R}} = \left\{ \ln\left(-\sqrt{2}\sin(\alpha-\pi/4) + \sqrt{3+2\sin^2(\alpha-\pi/4)}\right), \, \alpha \in \mathbb{R} \right\}$$

. Si $\alpha$ est aussi une inconnue

$$S_{\mathbb{R}^2} = \left\{ \left(\ln\left(-\sqrt{2}\sin(\lambda-\pi/4) + \sqrt{3+2\sin^2(\lambda-\pi/4)}\right), \, \lambda\right), \, \lambda \in \mathbb{R} \right\}$$ [lecture incertaine — $\alpha$ corrigé en $\lambda$]

## Page 3

g/ $J = \int_0^1 x^1 \arctan x \, dx$ [lecture incertaine — exposant : « 1 » ou trace parasite ?]

$$= [x \arctan x]_0^1 - \frac{1}{2}\int_0^1 \frac{2x}{1+x^2} \, dx$$ [*sic* — le crochet $[x \arctan x]$ et l'intégrande $2x/(1+x^2)$ correspondent à $\int \arctan x \, dx$]

$$= \pi/4 - \frac{1}{2}\left[\ln(1+x^2)\right]_0^1$$

$$J = \frac{\pi}{4} - \frac{1}{2}\ln 2$$

---

h/ $I = \int \frac{7}{x+x\ln^2 x} \, dx$

$$= 7\int \frac{1/x}{1+\ln^2 x} \, dx$$

$$= 7 \arctan \ln x + C, \, C \in \mathbb{R}$$

---

## Figures

Aucune figure sur la source (3 pages de calculs manuscrits seuls, sans schéma) — rien à reproduire en code.

## Vocabulaire

- **Mesure principale** : non employée ici ; résolutions par équivalences trigonométriques ($\cos$, $\sin$, $\arctan$).
- **Logarithme** : $\log_2 x$, $\ln x$ avec condition $x > 0$.
- **Hyperboliques** : $\cosh x = \frac{e^x+e^{-x}}{2}$, $\sinh x = \frac{e^x-e^{-x}}{2}$.
- **Intégration par parties** : $[x \arctan x]_0^1 - \int_0^1 \frac{x}{1+x^2}\,dx$ (g/).
- **Forme canonique** : $y^2-(8+2)y+2\times 8 = 0$ (c/).
