# Euler-phi congruence (théorème d'Euler) — transcription fidèle

> 🧾 **Manuscrit original :** `euler-phi-congruence.pdf` (scan, 3 pages) · ✍️ KpihX
> 🔍 **Statut :** lisible à ~95 %, transcrit mot à mot. Les maths sont conservées telles quelles ;
> seules les coquilles d'orthographe évidentes sont corrigées (signalées). Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`euler-phi-congruence.pdf`](euler-phi-congruence.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Théo : Soient $a, b \in \mathbb{N}^* \times \mathbb{N}^*$ [lecture incertaine — probablement $(a, b) \in \mathbb{N}^* \times \mathbb{N}^*$] $/ a \wedge b = 1$. On a : $a^{\varphi(b)} \equiv 1[b]$

Rq : En regardant de plus près, ce théo se présente comme une généralisation du petit théo de Fermat.

$\exists! (p_i, \alpha_i)_{i=1}^n \in (\mathbb{P} \times \mathbb{N}^*)^n \mid b = \prod_{i=1}^n p_i^{\alpha_i}$ ($\mathbb{P}$ : ens des nbrs 1ers)

On a : $\varphi(b) = b\prod_{i=1}^n \left(1 - \frac{1}{p_i}\right) = \prod_{i=1}^n (p_i - 1) \times p_i^{\alpha_i - 1}$

Lemme 1 : (on va démontrer le théorème pour le cas particulier $n = 1$). Soit $(a, p, \alpha) \in \mathbb{N}^* \times \mathbb{N}^* \times \mathbb{P} \times \mathbb{N}^*$ [*sic* — lire $(a, p, \alpha) \in \mathbb{N}^* \times \mathbb{P} \times \mathbb{N}^*$]. On a : $a^{\varphi(p^\alpha)} = a^{(p-1) \times p^{\alpha-1}} \equiv 1[p^\alpha]$ si $a \wedge p = 1$

