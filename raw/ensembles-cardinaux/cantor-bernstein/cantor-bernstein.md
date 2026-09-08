# Théorème de Cantor-Bernstein — transcription fidèle

> 🧾 **Manuscrit original :** `cantor-bernstein.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** démonstration sur cahier quadrillé (la page 1 est une double page photographiée, pliure centrale) ; passages masqués par la reliure en `[lecture incertaine — …]`, coquille conservée `[*sic* — …]`. Transcrit mot à mot.
> 📄 **Source scannée :** [cantor-bernstein.pdf](cantor-bernstein.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

Théo de Kantor-Bernstein [*sic* — « Kantor » pour « Cantor »].

Soient $A$, $B$ 2 ens tels qu'il existe une bijection $f : A \to B_1$ ($B_1 \subseteq B$) et une autre $g : B \to A_1$ ($A_1 \subseteq A$). Mtq $A$ et $B$ sont équivalents. On va construire une bijection $h : A \to B$. SNMLG on va considérer $A \cap B = \emptyset$ [lecture incertaine — le scan porte « $A \cap B$ − $\emptyset$ », lu comme $= \emptyset$] car dans le cas où il serait non vide, si $x \in A \cap B$ on aurait juste $f(x) = x$ et on se ramène ainsi au cas plus intéressant en cherchant $f$ entre $A \setminus (A \cap B)$ et $B \setminus (A \cap B)$.

Soit $x \in A$. Construisons la suite $(x_n)$ comme suit : $x_0 = x$. Pour $n$ pair, on prend s'il existe [reconstruction — « Pour $n \in 2\mathbb{N}$, on prend s'il existe », début de ligne lisible sur le volet gauche, suite masquée par la pliure] :

un antécédent de $x_n$ par $g$ dans $B$ s'il existe vérifiant $x_n = g(x_{n+1})$ [reconstruction — fragment « …ett de $y$ … on prend $x_n$ … un elt de $y$ s'il existe vérifiant … $= g(x_{n+1})$ », $y$ lu comme $B$ par cohérence avec $g : B \to A_1$ ; argument standard : $x_n \in A$, on remonte par $g^{-1}$ quand $x_n \in A_1$]. Pour $n$ impair, $x_n$ est un élément de $A$ s'il existe vérifiant $x_n = f(x_{n+1})$ [reconstruction — fragment « Pour $n$ impair, $x_n$ est … elt de $A$ s'il existe vérifiant … $= f(x_{n+1})$ », $x_n \in B$, on remonte par $f^{-1}$ quand $x_n \in B_1$ ; paraphrase de l'argument standard Cantor-Bernstein]. En construisant ainsi la chaîne des antécédents successifs [reconstruction — « En construisant ainsi … », suite masquée], trois situations peuvent se présenter [reconstruction — « … situations peuvent se présenter … », standard : arrêt à un rang pair, arrêt à un rang impair, ou chaîne infinie] : on aboutit à un rang $n$ tel que l'antécédent n'existe plus [reconstruction — « on aboutit à un rang $n$ tel que … n'existe … »] ; $n$ est alors le rang de $x$ [reconstruction — « $n$ est alors le rang de … » ; pair si l'arrêt a lieu côté $A$, impair si côté $B$] ; si la chaîne ne s'arrête jamais, elle est infinie ; $x$ est alors dit d'ordre infini [reconstruction — « … est infinie ; … est appelé d'ordre infini », $x$ restitué par cohérence avec la décomposition $A_\infty$ qui suit].

On décompose ainsi $A$ en les sous-ensembles : $A_p$, formé des éléments de rang pair, $A_i$, formé des éléments de rang impair, et $A_\infty$, formé des éléments d'ordre infini. De la même manière on décompose $B$ en $B_p$, $B_i$, $B_\infty$ [reconstruction — les trois morceaux de $B$ nommés par symétrie, le scan ne nomme explicitement que la décomposition de $A$ avant « De la même manière on décompose $B$ »]. On constate alors que [la suite passe page 2] :

## Page 2

— $f$ fait correspondre $A_p$ sur $B_i$. En effet $\forall p \in A_p$, $f$ étant bijective de $A \to B_1$, $\exists!\ i \in B_1 \mid f(p) = i$. Or $p$ étant d'ordre pair, $i$ est d'ordre impair : la chaîne de $i$ prolonge celle de $p$ d'un cran vers l'avant [reconstruction — justification standard : appliquer $f$ décale le rang de $1$]. $f$ restreinte à $A_p$ est donc une application à valeurs dans $B_i$.

De même $\forall i \in B_i$, [raturé : fragment] $\exists!\ i_1 \in A \mid f(i_1) = i$ : $i$ étant d'ordre impair, son antécédent $i_1$ par $f$ existe et est d'ordre pair [reconstruction — existence due au rang impair $\geq 1$, parité décalée d'un cran vers l'arrière] (ainsi $f$ réalise une bijection de $A_p$ sur $B_i$).

Par un raisonnement analogue on montre que $f$ fait correspondre $A_\infty$ sur $B_\infty$ : une chaîne infinie des deux côtés reste infinie après application de $f$ [reconstruction — explicitation de l'argument standard, le scan porte seulement « Par un raisonnement analogue on mtq $f$ fait correspondre … sur $B_\infty$ », $A_\infty$ restitué]. De même, on montre que $g^{-1}$ fait correspondre $A_i$ sur $B_p$ : si $x \in A$ est d'ordre impair, son antécédent par $g$ existe dans $B$ et est d'ordre pair [reconstruction — symétrie $f \leftrightarrow g$, rangs décalés].

$h$ est alors l'application coïncidant sur $A_p \cup A_\infty$ avec $f$ et sur $A_i$ avec $g^{-1}$ [lecture incertaine — le scan porte « sur $A_p \cap A_\infty$ avec $f$ et sur $A_\infty$ avec $g^{-1}$ », $g^{-1}$ lu comme $g^{-1}$ d'après p.2 scan « avec $g^{-1}$ » ; $\cup$ et $A_i$ restitués par cohérence : $A_p$, $A_i$, $A_\infty$ forment une partition de $A$, et $f$ couvre $A_p \cup A_\infty$ tandis que $g^{-1}$ couvre $A_i$]. Par construction $h$ est bijective de $A$ sur $B$, ce qui établit le théorème [reconstruction — conclusion standard, implicite dans « On va construire une bijection $h : A \to B$ » de la page 1].

> 🔎 **Relecture HR :** page 1 re-rendue en haute résolution (`pdftoppm -png -r 150 -f 1 -l 1 -singlefile`), double volet gauche/droit relus ; les fragments entre crochets `[reconstruction — …]` infèrent $(x_n)$ par l'argument standard, sans altérer les passages lisibles.

---

## Figures

Aucune figure sur les 2 pages relues (N == pdfinfo) : texte seul sur cahier quadrillé, sans schéma ni tableau.

## Vocabulaire

- **Équivalents** : $A$ et $B$ sont équivalents s'il existe une bijection $h : A \to B$.
- **SNMLG** : « sans nuire à la généralité » (ramenée à $A \cap B = \emptyset$).
- **Mtq** : « montrer que ».
- **Rang / ordre infini** : longueur de la chaîne des antécédents successifs par $f^{-1}$/$g^{-1}$ ; $A_p$, $A_i$, $A_\infty$ (pair, impair, infini).
