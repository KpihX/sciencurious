# Systèmes de numération binaire / Binary Number Systems — transcription fidèle bilingue

> 🧾 **Manuscrits originaux :** `unites-binaires.pdf` (diaporama FR, 8 pages) + `binary-system.pdf` (diaporama EN, 8 pages) · ✍️ KPIHX, SUPERVISEUR / CORDINATOR [*sic*] : Dr CHANA
> 🔍 **Statut :** même diaporama en français et en anglais (système binaire, besoin d'unités binaires, kibi/mébi/gibi, tableau des préfixes CEI 1998), vérifié en texte (`pdftotext`) + spot pp. 1 et 7 de chaque PDF (rendus `/tmp/mdt/G-fr-*.png`, `/tmp/mdt/G-en-*.png`, 2026-09-07). Transcrit mot à mot, coquilles d'origine conservées et signalées `[*sic* — …]`.
> 📄 **Sources scannées :** [unites-binaires.pdf](unites-binaires.pdf) + [binary-system.pdf](binary-system.pdf) (restaurées Datas1, vérifiées pdfinfo, 2026-09-07)
> 🗑️ **Doublons fusionnés (2026-09-07) :** dossiers `informatique/unites-binaires/` et `anglais/binary-system/` supprimés, les 2 PDF gardés ici, un seul md bilingue. Aucun asset/PNG ni script de reproduction (visuels décoratifs uniquement, voir Figures).

---

# 🇫🇷 Version française (unites-binaires.pdf)

## Page FR 1

(Logo haut-gauche : « Binary Unit Systems » — B, U, S en noir, « inary », « nit », « ystems » en rouge, sigle rouge à gauche. Logo haut-droit : cachet orange ENSP — École Nationale Supérieure Polytechnique, Université de Yaoundé I. Fond : polygones verts et bleus.)

Au-delà du binaire : les secrets du kibi, du mébi, du gibi, …

SUPERVISEUR : Dr CHANA

BY KPIHX

## Page FR 2

(Bandeau latéral bleu : SOMMAIRE. Quatre notes autocollantes sur panneau de liège, chacune piquée d'une punaise bleue :)

I. Le système de numération binaire

II. Le besoin d'unités binaires

III. Kibi, Mébi, Gibi et au-delà

IV. Les unités binaires en pratique

## Page FR 3

(Bandeau latéral bleu : INTRODUCTION.)

Dans le monde d'aujourd'hui, où la technologie progresse à un rythme sans précédent, comprendre le système binaire des unités est devenu plus important que jamais. Des ordinateurs aux smartphones, du stockage de données aux réseaux, le système binaire des unités est au cœur de tout ce que nous faisons. Mais qu'est-ce exactement que le système binaire des unités ? En termes simples, c'est un système de numération qui n'utilise que deux chiffres 0 et 1. Cela peut sembler une façon étrange de compter pour ceux qui ne le connaissent pas, mais il s'est avéré être incroyablement utile dans l'informatique moderne. Alors, plongeons dans le monde des unités binaires et voyons comment elles fonctionnent !

## Page FR 4

(Bandeau latéral bleu : LE SYSTÈME DE NUMÉRATION BINAIRE.)

Le système de numération binaire est un système de base 2 qui n'utilise que deux chiffres, 0 et 1. Cela signifie que tout nombre peut être représenté en utilisant seulement ces deux chiffres. En revanche, le système décimal que nous utilisons dans notre vie quotidienne est un système de base 10 qui utilise dix chiffres, de 0 à 9.

Dans le système binaire, chaque chiffre représente une puissance de 2, en commençant par $2^0$ à droite et en augmentant d'une puissance de 2 à chaque fois que l'on se déplace vers la gauche. Par exemple, le nombre binaire 1011 représente $2^0 + 2^1 + 2^3$ ce qui équivaut à 11 en décimal.

## Page FR 5

(Bandeau latéral bleu : LE BESOIN DES UNITÉS BINAIRES.)

Utiliser des unités décimales dans l'informatique peut entraîner des imprécisions et des inefficacités. Cela est dû au fait que les ordinateurs utilisent le code binaire pour traiter les informations, ce qui implique que les valeurs décimales doivent être converties en binaire avant de pouvoir être traitées. Par exemple, quand un ordinateur stocke un fichier d'une taille de 1 kilooctet (Ko), il stocke en réalité 1024 octets, qui est la puissance de 2 la plus proche de 1000. Cela signifie que si vous essayez de stocker un fichier qui fait exactement 1000 octets, il occupera 2 Ko d'espace de stockage au lieu de 1 Ko

(Image centrale : fond de chiffres binaires colorés avec étiquettes « Kibibytes », « Mebibites » [*sic* — « Mebibytes »], « Tebibytes », « Gibibites » [*sic* — « Gibibytes »] — illustration générique, non reproductible en figure vectorielle.)

## Page FR 6

(Bandeau latéral bleu : KIBI, MEBI, GIBI, ET AU-DELAS.)

Pour mesurer le stockage numérique, le système décimal traditionnel ne suffit pas. Place au système binaire, qui utilise des puissances de deux au lieu de dix. Les unités binaires les plus couramment utilisées sont le kibioctet (Kio), le mébioctet (Mio) et le gibioctet (Gio). Pour vous donner une idée, 1 Kio équivaut à 1024 octets, alors qu'un kilooctet n'en vaut que 1000. Cela peut sembler négligeable, mais quand on manipule de grandes quantités de données, cela peut faire une grande différence. Par exemple, un fichier qui fait 1 Go, fait en réalité 931 gibioctets (Gio) [*sic* — 1 Go ≈ 0,931 Gio, « 931 » sans décimale ni virgule dans l'original]. Comprendre ces différences est essentiel dans l'informatique moderne.

## Page FR 7

(Bandeau latéral bleu : LES UNITÉS BINAIRES EN PRATIQUE.)

La normalisation des préfixes binaires en 1998 par la Commission Electrotechnique Internationale spécifie les préfixes suivants pour représenter des multiples calculés en puissances de 2 : kibi pour "kilo binaire", mebi pour "méga binaire", gibi pour "giga binaire", tebi pour "téra binaire", et ainsi de suite. Les préfixes binaires sont donnés comme dans le tableau :

| System of Units (SI) |  |  | Binary Numeral |  |  |  | % |
|---|---|---|---|---|---|---|---|
| Factor | Name | Symbol | Factor | Name | Symbol | # of Bytes | Difference |
| $10^3$ | kilobyte | KB | $2^{10}$ | kibibyte | KiB | 1,024 | 2.4% |
| $10^6$ | megabyte | MB | $2^{20}$ | mebibyte | MiB | 1,048,576 | 4.9% |
| $10^9$ | gigabyte | GB | $2^{30}$ | gibibyte | GiB | 1,073,741,824 | 7.4% |
| $10^{12}$ | terabyte | TB | $2^{40}$ | tebibyte | TiB | 1,099,511,627,776 | 10.0% |
| $10^{15}$ | petabyte | PB | $2^{50}$ | pebibyte | PiB | 1,125,899,906,842,624 | 12.6% |
| $10^{18}$ | exabyte | EB | $2^{60}$ | exbibyte | EiB | 1,152,921,504,606,846,976 | 15.3% |
| $10^{21}$ | zettabyte | ZB | $2^{70}$ | zebibyte | ZiB | 1,180,591,620,717,411,303,424 | 18.1% |
| $10^{24}$ | yottabyte | YB | $2^{80}$ | yobibyte | YiB | 1,208,925,819,614,629,174,706,176 | 20.9% |

## Page FR 8

(Bandeau latéral bleu : CONCLUSION.)

En résumé, nous avons appris que le système binaire des unités est essentiel dans l'informatique moderne. Il nous permet de représenter les données de façon plus efficace et précise, ce qui est crucial dans le monde numérique d'aujourd'hui. Nous avons aussi vu comment utiliser des unités binaires comme le kibioctet, le mébioctet et le gibioctet peut nous aider à surmonter les limites des unités décimales dans l'informatique et le stockage de données. En comprenant ces unités, nous pouvons prendre de meilleures décisions quand il s'agit de gérer et de stocker nos informations numériques. À mesure que nous dépendons davantage de la technologie, il devient de plus en plus important de comprendre les principes fondamentaux qui la sous-tendent. En saisissant le concept des unités binaires, nous pouvons débloquer de nouvelles possibilités et repousser les frontières de ce qui est possible dans le domaine numérique.

Sources : * https://en.wikipedia.org/wiki/Byte

* www.bard.com

---

# 🇬🇧 English version (binary-system.pdf)

## Page EN 1

(Logo haut-gauche : « Binary Unit Systems » — B, U, S en noir, « inary », « nit », « ystems » en rouge, sigle rouge à gauche. Logo haut-droit : cachet orange ENSP — École Nationale Supérieure Polytechnique, Université de Yaoundé I. Fond : polygones verts et bleus.)

Breaking the Binary: Understanding the Kibi, Mébi, and Beyond

CORDINATOR [*sic* — « COORDINATOR »] : Dr CHANA

BY KPIHX

## Page EN 2

(Bandeau latéral bleu : PRESENTATION. Titre : SUMMARY. Quatre notes autocollantes sur panneau de liège, chacune piquée d'une punaise bleue :)

I. The Binary Number System

II. The Need for Binary Units

III. Kibi, Mebi, Gibi, and Beyond

IV. Binary Units in Practice

## Page EN 3

(Bandeau latéral bleu : INTRODUCTION.)

In today's world, where technology is advancing at an unprecedented pace, understanding the binary system of units has become more important than ever before. From computers to smartphones, from data storage to networking, the binary system of units is at the heart of everything we do.

But what exactly is the binary system of units? In simple terms, it is a system of numbering that uses only two digits 0 and 1. This may seem like a strange way of counting to those unfamiliar with it, but it has proven to be incredibly useful in modern computing. So, let's dive into the world of binary units and see how they work!

## Page EN 4

(Bandeau latéral bleu : THE BINARY NUMBER SYSTEM.)

The binary number system is a base-2 numbering system that uses only two digits, 0 and 1. This means that any number can be represented using only these two digits. In contrast, the decimal system that we use in our daily lives is a base-10 numbering system that uses ten digits, 0 through 9.

In the binary system, each digit represents a power of 2, starting from $2^0$ on the right and increasing by a power of 2 as you move left. For example, the binary number 1011 represents $2^0 + 2^1 + 2^3$ which equals 11 in decimal.

## Page EN 5

(Bandeau latéral bleu : THE NEED FOR BINARY UNITS.)

Using decimal units in computing can lead to inaccuracies and inefficiencies. This is because computers use binary code to process information, which means that decimal values must be converted into binary before they can be processed.

For example, when a computer stores a file with a size of 1 kilobyte (KB), it actually stores 1024 bytes, which is the closest power of 2 to 1000. This means that if you try to store a file that is exactly 1000 bytes, it will take up 2 KB of storage space instead of 1 KB.

(Image centrale : fond de chiffres binaires colorés avec étiquettes « Kibibytes », « Mebibites » [*sic* — « Mebibytes »], « Tebibytes », « Gibibites » [*sic* — « Gibibytes »] — illustration générique, non reproductible en figure vectorielle.)

## Page EN 6

(Bandeau latéral bleu : KIBI, MEBI, GIBI, AND BEYOND.)

When it comes to measuring digital storage, the traditional decimal system falls short. Enter the binary system, which uses powers of two instead of ten. The most commonly used binary units are the kibibyte (KiB), mebibyte (MiB), and gibibyte (GiB).

To put this in perspective, 1 KiB is equal to 1024 bytes, while one kilobyte is only 1000 bytes. This may not seem like a significant difference, but when you're dealing with large amounts of data, it can add up quickly. For example, a file that is 1 GB in size, is actually 931 gibibytes (GiB) in size [*sic* — 1 Go ≈ 0,931 Gio, « 931 » sans décimale ni virgule dans l'original]. Understanding these differences is crucial in modern computing.

## Page EN 7

(Bandeau latéral bleu : BINARY UNITS IN PRACTICE.)

The standardization of binary prefixes in 1998 by the International Electrotechnical Commission specifies the following prefixes to represent multiples calculated in powers of 2: kibi for "binary kilo", mebi for "binary mega", gibi for "binary giga", tebi for "binary tera", and so on. Binary prefixes have the following order relation:

| System of Units (SI) |  |  | Binary Numeral |  |  |  | % |
|---|---|---|---|---|---|---|---|
| Factor | Name | Symbol | Factor | Name | Symbol | # of Bytes | Difference |
| $10^3$ | kilobyte | KB | $2^{10}$ | kibibyte | KiB | 1,024 | 2.4% |
| $10^6$ | megabyte | MB | $2^{20}$ | mebibyte | MiB | 1,048,576 | 4.9% |
| $10^9$ | gigabyte | GB | $2^{30}$ | gibibyte | GiB | 1,073,741,824 | 7.4% |
| $10^{12}$ | terabyte | TB | $2^{40}$ | tebibyte | TiB | 1,099,511,627,776 | 10.0% |
| $10^{15}$ | petabyte | PB | $2^{50}$ | pebibyte | PiB | 1,125,899,906,842,624 | 12.6% |
| $10^{18}$ | exabyte | EB | $2^{60}$ | exbibyte | EiB | 1,152,921,504,606,846,976 | 15.3% |
| $10^{21}$ | zettabyte | ZB | $2^{70}$ | zebibyte | ZiB | 1,180,591,620,717,411,303,424 | 18.1% |
| $10^{24}$ | yottabyte | YB | $2^{80}$ | yobibyte | YiB | 1,208,925,819,614,629,174,706,176 | 20.9% |

## Page EN 8

(Bandeau latéral bleu : CONCLUSION.)

In short, we have learned that the binary system of units is essential in modern computing. It allows us to represent data more efficiently and accurately, which is crucial in today's fast-paced digital world.

We have also seen how using binary units such as kibibyte, mebibyte, and gibibyte can help overcome the limitations of decimal units in computing and data storage. By understanding these units, we can make better decisions when it comes to managing and storing our digital information.

As we continue to rely more on technology, it becomes increasingly important to understand the fundamental principles behind it. By grasping the concept of binary units, we can unlock new possibilities and push the boundaries of what is possible in the digital realm.

Sources : * https://en.wikipedia.org/wiki/Byte

* www.bard.com

---

## Figures

Aucune figure vectorielle sur les 16 pages (8 FR + 8 EN) : les seuls visuels sont décoratifs et strictement identiques dans les 2 versions (logos « Binary Unit Systems »/ENSP p.1, notes autocollantes du sommaire p.2, illustration générique p.5 décrite en place). Motif : illustration générique non reproductible en figure vectorielle, aucun schéma à coder — aucun script `reproduce_*` ni PNG, aucun dossier `assets/`.

## Vocabulaire FR

- bit/octet ; base 2 (binaire) vs base 10 (décimal) ; $2^0$, $2^1$, $2^3$ : puissances de 2 (1011 = 11).
- kibioctet (Kio), mébioctet (Mio), gibioctet (Gio) : $1024 = 2^{10}$ vs kilooctet $= 1000$.
- kibi/mébi/gibi/tebi : « kilo/méga/giga/téra binaire » (CEI, 1998) ; KiB/MiB/GiB/TiB/PiB/EiB/ZiB/YiB.
- SI : système décimal (KB/MB/GB…) ; écart % croissant (2,4 % → 20,9 %).
- SUPERVISEUR : Dr CHANA ; BY KPIHX : graphies d'origine conservées.

## Vocabulaire EN

- bit/byte ; base-2 (binary) vs base-10 (decimal) ; $2^0$, $2^1$, $2^3$ : powers of 2 (1011 = 11).
- kibibyte (KiB), mebibyte (MiB), gibibyte (GiB) : $1024 = 2^{10}$ vs kilobyte $= 1000$.
- kibi/mebi/gibi/tebi : "binary kilo/mega/giga/tera" (IEC, 1998) ; KiB/MiB/GiB/TiB/PiB/EiB/ZiB/YiB.
- SI : decimal system (KB/MB/GB…) ; growing gap % (2.4 % → 20.9 %).
- CORDINATOR [*sic* — « COORDINATOR »], Mebibites/Gibibites [*sic* — Mebibytes/Gibibytes], « 931 gibibytes » [*sic*] : coquilles d'origine conservées.

## Correspondance FR ↔ EN (même diaporama)

| FR | EN |
|---|---|
| Au-delà du binaire… / SUPERVISEUR | Breaking the Binary… / CORDINATOR [*sic*] |
| SOMMAIRE (I–IV) | SUMMARY (I–IV) |
| INTRODUCTION | INTRODUCTION |
| LE SYSTÈME DE NUMÉRATION BINAIRE | THE BINARY NUMBER SYSTEM |
| LE BESOIN DES UNITÉS BINAIRES | THE NEED FOR BINARY UNITS |
| KIBI, MEBI, GIBI, ET AU-DELAS | KIBI, MEBI, GIBI, AND BEYOND |
| LES UNITÉS BINAIRES EN PRATIQUE (tableau CEI) | BINARY UNITS IN PRACTICE (same IEC table) |
| CONCLUSION + Sources | CONCLUSION + Sources |
