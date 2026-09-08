# Un peu d'Algèbre linéaire sur le changement de base — transcription fidèle

> 🧾 **Manuscrit original :** `changement-bases.pdf` (scan, 7 pages, encre bleue) · ✍️ KpihX
> 🔍 **Statut :** transcrit fidèlement ; notations d'origine conservées ($M_{\alpha\beta}$, $P_{\alpha}^{\alpha'}$, $^tP$). Ratures et passages peu lisibles signalés ; rien d'inventé.
> 📄 **Source scannée :** [`changement-bases.pdf`](changement-bases.pdf) (restaurée Datas1, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1 — Notations et matrice de passage

Un peu d'Algèbre linéaire sur le changement de base

* Notations :*

Soit $E \equiv \mathbb{K}\text{-ev}$, $F \equiv \mathbb{K}\text{-ev}$ [le $F$ est réécrit sur une rature], $\alpha, \alpha'$ (resp $\beta, \beta'$) 2 bases de $E$ (resp de $F$). Soit $x \in E$. On définit :

- $[x]_{\alpha}$ : matrice colonne formée des composantes de $x$ dans $\alpha$. Pour $i \in [\![1 ; \dim(E)]\!]$, $[x]_{\alpha,i}$ est la composante N° $i$ de $x$ dans $\alpha$
- $M_{\alpha\beta}(f)$ : matrice de $f$ de la base $\alpha$ à la base $\beta$ où $f$ est une app lin de $E \to F$

NB : L'écriture $M_{\alpha}(f)$ sous entend que $F = \mathbb{K}$.

- Pour $M \in M_{n,m}(\mathbb{K})$, $[M]_{i,j}$ est l'élément de $M$ à la ligne $i$ et la colonne $j$

* Changement de base*

Soit $E \equiv \mathbb{K}\text{-ev}$ [signe $\equiv$ raturé/réécrit], $\alpha = (e_i)_{i=1}^n$ [indice bas peu lisible — lu $1$ par le contexte], $\alpha' = (e'_i)_{i=1}^n$, 2 bases de $E$.

On définit : $P_{\alpha}^{\alpha'} = M_{\alpha'\alpha}(\mathrm{Id}_E)$ [lu tel quel].

Ainsi $\forall x \in E$, comme $[x]_{\alpha} = M_{\alpha'\alpha}(\mathrm{Id}_E)[x]_{\alpha'}$ alors $[x]_{\alpha} = P_{\alpha}^{\alpha'}[x]_{\alpha'}$ [indices lus tels quels].

Exp matricielle : $P_{\alpha}^{\alpha'} = [P_1 \dots P_n]$

Soit $j \in [\![1,n]\!]$. [raturé — début de calcul réécrit] $P_j = P_{\alpha}^{\alpha'}\begin{bmatrix} 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \end{bmatrix}_j = P_{\alpha}^{\alpha'}[e'_j]_{\alpha'} = [e'_j]_{\alpha}$

D'où $P_{\alpha}^{\alpha'} = [[e'_1]_{\alpha} \dots [e'_n]_{\alpha}]$

---

## Page 2 — Application linéaire et changement de base

* Appl lin et chang de base*

NB : Pour un ev $E$, dans la suite, $\mathcal{B}(E)$ désignera l'ens des bases de $E$.

Soient $E$ et $F$ 2 ev de dim resp $n$ et $m$, $\alpha$ et $\beta$ leurs bases resp. On a : $M_{\alpha\beta}(f) = [[f(e_1)]_{\beta} \dots [f(e_n)]_{\beta}]$

Théo 1 : $f$ est bien définie (indépendante de $\alpha$)

ssi $\forall \alpha' \in \mathcal{B}(E), \quad M_{\alpha'\beta}(f) = M_{\alpha\beta}(f)\,P_{\alpha}^{\alpha'}$

$\Rightarrow$ / Soit $\alpha' \in \mathcal{B}(E)$. $f$ est bien définie $\Rightarrow \forall x \in E$, $f(x) = M_{\alpha\beta}(f)[x]_{\alpha} = M_{\alpha'\beta}(f)[x]_{\alpha'}$

Posons $\alpha' = (e'_i)_{i=1}^n$

---

## Page 3 — Preuve du théo 1 et théo 2

