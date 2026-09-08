# Applications linéaires continues (caractérisation par la sphère unité) — transcription fidèle

> 🧾 **Manuscrit original :** `applis-lineaires-continues.pdf` (scan, 3 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à ~95 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`applis-lineaires-continues.pdf`](applis-lineaires-continues.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Théo : Soit $(E, \lVert\cdot\rVert)$ un ev normé et $u \in \mathcal{L}(E)$. $u$ est continue $\iff F = \{x \in E \mid \lVert u(x)\rVert = 1\}$ est fermé.

$\Rightarrow$ / Posons $\forall x \in E$, $f(x) = \lVert u(x)\rVert$. Vu que $\{1\}$ est un fermé de $(\mathbb{R}, |\cdot|)$ il suffit de mtq $f$ est continue et ainsi $F = f^{-1}(\{1\})$ sera fermé.

Soit $x_0 \in E$. Soit $\varepsilon > 0$. Cherchons $\eta > 0 \mid \forall x \in E$, $\lVert x - x_0\rVert < \eta \Rightarrow |f(x) - f(x_0)| < \varepsilon$.

Soit $x \in E$. On a : $|f(x) - f(x_0)| = \big|\lVert u(x)\rVert - \lVert u(x_0)\rVert\big| \leq \lVert u(x) - u(x_0)\rVert$.

Or ce $u$ est continue, $\exists \eta' > 0 \mid \forall y \in E$, $\lVert y - x_0\rVert < \eta' \Rightarrow \lVert u(y) - u(x_0)\rVert < \varepsilon$.

Pour $x \in E \mid \lVert x - x_0\rVert < \eta'$ on a $|f(x) - f(x_0)| < \varepsilon$. Prendre alors $\eta = \eta'$. Ainsi $f$ est continue en $x_0$, cqfd.

Rq : on pouvait plus simplement justifier la continuité de $f$, ce composée de fts continues, vu que $\lVert\cdot\rVert$ est une application continue sur $(E, \lVert\cdot\rVert)$ (au vu de l'inégalité de Minkowski).

## Page 2

$\Leftarrow$ / Mtq $u$ est continue.

Soit $(x_n) \in E^{\mathbb{N}} \to x \in E$. Il suffit de mtq $u(x_n) \to u(x) \iff u(x_n) - u(x) \to 0_E \iff u(x_n - x) \to 0_E$.

Ceci équivaut à montrer que pour tout $(x_n) \in E^{\mathbb{N}} \to 0_E$, on a $u(x_n) \to 0_E \iff \lVert u(x_n)\rVert \to 0$.

Soit donc $(x_n)_{n \in \mathbb{N}} \in E^{\mathbb{N}} \to 0_E$ [flèche vers $0_E$ peu lisible]. Supposons par l'absurde que $\lVert u(x_n)\rVert \not\to 0 \Rightarrow \exists$ une sous suite $(x_{\varphi(n)})$ et $\exists c > 0 \mid \forall n \in \mathbb{N}$, $\lVert u(x_{\varphi(n)})\rVert > c$.

Considérons alors la suite $(y_n) = \left(\frac{x_{\varphi(n)}}{\lVert u(x_{\varphi(n)})\rVert}\right) \in F$ vu que $\forall n \in \mathbb{N}$, $\lVert u(y_n)\rVert = 1$.

Or $(x_{\varphi(n)}) \to 0_E$ et $0 < \frac{1}{\lVert u(x_{\varphi(n)})\rVert} < \frac{1}{c}$ $\forall n \in \mathbb{N}$ d'où $y_n = \frac{x_{\varphi(n)}}{\lVert u(x_{\varphi(n)})\rVert} \underset{n \to +\infty}{\longrightarrow} 0_E \Rightarrow 0_E \in F$ car $F$ est fermé ce qui est absurde vu que $\lVert u(0_E)\rVert = 0 \neq 1$.

Donc $\lVert u(x_n)\rVert \to 0 \iff u(x_n) \to 0_E$. Et au vu de ce qui précède $u$ est continue.

## Page 3

[La page 3 reprend quasi mot à mot la démonstration de la page 2 (même sens $\Leftarrow$, mêmes notations), avec en plus la remarque finale ci-dessous. Seules les différences sont signalées.]

$\Leftarrow$ / Mtq $u$ est continue.

Soit $(x_n) \in E^{\mathbb{N}} \to x \in E$. Il suffit de mtq $u(x_n) \to u(x) \iff u(x_n) - u(x) \to 0_E \iff u(x_n - x) \to 0_E$.

Ceci équivaut à montrer que pour tout $(x_n) \in E^{\mathbb{N}} \to 0_E$, on a $u(x_n) \to 0_E \iff \lVert u(x_n)\rVert \to 0$.

Soit donc $(x_n)_{n \in \mathbb{N}} \in E^{\mathbb{N}}$. Supposons par l'absurde que $\lVert u(x_n)\rVert \not\to 0 \Rightarrow \exists$ une sous suite $(x_{\varphi(n)})$ et $\exists c > 0 \mid \forall n \in \mathbb{N}$, $\lVert u(x_{\varphi(n)})\rVert > c$.

Considérons alors la suite $(y_n) = \left(\frac{x_{\varphi(n)}}{\lVert u(x_{\varphi(n)})\rVert}\right) \in F$ vu que $\forall n \in \mathbb{N}$, $\lVert u(y_n)\rVert = 1$.

Or $(x_{\varphi(n)}) \to 0_E$ et $0 < \frac{1}{\lVert u(x_{\varphi(n)})\rVert} < \frac{1}{c}$ $\forall n \in \mathbb{N}$ d'où $y_n = \frac{x_{\varphi(n)}}{\lVert u(x_{\varphi(n)})\rVert} \underset{n \to +\infty}{\longrightarrow} 0_E \Rightarrow 0_E \in F$ car $F$ est fermé ce qui est absurde vu que $\lVert u(0_E)\rVert = 0 \neq 1$.

Donc $\lVert u(x_n)\rVert \to 0 \iff u(x_n) \to 0_E$. Et au vu de ce qui précède $u$ est continue.

Rq : ce résultat reste valable pour $u \in \mathcal{L}(E, F)$ et $F = \{x \in E, \lVert u(x)\rVert_F = 1\}$.

---

## Figures

- Aucune figure pp. 1–3 relues (p. 2–3 : même démonstration $\Leftarrow$, texte seul, sans schéma).

## Vocabulaire

ev normé, $\mathcal{L}(E)$, continuité, fermé, image réciproque $f^{-1}(\{1\})$, inégalité de Minkowski, suites $(x_n)$, sous-suite $(x_{\varphi(n)})$, $0_E$, $mtq$ (= montrer que), $cqfd$.
