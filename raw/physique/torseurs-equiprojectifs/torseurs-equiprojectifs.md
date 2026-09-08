# Torseurs équiprojectifs — transcription fidèle

> 🧾 **Manuscrit original :** `torseurs-equiprojectifs.pdf` (scan, 11 pages) · ✍️ KpihX — notes au stylo bleu, photos de feuilles volantes (pliures, recouvrements partiels, inscriptions en marge).
> 🔍 **Statut :** champ équiprojectif et antisymétrique (préliminaires, équivalence, formule du repère mobile) ; pages 6–7 et 8–9 = reprises photographiées deux fois (doublons confirmés au second passage 2026-09-07 : mêmes feuilles, cadrages différents — p.6 tronquée en bas, p.7 complète avec « D'où le résultat » ; p.8≈p.9 identiques), page 2 seule avec grande rature en croix (p.3 = suite propre, sans rature) ; rien d'inventé — tags `[lecture incertaine — …]` / `[raturé]` / `[*sic* — …]`. Transcrit mot à mot.
> 📄 **Source scannée :** [torseurs-equiprojectifs.pdf](torseurs-equiprojectifs.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

## Page 1

Champ équiprojectif et antisymétrique. [En haut à droite : `01/10/2022` — lecture incertaine]

On se munit d'un espace métrique $(\mathcal{E}, E, \cdot)$ [lecture incertaine — « $(\mathcal{E}, E, \cdot)$ »] de dimension 3, dont un repère orthonormé direct est $R = (O, \vec{e}_1, \vec{e}_2, \vec{e}_3)$ [lecture incertaine — fin de ligne].

I/ Préliminaires

1/ Deff [*sic* — orthographe d'origine] : Soit $f \in \mathcal{L}(E, E)$. $f$ est dite antisymétrique si $\forall \vec{u}, \vec{v} \in E$, $\vec{u} \cdot f(\vec{v}) + \vec{v} \cdot f(\vec{u}) = 0$.

En part. [*sic*] : on a : $\vec{u} \cdot f(\vec{u}) = 0$ d'où $\vec{u} \perp f(\vec{u})$.

2/ Théo : La matrice $M = \begin{pmatrix} m_{11} & m_{12} & m_{13} \\ m_{21} & m_{22} & m_{23} \\ m_{31} & m_{32} & m_{33} \end{pmatrix}$ associée à $f$ dans une base $B = (\vec{e}_1, \vec{e}_2, \vec{e}_3)$ est antisymétrique (c.-à-d. $M = \begin{pmatrix} 0 & m_{12} & m_{13} \\ -m_{12} & 0 & m_{23} \\ -m_{13} & -m_{23} & 0 \end{pmatrix}$ [lecture incertaine — coefficients recopiés au mieux]) équivalent à $\forall i, j \in [\![1, 3]\!]$, $m_{ij} + m_{ji} = 0$.

De la deff de $f$ découle $\forall i \in [\![1, 3]\!]$, $\vec{e}_i \cdot f(\vec{e}_i) = 0 \Rightarrow$ [lecture incertaine — produit développé] $\Rightarrow m_{ii} = 0$.

$\forall i, j \in [\![1, 3]\!]$, $i \ne j$, $\vec{e}_i \cdot f(\vec{e}_j) + \vec{e}_j \cdot f(\vec{e}_i) = 0$ c.-à-d. $\vec{e}_i \cdot (m_{ji} \vec{e}_j) + \vec{e}_j \cdot (m_{ij} \vec{e}_i)$ [lecture incertaine — indices] $= 0 \Rightarrow m_{ij} + m_{ji} = 0$.

D'où le résultat.

3/ Théo : $\exists ! \ \vec{R} \in E \ / \ \forall \vec{u} \in E$, $f(\vec{u}) = \vec{R} \wedge \vec{u}$.

L'existence d'un tel $\vec{R}$ est assurée par le fait que $\vec{u} \perp f(\vec{u})$.

Construisons $\vec{R}$ indépendamment de $\vec{u}$ [lecture incertaine — « $(x_1, y_1, z_1)$ » en marge].

On a : $f(\vec{u}) = \begin{pmatrix} m_{12} y + m_{13} z \\ -m_{12} x + m_{23} z \\ -m_{13} x - m_{23} y \end{pmatrix} = \begin{pmatrix} x \\ y \\ z \end{pmatrix} \wedge \begin{pmatrix} m_{23} \\ -m_{13} \\ m_{12} \end{pmatrix}$ [lecture incertaine — lettres $x, y, z$].

D'où l'existence et l'unicité de $\vec{R}$ qui vaut $\vec{R} = \begin{pmatrix} m_{23} \\ -m_{13} \\ m_{12} \end{pmatrix}$.

## Page 2

[raturé — une grande croix barre la quasi-totalité de la page ; transcription au mieux, calculs biffés]

4/ Rq : En travaillant sur une dimension quelconque $n \in \mathbb{N}^*$, on peut aussi définir un produit vectoriel plus général qu'on peut noter $\wedge$ avec en particulier $\wedge = \wedge^3$. En fait en définissant $f$ comme en ①, on aboutit à $M = [m_{ij}]_n$ est antisymétrique c.-à-d. $\forall i, j \in [\![1, n]\!]$, $m_{ij} = -m_{ji}$, on peut écrire $M = \begin{pmatrix} 0 & m_{12} & \cdots & m_{1n} \\ -m_{12} & 0 & \cdots & m_{2n} \\ \vdots & & \ddots & \\ -m_{1n} & \cdots & & 0 \end{pmatrix}$ [lecture incertaine — matrice] d'où $\forall \vec{u} = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} \in E$.

$f(\vec{u}) = M\vec{u} = \begin{pmatrix} \sum_{i=2}^{n} m_{1j} x_j \\ \vdots \\ \sum_{i=1}^{n} m_{ij} x_j \\ \vdots \\ \sum_{i=1}^{n} m_{nj} x_n \end{pmatrix}$ [lecture incertaine — sommes] qui peut être défini et le résultat de l'opération $\vec{R} \wedge \vec{u}$ où $\vec{R} = [\cdots] m_{a,b,n}$ [lecture incertaine — fin illisible, biffée].

4/ Rq : dans la mesure où $\dim E = n \in \mathbb{N}^*$, on montre que $l \in \mathcal{L}(E, E)$ est antisymétrique ssi sa matrice dans une base orthonormée directe $B = (\vec{e}_i)_n$ est antisymétrique ; en effet le sens $\Rightarrow$ se fait de façon analogue à ce qui précède quant à $\Leftarrow$ en considérant $\vec{v} = (x_i)_n = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$, $\vec{v}' = (x'_i)_n$ dans $B$ et $M = \begin{pmatrix} 0 & m_{12} & \cdots & m_{1n} \\ -m_{12} & 0 & \cdots & m_{2n} \\ \vdots & & \ddots & \\ -m_{1n} & \cdots & & 0 \end{pmatrix}$ antisymétrique [lecture incertaine — suite biffée, se prolonge page 3], on a : $\vec{v}' \cdot (M\vec{v}) = \sum_{i=1}^{n} \sum_{j=i+2}^{n} m_{ij} x_j x'_i + \sum_{j=i+2}^{n} m_{ij} x_j x'_i$ [raturé — sommes biffées].

## Page 3

[Feuille posée sur la précédente : le bas de la page 2 transparaît en bas ; en-tête partiellement coupé : « … $l(\vec{v}) = \vec{0}$ »]

Suite 4/ Rq : en considérant $\vec{v} = (x_i)_n$, $\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$, $\vec{v}' = (x'_i)_n$ dans $B = (\vec{e}_i)_n$, et $M = \begin{pmatrix} 0 & m_{12} & \cdots & m_{1n} \\ -m_{12} & 0 & \cdots & m_{2n} \\ \vdots & & \ddots & \\ -m_{1n} & \cdots & & 0 \end{pmatrix}$, on a :

