# Projet Base de données: Vaisseaux Star Wars
*Paul Delamarre & Nathan Ganser*
![introduction](https://siasky.net/3AHevumGMD0L17Q1cJMvtX8GJ6CAG4_Bj81DxSwI2yLaEA)

## Introduction & Description générale
L'univers Star Wars et les différents vaisseaux en particuliers sont un sujet vaste et complexe, c'est pourquoi nous avons décidé de concevoir une base de donnée qui recense les différents vaisseaux ainsi que leurs caractéristiques.

### Motivation
Partiellement passion personnelle, partiellement volonté de créer une base de donnée pratique qui permet de trouver des réponses à des questions complexes liées aux vaisseaux Star Wars. 

### Usages
La base de donnée peut être utilisée pour trouver des informations telles que:
- Quels constructeurs de vaisseaux viennent de la planète Kuat?
- De quelle planète viennent les vaisseaux les plus longs? 

Trouver des réponses à ce genre de questions est nécessaire dans plusieurs situations. Un annuaire de vaisseaux star wars, un catalogue de vaisseaux pour un jeu en ligne, etc... 

*Il est important de noter que même si l'univers Star Wars tel quel n'est pas réel, tout l'univers est précisément documenté et réaliste. Cette base de donnée est basée sur les informations publiquement disponibles sur l'univers de Star Wars.*

*Source principale*: [Star Wars Fandom](https://starwars.fandom.com/wiki/Main_Page)

## Comment lancer le projet
Le fichier contenant la base de donnée est accessible ici: [/bd.sql](/bd.sql)

Notre recommendation est d'utiliser [TablePlus](https://tableplus.com/) qui permet d'importer toute la base de donnée en 1 clic en sélectionnant: `File > Import > From SQL Dump`.

## Diagramme des cas d'utilisation
![enter image description here](https://siasky.net/XAGYC5IHJ1v5TlQpCgbYr0yP7z9YjWjtac3nbizrJWaOPg)
Il y a deux acteurs principaux qui vont nous intéresser pour les cas d'utilisations: le fan de Star Wars qui va utiliser la base de donnée pour explorer et trouver des réponses à ses questions, puis, l'administrateur de la base de donnée qui va s'occuper de maintenir la base de donnée et l'améliorer basé sur les suggestions des utilisateurs. 

Quelques cas d'utilisations pratiques: 
**Fan de Star Wars**
- Sur quelle planète à été conçu le vaisseau le plus cher?
- Je dois sélectionner un vaisseau pour un jeu en ligne, quel est le vaisseau le plus puissant (avec le plus de x et y @TODO)
- Il y a une erreur dans la base de donnée et j'aimerai en informer l'administrateur

**Administrateur**
- Voir les suggestions des utilisateurs 
- Informer les utilisateurs que leur suggestion à été prise en compte
- Ajouter un nouveau vaisseau à la base de données
## Diagramme des classes & relations
**Diagramme des classes**
![enter image description here](https://siasky.net/HAHKGfAmD0UR1Dt6aMEgdRAhQhIG06xn6e4Scx_HVJmKeg)
Le diagramme des classes montre clairement les deux parties distinctes de al base de donnée. D'un côté, la base de donnée principale avec les différents liens entre les tables, de l'autre, la table qui contient les suggestions. 

**Diagramme des relations**
![enter image description here](https://siasky.net/nADKwBdkhBpd7Kj4DbPoi_fYhiMlcCHtCrHmqseeMj5T1w)

## Principales requêtes d'interrogation
Nous avons créé des vues pour les principales requêtes d'interrogations, les voici: 

**Filter par classe de vaisseau**
*Il est par exemple utile de pouvoir sélectionner les vaisseaux par type.*
`SELECT * FROM VAISSEAU WHERE CLASSE_ID=?`

Voici par exemple la vue pour les vaisseaux de type **Croiseur**:
![enter image description here](https://siasky.net/JAABdeLOoC2Wqv7H5vMfYP4jkYGOJqtdVTqFjivyvA8P9g)
*Des vues pour chaque type de vaisseau ont été créées avec le nom du type de vaisseau* 

**Voir info constructeurs**
*Il est utile de pouvoir avoir une vue d'ensemble sur les constructeurs, la vue `info_constructeurs` permet de voir de quelle planète vient chaque constructeur et combien de vaisseaux il a construit*
![enter image description here](https://siasky.net/LAAiNcsVKyUA0jaBYx5RvQUg0ZsZtZ8xf4sOeq1oPfj3zA)

**Voir les suggestions à prendre en compte**
*Au fur et à mesure que l'administrateur lit et prends en compte les suggestions qu'il reçoit, il modifie le boolean `pris_en_compte` de `0` à `1`. Il n'a plus besoin de voir les suggestions qu'il a déjà pris en compte, c'est ce que la vue `suggestions_a_process` permet*
`SELECT * FROM SUGGESTIONS WHERE PRIS_EN_COMPTE=0`

Voici une capture d'écran:
![enter image description here](https://siasky.net/KAAjhPaZ6ED88dKg7pZA588ttRfBhIu9gM9o4X-1WzQrWg)

## Conclusion
Ce projet nous à permis de mettre nos connaissances de l'univers Star Wars en pratique et de diviser le concept de vaisseau qui nous est si familier en classes distinctes et de clarifier les définitions entre-elles. 

Nous sommes maintenant tentés de rajouter une petite interface par dessus notre base de donnée pour transformer ce *proof of concept* en une vraie application. Réfléchir aux besoins de l'administrateur à été très formateur également étant donné que nous sommes d'habitude plutôt du côté du *consommateur* d'information. 