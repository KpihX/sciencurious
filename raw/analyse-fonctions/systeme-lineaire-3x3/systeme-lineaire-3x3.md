# Système symétrique 3×3 et résolution de Cardan — transcription fidèle

> 🧾 **Manuscrit original :** `systeme-lineaire-3x3.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible (~85 %), transcrit fidèlement. Sommes symétriques $S_1, P, S_2, S_3$ du système $x+y+z=1$, $x^2+y^2+z^2=2$, $x^3+y^3+z^3=3$, puis résolution complète du cubic par la méthode de Cardan (condition de jauge, résultante $(F)$, formule explicite, valeurs approchées). Deux coquilles de signe (signalées) : le calcul impose $-\frac{1}{6}$ là où un « $+$ » est tracé, et $\sqrt{26}$ là où « $\sqrt{126}$ » semblait se lire.
> 📄 **Source scannée :** [`systeme-lineaire-3x3.pdf`](systeme-lineaire-3x3.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Sommes symétriques

$$\begin{cases} x+y+z = 1 & (E_1) \\ x^2+y^2+z^2 = 2 & (E_2) \\ x^3+y^3+z^3 = 3 & (E_3) \end{cases}$$

[raturé : « 1/ $R = xyz = ?$ » puis $(x+y+z)(xy+yz)$ — essai entièrement biffé d'une grande croix]

1/ $S_1 = xy+yz+zx = \frac{1}{2}[(x^2+y^2+z^2)+(x+y+z)^2] = -1/2$ [*sic* — avec le « $+$ » tracé le calcul donnerait $+3/2$ ; le résultat $-\frac{1}{2}$ suppose $(x+y+z)^2-(x^2+y^2+z^2)$]

2/ $P = xyz = ?$

$S_1(x+y+z) = -1/2 \iff (xy+yz+zx)(x+y+z) = -1/2$

$$\iff 3xyz + x^2(y+z) + y^2(x+z) + z^2(x+y) = -1/2$$

$$\iff 3P + x^2(1-x) + y^2(1-y) + z^2(1-z) = -1/2$$

$$\iff 3P + 2 - 3 = -1/2$$

$$\iff P = 1/6$$

3/ $S_2 = x^2y^2 + x^2z^2 + y^2z^2 = ?$

$$S_2 = S_1^2 - 2(x^2yz + y^2xz + z^2xy) = \frac{1}{4} - 2P(x+y+z) = -1/12$$

4/ $S_3 = x^4+y^4+z^4 = ?$

$$S_3 = (x^2+y^2+z^2)^2 - 2(x^2y^2+y^2z^2+x^2z^2) = 2^2 - 2\times\frac{-1}{12} = \frac{25}{6}$$ [le « $\times$ » est tracé « x », sans parenthèses]

5/ $x, y, z = ?$ Solutions de $(E)$ : $X^3 - X^2 - \frac{1}{2}X + \frac{1}{6} = 0$ [*sic* — le signe devant $\frac{1}{6}$ est tracé « $+$ » mais la réduite $Y^3-\frac{5}{6}Y-\frac{11}{27}$ en fin de page impose $-\frac{1}{6}$]

Cherchons $a \in \mathbb{R}$ / pour $X = Y+a$ on a : $Y^3 + pY + q = 0$

on trouve $a = 1/3$ et dans(?) $(E) \iff Y^3 - \frac{5}{6}Y - \frac{11}{27} = 0$

## Page 2 — Méthode de Cardan et valeurs approchées

$(E) \iff 54Y^3 - 45Y - 22 = 0$

Cherchons $u$ et $v \in \mathbb{R}$ / $Y = u+v$ soit sol de $(E)$ [ligne empâtée]

$(E) \iff 54(u^3+v^3) + (u+v)(162uv-45) - 22 = 0$

Pour faire disparaître le terme en $u+v$ on va fixer une condition de Jauge : $162uv-45 = 0$ d'où $\begin{cases} u^3+v^3 = \frac{11}{27} \\ u^3v^3 = \frac{125}{5832} \end{cases}$

Sont sols de $(F)$ : $U^2 - \frac{11}{27}U + \frac{125}{5832} = 0$ [début de phrase peu lisible]

$\times 5832$ : $(F) \iff 5832U^2 - 2376U + 125 = 0$ [symbole de tête peu lisible]

$$\iff U = \frac{2376 \pm \sqrt{2729376}}{11664}$$

ainsi [raturé] $(E) \implies X = \sqrt[3]{\frac{2376+\sqrt{2729376}}{11664}} + \sqrt[3]{\frac{2376-\sqrt{2729376}}{11664}}$

$$X = \sqrt[3]{\frac{11}{54}+\frac{\sqrt{26}}{36}} + \sqrt[3]{\frac{11}{54}-\frac{\sqrt{26}}{36}} + \frac{1}{3}$$ [le radicande est bien $\sqrt{26}$ : $\sqrt{2729376}/11664 = \sqrt{26}/36$ car $2729376 = 11664 \times 234 = 11664 \times 9 \times 26$ ; le glyphe ressemblait à $\sqrt{126}$]

[grande accolade sous l'expression, légendée $X_0$ ; mot raturé au-dessus]

[raturé] Par la suite on déduit que $X_0$ est la seule solution de $(E)$, ainsi $x, y, z$ ne peuvent exister dans $\mathbb{R}$ mais plutôt dans $\mathbb{C}$ et on a approximativement

$$\{x, y, z\} = \{1,431,\ -0,215+0,265i,\ -0,215-0,265i\} \text{ [virgules décimales d'origine]}$$

---

## Figures

Aucune figure ni schéma sur les 2 pages (relues intégralement).

## Vocabulaire

- $(E_1)(E_2)(E_3)$ = équations du système ; $(E)$ = cubic ; $(F)$ = résultante ; $S_1, P, S_2, S_3$ = sommes symétriques ; jauge ($162uv-45 = 0$) ; Cardan ; $X_0$.

---

## 📝 Notes de transcription (fidélité)

- L'expansion $(xy+yz+zx)(x+y+z) = 3xyz + \sum x^2(y+z)$ puis $y+z = 1-x$ (grâce à $(E_1)$) donne $3P + (x^2+y^2+z^2) - (x^3+y^3+z^3) = 3P + 2 - 3 = -1/2$, d'où $P = 1/6$.
- Le cubic des racines $X^3 - X^2 - \frac{1}{2}X - \frac{1}{6} = 0$ se réduit via $X = Y + \frac{1}{3}$ en $Y^3 - \frac{5}{6}Y - \frac{11}{27} = 0$, soit $\times 54$ : $54Y^3 - 45Y - 22 = 0$.
- La valeur approchée $X_0 \approx 1,431$ vérifie bien $X_0^3-X_0^2-X_0/2-1/6 \approx 0$ ; les deux autres racines sont complexes conjuguées de module $\approx 0,34$.
- Aucune figure ni schéma sur les 2 pages.
