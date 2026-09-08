# Critère des séries alternées — transcription fidèle

> 🧾 **Manuscrit original :** `critere-series-alternees.pdf` (scan, 2 pages) · ✍️ KpihX
> 🔍 **Statut :** écriture rapide à l'encre bleue, plusieurs ratures et calculs compacts en `[lecture incertaine — …]` ; bas de la page 1 rogné ; brouillon rouge en marge de la page 2 ; aucune figure à reproduire. Transcrit mot à mot.
> 📄 **Source scannée :** [critere-series-alternees.pdf](critere-series-alternees.pdf) (restaurée Datas1, vérifiée pdfinfo, 2026-09-07)

---

## Page 1

[raturé : en-tête]

$*$ Nature de $\sum_{n \ge 0} e^{-(2n+1)^2}$ avec le critère des séries alternées.

Posons $\forall n \in \mathbb{N},\ U_n = (-1)^{[\text{lecture incertaine — exposant, « } n \text{ »}]} e^{-n^2}$.

on a : $\sum_{n \ge 0} e^{-(2n+1)^2} = \sum_{n \ge 0} U_{2n+2}$ [lecture incertaine — indice « $2n+2$ »].

[raturé : « or »] $\forall N \in \mathbb{N},\ \sum_{n=0}^{N} U_{2n+2} + \sum_{n=0}^{N+1} U_{2n} = \sum_{n=0}^{2N+2} U_n$ [lecture incertaine — borne « $N+1$ » de la deuxième somme, rature sus-jacente].

d'où $\sum_{n=0}^{N} U_{2n+2} = \sum_{n=0}^{[\text{lecture incertaine — borne, rature}]} U_n + \sum_{n=0}^{N} -U_{2n+1}$ (flèche courbe vers : $\sum_{n \ge 0} U_n$ cvge d'après le critère des séries alternées).

Car $|U_n| = e^{-n^2} \xrightarrow[n \to +\infty]{} 0$ alors $\sum_{n \ge 0} U_n$ cvge d'après le critère des séries alternées.

• Cas de $\sum_{n \ge 0} -U_{2n+1}$.

On a : $0 \le \sum_{n=0}^{N} -U_{2n} = \sum_{n=0}^{N} e^{-4n^2} \le \sum_{n=0}^{N} e^{-4n}$ [lecture incertaine — indice « $2n$ » alors que le cas annoncé porte « $2n+1$ »] [raturé : fin de ligne].

or car $|e^{-4}| < 1$ alors $\sum_{n \ge 0} e^{-4n}$ cvge d'après le critère des séries géométriques d'où $\sum_{n \ge 0} +U_{2n}$ cvge. Donc $\sum_{n \ge 0} e^{-(2n+1)^2}$ cvge.

$*$ $R_N = ?$ [bas de page rogné — la ligne suivante est coupée : $R_N = \sum_{n=N+1}^{+\infty} U_{2n+2} = \sum_{n=2N+2}^{+\infty} U_n + \sum_{n=0}^{+\infty} \ldots$].

## Page 2

$R_N = \sum_{n=N+1}^{+\infty} U_{2n+2} = \sum_{n=2N+2}^{+\infty} U_n + \sum_{n=N+1}^{+\infty} -U_{2n}.$

$|R_N| \le \left| \sum_{n=2N+2}^{+\infty} U_n \right| + \left| \sum_{n=N+1}^{+\infty} -U_{2n} \right|.$

or car $\sum_{n \ge 0} U_n$ est alternée et cvge alors $\left| \sum_{n=2N+2}^{+\infty} U_n \right| \le |U_{2N+3}| = e^{-(2N+3)^2}.$

De plus $\left| \sum_{n=N+1}^{+\infty} -U_{2n} \right|$ [raturé : $\left| \sum e^{\ldots} \right|$]

$$= \left| \sum_{n=N+1}^{+\infty} e^{-4n^2} \right|$$
$$\le \left| \sum_{n=N+1}^{+\infty} e^{-4(N+1)n} \right| \text{ car } n \ge N+1$$
$$\le \left| \sum_{n=N+1}^{+\infty} \left(e^{-4(N+1)}\right)^n \right| \text{ (flèche : série géo)}$$
$$\le \frac{\left(e^{-4(N+1)}\right)^{N+1}}{1 - e^{-4(N+1)}}.$$

Note rouge en marge (vertical, brouillon) : [lecture incertaine — « $a = \ln b$ », « $e^{\ln 2} = 2$ », « $e^t = (e^t)^{\ldots}$ »].

donc $|R_N| \le e^{-(2N+3)^2} + \underbrace{\frac{e^{-4(N+1)^2}}{1 - e^{-4(N+1)}}}_{P_N}.$

(rouge, en bas à gauche) [lecture incertaine — « $e^{\ldots} \to +\infty$ »].

## Figures

Aucune figure : 2 pages de texte manuscrit seul, sans schéma ni graphe (transcription § Statut : « aucune figure à reproduire » ; confirmé p. 1 sur source le 2026-09-07, rendu `/tmp/qas/` ; p. 2 relue le 2026-09-07, rendu `/tmp/s10/`). 0 PNG, 0 script `reproduce_*` — motif : rien à reproduire (la « flèche courbe » et le brouillon rouge marginal sont décrits en place, non reproductibles en figure).

## Vocabulaire

- cvge : converge ; ona : on a ; car : car ; or : or ; donc : donc.
- $R_N$ : reste de rang $N$ ; $P_N$ : majorant auxiliaire du reste ; série géo : série géométrique.
- critère des séries alternées / géométriques : règles de convergence utilisées.
