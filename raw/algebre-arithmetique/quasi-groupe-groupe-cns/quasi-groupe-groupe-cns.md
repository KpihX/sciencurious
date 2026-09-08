# CNS pour que quasi-groupe = groupe — transcription fidèle

> 🧾 **Manuscrit original :** `quasi-groupe-groupe-cns.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** transcrit mot à mot depuis les rendus. Le haut de la page 1 est rogné sur le scan source. Les maths sont conservées telles quelles. Les ratures sont notées `[raturé]`.
> 📄 **Source scannée :** [`quasi-groupe-groupe-cns.pdf`](quasi-groupe-groupe-cns.pdf) (restaurée depuis `/run/media/kpihx/KpihX-Datas1/Travaux/Documents/PDF/CNS pour que quasi-groupe = groupe.pdf`, vérifiée `pdfinfo`, 2026-09-07)

---

## Page 1

[* Quasi-groupe : si associatif, c'est un groupe $(G, \cdot)$ — première ligne lisible malgré la marge haute rognée]

**Preuve :**
- Neutralité : $\forall a \in G,\ \exists!\ e_{a1}, e_{a2} \in G \mid e_{a1} \times a = a$ et $a \times e_{a2} = a$.
- Unicité des … : soit $a, a' \in G$. D'après ce qui précède $e_{a1} \times (e_{a1}' \times a') = a \implies (e_{a1} \times e_{a1}') \times a' = e_{a1} \times a' \implies e_{a1} \times e_{a1}' = e_{a1} \implies e_{a1}' = e_{a1}$.

De même on mtq $\forall a, a' \in G,\ e_{a2} = e_{a2}'$ et on peut déduire que $\exists e_1, e_2 \in G \mid \forall a \in G,\ e_1 \times a = a$ et $a \times e_2 = a$.

- [raturé] Égalité $e_1 = e_2$ : soit $G$, $(a \times e_1) \times e_2 = a \times e_1 \implies a \times (e_1 \times e_2) = a \times e_1 \implies e_2 \times e_1 = e_1 \implies e_2 = e_1$.

Donc $e_1 = e_2$, on peut conclure que $\exists e \in G \mid \forall a \in G,\ a \times e = e \times a = a$.

---

## Page 2

- Elt neutre [*sic* — il s'agit du symétrique] : soit $a \in G$, $\exists a_1^{-1}, a_2^{-1} \in G \mid a_1^{-1} \times a = e$ et $a \times a_2^{-1} = e$. Ona : $a_1^{-1} \times (a \times a_2^{-1}) = (a_1^{-1} \times a) \times a_2^{-1} = e \times a_2^{-1} = a_2^{-1} \implies a \times a_2^{-1} = e \implies a_1^{-1} = a_2^{-1}$.

Donc $\forall a \in G,\ \exists a^{-1} \in G \mid a \times a^{-1} = a^{-1} \times a = e$.

---

## Figures

Aucune figure à reproduire : p. 1 vérifiée (texte + équations, première ligne lisible) ; p. 2 vérifiée S4 (symétrique : $a_1^{-1} = a_2^{-1}$ — texte seul). Aucun script `reproduce_quasi_groupe_groupe_cns_N.py`, aucun PNG (aucun `assets/` créé).

---

## Vocabulaire

- $e_{a1}, e_{a2}$ = neutres à gauche/droite relatifs à $a$ ; $e_1, e_2$ puis $e$ = neutres globaux.
- $mtq$ = montrons que ; $Ona$ = on a ; $\times$ = loi du quasi-groupe.
