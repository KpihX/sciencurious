# Intégrales Eulériennes — transcription fidèle

> 🧾 **Manuscrit original :** `integrales-euleriennes.pdf` (scan, 6 pages) · ✍️ KpihX · restaurée Datas1 2026-09-07
> 🔍 **Statut :** lisible (~90 %), transcrit fidèlement. Encre légère par endroits, ratures et notes marginales conservées.

📄 **Source scannée :** [`integrales-euleriennes.pdf`](integrales-euleriennes.pdf)

---

## Page 1 — Fonction Gamma (2ᵉ espèce)

[En-tête : « Intégrales Eulériennes »]

Celles de 2ⁿᵈᵉ espèce sont représentées par la f° de Gamma :

$$\Gamma(x) = \int_0^{\infty} e^{-t} t^{x-1}\,dt.$$

Posons $f(t) = e^{-t} t^{x-1}$ $\forall t \in \mathbb{R}_+^*$ et pour $x$ fixé.

• $D_{\Gamma} =$ ? Soit $x \in \mathbb{R}$. $\Gamma \equiv$ I.I.C en $+\infty$ et $0^+$ (à priori) [en marge droite : « limite »].

Du coup $\Gamma(x)$ cvge ssi $I_1 = \int_0^1 f(t)\,dt$ et $I_2 = \int_1^{+\infty} f(t)\,dt$ cvgent. Remarquons de $f(t) > 0$ $\forall t \in \mathbb{R}_+^*$ [lecture incertaine — « $>$ » ou « $\geqslant$ » ?].

— Ona : $f(t) \underset{0^+}{\sim} t^{x-1}$, ainsi d'après le critère des équivalents $I_1$ cvge ssi $x - 1 > -1 \iff x > 0$.

— De plus [raturé — « $\forall x \in \mathbb{R}$ » barré] $\lim_{t \to +\infty} t^2 f(t) = 0$, ainsi d'après la règle [lecture incertaine — « si … » entre chevrons] (où $\alpha = 2$), car $\alpha > 1$, $I_2$ converge $\forall x \in \mathbb{R}$.

En définitive [encadré : $D_{\Gamma} = \mathbb{R}_+^*$].

• $\forall x \in \mathbb{R}_+^*$, $\Gamma(x+1) = x\Gamma(x)$, $\Gamma(1) = 1 \implies \Gamma(n) = (n-1)!$ $\forall n \in \mathbb{N}^*$.

• Soit $n \in \mathbb{N}$,

$$\Gamma(n+1/2) = (n-1/2)\,\Gamma(n-1/2) \quad \text{si } n \geqslant 1$$
$$= (n-1/2)\,(n-3/2)\,\Gamma(n-3/2) \quad \text{si } n \geqslant 2$$
$$\vdots$$
$$\Gamma(n+1/2) = (n-1/2)\,(n-3/2)\cdots\left(n-\frac{2n-1}{2}\right)\Gamma\left(n-\frac{2n-1}{2}\right)$$

d'où [encadré : $\Gamma(n+1/2) = (n-1/2)(n-3/2)\cdots 1/2\ \Gamma(1/2) = \prod_{k=1}^{n}\left(n-\frac{2k-1}{2}\right)\Gamma(1/2)$].

— $\Gamma(1/2) =$ ? Ona : $\Gamma(1/2) = \int_0^{\infty} e^{-t} t^{-1/2}\,dt$. Posons $x = \sqrt{t}$. Ona : $\Gamma(1/2) = 2\int_0^{\infty} e^{-x^2}\,dx = 2 \times \frac{\sqrt{\pi}}{2} \implies$ [encadré : $\Gamma(1/2) = \sqrt{\pi}$].

Donc $\forall n \in \mathbb{N}$, $\Gamma(n+1/2) = \sqrt{\pi} \prod_{k=0}\left(n-\frac{2k-1}{2}\right)$ [lecture incertaine — bornes du produit] $= \frac{(2n)!}{2^{2n}\,n!}\sqrt{\pi}$.

---

## Page 2 — Fonction Bêta (1ʳᵉ espèce)

✳ Celles de 1ʳᵉ espèce sont représentées par

