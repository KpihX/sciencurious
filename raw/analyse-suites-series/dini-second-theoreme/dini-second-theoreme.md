# Second théorème de Dini — transcription fidèle

> 🧾 **Manuscrit original :** `dini-second-theoreme.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** rédaction guidée (questions « ? », « ! », « • ») à l'encre bleue, écriture rapide et calculs compacts en `[lecture incertaine — …]` ; coin inférieur droit de la page 2 rogné ; accolade marginale décrite en place ; aucun schéma mathématique à reproduire. Transcrit mot à mot.
> 📄 **Source scannée :** [dini-second-theoreme.pdf](dini-second-theoreme.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

2ᵉ thm de Dini : soit $(f_n)_{n \in \mathbb{N}} \xrightarrow{CS} f$. Si $f$ continue et $\forall n \in \mathbb{N}$, $f_n \nearrow$ alors $(f_n) \xrightarrow{CU} f$ ($\forall n \in \mathbb{N}$, $f_n$ et $f$ sont définies sur $I = [a, b]$).

Soit $\varepsilon > 0$. Cherchons $N_x \in \mathbb{N}$ / $\forall n \in \mathbb{N},\ n \ge N_x \implies \sup_I |g_n| \le \varepsilon$ [lecture incertaine — le manuscrit porte « $\sup_I |g_n(x_0)|$ »] (où $\forall n \in \mathbb{N}$, $g_n = f_n - f$).

? : l'idée ici est de trouver un rang à partir duquel $\varepsilon$ est un majorant de $\{|g_n(x)|,\ x \in I\}$.

• Soit alors $x \in I$.

! : Pour bien exploiter la croissance des $(f_n)$ et de $f$ (car limite de $f_n$ croissantes), il serait utile de mettre $x$ dans un intervalle $[\alpha_x, \beta_x] \subset I$ ce qui est tjs possible. Ainsi on aurait en exploitant cette croissance,

— $g_n(x) = f_n(x) - f(x) \le f_n(\beta_x) - f(\alpha_x)$ [lecture incertaine — « $x$ » ou « $x_0$ » dans le manuscrit]

— $g_n(x) \ge f_n(\alpha_x) - f(\beta_x)$ [lecture incertaine — « $x$ » ou « $x_0$ » dans le manuscrit].

! : et pour exploiter la CS il serait utile de fabriquer les termes $f_n(\beta_x) - f(\beta_x)$ et $f_n(\alpha_x) - f(\alpha_x)$ pour pouvoir l'utiliser — [raturé : « l'utiliser »] appliquer (CS) à $\alpha_x$ et $\beta_x$.

Ainsi — $g_n(x) \le f_n(\beta_x) - f(\beta_x) + f(\beta_x) - f(\alpha_x)$ [lecture incertaine — « $x$ » ou « $x_0$ » dans le manuscrit]

— $g_n(x) \ge f_n(\alpha_x) - f(\alpha_x) + f(\alpha_x) - f(\beta_x)$ [lecture incertaine — « $x$ » ou « $x_0$ » dans le manuscrit].

• La CS en $\alpha_x$ et $\beta_x$ nous garantirait ainsi l'existence d'un $N_1^x$ / $\forall n \in \mathbb{N},\ n \ge N_1^x \implies |f_n(\beta_x) - f(\beta_x)| < \frac{\varepsilon}{2}$ et de $N_2$ / $\forall n \in \mathbb{N}$,

## Page 2

$n \ge N_2 \implies |f_n(\alpha_x) - f(\alpha_x)| < \frac{\varepsilon}{2}$.

Pour $n \ge N = \max\{N_1, N_2\}$, on aurait ainsi $-\frac{\varepsilon}{2} - (f(\beta_x) - f(\alpha_x)) < g_n(x_0) < \frac{\varepsilon}{2} + (f(\beta_x) - f(\alpha_x))$ [lecture incertaine — « $x$ » ou « $x_0$ » dans le manuscrit].

! : Il ne reste plus qu'alors à chercher les réels $\alpha_x$ et $\beta_x$ tels que $f(\beta_x) - f(\alpha_x) < \frac{\varepsilon}{2}$ et il suffirait alors de prendre $N_x = N$.

On peut ainsi songer à un partitionnement de $[f(a), f(b)]$, une subdivision en $K$ intervalles de longueur inférieure à $\frac{\varepsilon}{2}$ [lecture incertaine — « en $K$ intervalles »]. (Accolade manuscrite en marge reliant « $f(b)$ » à « $f(a)$ ».)

On doit ainsi avoir $\frac{f(b) - f(a)}{K} < \frac{\varepsilon}{2}$.

Soit alors $K = E\left(\frac{f(b) - f(a)}{\varepsilon} \times 2\right) + 1 > \frac{f(b) - f(a)}{\varepsilon/2}$. Considérons la subdivision de $[f(a), f(b)]$ : $y_0 = f(a)$, $\forall i \in [\![0, K[\![,\ y_i = f(a) + i\frac{f(b) - f(a)}{K}$ [lecture incertaine — formule des $y_i$] (avec $y_K = f(b)$). Car $f$ continue d'après le thm des valeurs intermédiaires, $\forall i \in [\![0, K[\![,\ \exists\, x_i \in [a, b]$ / $f(x_i) = y_i$ (avec $x_i \le x_{i+1}\ \forall i \in [\![0, K[\![$ [lecture incertaine — croissance des $x_i$]). Il est clair que $x_0, \ldots, x_K$ forment une subdivision de $[a, b]$.

Par conséquent $\exists\, i \in [\![0, K[\![$ / $x \in [x_i, x_{i+1}]$. Comme $f(x_{i+1}) - f(x_i) = \frac{f(b) - f(a)}{K} < \frac{\varepsilon}{2}$, il suffit donc de prendre $\alpha_x = x_i$ et $\beta_x = x_{i+1}$ et on a bien $\forall n \ge N$, $-\frac{\varepsilon}{2} - \frac{\varepsilon}{2} < g_n(x_0) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} \implies |g_n(x_0)| < \varepsilon$ [lecture incertaine — « $x$ » ou « $x_0$ » dans le manuscrit] ($\forall n \ge$ [coin inférieur droit rogné]) $\implies \sup_I |g_n| \le \varepsilon$. Prendre [coin inférieur droit rogné — fin de ligne coupée, « $N = \ldots$ »].

## Figures

Aucune figure : 2 pages de texte manuscrit seul, sans schéma mathématique (transcription § Statut : « aucun schéma mathématique à reproduire », accolade marginale décrite en place ; confirmé p. 1 sur source le 2026-09-07, rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07, rendu `/tmp/s10/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire.

## Vocabulaire

- CS : convergence simple ; CU : convergence uniforme ; $\nearrow$ : croissante ; tjs : toujours.
- $g_n = f_n - f$ ; $\alpha_x, \beta_x$ : encadrement local de $x$ ; $N_x, N_1^x, N_2$ : rangs associés.
- ? / ! / • : marques de rédaction guidée du manuscrit (question, idée, étape).
