# Intégrale de Wallis & Formule de Stirling — transcription fidèle

> 🧾 **Manuscrit original :** `wallis-stirling.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible (~95 %), transcrit fidèlement. Calculs d'équivalents très denses,
> ratures et marges conservées (encadrés/notes marginales en fin de transcription).

📄 **Source scannée :** [`wallis-stirling.pdf`](wallis-stirling.pdf)

---

## Page 1 — La limite $l = 1$ (rapport de Wallis)

[En-tête : « Intégrale de Wallis »]

$$l = \lim_{p \to +\infty} \frac{(2^p p!)^4 \cdot 2}{\pi (2p+1)! (2p)!}$$

[avec, en marge : $\lim \frac{W_{2p+2}}{W_{2p}} = 1$]

$$= \lim_{p \to +\infty} \frac{2^{4p} ((2p)!)^2 \cdot (p/e)^{4p} \cdot 2}{\pi \sqrt{2\pi(2p+1)} \left(\frac{2p+1}{e}\right)^{2p+1} \cdot \sqrt{2\pi \cdot 2p} \left(\frac{2p}{e}\right)^{2p}}$$

$$= 2 \cdot \lim_{p \to +\infty} 2^{2p} \cdot e^{4p \ln(p/e)} \cdot e^{-(2p+1)\ln(2p+1)} \cdot e^{-2p \ln(2p/e)} \cdot e^{\ln p} \cdot \sqrt{\frac{2^p \cdot p}{p^2}}$$

[encadré : $-4p + 2p + 1 + 2p$]

$$= 2 \times \lim_{p \to +\infty} e^{4p\ln(p/e) - (2p+1)\ln(2p+1) - 2p\ln(2p/e) + \ln p + 2p\ln 2}$$

$$= 2 \times \lim_{p \to +\infty} e^{2p\ln p + \ln p + \ln e - (2p+1)\ln(2p+1) + 2p\ln 2}$$

$$= 2 \times \lim_{p \to +\infty} e^{-\frac{2}{m}\ln m - \ln m + \ln e - \left(\frac{2}{m}+1\right)(\ln(2+m) - \ln m) + \frac{2}{m}\ln 2} \quad \text{où } m = \frac{1}{p}$$

$$= 2 \times \lim_{m \to 0^+} e^{\ln e - \left(\frac{2}{m}+1\right)\ln m + \left(\frac{2}{m}+1\right)\ln m - \ln(2+m)\left(\frac{2}{m}+1\right) + \frac{2}{m}\ln 2}$$

$$= 2 \times \lim_{m \to 0^+} e^{\frac{2}{m}\ln\frac{2}{2+m} - \ln(2+m)}$$

$$= 2e \times e^{-\ln 2} \times \lim_{m \to 0^+} e^{-\frac{2}{m}\ln\left(\frac{2}{m}+1\right)}$$

[encadré : $\ln\left(\frac{m+2}{2}\right)$, $\ln\left(1+\frac{m}{2}\right)$]

$$= e \times \lim_{y \to 0^+} e^{-\frac{\ln(1+y)}{y}} \quad \text{où } y = \frac{m}{2} \to 0^+$$

$$= e \times e^{-1}$$

$$l = 1$$

[À droite : $W_{2p} W_{2p+1} = \frac{\pi}{2} \frac{(2p)!}{(2^p p!)^2} = \frac{\pi/2}{(2p+1)} \cdot \frac{2p}{2p+1}$ et $W_n \sim \sqrt{\frac{\pi}{2n}}$]

[dont :] $\lim \frac{W_{2p}^2}{\frac{\pi}{2(2p+1)}} = 1 \implies \lim \frac{W_{2p}}{\sqrt{\frac{\pi}{2(2p+1)}}} \times \frac{1}{\sqrt{\frac{2p}{2p+1}}} = 1$, ainsi $\lim \frac{W_n}{\sqrt{\frac{\pi}{2n}}} = 1$.

---

## Page 2 — Équivalent de $W_n$ puis Stirling

$W_{2p} W_{2p+1} = \frac{\pi/2}{(2p+1)} = \frac{\pi/2}{2p} \times \frac{2p}{2p+1}$ et $W_{2p+1}/W_{2p+1} = \pi/2$ [raturé].

$$W_{2p}^2 = \frac{\pi/2}{2p} \times \frac{W_{2p}}{W_{2p+1}} \times \frac{2p}{2p+1}$$

$$\frac{W_{2p}}{\sqrt{\frac{\pi}{2(2p)}}} = \frac{W_{2p}}{W_{2p+1}} \times \frac{2p}{2p+1}$$

ainsi $\lim_{p \to +\infty} \frac{W_{2p}}{\sqrt{\frac{\pi}{2(2p)}}} = 1 \times 1 = 1$.

~~or $W_{2p+1}$~~ d'où $W_{2p} \sim \sqrt{\frac{\pi}{2(2p)}}$.

or $W_n \searrow$ et est minorée par $0$ donc $W_n \to$ … ainsi $W_n \underset{+\infty}{\sim} W_{2p}$ d'où $W_n \sim \sqrt{\frac{\pi}{2n}}$.

---

$$n! \sim C\sqrt{n}\left(\frac{n}{e}\right)^n$$

~~soit~~ $W_{2p} = \frac{\pi}{2} \frac{(2p)!}{(2^p p!)^2} \sim \frac{\pi}{2} \frac{C\sqrt{2p}\,(2p/e)^{2p}}{(2^p C\sqrt{p}\,(p/e)^p)^2} = \frac{\pi}{\sqrt{2}\sqrt{p}\ C}$

ainsi $C = \lim_{p \to +\infty} \frac{\pi}{\sqrt{2p}\,W_{2p}} = \lim_{p \to +\infty} \frac{\pi}{\sqrt{2p}} \times \sqrt{\frac{2(2p)}{\pi}} = \sqrt{2\pi}$.

Donc $n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$.

$e^u - (1+u/n)^n$ ; $f(u) = e^u - (1+u/n)^n$ [brouillon] ; $e^u - (1+u)$ ; $u = x + h$ ; $-x < u < 1$ ; $\frac{1}{1-u} < \frac{1}{1-u} < \frac{1}{2}$ ; $\frac{1}{1-u} < \frac{1}{2}$ [brouillons].

---

## Notes marginales (page 2, fidèlement recopiées)

- $\frac{n! \cdot e^n}{n^n \sqrt{n}}$ [coin supérieur droit].
- $\frac{dy}{y} = a\,dt$ ; $\ln|y| = at + c$ ; $y = Ke^{at}$ ; $y_0 = K$ ; … ; $Ae^{tx}$ [révisions EDO].
- $f(x+h) \simeq f(x) + hf'(x)$ ; $f(x+\frac{h}{n}) \simeq f(x) + \frac{h}{n}f'(x)$ ; … ; $f(x_0+h) \simeq f(x_0) + hf'(x_0)$ ; $f(x) \simeq f(x_0) + (x-x_0)f'(x_0)$ [formules de Taylor, colonne droite].

## 📝 Notes de transcription (fidélité)

- Calculs très denses, encre parfois légère : les exposants $(n-k)$, $(k+1)$ ont été relus deux fois.
- Plusieurs lignes raturées (débuts abandonnés) : transcrites barrées quand lisibles, sinon notées `[raturé]`.
- Les marges EDO/Taylor sont des révisions annexes sur la même feuille, sans lien direct avec Wallis.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q17-wallis-1.png`, r150) — calculs denses, encadrés et marges `W_{2p}` confirmés, aucune figure ; p. 2 vérifiée visuellement le 2026-09-07 (rendu `/tmp/s9/wallis-2.png`, r150, 2e passage) — `W_{2p} ∼ √(π/2(2p))`, `C = √(2π)`, brouillons `e^u − (1+u/n)^n`, marges EDO (`dy/y = adt`) et Taylor confirmés, aucune figure. Aucun script `reproduce_wallis-stirling_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- `W_n` = intégrales de Wallis ; `W_n ∼ √(π/2n)` ; `C = √(2π)` = constante de Stirling (`n! ∼ C√n(n/e)ⁿ`).
- `l = 1` = rapport de Wallis ; marges EDO/Taylor = révisions annexes sans lien (conservées p. 2).
