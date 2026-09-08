# Fermé et complet (voisinages, Cauchy, complétude) — transcription fidèle

> 🧾 **Manuscrit original :** `ferme-complet.pdf` (scan, 4 pages, encre bleue sur papier blanc ; bords droit et bas partiellement rognés) · ✍️ KpihX
> 🔍 **Statut :** lisible (~80 %), transcrit fidèlement. Page 1 : limite, voisinages (avec NB critique), suites de Cauchy, convergente ⟹ Cauchy. Page 2 : $E$ complet, ouverts/fermés/complets, début du théorème « complète ssi fermée ». Page 3 : construction des $(a_n)$, $(r_n)$ et contradiction. Page 4 : réciproque, remarques ($|K| \equiv \mathbb{R}$, $\frac{1}{n}$) et application $(\mathbb{R}, \mathbb{Q})$.
> 📄 **Source scannée :** [`ferme-complet.pdf`](ferme-complet.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Limite, voisinages, Cauchy, convergente ⟹ Cauchy

Soit un $K$-ev $E$, muni d'une norme $\|\cdot\|$.

Soit $(U_n)_{n \in \mathbb{N}}$ une suite d'elts de $E$ et $u \in E$.

. $\lim_{n\to+\infty} U_n = u \iff \forall \varepsilon > 0, \exists N_\varepsilon \in \mathbb{N}$ / $\forall n \in \mathbb{N}, n \ge N_\varepsilon \Rightarrow \|U_n - u\| < \varepsilon$

[sous la définition : $(\varepsilon \in K)$]

($>$ une relation d'ordre totale sur $K$, [fin raturée])

[en marge droite, pâle : « …$(|K|, >) \equiv (\mathbb{R}, >_{\mathbb{R}})$ » — transparence de la feuille voisine]

. un voisinage de $u$ est tout sous ensemble $V$ de $E$ / $u \in V$. On note $\mathcal{V}(u)$, l'ens des voisinages de $u$ dans $E$.

NB : la deft donnée en amont est nécessaire mais pas suffisante car sinon $\{u\}$ [lecture incertaine — « $2u$ ? »] serait un voisinage de $u$ ce qui n'a pas grande utilité. En plus de la condition donnée sur $V$, il faut aussi qu'$\exists w \in E$ [raturé] et $r \in |K|$ / $r > 0_{|K|}$ et $\{w \in E / \|u-w\| < r\} \subseteq V$.

En définitive, $V \in \mathcal{V}(u) \iff \exists r \in |K|$ / $r > 0_{|K|}$ et $\{w \in E / \|u-w\| < r\} \subseteq V$.

. Soit $(U_n)_{n \in \mathbb{N}}$, une suite d'elts de $E$. $(U_n)$ est dite de Cauchy ssi $\forall \varepsilon > 0, \exists N \in \mathbb{N}$ / $\forall n, m \in \mathbb{N}, n, m \ge N \Rightarrow \|U_n-U_m\| < \varepsilon$. [le « $N$ » est réécrit sur une rature]

Prop : Toute suite crgte [« convergente » abrégé] de $E$ est de Cauchy.

En effet, soit $(U_n)$ une suite d'elts de $E$ [« crgte » ajouté en exposant] Soit $\varepsilon > 0$

Cherchons $N \in \mathbb{N}$ / $\forall n, m \in \mathbb{N}, n, m \ge N \Rightarrow \|U_n-U_m\| < \varepsilon$.

Soient $m, n \in \mathbb{N}$. $\|U_n-U_m\| \le$ [membre de droite raturé] Car $(U_n)$ converge dans $E$ alors $\exists u \in E$ / $\lim_{n\to+\infty} U_n = u$

---

## Page 2 — Complétude, ouverts, fermés ; théorème (sens $\Rightarrow$)

Ona alors : $\|U_n-U_m\| \le \|U_n-u\| + \|U_m-u\|$

Car $\frac{\varepsilon}{2} > 0$ et $\lim_{n\to+\infty} U_n = u$ alors $\exists N' \in \mathbb{N}$ / $\forall n \in \mathbb{N}, n \ge N' \Rightarrow \|U_n-u\| < \varepsilon/2$.

Pour $n, m \ge N'$, $\|U_n-U_m\| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$. Prendre $N = N'$ [fin de ligne rognée]

Deft : $E$ est dit complet ssi toute suite de Cauchy de $E$ crge dans $E \iff \forall (U_n) \equiv$ de Cauchy dans $E, \exists u \in E$ / $\lim_{n\to+\infty} U_n = u$.

. Soit $A \subseteq E$. \* $A$ est dite ouverte ssi $\forall a \in A, A \in \mathcal{V}(a) \iff \forall a \in A, \exists r \in |K|$ / $r > 0_{|K|}$ et $\{b \in E / \|a-b\| < r\} \subseteq A$.

\* $A$ est dite fermée ssi $C_E^A$ est ouverte $\iff \forall a \in C_E^A, \exists r \in |K|$ / $r > 0_{|K|}$ et $\{b \in E / \|a-b\| < r\} \cap A = \emptyset$

\* $A$ est dite complète ssi toute suite […] de Cauchy de $A$ crge dans $A \iff \forall (A_n) \equiv$ de Cauchy dans $A, \exists a \in A$ / $\lim_{n\to+\infty} A_n = a$. [bord gauche rogné]

[Th]éo : $A$ est complète ssi $A$ est fermée. (pour $E$ complet) [bord gauche rogné]

[⇒] / Supposons par l'absurde qu'$\exists a \in C_E^A$ / $\forall r \in |K|$ / $r > 0_{|K|}$, on ait $\{b \in E / \|a-b\| < r\} \cap A \neq \emptyset$. Mq $a \in A$. [bord gauche rogné]

[Co]nstruisons les suites $(a_n)_\mathbb{N}$ et $(r_n)_\mathbb{N}$ de la façon suivante : [bord gauche rogné ; suite page 3]

---

## Page 3 — Construction de $(a_n)$, $(r_n)$ et contradiction

[…]$r_0$ est un scalaire quelconque strict positif de $K$.

D'après l'hypothèse de départ $\exists b \in A$ / $\|a-b\| < r_0$ [en interligne : on prend $a_0 = b$]

− pour $n \in \mathbb{N}^*$ / $r_{n-1}$ ont déjà et $a_{n-1}$ ayant déjà été construits, $r_n = \min(\frac{1}{n}, \|a-a_{n-1}\|)$ [$> 0$ — empâté] et d'après l'hypothèse de départ, $\exists b \in A$ / $\|a-b\| < r_n$

on prend alors $a_n = b$. Et vu que $\|a-a_n\| < r_n$ […] [fin de ligne rognée]

alors $a_n \neq a_{n-1}$

Rq : $a_n \in A$ $\forall n \in \mathbb{N}$. $(r_n)_\mathbb{N}$ est strict ↓ [flèche : strictement décroissante]

Mq $\lim_{n\to+\infty} a_n = a$. Soit $\varepsilon > 0$. Cherchons $N_\varepsilon \in \mathbb{N}$ / $\forall n \in \mathbb{N}, n \ge N_\varepsilon \Rightarrow \|a_n-a\| < \varepsilon$

[« Soit » raturé] $n \in \mathbb{N}$ / $n \ge N = E(\frac{1}{\varepsilon}) + 1$. [$E$ = partie entière]

[« Car $(r_n)_\mathbb{N}$ est décroissante » — raturé]

Ona : $\|a_n-a\| < r_n \le \frac{1}{n} \le \frac{1}{N} < \varepsilon$. prendre alors $N_\varepsilon = N$

Ainsi $\lim_{n\to+\infty} a_n = a$. Car $a_n \in A$ $\forall n \in \mathbb{N}$ et que $A$ est complète alors $a \in A$ (vu que le fait $\lim_{n\to+\infty} a_n = a \Rightarrow (a_n)$ est de Cauchy d'après une proposition précédente et car $(a_n)_\mathbb{N} \in A^\mathbb{N}$, alors $(a_n)_\mathbb{N}$ doit converger dans $A$ d'après l'hypothèse de départ)

or $a \in A$ est absurde vu que dès le départ ona $a \in C_E^A$

Ainsi $\forall a \in C_E^A, \exists r \in K$ / $r > 0_K$ et $\{b \in E / \|a-b\| < r\} \cap A = \emptyset$. CQFD !

---

## Page 4 — Réciproque, remarques et application $(\mathbb{R}, \mathbb{Q})$

$\Leftarrow$ / Supp par l'absurde qu'$\exists$ une suite $(a_n)_\mathbb{N}$ de Cauchy non convergente dans $A$. Car $E$ est complet $(a_n)_\mathbb{N}$ crge dans $E$ et plus précisément dans $C_E^A$.

Soit $a = \lim_{n\to+\infty} a_n \in C_E^A$. Car $A$ est fermé, $\exists r \in |K|$ / $r > 0_{|K|}$ et $\{b \in E / \|a-b\| < r\} \cap A = \emptyset$. [bord droit rogné]

Pour $\varepsilon =$ […] [bord droit rogné] $\forall N \in \mathbb{N}$, pour $n = N$, ona : $\|a_n-a\| > r = \varepsilon$ car $a_n \in A$

et ainsi $(a_n)_\mathbb{N}$ [« converge… » raturé] ne crge pas vers $a$, ce qui est absurde !

Donc $\forall$ suite $(a_n)_\mathbb{N}$ de Cauchy dans $A$, $(a_n)$ crge dans $A$. D'où $A$ est complet, cqfd !

Rq : le théorème et la démonstration restent valables quand bien même $E$ n'est pas complet à condition qu'on puisse trouver un plus grand ev complet contenant $A$ et prendre $E$ comme cet ev

NB : on peut se permettre d'écrire $\frac{1}{n}$ avec elt de $|K|$ dans la mesure où car $(|K|, >) \equiv (\mathbb{R}, >)$, alors $\frac{1}{n}$ est sous entendu comme le correspondant biunivoque de l'elt $1$ de $\mathbb{R}$ dans $|K|$.

Application : pour $(E, A) = (\mathbb{R}, \mathbb{Q})$, car $\mathbb{Q}$ n'est pas fermé, il existe des suites de $\mathbb{Q}$ non crgtes dans $\mathbb{Q}$. Ex : $u_n = (1+\frac{1}{n})^n \xrightarrow[n\to+\infty]{} e$ [bas rogné]

---

## Figures

Aucune figure ni schéma : définitions et preuves textuelles uniquement (constaté sur les pages 1 et 4 relues + second passage pp. 2–3 le 2026-09-07, /tmp/s7/, pdftoppm -png -r 150, texte seul, pas de PNG requis).

## Vocabulaire

- $crgte$ = convergente (abrégé) ; $Deft$/deft = définition ; $Mq$ = montrons que ; $Ona$ = on a ; $Rq$ = remarque ; $cqfd$.
- $\equiv$ = « qui est » ; $E(\cdot)$ = partie entière ; $C_E^A$ = complémentaire de $A$ dans $E$ ; $\mathcal{V}(u)$ = voisinages de $u$.
- $|K|$ = copie ordonnée de $\mathbb{R}$ dans $K$ (notation volontaire de l'auteur, cf. NB p. 4 et marge p. 1).

---

## 📝 Notes de transcription (fidélité)

- Encre bleue sur papier blanc ; bords droit et bas rognés sur les pages 2–4 (chaque coupe est balisée).
- $|K|$ est une notation volontaire de l'auteur (copie ordonnée de $\mathbb{R}$ dans $K$, cf. NB p. 4 et marge p. 1) — conservée partout, sauf p. 3 où l'auteur écrit $\exists r \in K$, $r > 0_K$ (incohérence conservée telle quelle).
- Abréviations d'origine : $crgte$ = convergente, $Deft$/deft, $Mq$, $Ona$, $Rq$, $cqfd$, $\equiv$ = « qui est », $E(\cdot)$ = partie entière, $C_E^A$ = complémentaire.
- Coquilles conservées : « une relation d'ordre totale », « dans la mesure où car », « $r_{n-1}$ ont déjà », « En plus de la condition donnée sur $V$, il faut aussi qu'$\exists w \in E$ » [quantificateur raturé aussitôt].
- Aucune figure à reproduire : ni courbe ni schéma (que des définitions et preuves textuelles).
