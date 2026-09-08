# Cinématique — transcription fidèle

> 🧾 **Manuscrit original :** `cinematique.pdf` (scan, 10 pages) · ✍️ KpihX
> 🔍 **Statut :** cinématique du point et composition des mouvements (vitesses/accélérations, méthodes 1/2, Coriolis, rappel de Varignon) ; écriture très dense, nombreux passages en `[lecture incertaine — …]`, ratures signalées. Transcrit mot à mot, rien d'inventé.
> 📄 **Source scannée :** [cinematique.pdf](cinematique.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

En haut : [lecture incertaine — en-tête, lu « Q1 (PCSI …) »] $\cdot \vec{V}(I_1 \mid R_0)$. En haut au centre : I entouré. En haut à droite : schéma des repères $R$, $R'$, $(C)$, points $H$, $G$, $M$, $I$, vecteurs $\vec{u}$, $\vec{v}$, $\vec{x}_1$, $\vec{y}_1$, angles $\psi$, $\theta$ [lecture incertaine — schéma main levée, non reproduit en figure faute de données].

- $\vec{V}(I_1 \mid R_1) = \frac{d}{dt}(\overrightarrow{?}\mid R_0)$ [lecture incertaine — ligne, vecteur sous la flèche illisible]
- $\vec{\Omega}(R' \mid R_1) = \dot{\psi}\,\vec{z}$, $\vec{\Omega}(R_1 \mid R') = -\dot{\theta}\,\vec{u}$ [lecture incertaine — notations des vecteurs]
- $\vec{\Omega}(R_1 \mid R_0) = \dot{\psi}\,\vec{z} - \dot{\theta}\,\vec{u}$
- $\vec{V}(G \mid R_0) = \frac{d}{dt}(R\,\vec{[incertain]})\big|_{R_0} = R\,\dot{\psi}\,\vec{v}$ [lecture incertaine — vecteur]
- $\vec{a}(G \mid R_0) = \frac{d}{dt}(R\,\dot{\psi}\,\vec{[incertain]}) = R(\ddot{\psi}\,\vec{[incertain]} + \dot{\psi}^2\,\vec{[incertain]})$ [lecture incertaine — vecteurs]
- $\vec{V}(I_1 \mid R_0) = ?$ | N.B. : $\left(\frac{d}{dt}f(x,y)\right)(x,y) \ne \frac{d}{dt}\left(f(x,y)\right)(x,y)$ |
- Meth 1 : $\vec{V}(I_1 \mid R_0) = \vec{V}(G \mid R_0) + \overrightarrow{I_1G} \wedge \vec{\Omega}(R_n \mid R_0) = R\,\dot{\psi}\,\vec{v} + r\,\vec{[incertain]} \wedge (\dot{\psi}\,\vec{z} - \dot{\theta}\,\vec{u})$ [lecture incertaine]

$$\vec{V}(I_1 \mid R_0) = (R\,\dot{\psi} - r\,\dot{\theta})\,\vec{[incertain]}$$

- Meth 2 : $\vec{V}(I_1 \mid R_0) = \frac{d}{dt}(\overrightarrow{HI_1})\big|_{R_0}$ car pour $M \in (C)$, $\overrightarrow{HM} = \overrightarrow{HG} + \overrightarrow{GM} = R\,\vec{[incertain]} + r\,\vec{[incertain]}$ [lecture incertaine]

d'où $\frac{d}{dt}(\overrightarrow{HI_1})\big|_{R_0} = R\,\dot{\psi}\,\vec{v} + r(\dot{\psi}\,\sin\theta\,\vec{v} - \dot{\theta}\,\vec{y}_1)$ [lecture incertaine — parenthèse].

or $I_1 = H \mid \theta = \pi \mid$ [lecture incertaine] ainsi $\vec{V}(I_1 \mid R_0) = R\,\dot{\psi}\,\vec{v} - r\,\dot{\theta}\,\vec{y}_1$,

et $\vec{y}_1(\theta = \pi) = \vec{[incertain]}$ [lecture incertaine] d'où $\vec{V}(I_1 \mid R_0) = (R\,\dot{\psi} - r\,\dot{\theta})\,\vec{[incertain]}$.

- $\vec{a}(I_1 \mid R_0) = ?$
- Meth 1 : $\vec{a}(I_1 \mid R_0) = \frac{d}{dt}\vec{V}(M \mid R_0)\big|_{R_0}^{M = I_1}$ [lecture incertaine]

or $\frac{d}{dt}\vec{V}(M \mid R_0)\big|_{R_0} = R(\ddot{\psi}\,\vec{v} + \dot{\psi}^2\,\vec{u}) + r\left(-(\ddot{\psi}\,\sin\theta + \dot{\psi}\,\dot{\theta}\,\cos\theta)\,\vec{[incertain]} - \dot{\psi}\,\sin\theta\,\vec{[incertain]} - \ddot{\theta}\,\vec{y}_1 - \dot{\theta}\,(\dot{\psi}\,\cos\theta\,\vec{[incertain]} + \dot{\theta}\,\vec{x}_1)\right)$ [lecture incertaine — vecteurs et signes].

En bas : $\boxed{\theta = \pi}$, A entouré [lecture incertaine — numérotation, lu « 1 »].

donc $\vec{a}(I_1 \mid R_0)$ : $\frac{d}{dt}\vec{V}(M \in (C) \mid R_0)\big|_{R_0}^{M = I_1} = R(\ddot{\psi}\,\vec{[incertain]} - \dot{\psi}^2\,\vec{[incertain]}) + r(+\ddot{\psi}\,\dot{\theta}\,\vec{[incertain]} - \dot{\theta}^2\,\vec{[incertain]} - \ddot{\theta}\,\dot{\psi}\,\vec{[incertain]} + \dot{\theta}\,\vec{[incertain]})$ [lecture incertaine — fin de page tronquée], avec $R\,\dot{\psi}^2$ [raturé] au-dessus.

## Page 2 — ⚠️ page mal classée (hors cinématique)

> ⚠️ **Page mal classée** — vérifié au second passage (2026-09-07) : cette page est une feuille de trigonométrie (formules du $\cos$ d'une somme, généralisation au $\cos$ d'une somme de $n$ termes via $\mathrm{Re}$), barrée d'un grand X en croix, sans aucun rapport avec la cinématique du point (repères $R$, $R'$, $I_1$, $\vec{\Omega}$) des pages 1 et 3–10. Glissée par erreur dans le scan `cinematique.pdf`. Transcription conservée ci-dessous par fidélité, à ne pas lire comme de la cinématique.

