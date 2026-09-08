# Ordinaux — transcription fidèle

> 🧾 **Manuscrit original :** `ordinaux.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** calculs d'ordinaux sur cahier quadrillé (fond : calendrier) ; indices et ensembles en `[lecture incertaine — …]`, une rature conservée. Transcrit mot à mot.
> 📄 **Source scannée :** [ordinaux.pdf](ordinaux.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

$2 \cdot \omega = \omega$ [lecture incertaine — amorce en haut de page].

$E_{2 \cdot \omega} = \{u_{11}, u_{12}, u_{21}, u_{22}, u_{31}, u_{32}, \ldots\}$ [lecture incertaine — doubles indices, p.1 re-rendue à $r = 150$ (relue 2026-09-07) : $u_{11}, u_{12}, u_{21}, u_{22}, u_{31}, u_{32}$, pas $u_1, u_2, v_1, v_2, w_1, w_2$] avec $\begin{matrix} \uparrow & \uparrow & \uparrow & \uparrow & \uparrow & \uparrow \\ 1 & 2 & 3 & 4 & 5 & 6 \end{matrix} \ldots$

Considérons $f : \mathbb{N} \to E_{2 \cdot \omega}$ [raturé : flèches] $f : E_{2 \cdot \omega} \to \mathbb{N},\ u_{ij} \mapsto \begin{cases} 2i-1 & \text{si } j = 1 \\ 2i & \text{si } j = 2 \end{cases}$ [lecture incertaine — conditions notées « si $j = 1$ » et « si $j = 2$ » (p.1 relue : $j$, pas $i$ ; cohérent avec $u_{ij}$)].

Il est clair que $f$ est un isomorphisme de $E_{2 \cdot \omega}$ vers $\mathbb{N}$.

• $E_{\omega \cdot 2} = \{0, 1, \ldots, \omega, \omega+1, \ldots\} = \mathbb{N} +$ [raturé : fragment] $\{\omega+n,\ n \in \mathbb{N}\}$.

• $E_{\omega \cdot \omega} = \underbrace{\{0, 1, \ldots,}_{\omega^2} \omega, \omega+1, \ldots, \omega \cdot 2, \omega \cdot 2+1, \ldots, \omega \cdot 3, \omega \cdot 3+1, \ldots, \vdots\}$ [lecture incertaine — accolade et exposant] $= \mathbb{N} + \{\omega \cdot i+n,\ n \in \mathbb{N}\} + \{\omega \cdot 2+n,\ n \in \mathbb{N}\} + \ldots$

## Page 2

$E_{\omega \cdot \omega} = \mathbb{N} + \sum_{i=1}^{\infty} \{\omega \cdot i+n,\ n \in \mathbb{N}\}$.

• $E_{\omega^2 \cdot n} = E_{\omega^2} + \{\omega^2+m,\ m \in \mathbb{N}\}$ [lecture incertaine — « $n \geq 2$ » en marge] $+ \{\omega^2 \cdot 2+m,\ m \in \mathbb{N}\}$, $\vdots$, $+ \{\omega^2 \cdot (m-1)+m,\ m \in \mathbb{N}\}$ [lecture incertaine — dernier terme]

$$= \{0, 1, \ldots, \omega, \omega+1, \ldots, \omega \cdot 2, \omega \cdot 2+1, \ldots, \omega^2, \omega^2+1, \ldots, \omega^2 \cdot 2, \omega^2 \cdot 2+1, \ldots, \omega^2 \cdot (m-1), \omega^2 \cdot (m-1)+1, \ldots\}.$$

• $E_{\omega^3} = E_{\omega^2} + \sum_{i=1}^{\infty} \{\omega^2 \cdot i+n,\ n \in \mathbb{N}\}$.

• $E_{\omega^l} = E_{\omega^{l-1}} + \sum_{i=1}^{\infty} \{\omega^{l-1} \cdot i+n,\ n \in \mathbb{N}\}$ [lecture incertaine — exposant $l$] $= \{0, 1, \ldots, \omega, \omega+1, \ldots, \omega^2, \omega^2+1, \ldots, \omega^l, \omega^l+1, \ldots\}$.

---

## Figures

Aucune figure sur les 2 pages relues (N == pdfinfo) : calculs seuls sur cahier quadrillé (fond calendrier), sans schéma ni tableau. P. 2 vérifiée visuellement au 2e passage le 2026-09-07 (rendu `/tmp/s9/ordinaux-2.png`, r150) — $E_{\omega\cdot\omega}$, $E_{\omega^2\cdot n}$ (« $n \geq 2$ » en marge), $E_{\omega^3}$, $E_{\omega^l}$ confirmés, incertitudes déjà signalées.

## Vocabulaire

- **$2 \cdot \omega = \omega$** : ordinal produit à gauche (amorce p.1).
- **$E_{\alpha}$** : ensemble sous-jacent à l'ordinal $\alpha$ (notation du manuscrit).
- **Isomorphisme** : abus du manuscrit pour « bijection » (p.1 relue).
