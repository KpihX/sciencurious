# Adiabatique Laplace — transcription fidèle

> 🧾 **Manuscrit original :** `adiabatique-laplace.pdf` (scan, 4 pages) · ✍️ KpihX
> 🔍 **Statut :** démonstration manuscrite (stylo bleu) : équation différentielle de l'adiabatique réversible d'un gaz, puis applications (gaz parfait, gaz en $PV = RT(1 + A/V)$, gaz de Dieterici) ; aucune figure géométrique. Transcrit mot à mot.
> 📄 **Source scannée :** [adiabatique-laplace.pdf](adiabatique-laplace.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Analyse de l'adiabatique réversible d'un gaz

Ici $\delta Q = 0$.

On alors [*sic* — « On alors », lire « On a alors »] $\begin{cases} 0 = C_v dT + l dV \\ 0 = C_p dT + h dP \end{cases} \Rightarrow \dfrac{dP}{dV} = \dfrac{C_p}{C_v} \times \dfrac{l}{h} = \gamma \dfrac{l}{h}$

où $l = (C_p - C_v) \left. \dfrac{\partial T}{\partial V} \right|_P$ et $h = -(C_p - C_v) \left. \dfrac{\partial T}{\partial P} \right|_V$ d'où

$\dfrac{dP}{dV} = -\gamma \left. \dfrac{\partial T}{\partial V} \right|_P \left. \dfrac{\partial P}{\partial T} \right|_V \Rightarrow \boxed{\dfrac{dP}{dV} = +\gamma \left. \dfrac{\partial P}{\partial V} \right|_T} \quad (\text{Ed}_{ARG})$ [lecture incertaine — « $(\text{Ed}_{ARG})$ », probablement « équation de l'adiabatique réversible des gaz »]

$\uparrow$

~Éqn diff de l'adiabatique réversible d'un gaz

⋆ Application à quelques gaz particuliers

NB : Dans la suite, on admettra que $\gamma \equiv \text{constant}$

• Cas du gaz parfait

Ici $\left. \dfrac{\partial P}{\partial V} \right|_T = -\dfrac{P}{V}$ ainsi $\dfrac{dP}{dV} = -\dfrac{\gamma P}{V}$

c-à-d $\dfrac{dP}{P} = -\gamma \dfrac{dV}{V}$

c-à-d $\exists$ $P_0, V_0$ constant / $\ln\left(\dfrac{P}{P_0}\right) = -\gamma \ln\left(\dfrac{V}{V_0}\right)$

c-à-d $\underline{P V^{\gamma} = P_0 V_0^{\gamma} = \text{cte}}$ $(\text{E}_{ARGP})$

?

## Page 2

• Cas du gaz d'équation $PV = RT\left(1 + \dfrac{A}{V}\right)$ (6) (cas d'une mole) [en marge droite — fragment « cansi », saignement de la page suivante]

Interprétation de l'éqn : (6) $\Leftrightarrow$ $P = \dfrac{RT}{V} + RT \dfrac{A}{V^2}$

Elle traduit ainsi le fait que pour un gaz de ce type, la pression sera plus grande que dans le carré du [lecture incertaine — « que dans le carré du », peut-être « quand le carré du »] volume sera d'autant plus petit, en comparaison au gaz idéal

Ici $\left. \dfrac{\partial P}{\partial V} \right|_T V + P = -\dfrac{RTA}{V^2} = -\dfrac{A}{V^2}\left(\dfrac{PV^2}{A+V}\right) = \dfrac{-AP}{A+V}$

d'où $\left. \dfrac{\partial P}{\partial V} \right|_T = -\dfrac{P}{V}\left(\dfrac{2A+V}{A+V}\right) = -P\left(\dfrac{2}{V} - \dfrac{1}{A+V}\right)$

Ainsi $(\text{Ed}_{ARG}) \Rightarrow \dfrac{dP}{P} = -\gamma dV \left(\dfrac{2}{V} - \dfrac{1}{A+V}\right)$

$\Rightarrow \exists$ $V_0, P_0$ / $\ln \dfrac{P}{P_0} = -\gamma \ln \dfrac{V^2}{A+V} \times \dfrac{A+V_0}{V_0^2}$

$\Rightarrow P \left(\dfrac{V^2}{A+V}\right)^{\gamma} = P_0 \left(\dfrac{V_0^2}{A+V_0}\right)^{\gamma} = \text{cte}$

Rq : Pour $A = 0$, on retrouve bien $PV^{\gamma} = \text{cte}$

• Cas du gaz de dieterici [*sic* — « dieterici », lire « Dieterici »] : $P(V-b) = e^{-\frac{a}{RTV}}$ ($n = 1$)

Ainsi $\ln P + \ln(V-b) = -\dfrac{a}{RTV} \Rightarrow \dfrac{1}{P} \left. \dfrac{\partial P}{\partial V} \right|_T + \dfrac{1}{V-b} = \dfrac{a}{RTV^2}$

$\Rightarrow \left. \dfrac{\partial P}{\partial V} \right|_T = P\left(\dfrac{a}{RTV^2} - \dfrac{1}{V-b}\right)$

$= P\left(-\dfrac{a}{V^2} \dfrac{V}{a \ln(P(V-b))} - \dfrac{1}{V-b}\right)$ [lecture incertaine — fraction « $\frac{V}{a \ln(P(V-b))}$ »]

$\alpha \ln(P(V-b)) = -\dfrac{a}{RTV}$ [lecture incertaine — « $\alpha$ », lire « or » (conjonction) d'après p.2 bas de page]

d'où $\dfrac{1}{RT} = -\dfrac{1}{a} \ln(P(V-b))$

## Page 3

ainsi $(\text{Ed}_{ARG}) \Rightarrow$ [raturé — « $dP(V) = -P(\dots)$ » biffé] $\left(+ \dfrac{1}{V \ln(P(V-b))} + \dfrac{1}{V-b}\right)$ [lecture incertaine — début de ligne biffé/illisible]

$= \dfrac{-P\gamma}{V \ln(P(V-b))} - \dfrac{P\gamma}{V-b}$

$\Rightarrow \boxed{P'(V) + \dfrac{P\gamma}{V-b} + \dfrac{P\gamma}{V \ln(P(V-b))} = 0}$

$(\text{Ed}_{ARGD})$

$(\text{Ed}_{ARGD}) \Leftrightarrow P'(V)(V-b)V \ln(P(V-b)) + \gamma P V \ln(P(V-b)) + \gamma P(V-b) = 0$

Posons $Q = P(V-b) \Rightarrow Q'(V) = P'(V)(V-b) + P$

$= P'(V)(V-b) + \dfrac{Q}{V-b}$

$(\text{Ed}_{ARGD}) \Leftrightarrow \left(Q'(V) - \dfrac{Q}{V-b}\right) V \ln Q + \dfrac{Q}{V-b} V \ln Q + Q = 0$ [avec « $V \ln Q$ » raturé puis récrit]

$\Leftrightarrow Q'(V) V \ln Q + Q = 0$

$\Leftrightarrow \dfrac{dQ \ln Q}{Q} = -\dfrac{\gamma dV}{V}$ [lecture incertaine — « $dQ \ln Q$ », peut-être « $dQ/\ln Q$ »]

$\Leftrightarrow \dfrac{1}{2} \ln^2 Q = -\ln V + \text{cte}$

$\Leftrightarrow$ [raturé — ligne biffée : « $\frac{1}{2} \ln^2 \frac{P}{V-b} = -\ln V + \text{cte}$ »]

$\Leftrightarrow \dfrac{1}{2} \ln^2(P(V-b)) = -\ln V + \text{cte}$

$\Leftrightarrow V(P(V-b))^{\frac{1}{2} \ln P(V-b)} = \text{cte}$ [lecture incertaine — exposant « $\frac{1}{2} \ln P(V-b)$ »]

$\left. \begin{array}{l} (\text{Ed}_{ARGD}) \Leftrightarrow \\ \text{Posons} \\ \\ (\text{Ed}_{ARGD}) \Leftrightarrow \\ \text{Pour} \\ \gamma = 1 \end{array} \right\}$ [accolade couvrant la dérivation pour $\gamma = 1$]

Rq : les résultats sont valables même lorsque $n \neq 1$ car $n \neq 1$ pour les 2 $1^{ers}$ cas car $V$ deviendra $V_m$ et on pourra reborder [raturé — phrase biffée d'un grand trait]

## Page 4

Rq : Pour $n \neq 1$, ces résultats restent les mêmes en remplaçant juste $V$ par $V_m$.

Page 4 sur 4

---

## Figures

Aucune figure géométrique sur la source (démonstration manuscrite, texte + équations) — vérifié p.1, rien à reproduire en code.

## Vocabulaire

- **Adiabatique réversible** : transformation avec $\delta Q = 0$.
- **$(\text{Ed}_{ARG})$** : équation différentielle de l'adiabatique réversible d'un gaz [lecture incertaine — sigle].
- **$(\text{E}_{ARGP})$** : cas particulier du gaz parfait, $PV^{\gamma} = \text{cte}$.
- **$\gamma$** : rapport admis constant dans la suite.
- **Gaz de Dieterici** : troisième application ($P(V-b)$).
- **$V_m$** : volume molaire, remplace $V$ quand $n \neq 1$.
