# Carnet démos utiles — transcription fidèle

> 🧾 **Manuscrit original :** `carnet-demos-utiles.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** quatre démos manuscrites enchaînées ; calculs de cubes en `[lecture incertaine — …]`, ratures conservées. Transcrit mot à mot.
> 📄 **Source scannée :** [carnet-demos-utiles.pdf](carnet-demos-utiles.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

$\forall n \in \mathbb{N}$, Mtq que P : « $2n+1$ carré parfait » $\implies$ Q : « $(n+1)$ somme de 2 carrés parfaits ».

Supposons que P soit vraie. On a : [raturé : soit … P vraie] $\implies \exists a \in \mathbb{N} \mid 2n+1 = a^2 \implies \begin{cases} a \text{ impair} \\ a \text{ pair} \end{cases}$ [raturé : vs $2n+1$ impair]

$$\implies \begin{cases} a = 2k+1 \\ a = 2k' \end{cases} k, k' \in \mathbb{N}$$
$$\implies \begin{cases} a^2 = 2(2k^2+k)+1 \\ a^2 = 2(2k'^2) \end{cases} \text{(Absurde car } a^2 = 2n+1 \text{ est impair et non pair)}$$
$$\implies 2(2k^2+2k)+1 = 2n+1$$
$$\implies 2(k^2+k) = n$$ [lecture incertaine — indices $k$/$k'$]
$$\implies n+1 = 2k^2+2k'+1$$ [lecture incertaine — mélange $k$, $k'$]
$$\implies n+1 = k^2 + k^2+2k'+1$$ [lecture incertaine]
$$\implies n+1 = k^2 + (k+1)^2$$ [lecture incertaine — le scan porte « $n+n = k^2 + (k+1)^2$ »]
$$\implies Q.$$

2q $\forall m \in \mathbb{R}_+^*,\ |\sqrt{m+1} - \sqrt{m}| \leq \frac{1}{2\sqrt{m}}$ [lecture incertaine — le scan porte « $\forall x \in \mathbb{R}_+^*$ » avec $m$ dans la formule].

Cherchons les $x \in \mathbb{R}_+^* \mid |\sqrt{m+1} - \sqrt{m}| \leq \frac{1}{2\sqrt{m}}$ (I).

$(I) \iff -\frac{1}{2\sqrt{m}} \leq \sqrt{m+1} - \sqrt{m} \leq \frac{1}{2\sqrt{m}}$

$\iff -\frac{\sqrt{m+1}+\sqrt{m}}{2\sqrt{m}} \leq (m+1)-m \leq \frac{\sqrt{m+1}+\sqrt{m}}{2\sqrt{m}}$ [lecture incertaine — numérateurs]

$\iff -\frac{\sqrt{m+1}+\sqrt{m}}{2\sqrt{m}} \leq 1$ et $1 \leq \frac{\sqrt{m+1}+\sqrt{m}}{2\sqrt{m}}$

$\iff \sqrt{m+1} + 2\sqrt{m} + \sqrt{m} \geq 0$ et $\sqrt{m+1} + \sqrt{m} - 2\sqrt{m} \geq 0$ [lecture incertaine — reconstitution des inégalités] (toujours vraie)

$\iff \sqrt{m+1} - \sqrt{m} \geq 0$

$\iff \sqrt{m+1} \geq \sqrt{m}$

$\iff 1 \geq 0$ (toujours vraie)

$\iff x \in \mathbb{R}_+^*$ [lecture incertaine — conclusion notée « $x \in \mathbb{R}_+^*$ »].

Donc $|\sqrt{m+1} - \sqrt{m}| \leq \frac{1}{2\sqrt{m}} \iff m \in \mathbb{R}_+^*$. Alors $\forall m \in \mathbb{R}_+^*,\ |\sqrt{m+1} - \sqrt{m}| \leq \frac{1}{2\sqrt{m}}$.

## Page 2

* Mtq $\sqrt{101} - \sqrt{99} > \frac{1}{10}$.

Cherchons la valeur de vérité de P : « $\sqrt{101} - \sqrt{99} > \frac{1}{10}$ ».

P $\iff 2 > \frac{\sqrt{101}+\sqrt{99}}{10}$

$\iff 20 > \sqrt{101}+\sqrt{99}$

$\iff 400 > 101+99+2\sqrt{9999}$ [lecture incertaine — le scan porte « $2\sqrt{9999}$ », produit $101 \times 99 = 9999$]

$\iff \sqrt{9999} < 100$

$\iff 9999 < 10000$ (toujours vraie).

Donc P est vraie, d'où $\sqrt{101} - \sqrt{99} > \frac{1}{10}$.

* Soit $x \in \mathbb{R} \mid \sqrt{\tan x} + \frac{1}{\sqrt{\tan x}} = 3$ (E). Cherchons $a = \tan x + \frac{1}{\tan x}$.

(E) existe $\iff \begin{cases} x \in \mathbb{R} \mid \exists \tan x,\ k \in \mathbb{Z} \\ \tan x > 0 \end{cases}$

$\iff \begin{cases} x \in ]k\pi, k\pi+\frac{\pi}{2}[,\ k \in \mathbb{Z} \\ x \text{ appartient à la réunion des intervalles de la forme } ]k\pi, k\pi+\frac{\pi}{2}[,\ k \in \mathbb{Z} \end{cases}$ [raturé : fragments « de la forme », « $]k\pi$ » répétés]

$\iff x \in \bigcup_{k \in \mathbb{Z}} ]k\pi, k\pi+\frac{\pi}{2}[$.

Ainsi $\forall x \in \bigcup_{k \in \mathbb{Z}} ]k\pi, k\pi+\frac{\pi}{2}[$, (E) $\implies \tan x + \frac{1}{\tan x} + 2 = 9$ (car …)

$\implies \tan^3 x + 3\tan x + \frac{3}{\tan x} + \frac{1}{\tan^3 x} = 7^3$ [lecture incertaine — le scan omet les cubes sur « $\tan x$ » et « $1/\tan x$ » dans l'égalité intermédiaire, $7^3$ entouré]

$\implies a + 3\left(\tan x + \frac{1}{\tan x}\right) = 343$ [lecture incertaine — $a = \tan^3 x + 1/\tan^3 x$]

$\implies a = 343 - 3 \times (9-2)$ [lecture incertaine — le scan porte « $343 - 3 \times (9-2)$ », soit $7 = 9-2$].

Donc $\forall x \in \bigcup_{k \in \mathbb{Z}} ]k\pi, k\pi+\frac{\pi}{2}[$, [raturé] $a = \tan^3 x + \frac{1}{\tan^3 x} = 322$ [lecture incertaine — cubes omis sur le scan, valeur $322 = 343 - 21$].

---

## Figures

Aucune figure sur la source (2 pages de texte manuscrit seul, sans schéma) — rien à reproduire en code.

## Vocabulaire

- **Carré parfait** : entier carré d'un entier ($2n+1 = a^2$).
- **Valeur absolue** : $|\sqrt{m+1} - \sqrt{m}|$ majorée par $\frac{1}{2\sqrt{m}}$.
- **Conjugué (quantité)** : $(\sqrt{101}-\sqrt{99})(\sqrt{101}+\sqrt{99}) = 2$.
- **Tangente** : $\tan x$ avec condition d'existence $\tan x > 0$.