$\vec{v}' \cdot (M\vec{v}) = \sum_{i=1}^{n} \left( \sum_{j=1}^{i-2} -m_{ji} x_j + \sum_{j=i+2}^{n} m_{ij} x_j \right) x'_i$ [lecture incertaine — bornes des sommes]

$= \sum_{i=1}^{n} \sum_{j=1}^{n} m_{ij} x_j x'_i$ où $m_{ij} = \begin{cases} m_{ij} \text{ pour } i < j \\ 0 \text{ pour } i = j \end{cases}$ [lecture incertaine]

$= \sum_{j=1}^{n} \sum_{i=1}^{n} m_{ij} x_j x'_i$

$= -\sum_{j=1}^{n} \sum_{i=1}^{n} m_{ji} x_j x'_i$ [lecture incertaine] car $\forall i, j \in [\![1, n]\!]$, $m_{ji} = -m_{ij}$

$= -\vec{v} \cdot (M\vec{v}')$.

D'où le résultat.

[Bas de page : bande de la page 2 visible par transparence/recouvrement : « … $\sum_{i=1}^{n} \sum_{j=1}^{n} m_{ij} x_j x'_i + \sum_{j=1}^{n} \sum_{i=1}^{n} m_{ij} x_j x'_i + \sum_{i=1}^{n} [\sum_{j=1}^{n} -m_{ji} x_j x'_i + \sum_{j=1}^{n} m_{ij} x_j x'_i]$ … » — [raturé / recouvrement, illisible]]

## Page 4

II/ Vif du sujet

1/ Deff : Soit $\vec{C}$ un champ vectoriel.

· $\vec{C}$ est équiprojectif ssi $\forall M, N \in \mathcal{E}^3$, $\overrightarrow{MN} \cdot \vec{C}(M) = \overrightarrow{MN} \cdot \vec{C}(N)$ [lecture incertaine — « $\overrightarrow{MN} \cdot \vec{C}(M)$ et $\overrightarrow{MN} \cdot \vec{C}(N)$ »].

· $\vec{C}$ est antisymétrique ssi $\forall M, N \in \mathcal{E}^3$, $\exists \vec{R} \in E \ / \ \forall M, N \in \mathcal{E}^3$, $\vec{C}(M) = \vec{C}(N) + \vec{R} \wedge \overrightarrow{NM}$ équivalent à dire qu'il existe en application linéaire $l$ antisymétrique / $\forall M, \vec{u} \in \mathcal{E}$ [lecture incertaine — fin de phrase], en ce point [lecture incertaine].

2/ Théor : $\vec{C}$ équiprojectif $\iff$ $\vec{C}$ antisymétrique.

$\Rightarrow$ / Soit $\vec{v} \in E$. $\exists ! M \in \mathcal{E}^3 / \ \vec{v} = \overrightarrow{OM}$. L'application linéaire $l : E \to E$, $\vec{v} \mapsto \vec{C}(M) - \vec{C}(O)$ est bien définie, où [lecture incertaine — « $\overrightarrow{OH}$ » biffé].

· Justifions $l$ linéaire [biffé — preuve reprise page 5]. Soit $(\vec{u}_0 = \overrightarrow{OH}, \vec{v} = \overrightarrow{ON}, \lambda) \in E^3 \times K$ [lecture incertaine — « $\overrightarrow{OH}$ »] où $K$ est le corps sur lequel est défini $E$.

· Justifions $l$ antisymétrique.

− Soit $\vec{u} = \overrightarrow{OM}$ et $\vec{v} = \overrightarrow{ON} \in E$. Mtq $\vec{u} \cdot l(\vec{v}) = -\vec{v} \cdot l(\vec{u})$ [lecture incertaine — « Mtq » = montrons que].

On a : $\vec{u} \cdot l(\vec{v}) = \vec{u} \cdot \vec{C}(N) - \vec{u} \cdot \vec{C}(O) = (\overrightarrow{OM} + \overrightarrow{MN}) \cdot \vec{C}(N) - \overrightarrow{OM} \cdot \vec{C}(O)$ [lecture incertaine] $= \overrightarrow{ON} \cdot \vec{C}(O)$ [lecture incertaine] $+ \overrightarrow{MN} \cdot \vec{C}(N) - \overrightarrow{OM} \cdot \vec{C}(O) = -(\overrightarrow{OM} \cdot \vec{C}(M) - \overrightarrow{ON} \cdot \vec{C}(O)) = -(\vec{v} \cdot \vec{C}(M) - \vec{v} \cdot \vec{C}(O))$ [lecture incertaine — enchaînement] $= -\vec{v} \cdot l(\vec{u})$.

[Bas de page, bande de la page précédente : « … $+ \sum_{i=1}^{n} \sum_{j=1}^{n} m_{ij} x_j x'_i$ … − Mtq $l$ linéaire. Soit $(\vec{u} = \overrightarrow{OH}, \vec{v} = \overrightarrow{ON}, \lambda) \in E^3 \times K$ où $K$ est le corps sur lequel est défini $E$. »]

## Page 5

Mtq $(l(\vec{u} + \lambda \vec{v}) = \vec{C}(M') - \vec{C}(O))$ où $M' = O + \vec{u} + \lambda \vec{v}$. D'après ce qui précède, $(\vec{C}(M') - (u + \lambda v)\vec{C}(O)$ [lecture incertaine — parenthésage] $l(\vec{u} + \lambda \vec{v}))$.

$\forall \vec{w} \in E$, $\vec{w} \cdot l(\vec{u} + \lambda \vec{v}) = -(\vec{u} + \lambda \vec{v}) \cdot l(\vec{w}) = -\vec{u} \cdot l(\vec{w}) - \lambda \vec{v} \cdot l(\vec{w})$ [lecture incertaine — « $-\lambda \vec{v} \cdot l(\vec{w})$ »] $= \vec{w} \cdot l(\vec{u}) + \vec{w} \cdot (\lambda l(\vec{v})) = \vec{w} \cdot (l(\vec{u}) + \lambda l(\vec{v}))$.

Vu que cela est vrai $\forall \vec{w} \in E$, on a donc $l(\vec{u} + \lambda \vec{v}) = l(\vec{u}) + \lambda l(\vec{v})$.

Ainsi $l$ antisymétrique d'où $\exists ! \vec{R} \in E \ / \ \forall \vec{u} \in E$, $l(\vec{u}) = \vec{R} \wedge \vec{u}$ c.-à-d. $\vec{C}(M) = \vec{C}(O) + \vec{R} \wedge \overrightarrow{OM}$.

Ainsi $\forall M, N \in \mathcal{E}^3$, $\begin{cases} \vec{C}(M) = \vec{C}(O) + \vec{R} \wedge \overrightarrow{OM} \\ \vec{C}(N) = \vec{C}(O) + \vec{R} \wedge \overrightarrow{ON} \end{cases} \Rightarrow \vec{C}(M) = \vec{C}(N) + \vec{R} \wedge \overrightarrow{NM}$.

Donc $\vec{C}$ antisymétrique.

$\Leftarrow$ / Soient $M, N \in \mathcal{E}^3$. On a : $\vec{C}(M) = \vec{C}(N) + \vec{R} \wedge \overrightarrow{NM}$ d'où $\overrightarrow{MN} \cdot \vec{C}(M) = \overrightarrow{MN} \cdot \vec{C}(N) + \overrightarrow{MN} \cdot (\vec{R} \wedge \overrightarrow{NM}) + (\overrightarrow{MN}, \vec{R}, \overrightarrow{NM}) + (\overrightarrow{NM}, \overrightarrow{MN}, \vec{R}) + \vec{R} \cdot (\overrightarrow{NM} \wedge \overrightarrow{MN})$ [lecture incertaine — produits mixtes intermédiaires] d'où $\overrightarrow{MN} \cdot \vec{C}(M) = \overrightarrow{MN} \cdot \vec{C}(N)$.

Donc $\vec{C}$ équiprojectif.

D'où le résultat.

## Page 6

[Photo inclinée, deux feuilles : en haut la fin du II/, en bas la « Suite 4/ Rq » déjà vue pages 2–3]

Rq : Un champ équiprojectif est un moment ssi $\exists O \in \mathcal{E}^3 \ / \ \forall P \in \mathcal{E}^3$, $\vec{C}(P) = \overrightarrow{S_0(O)} \wedge \overrightarrow{OP}$ [lecture incertaine] ($\vec{\sigma}$ peut aussi être pris car l'origine de $\vec{R}$) $\iff \forall P, Q \in \mathcal{E}^3$, [raturé — passage biffé] $P = S_{\sigma}(Q) \iff \vec{S}(P) = -\vec{S}(Q)$. Il existe en [*sic* — « Il en existe »] une infinité de tels pts $O$ formant une droite $(\Delta)$ appelée axe central dans la mesure où $\vec{R} \ne \vec{0}$. Le cas échéant $\forall P \in \mathcal{E}^3$, $\vec{C}(P) = \vec{0}$ [lecture incertaine — « Le cas échéant »].

Suite 4/ Rq : en considérant $\vec{v} = (x_i)_n$, $\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$, $\vec{v}' = (x'_i)_n$ dans $B = (\vec{e}_i)_n$, et $M = \begin{pmatrix} 0 & m_{12} & \cdots & m_{1n} \\ -m_{12} & 0 & \cdots & m_{2n} \\ \vdots & & \ddots & \\ -m_{1n} & \cdots & & 0 \end{pmatrix}$, on a : [même calcul que page 3, recopié — bas de photo tronqué, sans la conclusion visible p.7] $\vec{v}' \cdot (M\vec{v}) = \sum_{i=1}^{n} (\sum_{j=1}^{i-2} -m_{ji} x_j + \sum_{j=i+2}^{n} m_{ij} x_j) x'_i$ [lecture incertaine] $= \sum_{i=1}^{n} \sum_{j=1}^{n} m_{ij} x_j x'_i$ où $m_{ij} = \begin{cases} m_{ij} \text{ pour } i < j \\ 0 \text{ pour } i = j \end{cases}$ $= \sum_{j=1}^{n} \sum_{i=1}^{n} m_{ij} x_j x'_i = \sum_{j=1}^{n} \sum_{i=1}^{n} m_{ji} x_j x'_i$ [lecture incertaine — signe] car $\forall i, j \in [\![1, n]\!]$, $m_{ji} = -m_{ij}$.

## Page 7

[Reprise photographiée de la page 6, mêmes contenus, cadrage différent]

II/ Vif du sujet [bandeau de tête, partiel].

Rq : Un champ équiprojectif est un moment ssi $\exists O \in \mathcal{E}^3 \ / \ \forall P \in \mathcal{E}^3$, $\vec{C}(P) = \overrightarrow{S_0(O)} \wedge \overrightarrow{OP}$ [lecture incertaine] ($\vec{\sigma}$ peut aussi être pris car l'origine de $\vec{R}$) $\iff \forall P, Q \in \mathcal{E}^3$, [raturé] $P = S_{\sigma}(Q) \iff \vec{S}(P) = -\vec{S}(Q)$. Il existe en [*sic* — « Il en existe »] une infinité de tels pts $O$ formant une droite $(\Delta)$ appelée axe central dans la mesure où $\vec{R} \ne \vec{0}$. Le cas échéant $\forall P \in \mathcal{E}^3$, $\vec{C}(P) = \vec{0}$ [lecture incertaine].

Suite 4/ Rq : en considérant $\vec{v} = (x_i)_n$, $\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$, $\vec{v}' = (x'_i)_n$ dans $B = (\vec{e}_i)_n$, et $M = \begin{pmatrix} 0 & m_{12} & \cdots & m_{1n} \\ -m_{12} & 0 & \cdots & m_{2n} \\ \vdots & & \ddots & \\ -m_{1n} & \cdots & & 0 \end{pmatrix}$, on a :

$\vec{v}' \cdot (M\vec{v}) = \sum_{i=1}^{n} (\sum_{j=1}^{i-2} -m_{ji} x_j + \sum_{j=i+2}^{n} m_{ij} x_j) x'_i$ [lecture incertaine]

$= \sum_{i=1}^{n} \sum_{j=1}^{n} m_{ij} x_j x'_i$ où $m_{ij} = \begin{cases} m_{ij} \text{ pour } i < j \\ 0 \text{ pour } i = j \end{cases}$

$= \sum_{j=1}^{n} \sum_{i=1}^{n} m_{ij} x_j x'_i$

$= -\sum_{j=1}^{n} \sum_{i=1}^{n} m_{ji} x_j x'_i$ [lecture incertaine] car $\forall i, j \in [\![1, n]\!]$, $m_{ji} = -m_{ij}$

$= -\vec{v} \cdot (M\vec{v}')$.

D'où le résultat.

## Page 8

[Feuille froissée, écriture serrée ; bas de page très chargé avec recouvrements]

Théo : Pour une app antisymétrique $l$, (vérifiant $\exists \vec{R} \in E \ / \ \forall \vec{u} \in E$, $l(\vec{u}) = \vec{R} \wedge \vec{u}$ en dim 3) $\in \mathcal{L}(E, E)$, on a : $\vec{R} = \frac{1}{2} \sum_{i=1}^{3} \vec{e}_i \wedge l(\vec{e}_i)$ où $B = (\vec{e}_i)_3$ est une base orthonormée directe de $E$ (c.-à-d. $\forall i, j \in [\![1, 3]\!]$, $\vec{e}_i \cdot \vec{e}_j$ [lecture incertaine — « $= 0$ »], $\vec{e}_1 = \vec{e}_2 \wedge \vec{e}_3$ [lecture incertaine]).

En effet $\forall i \in [\![1, 3]\!]$, $\sum_{i=1}^{3} \vec{e}_i \wedge l(\vec{e}_i) = \sum_{i=1}^{3} \vec{e}_i \wedge (\vec{R} \wedge \vec{e}_i) = \sum_{i=1}^{3} \vec{R} - (\vec{e}_i \cdot \vec{R}) \vec{e}_i = 3\vec{R} - \sum_{i=1}^{3} x_i \vec{e}_i$ [lecture incertaine — « $x_i \vec{e}_i$ »] $= 3\vec{R} - \vec{R} = 2\vec{R}$.

Donc $\boxed{\vec{R} = \frac{1}{2} \sum_{i=1}^{3} \vec{e}_i \wedge l(\vec{e}_i)}$.

App : Soit $E$, tel que … $\mathbb{R}^3$. Soient 2 orthonormées directes bases $B_0 = (\vec{e}_{0i})_n$ et $B_1 = (\vec{e}_{1i})_n$.

Deff : soit $\vec{u} \in E$. $\vec{u}$ est lié à $B_0$ ssi $\forall i \in [\![1, n]\!]$, $\vec{u} \cdot \vec{e}_i = \text{cste}$ c.-à-d. $u_i = u_{1i}$ [lecture incertaine]. On notera $\vec{u}$ — $B_1$. Soit une variable réelle $t$ (faisant allusion au temps en physique). En posant … Considérant $\frac{d}{dt}\big|_{B_0} : E' \to E'$ où $E' = \{\vec{u} \in E \ / \ \vec{u} - B_0\}$ [lecture incertaine] on $l$ linéaire et antisymétrique vu que $\forall \vec{u}, \vec{v} \in E'$, $\vec{u} \cdot l(\vec{v}) + \vec{v} \cdot l(\vec{u}) = \frac{d}{dt}(\vec{u} \cdot \vec{v})\big| \dots$ [lecture incertaine — bas de page à recouvrements, plusieurs lignes superposées] $= \frac{d}{dt} \sum u_i v_i = 0$ [lecture incertaine] avec $\exists ! \vec{R} \in E^3 \ / \ \forall \vec{u} \in E$, $l(\vec{u}) = \vec{R} \wedge \vec{u}$ [lecture incertaine]. Donc : $\vec{R} = \frac{1}{2} \sum_{i=1}^{3} \vec{e}_i \wedge \frac{d\vec{e}_i}{dt}\big|_{B_0}$.

## Page 9

[Reprise photographiée de la page 8, mêmes contenus]

Théo : Pour une app antisymétrique $l$, (vérifiant $\exists \vec{R} \in E \ / \ \forall \vec{u} \in E$, $l(\vec{u}) = \vec{R} \wedge \vec{u}$ en dim 3) $\in \mathcal{L}(E, E)$, on a : $\vec{R} = \frac{1}{2} \sum_{i=1}^{3} \vec{e}_i \wedge l(\vec{e}_i)$ où $B = (\vec{e}_i)_3$ est une base orthonormée directe de $E$ (c.-à-d. $\forall i, j \in [\![1, 3]\!]$, $\vec{e}_i \cdot \vec{e}_j$ [lecture incertaine], $\vec{e}_1 = \vec{e}_2 \wedge \vec{e}_3$ [lecture incertaine]).

En effet $\forall i \in [\![1, 3]\!]$, $\sum_{i=1}^{3} \vec{e}_i \wedge l(\vec{e}_i) = \sum_{i=1}^{3} \vec{e}_i \wedge (\vec{R} \wedge \vec{e}_i) = \sum_{i=1}^{3} \vec{R} - (\vec{e}_i \cdot \vec{R}) \vec{e}_i = 3\vec{R} - \sum_{i=1}^{3} x_i \vec{e}_i$ [lecture incertaine] $= 3\vec{R} - \vec{R} = 2\vec{R}$.

Donc $\boxed{\vec{R} = \frac{1}{2} \sum_{i=1}^{3} \vec{e}_i \wedge l(\vec{e}_i)}$.

App : Soit $E$, tel que … $\mathbb{R}^3$. Soient 2 orthonormées directes bases $B_0 = (\vec{e}_{0i})_n$ et $B_1 = (\vec{e}_{1i})_n$.

Deff : soit $\vec{u} \in E$. $\vec{u}$ est lié à $B_0$ ssi $\forall i \in [\![1, n]\!]$, $\vec{u} \cdot \vec{e}_i = \text{cste}$ [lecture incertaine] c.-à-d. $u_i = u_{1i}$ [lecture incertaine]. On notera $\vec{u}$ — $B_1$. Soit une variable réelle $t$ (faisant allusion au temps en physique). En posant … Considérant $\frac{d}{dt}\big|_{B_0} : E' \to E'$ où $E' = \{\vec{u} \in E \ / \ \dots\}$ [lecture incertaine] on $l$ linéaire et antisymétrique vu que $\forall \vec{u}, \vec{v} \in E'$, $\vec{u} \cdot l(\vec{v}) + \vec{v} \cdot l(\vec{u}) = \frac{d}{dt}(\vec{u} \cdot \vec{v})$ [lecture incertaine — lignes superposées en bas de page] $= \frac{d}{dt} \sum u_i v_i = 0$ [lecture incertaine] avec $\exists ! \vec{R} \in E^3 \ / \ \forall \vec{u} \in E$, $l(\vec{u}) = \vec{R} \wedge \vec{u}$ [lecture incertaine]. Donc : $\vec{R} = \frac{1}{2} \sum_{i=1}^{3} \vec{e}_i \wedge \frac{d\vec{e}_i}{dt}\big|_{B_0}$.

## Page 10

[En-tête partiellement masqué : « II/ Vif du sujet » ; première ligne en partie cachée]

1/1/1/. Soit $\vec{?}$ … [lecture incertaine — ligne masquée par la feuille du dessus].

App : formule fondamentale de la dérivation ou du repère mobile. En considérant $E$, $b_0$, $b_2$ [lecture incertaine — « $b_0$, $b_2$ »] définis précédemment posons $l = \frac{d}{dt}\big|_{b_0} - \frac{d}{dt}\big|_{b_2} : E \to E$.

− $l$ est linéaire.

− $l$ est antisymétrique.

En effet $\forall \vec{u}, \vec{v} \in E$, $\vec{u} \cdot l(\vec{v}) + \vec{v} \cdot l(\vec{u}) = \vec{u} \cdot \frac{d\vec{v}}{dt}\big|_{b_0} - \vec{v} \cdot \frac{d\vec{u}}{dt}\big|_{b_0} + \vec{u} \cdot \frac{d\vec{v}}{dt}\big|_{b_2} - \vec{v} \cdot \frac{d\vec{u}}{dt}\big|_{b_2}$ [lecture incertaine — signes] $= \frac{d}{dt}(\vec{u} \cdot \vec{v})\big|_{b_0} - \frac{d}{dt}(\vec{u} \cdot \vec{v})\big|_{b_2} = \frac{d}{dt}(\|\vec{u}\| \|\vec{v}\| \cos(\vec{u}, \vec{v})) - \frac{d}{dt}(\|\vec{u}\| \|\vec{v}\| \cos(\vec{u}, \vec{v}))$ [lecture incertaine — « $\cos$ »] on se débarrasse de ceci car le produit scalaire ne dépend d'aucune base $= 0$.

Ainsi d'après les résultats en amont, $\exists ! \vec{R} \in E \ / \ \forall \vec{u} \in E$, $l(\vec{u}) = \vec{R} \wedge \vec{u}$ c.-à-d. $\boxed{\frac{d\vec{u}}{dt}\big|_{b_0} = \frac{d\vec{u}}{dt}\big|_{b_2} + \vec{R} \wedge \vec{u}}$ avec $\vec{R} = \frac{1}{2} \sum_{i=1}^{3} \vec{e}_{0i} \wedge l(\vec{e}_{0i}) = \frac{1}{2} \sum_{i=1}^{3} \vec{e}_{0i} \wedge \frac{d\vec{e}_{0i}}{dt}\big|_{b_0} = \frac{1}{2} \sum_{i=1}^{3} \vec{e}_{0i} \wedge \frac{d\vec{e}_{0i}}{dt}\big|_{b_0}$ [lecture incertaine — fin de ligne coupée].

## Page 11

Rq : Pour 2 bases orthonormées directes de $\mathbb{R}^3$ on a

· $\sum_{i=1}^{3} \vec{e}_{0i} \wedge \frac{d\vec{e}_{0i}}{dt}\big|_{B_0} + \sum_{i=1}^{3} \vec{e}_{1i} \wedge \frac{d\vec{e}_{1i}}{dt}\big|_{B_1} = 0$ [lecture incertaine — second membre].

· $\frac{d}{dt}(\vec{u} \cdot \vec{v})\big|_{B_0} = \frac{d}{dt}(\vec{u} \cdot \vec{v})\big|_{B_1}$ puisque pour $\vec{u}, \vec{v} \in E'$, $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos(\vec{u}, \vec{v})$ et défini indépendamment de toute base [lecture incertaine — « défini » sans accord, recopié tel quel] et il en va de même pour toute fonction scalaire $f : t \mapsto f(t)$.

---

## Figures

Aucune figure : les 11 pages sont du texte mathématique seul (matrices, calculs, rature en croix p.2, recouvrements/pliures). Échantillon visuel vérifié : p.1 et p.10 (texte seul confirmé) ; second passage 2026-09-07 : pp.2–9 relues — p.6≈p.7 doublon confirmé (p.6 : bas tronqué, sans la conclusion ; p.7 : complète) et p.8≈p.9 doublon confirmé (contenus identiques). 100 % code vérifié sur l'échantillon (rien à reproduire).

## Vocabulaire

- **champ équiprojectif** — $\overrightarrow{MN} \cdot \vec{C}(M) = \overrightarrow{MN} \cdot \vec{C}(N)$.
- **application antisymétrique** — $f$ avec $\vec{u} \cdot f(\vec{v}) + \vec{v} \cdot f(\vec{u}) = 0$ ; matrice $M = -M^T$.
- **vecteur tourbillon $\vec{R}$** — unique tel que $f(\vec{u}) = \vec{R} \wedge \vec{u}$ ; $\vec{R} = \frac{1}{2}\sum \vec{e}_i \wedge l(\vec{e}_i)$.
- **axe central $(\Delta)$** — droite des points $O$ pour un champ = moment ($\vec{R} \ne \vec{0}$).
- **formule du repère mobile** — $\frac{d\vec{u}}{dt}\big|_{b_0} = \frac{d\vec{u}}{dt}\big|_{b_2} + \vec{R} \wedge \vec{u}$.
