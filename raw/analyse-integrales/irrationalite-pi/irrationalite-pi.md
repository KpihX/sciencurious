# Irrationalité de $\pi$ via $I_n = \frac{1}{n!}\int_0^\pi x^n(\pi-x)^n\sin x\,dx$ — transcription fidèle

> 🧾 **Manuscrit original :** `irrationalite-pi.pdf` (scan, 4 pages) · ✍️ KpihX · preuve type Niven en deux méthodes ($I_n \in \mathbb{Z}_n[\pi]$ par récurrence puis par exponentielle complexe), puis contradiction via $d_n = q^n I_n \in \mathbb{Z}$, $d_n \to 0$
> 🔍 **Statut :** lisible (~80 %), transcrit fidèlement. Calculs intermédiaires raturés ou elliptiques (signalés) ; la récurrence encadrée $I_n = (4n-2)I_{n-1} - \pi^2 I_{n-2}$ est correcte.
> 📄 **Source scannée :** [`irrationalite-pi.pdf`](irrationalite-pi.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1 — Récurrence : $I_n \in \mathbb{Z}_n[\pi]$ (méthode 1)

[encadré :] Irrationalité de $\pi$ : Étude de $I_n = \frac{1}{n!}\int_0^\pi x^n(\pi-x)^n \sin x\,dx$, $n \in \mathbb{N}$

I/ Mq [montrons que] $\forall n \in \mathbb{N}$, $I_n \in \mathbb{Z}_n[\pi]$

• Meth1 : Soit $n \in \mathbb{N}$ ($n \geqslant 2$)

$$I_n = \frac{1}{n!}\left(-\left[x^n(\pi-x)^n \cos x\right]_0^\pi + \int_0^\pi n(\pi-2x)(x(\pi-x))^{n-1} \cos x\,dx\right)$$

$$= \frac{1}{(n-2)!}\left(\left[(\pi-2x)(x(\pi-x))^{n-2} \sin x\right]_0^\pi \text{[terme biffé]} - \int_0^\pi \sin x\,dx\left(-2(x(\pi-x))^{n-2} + (\pi-2x)^2(nx)(x(\pi-x))^{n-2}\right)\right)$$

[(nx) : lecture incertaine — commission de dérivation, attendre $n(n-1)$]

$$= \frac{1}{(n-2)!}\left(2^{\text{[raturé : exposant } (n-2)! \text{ biffé]}} I_{n-2} + (n-2)\left(\pi^2 (n-2)! I_{n-2} - 4\pi \int_0^\pi \sin x \, x^{n-1}\frac{(\pi-x)^{n-1}}{(\pi-x)}\,dx \text{ [dénominateur } (\pi-x) \text{ raturé]} + 4 \int_0^\pi \sin x \, x^n (\pi-x)^{n-2}\,dx\right)\right)$$

$$= \frac{1}{(n-2)!}\left(2(n-2)! I_{n-2} - (n-1)! \pi^2 I_{n-1} + 4(n-2)\left(\int_0^\pi \sin x \, x^{n-1}(\pi-x)^{n-1}(\pi-x)\,dx\right.\right.$$

[fin de ligne hors champ — la ligne suivante identifie cette intégrale à $(n-2)!I_{n-2}$]

$$= \frac{1}{(n-2)!}\left(2(n-2)! I_{n-2} - (n-1)! \pi^2 I_{n-1} + 4(n-2)(n-2)! I_{n-2}\right)$$

[encadré :] d'où $I_n = (4n-2)I_{n-1} - \pi^2 I_{n-2}$

Ainsi en raisonnant par récurrence on a :

$I_0 = 2 \in \mathbb{Z}_0[\pi]$, $I_1 = 4 \in \mathbb{Z}_1[\pi]$ [raturé : gribouillis après $I_1$]

Si pour $n \in \mathbb{N}$ ($n \geqslant 2$), $(I_{n-2}, I_{n-1}) \in \mathbb{Z}_{n-2}[\pi] \times \mathbb{Z}_n[\pi]$ [lecture incertaine — le second facteur pourrait être $\mathbb{Z}_{n-1}[\pi]$], alors $((4n-2)I_{n-2}, -\pi^2 I_{n-1}) \in \mathbb{Z}_{n-2}[\pi] \times \mathbb{Z}_n[\pi] \subset \mathbb{Z}_n[\pi]^2$ [*sic* — indices échangés par rapport à la récurrence encadrée : il faudrait $((4n-2)I_{n-1}, -\pi^2 I_{n-2})$], d'où $I_n \in \mathbb{Z}_n[\pi]$ car $\mathbb{Z}_n[\pi]$ est un groupe. CQFD

• Meth1 : [lecture incertaine — tracé compatible avec « 1 » comme avec « 2 » ; doublon possible avec le « Meth1 » du haut, la seconde méthode (exponentielle complexe, pages 2–3) aurait dû être numérotée « Meth2 »]

## Page 2 — Exponentielle complexe et polynôme $P_n$

Soit $n \in \mathbb{N}^*$ on a : $I_n = \mathrm{Re}(J_n)$ où $J_n = \frac{1}{n!} \int_0^\pi \underbrace{x^n(\pi-x)^n}_{P_n(x)} e^{ix}\,dx$

$$= \frac{1}{n!}\left(\sum_{k=1}^n \left[\frac{P_n^{(k-1)}(x) e^{ix}}{ik}(-1)^{\text{[lecture incertaine — exposant « } k+1 \text{ » ou « } k-1 \text{ »]}}\right]_0^\pi + (-1)^n \int_0^\pi \frac{P_n^{(n)}(x) e^{ix}}{i^n}\,dx\right)$$

⇓ en intégrant $n$ fois par partie

Or $0$ et $\pi$ sont des racines de multiplicité $n$ de $P_n$ ainsi $\forall k = 0(1)n-1$ [lecture incertaine — notation d'intervalle d'entiers, sens : $0 \leqslant k \leqslant n-1$], $P_n^{(k)}(0) = P_n^{(k)}(\pi) = 0$

Ainsi $J_n = \frac{i^n}{n!} \int_0^\pi P_n^{(n)}(x) e^{ix}\,dx$

or $P_n(x) = x^n \sum_{k=0}^n C_n^k (-1)^k x^k \pi^{n-k} = \sum_{k=0}^n C_n^k (-1)^k \pi^{n-k} x^{n+k}$

Ainsi $P_n^{(n)}(x) = \sum_{k=0}^n C_n^k (-1)^k \pi^{n-k} \frac{(n+k)!}{k!} x^k$

Ainsi $J_n = i^n \sum_{k=0}^n C_n^k (-1)^k \pi^{n-k} C_{n+k}^n \int_0^\pi e^{ix} x^k\,dx$

or en intégrant $k$ fois par partie,

$$\int_0^\pi e^{ix} x^k\,dx = \sum_{j=1}^k \text{[raturé : coefficient biffé illisible]} \left[\frac{A_k^{j-1} x^{k-j+1}}{ij} e^{ix} (-1)^{\text{[lecture incertaine — « } j+1 \text{ » ou « } j+2 \text{ »]}}\right]_0^\pi + (-1)^k \int_0^\pi \frac{k! e^{ix}}{i^k}\,dx$$

$$= \sum_{j=1}^k A_k^{j-1} \pi^{k-j+1} i^j + \frac{i^k k!}{i}(-2) \text{ [corrigé second passage — } i^j \text{ et } (-2) \text{ confirmés sur crop `/tmp/s8/crop-pipi2-bot.png`]}$$

[*sic* conservé pour mémoire sur l'historique — le manuscrit porte bien $(-2)$ en bas de p. 2 (crop `/tmp/s8/crop-pipi2-bot.png`), cohérent avec « $+2i^{k+1}k!$ » p. 3 ; « $i^j$ » confirmé sur le même crop]

## Page 3 — Forme close de $J_n$ et hypothèse $\pi = p/q$

d'où $\int_0^\pi e^{ix} x^k\,dx = \sum_{j=1}^k A_k^{j-1} \pi^{k-j+1} ij + 2i^{k+1}k!$

Ainsi $J_n = i^n \sum_{k=0}^n C_n^k (-1)^k \pi^{n-k} C_{n+k}^n \left(\sum_{j=1}^k A_k^{j-1} \pi^{k-j+1} ij + 2i^{k+1}k!\right)$

$$= \sum_{k=0}^n \sum_{j=1}^k C_n^k C_{n+k}^n A_k^{j-1} (-1)^k \pi^{k-j+1} i^{j+n} + 2\sum_{k=0}^n C_n^k (-1)^k C_{n+k}^n k! i^{n+k+2}$$

[exposants « $k-j+1$ » (attendre $n-j+1$ par produit $\pi^{n-k}\pi^{k-j+1}$) et « $n+k+2$ » (attendre $n+k+1$) : lectures incertaines]

Ainsi $I_n = \mathrm{Re}(J_n) \in \mathbb{Z}_n[\pi]$

II/ Déduisons que $\pi$ est irrationnel

Supposons par l'absurde le contraire ; ainsi $\exists (p,q) \in \mathbb{N} \times \mathbb{N}^* \mid \pi = \frac{p}{q}$

D'après I, $\exists (a_i)_{i=0}^n \in \mathbb{Z}^n$ [*sic* — $n+1$ coefficients, attendre $\mathbb{Z}^{n+1}$] $\mid I_n = \sum_{i=0}^n a_i \pi^i$

$$= \sum_{i=0}^n \frac{a_i p^i}{q^i}$$

$$= \frac{1}{q^n} \sum_{i=0}^n a_i p^i q^{n-i}$$

ainsi $d_n = \sum_{i=0}^n a_i p^i q^{n-i} \in \mathbb{Z}$. [encadré :] $n \geqslant 2$

or $|I_n| \leqslant \frac{1}{n!} \int_0^\pi \left(\frac{\pi^2}{4}\right)^n \sin x\,dx \leqslant \frac{\pi^{2n}}{n! 4^n} \times 2 \leqslant \frac{\pi^{2n}}{n!}$

ainsi $d_n \leqslant \frac{(q^n \pi^2)^n}{n!} \xrightarrow[n \to +\infty]{} 0$ [*sic* — lire $(q\pi^2)^n$ : $d_n = q^n I_n$ et $|I_n| \leqslant \pi^{2n}/n!$]

## Page 4 — Stationnarité et contradiction

or $(d_n)$ étant une suite d'entiers, elle est stationnaire d'où $\exists n_0 \in \mathbb{N} \mid \forall n \in \mathbb{N}, n \geqslant n_0 \Rightarrow d_n = 0$

En particulier $d_{n_0} = 0 \Rightarrow I_{n_0} = 0 \Rightarrow \int_0^\pi x^n(\pi-x)^n \sin x\,dx = 0$ [exposants « $n$ » ou « $n_0$ » : lecture incertaine]

ce qui est absurde vu que $x^n(\pi-x)^n \sin x > 0$ $\forall x \in ]0;\pi[$ et que $x \mapsto x^n(\pi-x)^n \sin x$ est continue sur $[0;\pi]$.

ce qui entraîne que pour $n < n_0$ en particulier $I_n > 0$. [*sic* — probablement « pour $n_0$ en particulier » : l'intégrande strictement positive sur $]0;\pi[$ donne $I_n > 0$ pour tout $n$, contredisant $I_{n_0} = 0$] [souligné :] CQFD

---

## 📝 Notes de transcription (fidélité)

- $\mathbb{Z}_n[\pi]$ désigne les polynômes en $\pi$ de degré $\leqslant n$ à coefficients entiers ; « Mq » = « montrons que ».
- La méthode 1 (récurrence après deux IPP) comporte ratures et ellipses mais aboutit à la récurrence encadrée, correcte (vérifiée : $I_2 = 6I_1 - \pi^2 I_0 = 24 - 2\pi^2$).
- La méthode 2 (pages 2–3) évalue $J_n$ par $n$ IPP : les signes alternés du crochet sont escamotés dans la somme (« $ij$ » pour $i^j$) et le facteur $(-1)$ page 2 devient $(-2)$ page 3.
- La majoration utilise $x(\pi-x) \leqslant \pi^2/4$ sur $[0,\pi]$.
- Aucune figure ni schéma sur les 4 pages.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée visuellement le 2026-09-07 (rendu `/tmp/qai/q12-pipi-1.png`, r150) — récurrence encadrée `(4n−2)I_{n−1} − π²I_{n−2}` et doublon « Meth1 » de bas de page confirmés, aucune figure ; pp. 2–4 revérifiées visuellement au second passage le 2026-09-07 (rendus `/tmp/s8/pipi-2.png` à `/tmp/s8/pipi-4.png`, r150) — texte + équations uniquement, aucune figure. Aucun script `reproduce_irrationalite-pi_N.py`, aucun PNG (aucun `assets/` créé, vérifié `uv run`).

---

## Vocabulaire

- `ℤ_n[π]` = polynômes en `π` de degré `≤ n` à coefficients entiers ; `Mq` = montrons que ; `Meth1/Meth2` = récurrence / exponentielle complexe.
- Niven = preuve par `d_n = qⁿI_n ∈ ℤ`, `d_n → 0` ⇒ stationnarité ⇒ contradiction (`I_{n₀} = 0` vs intégrande `> 0`).
