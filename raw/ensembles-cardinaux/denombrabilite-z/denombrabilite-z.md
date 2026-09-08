# Dénombrabilité de Z — transcription fidèle

> 🧾 **Manuscrit original :** `denombrabilite-z.pdf` (dactylographié, 3 pages : 1 page de démonstration + 2 pages blanches) · ✍️ KpihX
> 🔍 **Statut :** démonstration de la dénombrabilité de $\mathbb{Z}$ par la bijection $n \mapsto m$ (pairs/impairs) ; sans figure. Transcrit mot à mot.
> 📄 **Source scannée :** [denombrabilite-z.pdf](denombrabilite-z.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

**Dénombrabilité de $\mathbb{Z}$**

Dire que $\mathbb{Z}$ est dénombrable, revient à trouver un procédé de numérotation des éléments de $\mathbb{Z}$ avec ceux de $\mathbb{N}$, comme celui ci-dessous :

$...; -3; -2; -1; 0; 1; 2; 3; ...$

$...; 6 ; 4 ; 2 ; 0; 1; 3; 5; ...$

On numérote ainsi les éléments de $\mathbb{Z}$ en disposant de droite à gauche ceux de $\mathbb{N}$, dans l'ordre croissant ; en poursuivant ainsi ce procédé à l'infini, on se rend alors compte intuitivement, que chaque élément de $\mathbb{Z}$ correspond de façon unique à un élément de $\mathbb{N}$ et vice versa.

De façon plus rigoureuse cette relation entre $\mathbb{Z}$ et $\mathbb{N}$, correspond à la fonction :

$f : \mathbb{Z} \to \mathbb{N}$

$n \mapsto m = f(n) = \begin{cases} 2n-1 & \text{si } n > 0 \\ -2n & \text{si } n \le 0 \end{cases}$

**Démontrons que f est bijective**

\* D'après la définition de f, tout élément $n \in \mathbb{Z}$ admet toujours une unique image $m \in \mathbb{N}$ ;

Donc f est une application.

\*De plus, pour tout $m \in \mathbb{N}$, cherchons $n \in \mathbb{Z}$ tel que $f(n) = m$.

-Si $m = 2k$, $k \in \mathbb{N}$, $f(n) = m \iff -2n = m$ (avec $n \le 0$) ou $2n-1 = m$ (avec $n > 0$)

(Absurde, car m est pair)

$\iff n = -m/2 = -k$ (avec $n \le 0$)

Or $-k \le 0$, ainsi n existe de façon unique et vaut $-k$.

-Si $m = 2k+1$, $k \in \mathbb{N}$, $f(n) = m \iff 2n-1 = m$ (avec $n > 0$) ou $-2n = m$ (avec $n \le 0$)

(Absurde, car m est impair)

$\iff n = (m+1)/2 = k+1$ (avec $n > 0$)

Or $k+1 > 0$, ainsi n existe de façon unique et vaut $k+1$.

Donc pour tout $m \in \mathbb{N}$, il existe un unique $n \in \mathbb{Z}$ tel que $f(n) = m$.

Par conséquent f est bijective.

\* En conclusion, comme il existe une correspondance bijective entre $\mathbb{Z}$ et $\mathbb{N}$ (la fonction f en amont), alors $\mathbb{Z}$ est dénombrable.

## Page 2

[Page blanche.]

## Page 3

[Page blanche.]

---

## Figures

Aucune figure : texte seul (tapuscrit WPS Office scanné, p.1 ; p.2–3 blanches vérifiées par tailles JPEG embarquées `20,5K` vs `427K`, sans lecture visuelle). Note : les puces « $*$ » du source devant $2n-1$ / $-2n$ sont rendues ci-dessus en cas accolés.

> 🗑️ **Doublon éliminé (2026-09-07) :** `../denombrabilite-z-fili/denombrabilite-z-fili.pdf` — md5 identique (`ad720d7e0b34c5e423198e5b7f0c0613`), rendu p.1 pixel-identique (`/tmp/mdt/D-z-1.png` = `/tmp/mdt/D-zfili-1.png`). Dossier `denombrabilite-z-fili/` supprimé, ce dossier est conservé.

## Vocabulaire

- **Dénombrable** : en bijection avec $\mathbb{N}$ (ici $f : \mathbb{Z} \to \mathbb{N}$, pairs/impairs).
- **Application / injective / surjective / bijective** : sens usuel, démontré par cas $m = 2k$ / $m = 2k+1$.
