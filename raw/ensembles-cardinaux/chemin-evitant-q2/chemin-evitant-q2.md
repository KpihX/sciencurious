# Chemin évitant Q² — transcription fidèle

> 🧾 **Manuscrit original :** `chemin-evitant-q2.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** chemin brisé $[O,B] \cup [B,A]$ dans le carré $D$ ; une figure reproduite (script + PNG + description), signes et bornes peu lisibles en `[lecture incertaine — …]`. Transcrit mot à mot.
> 📄 **Source scannée :** [chemin-evitant-q2.pdf](chemin-evitant-q2.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Soit $\mathcal{D} = \{M = (x,y) \in \mathbb{R}^2 \mid 0 \leq x, y \leq 1\}$ (scan p.1 confirmé : « $0 \leq x, y \leq 1$ »). Cherchons un chemin continu $\mathcal{C} \subseteq \mathcal{D}$ permettant de quitter $O = (0,0)$ pour aller à $A = (1,1)$ avec la contrainte de ne passer par aucun point dont les 2 coordonnées sont rationnelles ; ainsi $\mathcal{C} \subseteq \mathcal{D} \setminus \mathbb{Q}^2 = \{M = (x,y) \ldots \mid (x,y) \notin \mathbb{Q}^2\}$, c'est-à-dire $(x \text{ ou } y) \in \complement_{\mathbb{R}}\mathbb{Q}$ (scan confirmé : « $(x \text{ ou } y) \in C_{\mathbb{R}}\mathbb{Q}$ », $C$ manuscrit du complémentaire).

Figure : le carré $\mathcal{D}$ avec $O$ en bas à gauche, $A$ en haut à droite, un point $B$ intérieur ; segments $[O,B]$ et $[B,A]$ ; une droite d'essai $(\Delta) \ni O$ ($y = ax$) barrant le carré vers le côté droit [correction 2026-09-07, p.1 re-rendue à $r = 150$ et relue : $(\Delta)$ n'est PAS la diagonale $[O,A]$ — c'est la droite d'essai $y = ax$ par $O$ ; aucune diagonale tracée sur le source].

![Carré D et chemin brisé [O,B]∪[B,A] — reproduction via lab/scripts/reproduce_chemin_evitant_q2_1.py](assets/chemin-ob-ba.png)

[Reproduction `lab/scripts/reproduce_chemin_evitant_q2_1.py` : carré bleu, chemin $[O,B] \cup [B,A]$ bleu, $B = (1/\sqrt{2}, 1-1/\sqrt{2})$, étiquettes rouges. La droite d'essai $(\Delta)$ n'est pas reproduite (pente $a$ non fixée) ; aucune diagonale sur le source.]

On va chercher $(\mathcal{C})$ de la forme d'un ou plusieurs segments pour faire simple. Considérons une droite $(\Delta) \subseteq \mathbb{R}^2$ et le segment $[S] = (\Delta) \cap \mathcal{D}$ [raturé : « 1st avec »] avec $O \in (\Delta)$. $\exists a \in \mathbb{R}_+ \mid \forall M = (x,y) \in ([S]),\ y = ax\ (0 \leq x \leq 1)$ (scan confirmé). On aimerait que $(x,y) \notin \mathbb{Q}^2$, $\forall (x,y) \in [S]$. Pour cela il serait intéressant d'avoir $a \in \bar{\mathbb{Q}}$ (irrationnel) et dans la grande majorité des cas $x \in [0,1]$ on aurait $y = ax \in \bar{\mathbb{Q}}$, sauf quelques rares cas car $a = x = 1/\sqrt{2} \implies y = 1/2 \notin \bar{\mathbb{Q}}$ (scan confirmé : l'exemple donne bien $y = 1/2$, rationnel donc hors de $\bar{\mathbb{Q}}$). En s'inspirant de cela, considérons $B = \left(\frac{1}{\sqrt{2}}, 1-\frac{1}{\sqrt{2}}\right) \in \mathcal{D}$ et le segment $[OB] = \left\{M = (x,y) \in \mathbb{R}^2 \mid 0 \leq x \leq \frac{1}{\sqrt{2}} \text{ et } y = \frac{1-\frac{1}{\sqrt{2}}}{\frac{1}{\sqrt{2}}}x = (\sqrt{2}-1)x\right\}$ (pente $\sqrt{2}-1 > 0$ confirmée par le calcul).

## Page 2

Justifions que $\forall M = (x,y) \in [O,B],\ (x,y) \notin \mathbb{Q}^2$. En effet en supposant par l'absurde $\exists M = (x,y) \in [O,B] \mid (x,y) \in \mathbb{Q}^2$ alors on a : $y = (\sqrt{2}-1)x \implies \sqrt{2} = \frac{y}{x}+1$ (car $x \neq 0$). Car $y, x \in \mathbb{Q}$ alors $\sqrt{2} = \frac{y}{x}+1 \in \mathbb{Q}$. Absurde ! d'où le résultat.

• Considérons $[BA] = \{M = (x,y) \in \mathbb{R}^2 \mid \frac{1}{\sqrt{2}} \leq x \leq 1$ (scan p.2 confirmé : borne basse $1/\sqrt{2}$, borne haute $1$ ; la preuve ci-dessous travaille sur $[BA[$, $A$ exclu car $x \neq 1$) et $M \in (BA)\}$. Car $(BA)$ est une droite, $\exists (a,b) \in \mathbb{R}^2 \mid \forall M = (x,y) \in (BA),\ y = ax+b$. On a : $a = \frac{y_A-y_B}{x_A-x_B} = \frac{1-(1-\frac{1}{\sqrt{2}})}{1-\frac{1}{\sqrt{2}}} = \frac{1}{\sqrt{2}-1} = \sqrt{2}+1$ (scan confirmé : le calcul donne bien $a = \sqrt{2}+1$). Car $A \in (BA)$, on a : $1 = (\sqrt{2}+1) \times 1 + b \implies b = -\sqrt{2}$ (scan confirmé : signe $-$ devant $\sqrt{2}$, cohérent avec $1 - (\sqrt{2}+1) = -\sqrt{2}$). Ainsi $[BA] = \{M = (x,y) \in \mathbb{R}^2 \mid \frac{1}{\sqrt{2}} \leq x \leq 1 \text{ et } y = (\sqrt{2}+1)x - \sqrt{2}\}$.

Justifions que $\forall M = (x,y) \in [BA[,\ (x,y) \notin \mathbb{Q}^2$. Supposons par l'absurde $\exists M = (x,y) \in [BA[ \mid (x,y) \in \mathbb{Q}^2$ alors on a : $y = (\sqrt{2}+1)x - \sqrt{2} = \sqrt{2}(x-1)+x \implies \sqrt{2} = \frac{y-x}{x-1}$ (car $x \neq 1$). Car $x, y \in \mathbb{Q}$, $\sqrt{2} = \frac{y-x}{x-1} \in \mathbb{Q}$. Absurde ! d'où le résultat.

En définitive il suffit de prendre $(\mathcal{C}) = [OB] \cup [B,A]$ car dans ce cas $(\mathcal{C})$ est continue, va de $O$ à $A$ et n'a pas de point à coordonnées toutes rationnelles.

> 🔎 **Relecture :** p.1–2 re-rendues (`pdftoppm -png -r 150 -f 1 -l 2`), signes et bornes confirmés ($a = \sqrt{2}+1$, $b = -\sqrt{2}$, $y = (\sqrt{2}-1)x$ sur $[OB]$) ; chaque crochet levé/confirmé ci-dessus ; figure `assets/chemin-ob-ba.png` : carré, $O$ bas-gauche, $A$ haut-droite, $B$ intérieur, chemin bleu (sans diagonale — le source n'en trace aucune). 2e passage 2026-09-07 (rendu `/tmp/s9/chemin-2.png`, r150) : p.2 confirmée — $\sqrt{2} = y/x+1$ ($x \neq 0$), $\sqrt{2} = (y-x)/(x-1)$ ($x \neq 1$), $(C) = [OB] \cup [B,A]$ ; aucune figure p.2 ; script re-vérifié `uv run`.

---

## Figures

- **Figure p.1** — carré $\mathcal{D}$, point $B$ intérieur, chemin $[O,B] \cup [B,A]$ : `assets/chemin-ob-ba.png` (reproduction via `lab/scripts/reproduce_chemin_evitant_q2_1.py`, vérifié `uv run` 2026-09-07 ; grille `#9db3d8`, `tick_params` sans étiquettes, jamais `axis("off")`). La droite $(\Delta)$ n'est pas reproduite (pente non fixée).

## Vocabulaire

- **$\mathcal{D} \setminus \mathbb{Q}^2$** : carré privé des points à deux coordonnées rationnelles.
- **$\bar{\mathbb{Q}}$** : irrationnels (manuscrit : $a \in \bar{\mathbb{Q}}$).
- **Chemin $(\mathcal{C}) = [OB] \cup [B,A]$** : continu, de $O$ à $A$, sans point de $\mathbb{Q}^2$.
