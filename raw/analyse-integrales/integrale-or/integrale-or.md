# Intégrale du nombre d'or $\int_0^{+\infty}\frac{x^{\pi/5-1}}{1+x^{2\pi}}dx = \varphi$ — transcription fidèle

> 🧾 **Manuscrit original :** `integrale-or.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible (~85 %), transcrit fidèlement. Substitution $t = 1/(1+x^{2\pi})$, fonction Bêta $B(9/10,1/10) = \pi/\sin(\pi/10)$, puis calcul exact de $\sin(\pi/10) = (\sqrt{5}-1)/4$ via $\sin(5x)$ en $x = \pi/5$. Résultat : le nombre d'or $\varphi = (1+\sqrt{5})/2$. Deux lapsus de signe (signalés).
> 📄 **Source scannée :** [`integrale-or.pdf`](integrale-or.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Substitution et fonction Bêta

$$I = \int_0^{+\infty} \frac{x^{\pi/5-1}}{1+x^{2\pi}}\,dx$$

Posons $t = \varphi(x) = \frac{1}{1+x^{2\pi}}$ qui est une bijection de $\mathbb{R}_+$ vers $[0,1]$

Or : $I = \int_0^1 t\left(\frac{1}{t}-1\right)^{\frac{\pi/5-1}{2\pi}} \times \frac{1}{2\pi} \times \frac{1}{t^2}\left(\frac{1}{t}-1\right)^{\frac{1}{2\pi}-1}$ [avec : $x = \left(\frac{1}{t}-1\right)^{1/2\pi}$]

$$= \frac{1}{2\pi}\int_0^1 \frac{1}{t}\left(\frac{1}{t}-1\right)^{-9/10}\,dt$$

$$= \frac{1}{2\pi}\int_0^1 t^{-9/10}(1-t)^{-1/10}\,dt$$ [ordre des exposants peu lisible — $B$ étant symétrique, $B(9/10,1/10)$ vaut dans tous les cas $\pi/\sin(\pi/10)$]

$$= \frac{1}{2\pi}B(9/10, 1/10) \quad \text{où } B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1}\,dt$$

fonction bêta $\forall x, y \in \mathbb{C}$ avec $\mathrm{Re}(x), \mathrm{Re}(y) > 0$

or la fonction Bêta vérifie la propriété $B(x,1-x) = \frac{\pi}{\sin(\pi x)} \to$ (cela se démontre avec le théorème des résidus)

Il vient que $I = \frac{1}{2\pi} \times \frac{\pi}{\sin(\pi/10)} = \frac{1}{2\sin(\pi/10)}$

or $\sin^2(\pi/10) = \frac{1-\cos(\pi/5)}{2}$, or $\cos^2(\pi/5)+\sin^2(\pi/5) = 1$ et $\forall x \in \mathbb{R}$, $\sin(5x) = \mathrm{Im}\left(e^{i5x}\right) = \mathrm{Im}\left((\cos x+i\sin x)^5\right)$ [bas de page]

## Page 2 — Calcul exact de $\sin(\pi/10)$ et conclusion

Ainsi $\sin 5x = 5(1-\sin^2x)^2\sin x - 10(1-\sin^2x)\sin^3x + \sin^5x$

Pour $x = \pi/5$ et $X = \sin(\pi/5)$, on a :

$$0 = 5(1-X^2)^2X - 10(1-X^2)X^3 + X^5$$

càd $X^4 - 10(1-X^2)X^2 + 5(1-X^2)^2 = 0$

càd $X^4 - 10X^2 + 10X^4 + 5 + 5X^4 - 10X^2 = 0$

càd $16X^4 - 20X^2 + 5 = 0$

càd $X^2 = \frac{20+\sqrt{80}}{32}$ [le « $+$ » est tracé seul — le « $\pm$ » apparaît à la ligne suivante]

$$= \frac{5}{8} \pm \frac{\sqrt{5}}{8}$$

[raturé] d'où $X = \sqrt{\frac{5\pm\sqrt{5}}{8}}$

or $\sin\frac{\pi}{5} < \sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$ [le « $3$ » est peu lisible — imposé par $\frac{\sqrt{3}}{2}$]

ainsi la bonne valeur est $\sin\frac{\pi}{5} = \sqrt{\frac{5-\sqrt{5}}{8}}$

Ainsi $\cos\frac{\pi}{5} = \sqrt{1-\frac{5-\sqrt{5}}{8}} = \sqrt{\frac{6+2\sqrt{5}}{16}} = \frac{1+\sqrt{5}}{4}$

d'où $\sin\frac{\pi}{10} = \sqrt{\frac{1-\frac{1+\sqrt{5}}{4}}{2}} = \sqrt{\frac{3-\sqrt{5}}{8}} = \sqrt{\frac{6-2\sqrt{5}}{16}} = \frac{-1+\sqrt{5}}{4}$

[encadré :] D'où $I = \frac{1}{2\left(\frac{1-\sqrt{5}}{4}\right)} = \frac{2}{1-\sqrt{5}} = \frac{1+\sqrt{5}}{2}$ [*sic* sur les deux premiers membres — lire $\sqrt{5}-1$ : avec $1-\sqrt{5}$ le quotient serait négatif ; le calcul précédent donne $\sin(\pi/10) = \frac{\sqrt{5}-1}{4}$ et $I = \frac{2}{\sqrt{5}-1} = \frac{1+\sqrt{5}}{2}$]

Donc $I = \int_0^{+\infty} \frac{x^{\pi/5-1}}{1+x^{2\pi}}\,dx = \frac{1+\sqrt{5}}{2} = \varphi$ [flèche vers le haut en dessous]

---

## 📝 Notes de transcription (fidélité)

- La substitution $t = 1/(1+x^{2\pi})$ donne $x = (1/t-1)^{1/2\pi}$ et $(\pi/5)/(2\pi)-1 = 1/10-1 = -9/10$, d'où la forme Bêta.
- $B(9/10,1/10) = \pi/\sin(9\pi/10) = \pi/\sin(\pi/10)$, puis $\sin(\pi/10) = (\sqrt{5}-1)/4$ via la sélection de racine $\sin(\pi/5) = \sqrt{(5-\sqrt{5})/8}$ (l'autre racine $\sqrt{(5+\sqrt{5})/8} \approx 0,95$ dépasse $\sin(\pi/3)$).
- Aucune figure ni schéma sur les 2 pages.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q05-or-1.png`, r150) — texte + équations, `B(9/10,1/10)` confirmé, aucune figure ; p. 2 vérifiée visuellement le 2026-09-07 (rendu `/tmp/s9/or-2.png`, r150, 2e passage) — chaîne `16X⁴−20X²+5 = 0`, sélection `sin(π/5) = √((5−√5)/8)`, encadré `D'où I = …` + `Donc I = … = φ` (flèche vers le haut) confirmés, *sic* `1−√5` maintenu, aucune figure. Aucun script `reproduce_integrale-or_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- `B` = fonction Bêta ; `φ` = nombre d'or `(1+√5)/2` ; résidus = théorème des résidus (admis pour `B(x,1−x)`).
- `[*sic*]` p. 2 : signes `1−√5` conservés tels que lus (quotient négatif), lecture corrigée en `√5−1`.