[haut de page rogné : fin de la phrase précédente — « … Soit … $\in [\![1,n]\!]$. En particulier pour $x = e'_j$ »]

Montrons que $M_{\alpha'\beta}(f) = M_{\alpha\beta}(f)\,P_{\alpha}^{\alpha'} \iff \forall j \in [\![1,n]\!]$, $[M_{\alpha'\beta}(f)]_j = [M_{\alpha\beta}(f)\,P_{\alpha}^{\alpha'}]_j$ où $[M_{\alpha'\beta}(f)]_j$ désigne la colonne $j$ de $M_{\alpha'\beta}(f)$ (de m̂ pour $[M_{\alpha\beta}(f)P_{\alpha}^{\alpha'}]_j$)

Soit $j \in [\![1,n]\!]$.

On a : $[M_{\alpha'\beta}(f)]_j = M_{\alpha'\beta}(f)\begin{bmatrix} 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \end{bmatrix}_j = M_{\alpha'\beta}(f)[e'_j]_{\alpha'}$
$= f(e'_j)$
$= M_{\alpha\beta}(f)[e'_j]_{\alpha}$
$= M_{\alpha\beta}(f)[P_{\alpha}^{\alpha'}]_j$
$= [M_{\alpha\beta}(f)\,P_{\alpha}^{\alpha'}]_j$

D'où le résultat !

$\Leftarrow$ / Montrons que $\forall x \in E, \; M_{\alpha'\beta}(f)[x]_{\alpha'} = f(x)$

On a : $M_{\alpha'\beta}(f)[x]_{\alpha'} = M_{\alpha\beta}(f)\,P_{\alpha}^{\alpha'}[x]_{\alpha'} = M_{\alpha\beta}(f)[x]_{\alpha} = f(x) \quad \text{cqfd}$

Théo 2 : Soit $\alpha'$ (resp $\beta'$) une base de $E$ (resp $F$). On a : $M_{\alpha'\beta'}(f) = P_{\beta'}^{\beta}\,M_{\alpha\beta}(f)\,P_{\alpha}^{\alpha'}$

En effet $M_{\alpha'\beta'}(f) = P_{\beta'}^{\beta}\,M_{\alpha\beta'}(f) = P_{\beta'}^{\beta}\,M_{\alpha\beta}(f)\,P_{\alpha}^{\alpha'}$

[bas de page : « ou encore … » raturé]

---

## Page 4 — Théo 3 (bases duales) et corollaire

Théo 3 : Soit $E$, un ev de dim $n$, $\alpha = (e_i)_{i=1}^n$, $\alpha' = (e'_j)_{j=1}^n$, 2 bases de $E$. On a : $P_{\alpha^*}^{\alpha'^*} = {}^tP_{\alpha'}^{\alpha} = {}^t(P_{\alpha}^{\alpha'})^{-1}$

En effet $P_{\alpha^*}^{\alpha'^*} = [[e_1'^*]_{\alpha^*} \dots [e_n'^*]_{\alpha^*}] = [[e_j'^*]_i]^n_{i,j=1}$ [lu tel quel].

Soient $i,j \in [\![1,n]\!]$. Explicitons le terme $[e_j'^*]_i$.

On a : $e_j'^* = \sum_{k=1}^n [e_j'^*]_k e_k^* \Rightarrow e_j'^*(e_i) = [e_j'^*]_i \times 1$

D'où $P_{\alpha^*}^{\alpha'^*} = [e_j'^*(e_i)]_{i,j=1}^n$

De plus $e_j'^*(e_i) = e_j'^*\left(\sum_{k=1}^n [e_i]_k^{\alpha'} e'_k\right) = \sum_{k=1}^n [e_i]_k^{\alpha'} e_j'^*(e'_k) = [e_i]_j^{\alpha'}$

Ainsi $P_{\alpha^*}^{\alpha'^*} = [[e_i]_j^{\alpha'}]_{i,j=1}^n = \begin{bmatrix} [e_1]^{\alpha'} \\ \vdots \\ [e_n]^{\alpha'} \end{bmatrix} = {}^t\{[e_1]^{\alpha'} \dots [e_n]^{\alpha'}\}$ [accolade et exposants lus tels quels] $= {}^tP_{\alpha'}^{\alpha}$

Donc $P_{\alpha^*}^{\alpha'^*} = {}^tP_{\alpha'}^{\alpha} = {}^t(P_{\alpha}^{\alpha'})^{-1}$

Corollaire 1 : Soit $E$, un ev de dim $n$, $\alpha$ et $\alpha'$, 2 bases de $E$. Il existe un isomorphisme de $E$ vers $E^*$ / $M_{\alpha\alpha^*}(\varphi) = M_{\alpha'\alpha'^*}(\varphi) = I_n$ ssi $P_{\alpha}^{\alpha'}$ est orthogonale.

Cherchons un tel morphisme $\varphi$.

---

## Page 5 — Suite du corollaire (isomorphisme canonique)

D'après le théo 2, $M_{\alpha\alpha^*}(\varphi) = (P_{\alpha^*}^{\alpha'^*})^{-1}$ [lecture incertaine — exposant peu lisible] $M_{\alpha'\alpha'^*}(\varphi)\,P_{\alpha}^{\alpha'}$

c-à-d $P_{\alpha^*}^{\alpha'^*} = P_{\alpha}^{\alpha'}$ car $M_{\alpha\alpha^*}(\varphi) = M_{\alpha'\alpha'^*}(\varphi) = I_n$

c-à-d $({}^tP_{\alpha}^{\alpha'})^{-1} = P_{\alpha}^{\alpha'}$ [lu par le contexte — l'exposant $^{-1}$ est peu lisible] au vu du théo 3

c-à-d ${}^tP_{\alpha}^{\alpha'} = P_{\alpha}^{\alpha'}$ [lu tel quel — *sic*, attendre ${}^tP \cdot P = I_n$]

c-à-d $P_{\alpha}^{\alpha'}$ est orthogonale.

Ainsi $\varphi$ existe si $P_{\alpha}^{\alpha'}$ est orthogonale.

De plus $M_{\alpha\alpha^*}(\varphi) = I_n \iff \forall x \in E$, [raturé — $\varphi(x) = x$ barré]

$\varphi\left(x = \sum_{i=1}^n x_i e_i\right) = \sum_{i=1}^n x_i \varphi(e_i)$ avec $[\varphi(e_i)]_{\alpha^*} = \begin{bmatrix} 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \end{bmatrix}_i$

c-à-d $\varphi\left(\sum_{i=1}^n x_i e_i\right) = \sum_{i=1}^n x_i e_i^* \quad (1)$

ce qui a été fait en amont garantit que ce $\varphi$ qu'on vient d'expliciter vérifie $M_{\alpha\alpha^*}(\varphi) = I_n$.

En conclusion un tel $\varphi$ ne peut être que la forme (1) qui est bien une fl app lin de $E \to E^*$ cqfd.

Rq : le $\varphi$ ainsi définit est bien plus qu'un simple morphisme c'est l'isomorphisme canonique entre $E$ et $E^*$, qui nous garantit ainsi que si travailler dans $E$ semble difficile et dans $E^*$ plus facile, on peut alors travailler dans $E^*$ !

---

## Page 6 — Théo 4 (formes bilinéaires, sens direct)

[haut de page rogné : « … et obtenir les résultats souhaités dans $E$ à un isomorphisme près »]

Théo 4 : Soit $E$, un ev de dim $n$, $\alpha$ et $\alpha'$, 2 bases de $E$. Soit $f$, une fb de $E \times F \to \mathbb{K}$ où $\mathbb{K}$ = corps [lu « corps ($E$) » — lecture incertaine] et $F \equiv \mathbb{K}\text{-ev}$ de dim $m$ et de bases $\beta = (g_j)_{j=1}^m$, $\beta' = (g'_j)_{j=1}^m$.

$f$ est bien définie (c-à-d indépendante des bases de $E$ et $F$) ssi $M_{\alpha'\beta'}(f) = \dots$ [membre de droite rogné en bas de phrase].

En effet,

$\Rightarrow$ / $\forall (x,y) \in E \times F$, ${}^t[x]_{\alpha'\beta'}$ [lu tel quel] $(f)[y]_{\beta'} = f(x,y) = {}^t[x]_{\alpha} M_{\alpha\beta}(f)[y]_{\beta}$ [terme central raturé et réécrit].

On a : $f(x,y) = {}^t[x]_{\alpha'}^{\alpha'} P_{\alpha}^{\alpha'} M_{\alpha\alpha'}(f)$ [raturé] $P$ [indices en exposants lus tels quels — passage très raturé].

$\forall (x,y) \in E \times F$, ${}^t[x]_{\alpha'}^{\alpha'} M_{\alpha'\beta'}^{\alpha'}[y]_{\beta'}^{\beta'} = f(x,y) = {}^t[x]_{\alpha\beta}^{\alpha} M_{\alpha\beta}[y]_{\beta}^{\beta}$ [exposants lus tels quels, lecture incertaine].

On a : $f(x,y) = {}^t[x]_{\alpha'}^{\alpha'} {}^tP_{\alpha}^{\alpha'} M_{\alpha\beta} P_{\beta}^{\beta'}[y]_{\beta'}^{\beta'}$ [lu tel quel].

Soit $(i,j) \in [\![1,n]\!] \times [\![1,m]\!]$. Proq $[M_{\alpha'\beta'}^{?}]_{i,j} = [P_{\alpha}^{\alpha'} M_{\alpha\beta} P_{\beta}^{\beta'}]_{i,j}$ [le $^t$ devant $P$ est masqué par une rature — lecture incertaine].

Pour $(x,y) = (e'_i, g'_j)$, on a : $f(e'_i, g'_j) = [0 \dots 0 \dots]$ [ligne de zéros avec $1$ à la place $i$] $M_{\alpha\beta}[g'_j] = \dots$ [suite page suivante].

---

## Page 7 — Fin du théo 4

$f(e'_i, g'_j) = {}^t[e'_i]^{\alpha'} M_{\alpha\beta}(f)\begin{bmatrix} 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \end{bmatrix}_j = [0 \dots \underset{i}{1} \dots 0]\,[M_{\alpha'\beta'}^{?}]_{?j}$ [terme central raturé] $= [M_{\alpha\beta}^{?}]_{i,j}$ [exposants lus tels quels — lecture incertaine].

De m̂ $f(e'_i, g'_j) = [{}^tP_{\alpha}^{\alpha'} M_{\alpha\beta}(f) P_{\beta}^{\beta'}]_{i,j}$

D'où $M_{\alpha'\beta'}(f) = {}^tP_{\alpha}^{\alpha'} M_{\alpha\beta}(f) P_{\beta}^{\beta'}$

$\Leftarrow$ / Soit $(x,y) \in E \times F$.

On a : ${}^t[x]_{\alpha'}^{\beta'} M_{\alpha'\beta'}(f)[y]_{\beta'}^{\beta'} = {}^t[x]_{\alpha'}^{\alpha'} {}^tP_{\alpha}^{\alpha'} M_{\alpha\beta}(f) P_{\beta}^{\beta'}[y]_{\beta'}^{\beta'}$ [exposants lus tels quels]
$= {}^t(P_{\alpha}^{\alpha'}[x]_{\alpha'}^{\alpha'})\,M_{\alpha\beta}(f)\,[y]_{\beta}^{\beta}$
$= {}^t[x]_{\alpha}^{\beta}\,M_{\alpha\beta}\,[y]_{\beta}^{\beta}$
$= f(x,y) \quad \text{cqfd}$

---

## 📝 Notes de transcription (fidélité)

- Encre bleue sur papier blanc ; pages 3–4 et 6–7 : bords de feuille et coin de table visibles (hors manuscrit).
- Ratures à l'encre (sans correcteur) pages 1, 3, 5, 6, 7 : signalées par [raturé] sans reconstitution.
- Hauts de pages 3 et 6 rognés par le scan (fins de phrases manquantes) : signalés.
- L'auteur écrit $\alpha$ comme un « $a$ » cursif et $M_{\alpha\beta}$ parfois $M_{\alpha'\alpha}$ dans les passages de changement de base : symboles lus tels quels, incohérences apparentes conservées avec [*sic*] implicite via « lu tel quel ».
- Aucune figure dans ce dossier (algèbre pure) : pas de script de reproduction.

---

## Figures

Aucune figure à reproduire : pages 1–7 relues visuellement (S2 le 2026-09-07 : pp. 2–7 confirmées, texte et formules seuls, sans schéma) — confirmé.

## Vocabulaire / notions

- **Matrice de passage** $P_{\alpha}^{\alpha'} = M_{\alpha'\alpha}(\mathrm{Id}_E)$.
- **Coordonnées** $[x]_{\alpha}$, **matrice d'application linéaire** $M_{\alpha\beta}(f)$.
- **Bases duales** (théo 3) et corollaire ; **isomorphisme canonique**.
- **Formes bilinéaires** (théo 4), transposée ${}^tP$.
- **Abréviations d'auteur** : notations $M_{\alpha\beta}$, $P_{\alpha}^{\alpha'}$ conservées telles quelles.
