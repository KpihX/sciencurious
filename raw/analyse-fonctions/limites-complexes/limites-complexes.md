# Limites complexes (module, argument, suites) — transcription fidèle

> 🧾 **Manuscrit original :** `limites-complexes.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible (~90 %), transcrit fidèlement. Inégalité triangulaire, convergence des parties réelle/imaginaire, du module, puis de l'argument (via $\cos$ et $\sin$) et équivalence finale. Un lapsus de signe et une lettre ambiguë (signalés).
> 📄 **Source scannée :** [`limites-complexes.pdf`](limites-complexes.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Inégalité triangulaire et convergence $z_n \to z$

Quelques propriétés sur les nombres complexes et les suites complexes [titre souligné]

Soit $a, b \in \mathbb{C}$.

. $|a+b| \leq |a|+|b|$

En effet, $|a+b|^2 = (a+b)(\bar a+\bar b) = |a|^2+|b|^2+ a\bar b + \bar a b = |a|^2+|b|^2+2\mathrm{Re}(a\bar b)$

$$\leq |a|^2+|b|^2+ 2|a\bar b| = |a|^2+|b|^2+ 2|a||b| = (|a|+|b|)^2$$

d'où $|a+b| \leq |a|-|b|$ [*sic* — on attend $|a|+|b|$ d'après le calcul qui précède]

. $\big||a|-|b|\big| \leq |a-b|$

En effet, $|a| \leq |a-b|+|b| \implies |a|-|b| \leq |a-b| \Big\} \implies \big||a|-|b|\big| \leq |a-b|$

de plus, $|b| \leq |b-a|+|a| \implies -|a-b| \leq |a|-|b| \Big\}$

Applications et + : Soit $(z_n = a_n+ib_n)_n$ une suite cplx,

$z = a+ib \in \mathbb{C}$.

. $(z_n)_{\mathbb{N}} \to z \iff a_n \to a$ et $b_n \to b$

En effet, $\forall n \in \mathbb{N}$, $|z_n-z| = \sqrt{(a_n-a)^2+(b_n-b)^2}$

Ainsi — si $(z_n)_n \to z$ alors $|a_n-a|$, $|b_n-b| \leq |z_n-z| \to 0$

d'où $a_n, b_n \to a, b$

— Réciproquement si $a_n, b_n \to a, b$, $|z_n-z| = \sqrt{(a_n-a)^2+(b_n-b)^2} \to 0$

d'où $z_n \to z$

. $(z_n)_{\mathbb{N}} \to z \implies (|z_n|)_{\mathbb{N}} \to |z|$

En effet, $\forall n \in \mathbb{N}$, $\big||z_n|-|z|\big| \leq |z_n-z| \xrightarrow[n\to+\infty]{} 0$ lorsque $(z_n) \to z$

d'où $(|z_n|)_{\mathbb{N}} \to |z|$

. Si $(z_n)_{\mathbb{N}} \to z \neq 0$, alors $(d_n = \mathrm{Arg}\, z_n)_{\mathbb{N}} \to d = \mathrm{Arg}\, z$ [la lettre est lue « $d$ » partout — probablement $\theta$]

En e[ffet] il suffit de m[ontrer que] $\cos d_n, \sin d_n \to \cos d, \sin d$ [ligne empâtée]

## Page 2 — Convergence de l'argument et équivalence

on traitera juste le cas de $(\cos d_n)_{\mathbb{N}}$ vu que celui de $(\sin d_n)_{\mathbb{N}}$ est très similaire

Or, [raturé — « a »] $\forall n \in \mathbb{N}$,

$$|\cos d_n - \cos d| = \left|\frac{a_n}{|z_n|} - \frac{a}{|z|}\right|$$

Car $(z_n) \to z \neq 0$ alors $(|z_n|) \to |z| \neq 0$ d'où $\exists N \in \mathbb{N}$, $\forall n \in \mathbb{N}$, $n > N \to |z_n| \neq 0$

Pour $n > N$, $|\cos d_n - \cos d| = \left|\frac{a_n}{|z_n|} - \frac{a}{|z|}\right|$

$$= \frac{|a_n|z|-a|z|+a|z|-a|z_n||}{|z||z_n|}$$

$$\leq \frac{|z||a_n-a|+|a|\big||z_n|-|z|\big|}{|z||z_n|} \to \frac{0+0}{|z|^2} = 0$$

ainsi $\cos d_n \to \cos d$ et on a de m[ême] $\sin d_n \to \sin d$

Rq : on aurait pu utiliser le résultat suivant : si $(a_n)$ et $(b_n)$ sont 2 suites cplx / $a_n \to a$, $b_n \to b \neq 0$ alors $\frac{a_n}{b_n} \to \frac{a}{b}$

. conclusion : si $|z_n| \to |z|$ et $d_n = \mathrm{Arg}\, z_n \to d = \mathrm{Arg}\, z$

alors $z_n \to z$

En effet $\lim_{n\to+\infty}|z_n-z| = \lim_{n\to+\infty}\big||z_n|e^{id_n}-z\big| = \big||z|e^{id}-z\big| = 0$

d'où $z_n \to z$

Donc $z_n \to z \neq 0 \iff \begin{cases} |z_n| \to |z| \\ d_n = \mathrm{Arg}\, z_n \to d = \mathrm{Arg}\, z \end{cases}$

---

## Figures

Aucune figure ni schéma sur les 2 pages (relues intégralement).

## Vocabulaire

- Arg = argument ($d_n \to d$, lu « d » partout, probablement $\theta$) ; Re = partie réelle ; cplx = complexe(s) ; Rq.

---

## 📝 Notes de transcription (fidélité)

- Page 1 : « d'où $|a+b| \leq |a|-|b|$ » est un lapsus manifeste (le calcul donne $(|a|+|b|)^2$) — conservé avec [*sic*].
- La lettre de l'argument ($d_n \to d$) est lue « d » ; il s'agit vraisemblablement de $\theta_n \to \theta$ — graphie conservée sans normalisation.
- Aucune figure ni schéma sur les 2 pages.
