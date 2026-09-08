# Formule de Dérivation n-ième (Leibniz) — transcription fidèle

> 🧾 **Manuscrit original :** `derivation-nieme.pdf` (scan, 2 pages, papier rose froissé) · ✍️ KpihX
> 🔍 **Statut :** lisible (~95 %), transcrit fidèlement. Papier froissé : quelques fins de lignes
> estompées (signalées). Preuve par récurrence de la linéarité puis de la formule de Leibniz.

📄 **Source scannée :** [`derivation-nieme.pdf`](derivation-nieme.pdf)

---

## Page 1 — Linéarité et initialisation de Leibniz

[…haut de page rogné : fin d'un calcul précédent…]

* $(f + \lambda g)^{(n)} = f^{(n)} + \lambda g^{(n)}$

$$(f + \lambda g)^{(n+1)} = \left((f + \lambda g)^{(n)}\right)' = \left(f^{(n)} + \lambda g^{(n)}\right)' = f^{(n+1)} + \lambda g^{(n+1)}$$

* $(fg)' = f'g + fg'$ [rappel du cas $n = 1$]

$$(fg)^{(n+1)} = \left((fg)^{(n)}\right)' = \left(\sum_{k=0}^{n} C_n^k f^{(n-k)} g^{(k)}\right)' = \sum_{k=0}^{n} C_n^k \left[f^{(n-k+1)} g^{(k)} + f^{(n-k)} g^{(k+1)}\right]$$

[bas de page : seconde somme $= \sum_{k=0}^{n} C_n^k f^{(n-k)} g^{(k+1)}$, puis essai raturé]

---

## Page 2 — Hérédité (règle de Pascal)

$(fg)^{(n+1)} =$ [début raturé]

$$= f^{(n+1)}g + \sum_{k=1}^{n} C_n^k f^{(n-k+1)} g^{(k)} + \sum_{k=0}^{n-1} C_n^k f^{(n-k)} g^{(k+1)} + fg^{(n+1)}$$

$$= f^{(n+1)}g + \sum_{k=1}^{n} C_n^k f^{(n-k+1)} g^{(k)} + \sum_{k=1}^{n} C_n^{k-1} f^{(n-k+1)} g^{(k)} + fg^{(n+1)}$$

$$= f^{(n+1)}g + \sum_{k=1}^{n} (\underbrace{C_n^k + C_n^{k-1}}_{C_{n+1}^k}) f^{(n-k+1)} g^{(k)} + fg^{(n+1)}$$

$$= \sum_{k=0}^{n+1} C_{n+1}^k f^{(n+1-k)} g^{(k)}$$

[fin : CQFD implicite — la formule au rang $n+1$]

---

## Figures

- Aucune figure sur les 2 pages (vérifié p. 1–2, document complet ; bas de p. 1 : essai raturé, pas une figure).

## Vocabulaire

dérivée $n$-ième $(\cdot)^{(n)}$, formule de Leibniz, coefficients $C_n^k$, règle de Pascal, récurrence/hérédité, $CQFD$.

## 📝 Notes de transcription (fidélité)

- Papier rose très froissé : reflets et plis, mais l'encre reste lisible partout sauf haut de page 1 (2 lignes rognées) et un essai raturé en bas de page 1.
- $C_n^k$ = coefficients binomiaux (notations d'origine conservées).
- En bas à droite de la page 1, on devine « …en exercice » sur la feuille du dessous (hors manuscrit).
