# Énergie cinétique — transcription fidèle

🧾 Source : [energie-cinetique.pdf](energie-cinetique.pdf)
🔍 Contenu : démonstration du théorème de l'énergie cinétique (TEC) — cas d'un solide (avec et sans torseurs), cas d'un système matériel de solides, énergie mécanique.
📄 Restauration : image restaurée Datas1 2026-09-07 — transcription fidèle, rien d'inventé.

## Page 1

TEC : \* (Cas d'un solide) : $\frac{d}{dt} E_c(S|R) = \mathcal{P}(\bar{S} \to S|R)$

Métho [lecture incertaine — « Metho : »] : (entre parenthèses) [lecture incertaine — ressemble à « tm… »] [mot encadré — lecture incertaine] :

$$\frac{dE_c}{dt}(S|R) = \frac{d}{dt}\left|\frac{1}{2} \{\mathcal{C}(S|R)\}_G \otimes \{\mathcal{V}(S|R)\}_G\right| \quad G = \text{centre d'inertie de } S$$

$$= \frac{1}{2}\frac{d}{dt}\left(m\,\vec{V}(G|R)^2 + \vec{\sigma}_G(S|R) \cdot \vec{\Omega}(S|R)\right)$$

$$= \frac{1}{2}\,2\,m\,\vec{a}(G|R)\cdot\vec{V}(G|R) + \frac{d}{dt}\left[\vec{\sigma}_G(S|R)\cdot\vec{\Omega}(S|R)\right]$$

où $X$ [lecture incertaine — le crochet de droite est noté $X$ en dessous] désigne le terme entre crochets.

Or il existe un repère principal $R_P = (G, \vec{u}, \vec{v}, \vec{w})$ lié à $S$ | $[I_G(S)]_{R_P}$ soit diagonale c-à-d $\exists\,\alpha, \beta, \gamma \in \mathbb{R}$ | $[I_G(S)]_{R_P} = \begin{bmatrix} \alpha & 0 & 0 \\ 0 & \beta & 0 \\ 0 & 0 & \gamma \end{bmatrix}$

dès lors, $X = \frac{d}{dt}\left(\alpha\Omega_u^2 + \beta\Omega_v^2 + \gamma\Omega_w^2\right) - 2\left(\alpha\dot{\Omega}_u\Omega_u + \beta\dot{\Omega}_v\Omega_v + \gamma\dot{\Omega}_w\Omega_w\right)$ [lecture incertaine — fin de la parenthèse]

Car $\dot{\alpha} = \dot{\beta} = \dot{\gamma} = 0$ vu que ces grandeurs dépendent de la géométrie et la masse de $(S)$, qui sont invariantes dans le temps pour $S =$ solide (indéformable)

d'où $X = 2\,\frac{d}{dt}\left([I_G(S)]\cdot\vec{\Omega}(S|R)\right)\cdot\vec{\Omega}(S|R)$

Ainsi $\frac{dE_c}{dt}(S|R) = \vec{R}_0(S|R)\cdot\vec{V}(G|R) + \vec{\delta}_A(S|R)\cdot\vec{\Omega}(S|R)$ [lecture incertaine — résultante et moment dynamiques]

$$= \{\mathcal{D}(S|R)\}_G \otimes \{\mathcal{C}(S|R)\}_G$$

$$= \{{T}_{\bar{S}\to S}\}_G \otimes \{\mathcal{C}(S|R)\}_G \text{ d'après le (PFD)}$$

D'où $\boxed{\frac{dE_c}{dt}(S|R) = \mathcal{P}(\bar{S}\to S|R)}$

## Page 2

\* Cas d'un solide (indéformable) de centre d'inertie $G$ (approche sans torseur) : $\Delta E_c = \sum_i W(\vec{F}_i)$ où $F_i \in \{\vec{F}_{\bar{S}\to S}\}$.

On a : $\sum_i W(F_i) = \sum_i \int_{t=t_i}^{t_f} \vec{F}_i \cdot \vec{V}(G|R)\,dt$

$$= \int_{t=t_i}^{t_f} \left(\sum_i \vec{F}_i\right)\cdot \vec{V}(G|R)\,dt$$

$$= \int_{t=t_i}^{t_f} m\,\vec{a}(G|R)\cdot \vec{V}(G|R)\,dt \quad \text{d'après la } 2^e \text{ loi de Newton}$$

$$= \int_{t=t_i}^{t_f} \frac{1}{2}\frac{d}{dt}\left(m\,\vec{V}(G|R)^2\right)dt$$

$$= \frac{1}{2}m\,\vec{V}(G|R)_{t_f}^2 - \frac{1}{2}m\,\vec{V}(G|R)_{t_i}^2$$

$$= \Delta E_c$$

\* Autre approche avec torseurs : $\frac{d}{dt}E_c(S|R) = \mathcal{P}(\bar{S}\to S|R)$

On a : $\frac{d}{dt}(E_c(S|R)) = \frac{d}{dt}\int_{P \in (S)} \frac{1}{2}\vec{V}(P|R)^2\,dm$

$$= \frac{1}{2}\int_{P \in (S)} 2\times\left(\vec{a}(P|R)\,dm\right)\cdot\vec{V}(P|R)$$

or d'après le PFD appliqué à $P$, $\vec{a}(P|R)\,dm = d\vec{R}(\bar{S}\to S)$

d'où $\frac{d}{dt}(E_c(S|R)) = \int_{P \in (S)} d\vec{R}(\bar{S}\to S)\cdot\vec{V}(P|R) = \mathcal{P}(\bar{S}\to S|R)$

## Page 3

\* Cas d'un système matériel $(S) = \bigcup_{i=1}^{n} S_i$ où les $S_i$, $_{1 \le i \le n}$ sont des solides.

$$\frac{dE_c(S|R)}{dt} = \mathcal{P}(\bar{S}\to S|R) + \sum_{1 \le i < j \le n} \mathcal{P}(S_i\to S_j|R)$$

En effet $\frac{dE_c(S|R)}{dt} = \frac{d}{dt}\left(\sum_{i=1}^{n} E_c(S_i|R)\right)$ [raturé]

$$= \sum_{i=1}^{n} \frac{d}{dt}E_c(S_i|R)$$

$$= \sum_{i=1}^{n} \mathcal{P}(\bar{S}_i\to S_i) \text{ d'après ce qui précède}$$

$$= \sum_{i=1}^{n}\left(\mathcal{P}(\bar{S}\to S_i|R) + \sum_{\substack{j=1 \\ j \ne i}}^{n} \mathcal{P}(S_j\to S_i|R)\right)$$

$$= \sum_{i=1}^{n}\mathcal{P}(\bar{S}\to S_i|R) + \sum_{i=1}^{n}\sum_{\substack{j=1 \\ j \ne i}}^{n} \mathcal{P}(S_j\to S_i|R)$$

$$= \mathcal{P}(\bar{S}\to S|R) + \sum_{1 \le i < j \le n} \left(\mathcal{P}(S_i\to S_j|R) + \mathcal{P}(S_j\to S_i|R)\right)$$

$$\frac{dE_c(S|R)}{dt} = \mathcal{P}(\bar{S}\to S|R) + \sum_{1 \le i < j \le n} \mathcal{P}(S_i \leftrightarrow S_j)$$

Énoncé : Dans un référentiel galiléen, la dérivée temporelle de l'énergie cinétique d'un système matériel $(S)$ est égale à la somme des puissances mutuelles entre les solides qui le constituent plus la puissance des actions mécaniques extérieures à $(S)$ [lecture incertaine — derniers mots en bas de page, partiellement coupés].

## Page 4

Dans le cas où les puissances [lecture incertaine — deux mots] dérivent d'une énergie potentielle $U(S|R_g)$, le TES [lecture incertaine — « TES »] s'écrit encore $\frac{dE_c}{dt}(S|R_g) = -\frac{dU}{dt}(S|R_g)$

Ainsi $\underline{E_c(S|R_g) + U(S|R_g) = \text{cste}} = \text{Énergie mécanique du système par rapport à } R_g$

---

## Figures

Aucune figure sur la source (démonstration manuscrite, texte + équations) — vérifié p.1, rien à reproduire en code.

## Vocabulaire

- **TEC** : théorème de l'énergie cinétique, $\frac{dE_c}{dt}(S|R) = \mathcal{P}(\bar{S}\to S|R)$.
- **Torseurs** : cinétique $\{\mathcal{C}\}$, dynamique $\{\mathcal{D}\}$, des actions $\{{T}\}$ ; produit $\otimes$ en $G$.
- **Puissance** : $\mathcal{P}(\bar{S}\to S|R)$ des actions extérieures ; puissances mutuelles $\mathcal{P}(S_i \leftrightarrow S_j)$.
- **PFD** : principe fondamental de la dynamique (passage torseur dynamique → torseur des actions).
- **Repère principal $R_P$** : $[I_G(S)]$ diagonale ($\alpha, \beta, \gamma$ invariants pour un solide).
- **Énergie mécanique** : $E_c + U = \text{cste}$ quand les puissances dérivent d'un potentiel (TES).