[Page d'un autre sujet — trigonométrie, formules de $\cos$ d'une somme ; grande croix en X sur tout le milieu [raturé].]

$$\cos(\theta_1 + \theta_2) = \cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2$$

$$\cos(\theta_1 + \theta_2 - \theta_3) = (\cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2)\cos\theta_3 - (\sin\theta_1\cos\theta_2 + \sin\theta_2\cos\theta_1)\sin\theta_3$$

$$= \cos\theta_1\cos\theta_2\cos\theta_3 - \cos\theta_3\sin\theta_1\sin\theta_2 - \sin\theta_1\cos\theta_2\sin\theta_3 - \sin\theta_2\cos\theta_1\sin\theta_3$$

$$\cos\left(\sum_{k \in N}\theta_k\right) = \mathrm{Re}\left(e^{i\sum_{k \in N}\theta_k}\right) = \mathrm{Re}\left(\prod_{k \in N}(\cos\theta_k + i\sin\theta_k)\right)$$

$n = 2q + r$ [lecture incertaine] $\cdot$ Dir $= 0$ [lecture incertaine], $\cos\left(\sum_{k \in N}\theta_k\right) = \mathrm{Re}\left(\prod_{k \in N}^{2q}(\cos\theta_k + i\sin\theta_k)\right)$ [lecture incertaine — ligne avec « … = 4q … + q_2 = … » [raturé]],

$= \prod_{k \in N}\cos\theta_k + [\text{raturé : grand X}]$ [lecture incertaine — développement croisé],