$$\beta(p,q) = \int_0^1 t^{p-1}(1-t)^{q-1}\,dt, \quad (p,q) \in \mathbb{R}^2.$$

• D'après l'ANNEXE, $\beta(p,q)$ converge ssi $p, q \in \mathbb{R}_+^*$ et absolument sur $\mathbb{K}$ ssi $\mathrm{Re}(p), \mathrm{Re}(q) \in \mathbb{R}_+^*$.

— $B(x,y) = B(y,x)$ $\forall x, y \in \mathbb{R}_+^*$.

— $B(x,1) = 1/x$.

— $\forall x, y \in \mathbb{R}_+^*$, $B(x,y) = \frac{y-1}{x}\,B(x+1, y-1)$ [en haut à droite : pour $q > 1$]. En particulier, $\forall n, m \in \mathbb{N}^*$,

$$B(n,m) = \frac{(n-1)!\,(m-1)!}{(n+m-1)!} = \frac{\Gamma(n)\Gamma(m)}{\Gamma(n+m)}.$$

• Autre expression de $\beta$ : $\forall p, q \in \mathbb{R}_+^*$,

$$B(p,q) = 2\int_0^{\pi/2} \cos^{2p-1} t\,\sin^{2q-1} t\,dt$$

[lecture incertaine — petite annotation sous l'intégrale, illisible].

• Relation avec $\Gamma$ (généralisation du cas des entiers). Soit $p, q \in \mathbb{R}_+^*$.

$$\Gamma(p) = \int_0^{+\infty} e^{-t} t^{p-1}\,dt = 2\int_0^{+\infty} e^{-x^2} x^{2p-1}\,dx \quad (x = \sqrt{t}).$$

Ainsi $\Gamma(p)\Gamma(q) = 4\left(\int_0^{+\infty} e^{-x^2} x^{2p-1}\,dx\right)\left(\int_0^{+\infty} e^{-y^2} y^{2q-1}\,dy\right)$

$$= 4\int_0^{+\infty}\!\!\int_0^{+\infty} e^{-(x^2+y^2)} x^{2p-1} y^{2q-1}\,dx\,dy$$
$$= 4\int_{\theta = 0}\int_{r = 0}^{+\infty} e^{-r^2} (r\cos\theta)^{2p-1} (r\sin\theta)^{2q-1} r\,dr\,d\theta$$

[lecture incertaine — bornes/ensemble d'intégration du passage en polaires].

---

## Page 3 — Relation $B = \Gamma\Gamma/\Gamma$, compléments

$$\Gamma(p)\Gamma(q) = \left(\int_0^{\pi/2} \cos^{2p-1}(\theta)\,\sin^{2q-1}(\theta)\,d\theta\right)\left(\int_0^{+\infty} e^{-r^2} r^{2p+2q-1}\,dr\right)$$
$$= B(p,q) \times \Gamma(p+q).$$

D'où [encadré : $B(p,q) = \dfrac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$].

Application : $I = \int_0^1 t^{3/2}(1-t)^{1/2}\,dt = B(3/2, 5/2) = \dfrac{\Gamma(3/2)\Gamma(5/2)}{\Gamma(4)}$.

$$I = \frac{3/2 \times \Gamma(3/2)^2}{6} = \frac{1}{4} \times \left(\frac{1}{2} \times \sqrt{\pi}\right)^2 \implies \text{[souligné : } I = \frac{\pi}{16}\text{]}.$$

✳ [« Formule des compléments »]

• Soit $p \in ]0,1[$, $\Gamma(p)\Gamma(1-p) =$ ?

D'après ce qui précède, $\Gamma(p)\Gamma(1-p) = \Gamma(p+1-p)\,B(p,1-p) = 0!\int_0^1 t^{p-1}(1-t)^{-p}\,dt$

$$=_{u = \frac{t}{1-t}} \int_0^{+\infty} \frac{u^{p-1}}{1+u}\,du \implies \Gamma(p)\Gamma(1-p) = \frac{\pi}{\sin(p\pi)} \quad \text{[en marge : (avec le thm des résidus)]}.$$

Ce résultat est valable $\forall p \in \mathbb{C}$ / $\mathrm{Re}(p) \in ]0,1[$.

Ex : $\Gamma(0,5) = \sqrt{\Gamma(0,5)\Gamma(1-0,5)} = \sqrt{\frac{\pi}{\sin(0,5\pi)}} = \sqrt{\pi}$.

✳ Relation avec $\binom{n}{k}$.

Soit $n, m \in \mathbb{N}^*$.

• $B(n,m) = \dfrac{(n-1)!\,(m-1)!}{(n+m-1)!} = \dfrac{1}{(m+n-1)}\,C_{\,m+n-2}^{\,n-1}$.

---

## Page 4 — Coefficients binomiaux, Wallis (1ʳᵉ approche)

[Jacobi — mot en haut de page]

• $\binom{x+y}{x} = \dfrac{(x+y)!}{x!\,y!} = \dfrac{(x+y)\,\Gamma(x+y)}{x\,\Gamma(x)\ y\,\Gamma(y)} = \dfrac{x+y}{xy} \times \dfrac{\Gamma(x+y)}{\Gamma(x)\Gamma(y)}$ [lecture incertaine — dénominateur du dernier facteur peu lisible].

Alors [encadré : $C_{x+y}^{x} = C_{x+y}^{y} = \dfrac{x+y}{xy\,B(x,y)}$].

d'où [encadré : $C_n^p = \dfrac{n}{p\,(n-p)\,B(p,\,n-p)}$].

Application : $I = \int_0^{+\infty} \dfrac{dx}{1+x^4} =_{u = x^4} \dfrac{1}{4}\int_0^{+\infty} \dfrac{du}{(1+u)\,u^{3/4}}$ [raturé — essais de changement de variable].

$$I = \ldots \int_0^1 t^{-3/4}(1-t)^{-1/4}\,dt = B(1/4, 3/4) = \frac{\pi}{\sin\frac{\pi}{4}} = \pi\sqrt{2} \quad \text{[*sic* — facteur } 1/4 \text{ du changement } u = x^4 \text{ omis dans la dernière égalité ; attendre } \pi\sqrt{2}/4 \text{, confirmé au second passage sur `/tmp/s8/euler-4.png` + crop]}.$$

[« 3) I. » ?] Intégrales de Wallis.

$I_n = \int_0^{\pi/2} \sin^n x\,dx$. ~~$I_{n+2} = -\int_0^{\pi/2} \cos x\,\sin^n x\,dx = n\int_0^{\pi/2} \cos x\,\sin^n x\,dx$~~ [raturé — IPP essayée puis abandonnée] $(n \in \mathbb{N})$. ~~[$I_{n+1} = n\,I_n$, $(n \in \mathbb{N}^*)$]~~ [raturé] $I_{n+2}$. Soit $n \in \mathbb{N}^*$ [lecture incertaine — fragment].

• $I_n = -\int_0^{\pi/2} \cos x\,\sin^{n-1} x\,dx$ [lecture incertaine — exposant] $= n\int_0^{\pi/2} \cos^2 x\,\sin^{n-2} x\,dx = n\int_0^{\pi/2} (1-\sin^2 x)\,\sin^{n-2} x\,dx \quad (n \geqslant 2)$.

$$I_n = (n-1)(I_{n-2} - I_n) \implies I_n = \frac{n-1}{n}\,I_{n-2}.$$

• $I_0 = \pi/2$, $I_1 = 1$ d'où pour $k \in \mathbb{N}$, $I_{2k} = \frac{2k-1}{2k} \times \frac{2k-3}{2k-2} \times \cdots \times \frac{1}{2}\,I_0$.

d'où $I_{2k} = \dfrac{(2k-1)!!}{(2k)!!} \times \dfrac{\pi}{2} = \dfrac{\pi}{2^{2k}} \times \dfrac{(2k)!}{k!\,(k-1)!}$ [lecture incertaine — dénominateur] $= \dfrac{\pi}{2^{2k}}\,C_{\,2k-2}^{\,k}$ [lecture incertaine — indice du coefficient binomial].

$$I_{2k+1} = \frac{2k}{2k+1} \times \frac{2k-2}{2k-1} \times \cdots \times \frac{2}{3} \times I_1 = \frac{(2k)!!}{(2k+1)!!} \times 1 = \frac{2^{2k}\,k!^2}{(2k+1)!}.$$

---

## Page 5 — Wallis (2ᵉ approche, via Bêta)

[En haut : fin de la page 4, « $I_{n+2} = \ldots$ », recouverte].

Approche 2 : Soit $n \in \mathbb{N}$, $I_n = \int_0^{\pi/2} \sin^n x\,dx =_{\sin x = \sqrt{t}} \int_0^1 t^{n/2} \times \dfrac{1}{2\sqrt{t}\sqrt{1-t}}\,dt$.

$$I_n = \frac{1}{2}\int_0^1 t^{\frac{n-1}{2}}(1-t)^{-1/2}\,dt = \frac{1}{2}\,B\left(\frac{n+1}{2},\,1/2\right) = \frac{1}{2}\,\frac{\Gamma\left(\frac{n+1}{2}\right)\sqrt{\pi}}{\Gamma\left(\frac{n}{2}+1\right)}.$$

• Si $n = 2k$ ($k \in \mathbb{N}$), $I_n = \dfrac{\sqrt{\pi}\ \Gamma(k+1/2)}{2\ \Gamma(k+1)} = \dfrac{\sqrt{\pi} \times (1/2 \times 3/2 \times \cdots \times (k-1/2)) \times \sqrt{\pi}}{2\ k!}$.

$$I_n = I_{2k} = \frac{\pi}{k!} \times \frac{(2k-1)!!}{2^{k+1}} = \frac{\pi}{k!} \times \frac{(2k-1)!}{(k-1)! \times 2^{2k}} = \frac{\pi}{2^{2k}}\,C_{\,2k-1}^{\,k}.$$

• Si $n = 2k+1$ ($k \in \mathbb{N}$), $I_n = \dfrac{1}{2}\,\dfrac{\Gamma(k+1)\sqrt{\pi}}{\Gamma(k+1+1/2)} = \dfrac{1}{2} \times \dfrac{k!\,\sqrt{\pi}}{1/2 \times 3/2 \times \cdots \times (k+1/2)\,\sqrt{\pi}}$.

$$I_n = I_{2k+1} = \frac{k!\ 2^{k+1}}{2 \times (2k+1)!!} = \frac{k!^2\,2^{2k}}{(2k+1)!}.$$

---

## Page 6 — ANNEXE (fonction Bêta : cas entiers, convergence complexe)

[En haut : fin d'une ligne de la page 5, recouverte].

✳ [« Fonction bêta »] — colonne de gauche.

$$B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1}\,dt.$$

• $B(x,y) = B(y,x)$.

• $B(x,y) = \dfrac{y-1}{x}\,B(x+1, y-1) \quad (y > 1)$.

~~• $B(x,0) = \ldots$~~ [raturé — ligne barrée, illisible].

~~Pour $x, y \in \mathbb{N}^*$~~ [raturé].

• $B(x,1) = \int_0^1 t^{x-1}\,dt = \dfrac{1}{x}$.

• Pour $x, y \in \mathbb{N}^*$ :

$$B(x,y) = \frac{y-1}{x}\,B(x+1, y-1) \quad \text{pour } y \geqslant 2$$
$$= \frac{y-1}{x} \times \frac{y-2}{x+1}\,B(x+2, y-2) \quad \text{pour } y \geqslant 3$$
$$= \frac{y-1}{x} \times \frac{y-2}{x+1} \times \cdots \times \frac{1}{x+y-2} \times B(x+y-1, 1)$$
$$= \frac{(y-1)!}{A^{y-1}_{x+y-1}} \times \frac{1}{x+y-1} \quad \text{[lecture incertaine — indices de l'arrangement]}.$$

~~$B(x,y) = \dfrac{1}{C^{y-1}_{x}\,(x+y-1)}$~~ [grande croix — passage abandonné].

$$B(x,y) = \frac{(y-1)!}{A^{y-1}_{x+y-2}} \times \frac{1}{(x+y-1)} \quad \text{[lecture incertaine — indices de l'arrangement]}.$$

[encadré : $B(x,y) = \dfrac{(y-1)!\,(x-1)!}{(x+y-1)!} = \dfrac{\Gamma(y)\,\Gamma(x)}{\Gamma(x+y)}$].

— Colonne de droite (convergence sur $\mathbb{C}$).

$\beta$ converge sur $\mathbb{R}$ ssi $x, y > 0$ et converge absolument sur $\mathbb{C}$ ssi $\mathrm{Re}(x), \mathrm{Re}(y) > 0$.

En effet, pour $x = \mathrm{Re}\,x + i\,\mathrm{Im}\,x$ et $y = \mathrm{Re}\,y + i\,\mathrm{Im}\,y$ [lecture incertaine — fin de ligne],

$$[\text{raturé — symbole barré}] \int_0^1 \left|t^{x-1}(1-t)^{y-1}\right|\,dt \equiv \text{I.I.C} \quad \text{[en marge : « en 0 et 1 à priori » ?]}$$
$$= \int_0^1 \left|t^{\mathrm{Re}\,x-1} \times (1-t)^{\mathrm{Re}\,y-1} \times e^{i(\mathrm{Im}\,x\,\ln t + \mathrm{Im}\,y\,\ln(1-t))}\right|\,dt$$
$$= \int_0^1 f(t)\,dt \quad \text{où } f(t) = t^{a-1}(1-t)^{b-1} \quad \text{[lecture incertaine — exposants]}.$$

— $f(t) \underset{0^+}{\sim} t^{a-1}$ avec $I_1 = \int_0 f(t)\,dt$ [lecture incertaine — borne sup. de $I_1$] $\equiv$ I.I.S en $0^+$ cvge ssi $a > 0$.

— $f(t) \underset{1^-}{\sim} (1-t)^{b-1}$ ainsi $I_2 = \int_{0,5}^{1} f(t)\,dt$ $\equiv$ I.I.S en $1^-$ cvge ssi $b > 0$. cqfd.

[En bas à droite, encadré : ANNEXE].

---

## 📝 Notes de transcription (fidélité)

- Encre parfois légère (p. 1, 4) ; exposants et indices relus sur rendus haute résolution (250 dpi).
- p. 1 : mot en marge droite lu « limite » ; nom de la règle du $\lim t^2 f(t) = 0$ partiellement illisible (conservé entre chevrons).
- p. 3 : l'intégrande $t^{3/2}(1-t)^{1/2}$ et $B(3/2, 5/2)$ se confirment mutuellement via $\Gamma(5/2) = \frac{3}{2}\Gamma(3/2)$.
- p. 4 : le passage en polaires et les dénominateurs des formes $I_{2k}$ portent des tags d'incertitude ; la 1ʳᵉ IPP tentée est raturée.
- p. 5 : $C^k_{2k-1}$ cohérent avec $\frac{(2k-1)!}{k!(k-1)!}$ ; $I_{2k+1}$ cohérent avec la 1ʳᵉ approche (p. 4).
- p. 6 : l'ANNEXE (citée p. 2) figure en dernière page, en deux colonnes ; un passage au $C^{y-1}_x$ est barré d'une grande croix.
- Aucune figure à reproduire (formules manuscrites uniquement).

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q08-euler-1.png`, r150) — en-tête « Intégrales Eulériennes », texte + équations, marge « limite » confirmée, aucune figure ; pp. 2–6 revérifiées visuellement au second passage le 2026-09-07 (rendus `/tmp/s8/euler-2.png` à `/tmp/s8/euler-6.png`, r150) — texte + équations uniquement, aucune figure. Aucun script `reproduce_integrales-euleriennes_N.py`, aucun PNG (aucun `assets/` créé, vérifié `uv run`).

---

## Vocabulaire

- `Γ` = Gamma (2ᵉ espèce) ; `β/B` = Bêta (1ʳᵉ espèce) ; `IIC/IIS` = intégrale impropre (convergence) ; `cvge` = converge.
- `ANNEXE` = p. 6 (cas entiers + convergence complexe) ; `!!` = double factorielle ; Wallis = `Iₙ = ∫₀^(π/2) sinⁿx dx`.