- pour $\alpha = 1$, d'après le corollaire direct du petit théo de Fermat dans la mesure où $a \wedge p = 1$, on a bien $a^{\varphi(p^1)} = a^{p-1} \equiv 1[p^1]$.
- Supposons que le lemme est vrai pour $\alpha - 1$ (avec $\alpha \in [\![2; +\infty[\![$) et mtq il est aussi vrai pour $\alpha$.

On a : $a^{(p-1) \times p^{\alpha-1}} - 1 = \left(a^{(p-1)p^{\alpha-2}}\right)^p - 1^p$

$$= \left(a^{(p-1)p^{\alpha-2}} - 1\right) \times C \text{ où } C = \sum_{k=0}^{p-1} a^{(p-1)p^{\alpha-2}k}$$

D'après l'hypothèse en amont, $p^{\alpha-1} \mid a^{(p-1) \times p^{\alpha-2}} - 1$. De plus $\forall k \in [\![0, p-1]\!]$ tqs d'après le corollaire direct du petit théo de Fermat, $a^{p-1} \equiv 1[p] \Rightarrow a^{(p-1)p^{\alpha-2}k} \equiv 1[p]$

## Page 2

d'où $C \equiv p[p] \equiv 0[p]$. Ainsi $p^{\alpha-1} = p \times p^{\alpha-2} \mid \left(a^{(p-1) \times p^{\alpha-2}} - 1\right)$ d'où $a^{\varphi(p^\alpha)} \equiv 1[p^\alpha]$ CQFD

Alors d'après le principe de la démonstration par récurrence, le lemme est vrai $\forall \alpha \in \mathbb{N}^*$.

En revenant au théo et en appliquant le lemme précédent, On a : $\forall i \in [\![1, n]\!]$, $a^{(p_i-1)p_i^{\alpha_i-1}} \equiv 1[p_i^{\alpha_i}] \Rightarrow a^{\varphi(b)}$ [le calcul intermédiaire du produit est peu lisible : $\prod_{j \neq i}(p_j-1)p_j^{\alpha_j-1}$ — lecture incertaine] $\Rightarrow p_i^{\alpha_i} \mid \left(a^{\varphi(b)} - 1\right)$

Lemme 2 : Soient $n \in \mathbb{N}^* \setminus \{1\}$, $(b, (a_i)_{i=1}^n) \in \mathbb{N}^* \times \mathbb{N}^{*n}$ [lecture incertaine] $/ \forall i, j \in [\![1, n]\!]$ $i \neq j \Rightarrow a_i \wedge a_j = 1$ et $\forall i \in [\![1, n]\!]$, $a_i \mid b$. On a : $\prod_{i=1}^n a_i \mid b$.

- pour $n = 2$, d'après le théo de Bézout, $\exists (u_i)_{i=1}^2 \in \mathbb{Z}^2 \mid \sum_{i=1}^2 u_i a_i = 1 \Rightarrow b = \sum_{i=1}^2 u_i a_i b$. Or $\forall i \in \{1, 2\}$, $a_i \mid b \Rightarrow \exists K_i \in \mathbb{Z}^* \mid b = a_i K_i$ ainsi $b = u_1 a_1 K_2 a_2 + u_2 a_2 K_1 a_1 = a_1 a_2(u_1 K_2 + u_2 K_1) = a_1 a_2 \parallel$ [fin coupée].
- Soit $n \in \mathbb{N}^* \setminus \{1, 2\}$. Supp que le lemme 2 est vrai pour $n-1$ et mtq il est vrai pour $n$. On a : $\prod_{i=1}^{n-1} a_i \mid b$ et $a_n \mid b$. Or comme $\forall i \in [\![1, n-1]\!]$, $a_i \wedge a_n$ [suite page 3]

## Page 3

alors $\left(\prod_{i=1}^{n-1} a_i\right) \wedge a_n = 1$ (En effet d'après le théo généralisé de Bézout $\exists (u_i)_{i=1}^n \in \mathbb{Z}^n \mid \sum_{i=1}^n u_i a_i = 1 \Rightarrow 1 \times \left(\sum_{i=1}^{n-1} u \cdots\right.$ [début peu lisible]. Soit $d \in D_+(a_n) \mid d \mid n$ [lecture incertaine — probablement $d \mid a_n$]. Si $d \mid \prod_{i=1}^{n-1} a_i$ alors en particulier $\exists$ un diviseur $1^{er}$ $p$ de $d$ qui divise un certain $a_i$ d'où $a_i \wedge a_n \geq p > 1$ ce qui est absurde ! Ainsi le seul diviseur positif commun à $\prod_{i=1}^{n-1} a_i$ et $a_n$ est $1$ d'où le résultat)

Vu que le lemme est vrai pour $n = 2$ alors $\prod_{i=1}^n a_i = \left(\prod_{i=1}^{n-1} a_i\right) \times a_n \mid b$. Ainsi d'après le principe d'induction, le lemme 2 est vrai.

En revenant au théo, vu que $\forall i, j \in [\![1, n]\!]$ ($i \neq j$) $p_i \wedge p_j = 1 \Rightarrow p_i^{\alpha_i} \wedge p_j^{\alpha_j} = 1$, en appliquant le lemme 2, on a : $b = \prod_{i=1}^n p_i^{\alpha_i} \mid \left(a^{\varphi(b)} - 1\right)$ d'où $a^{\varphi(b)} \equiv 1[b]$ CQFD

Rq : Vu $\exists! m \in \mathbb{N}^*$ t.q [lecture incertaine — probablement : $\forall n \in \mathbb{N}$, $a^n \equiv 1[b] \iff m \mid n$, i.e. $m$ l'ordre de $a$ modulo $b$] $/ a^n \equiv 1[b] \iff m \mid N$ alors $m \mid \varphi(b)$.

---

## Figures

Aucune figure à reproduire : pages 1–3 relues visuellement (relecture 2026-09-07, texte et formules, sans schéma).

## Vocabulaire / notions

- **Théorème d'Euler** : $a \wedge b = 1 \implies a^{\varphi(b)} \equiv 1[b]$.
- **Indicatrice** $\varphi(b) = b\prod_{i=1}^n (1 - 1/p_i)$ ; généralisation du petit théorème de Fermat.
- **Lemme 1** : cas $n = 1$, $a^{\varphi(p^{\alpha})} \equiv 1[p^{\alpha}]$ par récurrence sur $\alpha$.
- **Lemme 2** : diviseurs deux à deux premiers entre eux, $\prod a_i \mid b$ (Bézout).
- **Ordre** $m$ de $a$ modulo $b$ : $a^n \equiv 1[b] \iff m \mid n$.