$= \sum_{K \subset N}\sum_{\substack{J \subset I_{2q} \\ |J| = 2K \\ j \in J}}\prod\cos(\theta_j) \times \prod_{j \in \bar{J}}\sin(\theta_j) \times (i\,[incertain])^{q-K}$ [lecture incertaine — passage barré d'un X],

$2q - 1K$ [lecture incertaine — en marge],

$$\cos\left(\sum_{k \in N}^n\theta_k\right) = \sum_{K=0}^{n/2}\sum_{\substack{J \subset I_n \\ |J| = 2K}}\left(\prod_{j \in J}\sin\theta_j\right)\left(\prod_{j \in \bar{J}}\cos\theta_j\right)$$ [lecture incertaine — formule barrée d'un X].

$$\cos(\theta_1 + \theta_2 + \theta_3) = \cos\theta_1\cos\theta_2\cos\theta_3 - (\sin\theta_1\sin\theta_2\cos\theta_3 + \sin\theta_1\sin\theta_3\cos\theta_2 + \sin\theta_2\sin\theta_3\cos\theta_1)$$

$\cos(\theta_1 + \theta_2 + \theta_3 + \theta_4) = \cos\theta_1\cos\theta_2\cos\theta_3\cos\theta_4 - (\sin\theta_1\sin\theta_2\cos\theta_3\cos\theta_4 + \sin\theta_1\sin\theta_3\cos\theta_2\cos\theta_4 + \sin\theta_3\sin\theta_4\cos\theta_1\cos\theta_2$ [page coupée en bas].

## Page 3

En bas à droite : 2 entouré.

Meth 2 :

$$\vec{a}(I_1 \mid R_0) = \underbrace{\vec{a}(I_1 \mid R_n)}_{0} + \vec{a}(G \mid R_0) + \vec{\Omega}(R_n \mid R_0) \wedge \overrightarrow{GI_1} + \frac{d}{dt}\vec{\Omega}(R_n \mid R_0)\big|_{R_0} \wedge \overrightarrow{GI_1} + 2\vec{\Omega}(R_n \mid R_0) \wedge \vec{V}[\text{coupé à droite}]$$ [lecture incertaine — fin de ligne hors cadre].

or $\vec{V}(I_1 \mid R_n?) = \vec{V}(G \mid R_0) + \vec{\Omega}(R_n \mid R_0) \wedge \overrightarrow{GI_1} = (R\,\dot{\psi} - r\,\dot{\theta})\,\vec{\text{[incertain]}}$ avec $\underbrace{\text{[illisible]}}_0$ [lecture incertaine].

$= R(\ddot{\psi}\,\vec{[incertain]} - \dot{\psi}^2\,\vec{[incertain]}) + (\dot{\psi}^2\,\vec{[incertain]} - \ddot{\theta}\,\vec{[incertain]}) \wedge (-r\,\dot{\theta}\,\vec{[incertain]})$ [lecture incertaine]

$+ r\,\vec{[incertain]}(\ddot{\psi}\,\vec{[incertain]} - \ddot{\theta}\,\vec{[incertain]} - \dot{\theta}\,\dot{\psi}\,\vec{[incertain]})$

$= R(\ddot{\psi}\,\vec{[incertain]} - \dot{\psi}^2\,\vec{[incertain]}) + r\,\dot{\theta}\,(\dot{\psi}\,\vec{[incertain]} + \dot{\theta}\,\vec{[incertain]}) + r\,(-\ddot{\theta}\,\vec{[incertain]} + \dot{\theta}\,\dot{\psi}\,\vec{[incertain]})$

$= \vec{[incertain]}(-R\,\dot{\psi}^2 + 2r\,\dot{\theta}\,\dot{\psi}) + \vec{[incertain]}(R\,\ddot{\psi} - r\,\ddot{\theta}) + r\,\dot{\theta}^2\,\vec{[incertain]}$

$$\boxed{\vec{a}(I_1 \mid R_0) = \vec{v}\,(r\,\dot{\theta}\,\dot{\psi}) + r\,\dot{\theta}^2\,\vec{[incertain]} = r\,\dot{\theta}\,(\dot{\psi}\,\vec{v} + \dot{\theta}\,\vec{[incertain]}) \quad \mid I' \in R' \mid}$$ [lecture incertaine — encadré et mention].

- $\vec{V}(I_2 \mid R_0) = ?$
- Meth 1 : $\vec{V}(I_2 \mid R_2?) = \frac{d}{dt}\vec{V}(M \in R' \mid \cdot)\big|_{R_0}^{M \in I'}$ [lecture incertaine], $\overrightarrow{OH} = x\,\vec{u}$

[raturé : $\vec{V}(M \in R')$ …] $\frac{d}{dt}(x\,\vec{u})\big|_{R_2} = \dot{x}\,\vec{u} + x\,\dot{\psi}\,\vec{v}$ pour $n = I'$ [lecture incertaine], $\dot{x} = 0$, $x = R$ [lecture incertaine]

d'où $\vec{V}(I_2? \mid R_1?) = R\,[incertain]$ [lecture incertaine — bas de page].

En bas à droite : gribouillis « 888 / T20 / … » [lecture incertaine] et 2 entouré.

## Page 4

En haut à gauche : II entouré. Schéma des repères en haut à gauche [lecture incertaine — croquis main levée, non reproduit en figure faute de données]. $I_1 \in (J_1?)$, $I_1 \in (S_1?)$ [lecture incertaine].

$R_0 = (O, \vec{x}_0?, \vec{y}_0?, \vec{z}_0?)$ [lecture incertaine], $R' = (O, \vec{i}, \vec{[incertain]}, \vec{[incertain]})$ avec $\downarrow \psi$, $R_2 = (O, \vec{m}_1?, \vec{y}_1?, \vec{[incertain]})$ avec $\frac{\theta}{u}$ [lecture incertaine — définitions des repères].

$$\vec{\Omega}(R' \mid R_1) = \dot{\psi}\,\vec{z}_0?, \quad \vec{\Omega}(R_1 \mid R') = \dot{\theta}\,\vec{x}_1?\,\vec{[incertain]}$$ [lecture incertaine]

$$\vec{\Omega}(R_1 \mid R_0?) = \dot{\psi}\,\vec{z}_0 - \dot{\theta}\,\vec{[incertain]} = -\dot{\theta}\,\vec{[incertain]}$$ [lecture incertaine]

- $\vec{V}(G \mid R_0) = \dot{x}\,\vec{u} + x\,\dot{\psi}\,\vec{v}$, $\vec{a}(G \mid R_0) = \ddot{x}\,\vec{u} + \dot{x}\,\dot{\psi}\,\vec{v} + (\ddot{x}\,\dot{\psi}? + x\,\ddot{\psi})\,\vec{[incertain]} + (x\,\dot{\psi})\,\dot{\psi}\,\vec{[incertain]}$ [lecture incertaine — première forme],

$$\vec{a}(G \mid R_0) = \vec{u}\,(\ddot{x} - x\,\dot{\psi}^2) + \vec{v}\,(2\dot{x}\,\dot{\psi} + x\,\ddot{\psi})$$

- $\vec{V}(I_1 \mid R_0)$
- Meth 1 : $\vec{V}(I_1 \mid R_0) = \frac{d}{dt}\overrightarrow{HI_1}\big|_{R_0}^{M = I_1}$ où $\overrightarrow{OH} = r\,\vec{x}_1$ [lecture incertaine]

$= \dot{x}\,\vec{u} + x\,\dot{\psi}\,\vec{v} + r\,(\dot{\psi}\,\vec{[incertain]} + \dot{\theta}\,\vec{y}_1)$ [lecture incertaine]

pour $M = I_1$, $\theta = -\pi/2$ [lecture incertaine], $\vec{x}_1 = -\vec{z}_0$ [lecture incertaine], $\vec{y}_1 = \vec{v}$ [lecture incertaine]

d'où $\vec{V}(I_1 \mid R_0) = \dot{x}\,\vec{u} + x\,\dot{\psi}\,\vec{v} + r\,(\dot{\theta}\,\vec{v}) = \dot{x}\,\vec{u} + x\,\dot{\psi}\,\vec{[incertain]}$ [lecture incertaine]

$= (\dot{x} + r\,\dot{\theta})\,\vec{[incertain]} + x\,\dot{\psi}\,\vec{v}$ [lecture incertaine]

- Meth 2 : $\vec{V}(I_1 \mid R_0) = \dot{x}\,\vec{u} + x\,\dot{\psi}\,\vec{v} + r\,\vec{z}_1 \wedge (\dot{\psi}\,\vec{z}_0 - \dot{\theta}\,\vec{[incertain]})$ [lecture incertaine]

$= (\dot{x} + r\,\dot{\theta})\,\vec{[incertain]} + x\,\dot{\psi}\,\vec{v}$ [lecture incertaine]

- $\vec{V}(I_2 \mid R_0)$
- Meth 1 : $\vec{V}(I_2 \mid R_0) = \frac{d}{dt}(\overrightarrow{OM})\big|_{R_0}^{M \in I_1?}$ où $\overrightarrow{OH} = x'\,\vec{u}$ [lecture incertaine]. En bas à droite : 1 entouré.

## Page 5

[Haut de page coupé] $\vec{[M]}\mid_{R_2} = \dot{x}\,\vec{u} + x'\,\dot{\psi}\,\vec{v}$ [lecture incertaine]. Pour $M = I_1$, $x' = r_1$ [lecture incertaine], $\dot{x}' = 0$

d'où $\vec{V}(I_2 \mid R_0) = x\,\dot{\psi}\,\vec{v}$ [lecture incertaine].

- Meth 2 : $\vec{V}(I_2 \mid R_1) + \dot{\psi}\,\vec{z}_0 \wedge x\,\vec{u} = \dot{\psi}\,x\,\vec{v}$ [lecture incertaine]

- $\vec{V}(I \in S_2 \mid S_1?) = ?$ [lecture incertaine — intitulé]
- Meth 0 : $\vec{V}(I \in S_1 \mid S_2) = \vec{V}(I \in S_1 \mid R_0) - \vec{V}(I \in S_2 \mid R_0)$

$\vec{V}(I \in S_1 \mid R_2?) = (\dot{x} + r\,\dot{\theta})\,\vec{[incertain]}$ [lecture incertaine]

- Meth 1 : [raturé : $\overrightarrow{I \in S_2}$ … $\frac{d}{dt}\overrightarrow{OI}$]

$\vec{V}(I_1 \mid S_2) = \frac{d}{dt}(\overrightarrow{OH})\big|_{R_1?}^{M \in I_1, H \in (x_1?)}$ [lecture incertaine], car $\vec{V}(G \mid R_2) \in x\,\vec{u}$ [lecture incertaine]

$= \dot{x}\,\vec{u} + \frac{d}{dt}(r\,\vec{x}_1?)\big|_{R_0?}$ [raturé — terme biffé] [lecture incertaine] $+ r\,\dot{\theta}\,\vec{y}_1$ [avec ratures]

or pour $M = I_1$, $\vec{y}_1? = \vec{v}$ [lecture incertaine]

d'où $\vec{V}(I_1 \mid S_2) = (\dot{x} + r\,\dot{\theta})\,\vec{[incertain]}$ [lecture incertaine]

- $\vec{a}(I_1 \mid S_2) = ?$
- Meth 1 : $\vec{a}(I_1 \mid S_2) = \frac{d}{dt}\vec{V}(M \in S_1 \mid S_2)\big|_{R_1?}^{M = I_1}$ [lecture incertaine]

or $\frac{d}{dt}(\vec{V}(M \in S_1 \mid S_2))\big|_{R_1?} = \ddot{x}\,\vec{u} + \ddot{x}\,\dot{\psi}\,\vec{v}? + r\,(\ddot{\theta}\,\vec{y}_1? + \dot{\theta}^2\,\vec{x}_1?)$ [lecture incertaine]

or pour $M = I_1$, $\vec{y}_1? = \vec{v}$, $\vec{x}_1? = -\vec{z}_0$ [lecture incertaine]

d'où $\vec{a}(I \in S_1 \mid S_2) = \ddot{x}\,\vec{u} + r\,(\ddot{\theta}\,\vec{v} + \dot{\theta}^2\,\vec{z}_0)$ [lecture incertaine]

$= (\ddot{x} + r\,\ddot{\theta})\,\vec{u} + r\,\dot{\theta}^2\,\vec{z}_0 = \frac{r\,\dot{\theta}^2\,\vec{[incertain]}}{[incertain]}$ [lecture incertaine — bas de page]. En bas à droite : [lettre entourée, lue « Q » — lecture incertaine].

## Page 6

En haut : Meth 2 [lecture incertaine] :

$$\vec{a}(I_1 \mid S_2) = \underbrace{\vec{a}(I_1 \mid S_1)}_{0} + \vec{a}(G \mid S_2) + \left.\dot{\vec{\Omega}}(S_1 \mid S_2)\right|_{[incertain]} \wedge [incertain] + \vec{\Omega} \wedge (\vec{\Omega} \wedge [incertain]) + 2\vec{\Omega} \wedge \underbrace{\vec{V}(I_1 \mid S_1)}_{0}$$

$= \ddot{x}\,\vec{u} + r\,\vec{z}_0? \wedge (-\ddot{\theta}\,\vec{[incertain]} + -\dot{\theta}\,\vec{[incertain]} \wedge (-\dot{\theta} \wedge -r\,\dot{\theta}\,\vec{[incertain]}))$ [lecture incertaine]

$= \dot{x}\,\vec{u}? + r\,\ddot{\theta}\,\vec{v} - \dot{\theta}\,\vec{[incertain]} \wedge (\dot{\theta}\,r\,\vec{v})$ [lecture incertaine]

$= \dot{\theta}^2\,r\,\vec{z}_0$ [raturé] [lecture incertaine]

$\vec{a}(I_2? \mid S_1?) = r\,\dot{\theta}\,\vec{z}_0? = \dot{x}\,\dot{\theta}\,\vec{z}_0?$ [lecture incertaine]. En haut à droite : 3 entouré.

- $\vec{a}(I_1 \mid R_0)$
- Meth 1 : $\vec{a}(I_1 \mid R_0) = \vec{a}(M \in R_n \mid R_0)_{M = I_1} = \frac{d}{dt}\vec{V}(M \in R_n \mid R_0)\big|_{R_0}^{M = I_1}$ [lecture incertaine]

or $\frac{d}{dt}\vec{V}(M \in R_n \mid R_0) = \ddot{x}\,\vec{u} + \dot{x}\,(\dot{\psi}\,\vec{v} \pm \dot{\theta}\,\vec{[incertain]}) + (\dot{x}\,\dot{\psi} + x\,\ddot{\psi})\,\vec{[incertain]} + x\,\dot{\psi}^2\,\vec{v} + r\,(|\dot{\psi}\,\cos\theta - \dot{\theta}\,\sin\theta)\,\vec{[incertain]} + \dot{\psi}^2\,\cos\theta\,\vec{v} + \ddot{\theta}\,\vec{z}_1? + \dot{\theta}\,(\dot{\psi}\,\sin\theta\,\vec{[incertain]} - \dot{\theta}\,\vec{x}_1)|$ [raturé] [lecture incertaine — longue formule ; une grande croix en X barre tout le bas de page [raturé]]

pour $M = I_1$, $\vec{a}(I_1 \mid R_0) = (\dot{x}\,\dot{\psi} + x\,\ddot{\psi})\,\vec{[incertain]} - x\,\dot{\psi}^2\,\vec{u}$

$+ r\,(\ddot{\theta}\,\vec{[incertain]} + \dot{\theta}\,\vec{v} + \dot{\theta}\,(\dot{\psi}\,\vec{[incertain]} + \dot{\theta}\,\vec{[incertain]})) + \ddot{x}\,\vec{u} + \dot{x}\,(\dot{\psi}\,\vec{v} + \dot{\theta}\,\vec{[incertain]})$ [lecture incertaine]

$= \vec{u}\,(-x\,\dot{\psi}^2\,[incertain] + r\,\dot{\theta}\,[incertain]) + \vec{v}\,(\dot{x}\,\dot{\psi} + x\,\ddot{\psi} + r\,\dot{\theta}\,\dot{\psi}? + \dot{\theta}\,\dot{\psi}? + \dot{x}\,\dot{\psi})$ [lecture incertaine]

$+ (r\,\dot{\theta}^2\,[incertain]\,\,\dot{x}\,\dot{\theta}\,[incertain]\,\vec{z}_0)$ [lecture incertaine]

$= \vec{u}\,(-x\,\dot{\psi}^2\,[incertain]) + \vec{v}\,(x\,\ddot{\psi} + [incertain])$ [lecture incertaine ; barré d'un X]

$$\vec{a}(I_1 \mid R_0) = -x\,\dot{\psi}^2\,\vec{u} + x\,\ddot{\psi}\,\vec{v} = x(-\dot{\psi}^2\,\vec{u} + \ddot{\psi}\,\vec{v})$$ [barré d'un X — raturé].

## Page 7

[Haut coupé] $(I_1 \mid R_0) = \underbrace{\vec{a}(I_1 \mid R_n)}_{0} + \vec{a}(G \mid R_0) + \left.\vec{\Omega}(R_n \mid R_0)\right|_{R_0} \wedge \overrightarrow{GI_1} + \vec{\Omega} \wedge (\vec{\Omega} \wedge \vec{[incertain]}) + 2\vec{\Omega} \wedge \underbrace{\vec{V}(I_1 \mid R_n)}_{0}$

$= \vec{u}\,(\ddot{x} - x\,\dot{\psi}^2) + \vec{v}\,(2\dot{x}\,\dot{\psi} + x\,\ddot{\psi})$

$+ (\ddot{\psi}\,\vec{z}_0 - \ddot{\theta}\,\vec{[incertain]} + \dot{\theta}\,\dot{\psi}\,\vec{[incertain]}) \wedge (-r\,\vec{z}_0?)$ [lecture incertaine]

$(+ r(\dot{\psi}\,\vec{z}_0 - \dot{\theta}\,\vec{[incertain]}) \wedge ([incertain] + \dot{\theta}\,\vec{v}))$ [lecture incertaine]

$+ r\,\ddot{\theta}\,\vec{v} + \dot{\theta}\,\dot{\psi}\,r\,\vec{[incertain]} + r\,\dot{\theta}\,(\dot{\psi}\,\vec{v} + \dot{\theta}\,\vec{[incertain]})$ [lecture incertaine]

$= \vec{u}(r\,\dot{\theta}\,[incertain] - x\,\dot{\psi}^2 + r\,\dot{\theta}\,[incertain]) + \vec{v}(2\dot{x}\,\dot{\psi} + x\,\ddot{\psi} + \dot{\theta}\,\dot{\psi}\,r + r\,\dot{\theta}\,\dot{\psi}\,[incertain]) + r\,\dot{\theta}^2\,\vec{[incertain]}$ [lecture incertaine]

$= -x\,\dot{\psi}^2\,\vec{u} + x\,\ddot{\psi}\,\vec{v} + r\,\dot{\theta}^2\,\vec{[incertain]}$ [lecture incertaine]

$\vec{a}(I_1 \mid R_0) = -x\,(\dot{\psi}^2\,\vec{u} + \dot{\psi}\,\vec{v}) + \dot{\theta}\,\dot{x}\,\vec{[incertain]}$ [lecture incertaine]

- Meth 1 : $\vec{a}(I_1 \mid R_0) = \vec{a}(M \in R_n \mid R_0)_{M = I_1}$
- or $\vec{a}(M \in R_n \mid R_0) = \frac{d}{dt}(\dot{x}\,\vec{u} + x\,\dot{\psi}\,\vec{v} + r\,(\dot{\psi}\,\cos\theta\,\vec{[incertain]} + \dot{\theta}\,\vec{z}_1?))$ [lecture incertaine]

$= \ddot{x}\,\vec{u} + \dot{x}\,\dot{\psi}\,\vec{v} + (\dot{x}\,\dot{\psi} + x\,\ddot{\psi})\,\vec{[incertain]} - x\,\dot{\psi}^2\,\vec{[incertain]} + r\,((\ddot{\psi}\,\cos\theta - \dot{\psi}\,\dot{\theta}\,\sin\theta)\,\vec{[incertain]} - \dot{\psi}^2\,\cos\theta\,\vec{v} + \ddot{\theta}\,\vec{[incertain]} + \dot{\theta}\,(\dot{\psi}\,\sin\theta\,\vec{[incertain]} - \dot{\theta}\,\vec{x}_1))$ [lecture incertaine]

or pour $M = I_1$, $\theta = -\pi/2$ [lecture incertaine], $\vec{x}_1? = -\vec{z}_0$ et $\vec{z}_1? = \vec{v}$ [lecture incertaine]

d'où $\vec{a}(I_1 \mid R_0) = \vec{u}\,(\ddot{x} - x\,\dot{\psi}^2 + r\,\ddot{\theta}) + \vec{v}\,(2\dot{x}\,\dot{\psi} + x\,\ddot{\psi} + \dot{\theta}\,\dot{\psi}\,r\,[incertain] + r\,\dot{\theta}\,[incertain]) + r\,\dot{\theta}^2\,\vec{z}_0$ [lecture incertaine]. En bas à droite : 4 entouré.

## Page 8

En haut : Car $\dot{x} + r\,\dot{\theta} = 0 \Rightarrow \ddot{x} + r\,\ddot{\theta} = 0$

Alors $\vec{a}(I_1 \mid R_0) = -x\,\dot{\psi}^2\,\vec{u} + x\,\ddot{\psi}\,\vec{v} + r\,\dot{\theta}^2\,\vec{[incertain]}$

$= x(-\dot{\psi}^2\,\vec{u} + \ddot{\psi}\,\vec{v}) + r\,\dot{\theta}^2\,\vec{[incertain]} = \dot{\theta}\,\dot{x}\,\vec{[incertain]}$ [lecture incertaine — fin de ligne]. En haut à droite : 5 entouré.

- $\vec{a}(I_2 \mid R_0) = ?$
- Meth 1 :

$$\vec{a}(I_2 \mid R_0) = \underbrace{\vec{a}(I_2 \mid R')}_{0} + \left.\dot{\vec{\Omega}}(R' \mid R_0)\right|_{R_0} \wedge \overrightarrow{OI_2} + \underbrace{\vec{a}(O \mid R_0)}_{0} + \vec{\Omega} \wedge (\vec{\Omega} \wedge \overrightarrow{OI_2}) + 2\vec{\Omega} \wedge \vec{V}(I_2 \mid R')$$

$= \ddot{\psi}\,\vec{z}_0 \wedge x\,\vec{u} + \dot{\psi}\,\vec{z}_0 \wedge (\dot{\psi}\,\vec{z}_0 \wedge x\,\vec{u})$ [lecture incertaine — vecteurs]

$= x\,\ddot{\psi}\,\vec{v} + \dot{\psi}\,\vec{z}_0 \wedge (x\,\dot{\psi}\,\vec{v})$

[flèche] $x\,\dot{\psi}^2\,\vec{u}$ [lecture incertaine]

$$\vec{a}(I_2 \mid R_0) = x\,(-\dot{\psi}^2\,\vec{u} + \ddot{\psi}\,\vec{v})$$

Rq : $\vec{a}(I_1 \mid R_0) = \vec{a}(I_2 \mid R_0) + \vec{a}(I_1 \mid S_2)$

cad $\boxed{\vec{a}(I \in S_1 \mid R_0) = \vec{a}(I \in S_1 \mid S_2) + \vec{a}(I \in S_2 \mid R_0)}$ [encadré].

Ce résultat est notable dans ce cas, vu qu'à chaque fois l'accélération de Coriolis était nulle.

En effet de façon générale, pour [un ? — lecture incertaine] de centre $O_1$

$$\underbrace{\vec{a}(M \in R_2 \mid R_0)}_{\text{absolue}} = \underbrace{\vec{a}(M \in R_2 \mid R_1)}_{\text{relative}} + \underbrace{\vec{a}(M \in R_1 \mid R_0)}_{\text{d'entraînement}} + \underbrace{2\vec{\Omega}(R_1 \mid R_0) \wedge \vec{V}(M \in R_2 \mid R_1)}_{\text{Coriolis}}$$

or $\vec{a}(M \in R_1 \mid R_0) = \vec{a}(O_1 \mid R_0) + \dot{\vec{\Omega}}(R_1 \mid R_0)\,\overrightarrow{O_1M} + \dot{\vec{\Omega}}(R_1 \mid R_0) \wedge (\vec{\Omega}(R_1 \mid R_0) \wedge \overrightarrow{O_1M})$ [lecture incertaine — fin coupée].

## Page 9

[Haut coupé] $(R_0 \mid R_0) = \vec{a}(R_2 \mid R_2) + \vec{a}(R_1 \mid R_0) = ?$ [lecture incertaine — début hors cadre]

$R_0 = (O, \vec{x}_0?, \vec{y}_0?, \vec{z}_0?)$, $R_n = (O_n, \vec{x}_n?, \vec{y}_n?, \vec{z}_n?)$, $R_0? = (O_1, \vec{x}_1?, \vec{y}_1?, \vec{z}_1?)$ [lecture incertaine — indices].

$\vec{a}(M \in R_2 \mid R_0) = \vec{a}(M \in R_2 \mid R_1) + \vec{a}(M \in R_1 \mid R_0)$ ?

Ora [*sic* — pour « Or »] :

$$\vec{a}(M \in R_2 \mid R_0) = \vec{a}(M \in R_2 \mid R_1) + \vec{a}(O_1 \mid R_0) + \left.\dot{\vec{\Omega}}(R_1 \mid R_0)\right|_{R_0} \wedge \overrightarrow{O_1M} + \vec{\Omega}(R_1 \mid R_0) \wedge (\vec{\Omega}(R_1 \mid R_0) \wedge \overrightarrow{O_1M}) + 2\vec{\Omega}(R_1 \mid R_0) \wedge \vec{V}(M \in R_2 \mid R_1)$$

Or $\vec{a}(M \in R_1 \mid R_0) = \underbrace{\vec{a}(M \in R_1 \mid R_n)}_{0} + \vec{a}(O_1 \mid R_0) + \vec{\Omega}(R_1 \mid R_0) \wedge \overrightarrow{O_1M} + \vec{\Omega}(R_1 \mid R_0) \wedge \vec{\Omega}(R_1 \mid R_0) \wedge \overrightarrow{O_1M} + 2\vec{\Omega}(R_1 \mid R_0) \wedge \underbrace{\vec{V}(M \in R_1 \mid R_n)}_{0}$ [lecture incertaine — points et chapeaux]

d'où $\vec{a}(M \in R_2 \mid R_0) = \vec{a}(M \in R_2 \mid R_2) + \vec{a}(M \in R_1 \mid R_0) + 2\vec{\Omega}(R_1 \mid R_0) \wedge \vec{V}(M \in R_2 \mid R_n)$ [lecture incertaine — dernier membre]. En bas à droite : 6 entouré.

## Page 10

En bas à droite : [chiffre entouré, lu « 7 » — lecture incertaine].

Rappel : Soit 2 repères orthonormés directs $R_0$, $R_1$ [lecture incertaine — second repère].

L'application $\varphi : \mathcal{E} \longrightarrow \mathcal{E}$, $\vec{u} \longmapsto \varphi(\vec{u}) = \frac{d\vec{u}}{dt}\big|_{R_0} - \frac{d\vec{u}}{dt}\big|_{R_1}$ [lecture incertaine — second repère] est linéaire,

et antisymétrique donc d'après le théo de Varignon,

$\exists\,\vec{R} \in \mathcal{E} \;/\; \forall\,\vec{u} \in \mathcal{E},\; \varphi(\vec{u}) = \vec{R} \wedge \vec{u}$

Dans le cadre de la cinématique $\vec{R} = \vec{\Omega}(R_1 \mid R)$ [lecture incertaine — repère].

Ainsi $\frac{d\overrightarrow{OH}}{dt}\big|_{R_0} = \frac{d\overrightarrow{OH}}{dt}\big|_{R_1} + \vec{R} \wedge \overrightarrow{OH}$

cad $\frac{d\overrightarrow{OH}}{dt}\big|_{R_0?} = \frac{d\overrightarrow{OO_1}}{dt}\big|_{R_0?} + \vec{\Omega}(M? \mid R_1?) + \vec{R} \wedge \overrightarrow{O_1M}$ [lecture incertaine]

* $\vec{V}(M \mid R_0) = \vec{V}(M \mid R_1) + \underbrace{\vec{V}(O_1 \mid R_0) + \vec{R} \wedge \overrightarrow{O_1M}}_{\vec{V}(M \in R_1 \mid R_0)}$

Pour $M \in R_1$, $\vec{V}(M \in R_2 \mid R_0) = \vec{V}(M \in R_2 \mid R_1) + \vec{V}(R_2 \in R_1 \mid R_0)$ [lecture incertaine]

* $\vec{a}(M \mid R_0) = \frac{d}{dt}\vec{V}(M \mid R_0)\big|_{R_0}$ $\boxed{\vec{R} = \vec{\Omega}(R_1 \mid R)}$ [lecture incertaine — encadré]

$= \frac{d}{dt}\left(\vec{V}(M \mid R_1) + \vec{V}(O_1 \mid R_0) + \vec{R} \wedge \overrightarrow{O_1M}\right)\big|_{R_0}$

$= \frac{d}{dt}\vec{V}(M \mid R_1)\big|_{R_1?} + \vec{\Omega}(R_1 \mid R_0) \wedge \vec{V}(M \mid R_1) + \vec{a}(O_1 \mid R_0)$

$+ \left.\vec{R}\right|_{R_0}? \wedge \overrightarrow{O_1M} + \vec{R} \wedge \left(\frac{d\overrightarrow{O_1M}}{dt}\big|_{R_0?} + \vec{\Omega}(R_1 \mid R_0) \wedge \overrightarrow{O_1M}\right)$ [lecture incertaine]

d'où $\vec{a}(M \mid R_0) = \vec{a}(M \mid R_1) + \vec{a}(O_1 \mid R_0) + \frac{d\vec{\Omega}(R_1 \mid R_0)}{dt}\big|_{R_0} \wedge \overrightarrow{O_1M} + \vec{\Omega}(R_1 \mid R_0) \wedge (\vec{\Omega}(R_1 \mid R_0) \wedge \overrightarrow{O_1M}) + 2\vec{\Omega}(R_1 \mid R_0) \wedge \vec{V}(M \mid R_1)$

Ainsi $\vec{a}(M \mid R_0) = \vec{a}(M \mid R_1) + \vec{a}(M \in R_1 \mid R_0) + 2\vec{\Omega}(R_1 \mid R_0) \wedge \vec{V}(M \mid R_1)$

or … $\vec{a}(\vec{V} \mid M \in R_1 \mid R_0) = \vec{a}(M \in R_1 \mid R_0)$ [lecture incertaine — bas de page coupé].

---

## Figures

Aucun PNG reproduit : les schémas main levée des repères ($R$, $R'$, $(C)$, angles $\psi$, $\theta$ — p.1 et suivantes) sont décrits dans chaque `## Page` mais non reproduits en figure faute de données cotées. À signaler : p.2 = page mal classée (trigonométrie, $\cos$ d'une somme, barrée d'un X — sans rapport avec la cinématique, voir note section Page 2).

## Vocabulaire

- **Meth 1 / Meth 2** : deux méthodes de calcul de $\vec{V}$ / $\vec{a}$.
- **Composition des mouvements** : $\vec{V}(M \mid R_0) = \vec{V}(M \mid R_1) + \vec{V}(M \in R_1 \mid R_0)$.
- **Accélération de Coriolis** : $2\vec{\Omega}(R_1 \mid R_0) \wedge \vec{V}(M \mid R_1)$.
- **$\vec{\Omega}(R_1 \mid R_0)$** : vitesse angulaire d'entraînement.
- **Rappel de Varignon** : formule citée en fin de document.
- **$I_1$** : point d'étude ($I_1 = H \mid \theta = \pi$).
