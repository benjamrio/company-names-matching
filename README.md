# Company Name Matching
Match une liste de noms d'entreprises saisies par l'humain (avec des erreurs, des noms non standards, des inversions) au nom standard présent dans la base de données SIREN de data.gouv. On utilise une méthode de fuzzy matching : pour chaque mot, extraire des n-grams, et calculer les similarités entre les noms à standardiser et les noms standards.

## Utilisation
Le package est encore en développement. Pour utiliser le matching, il faut utiliser le notebook predict.ipynb. La table `siren_table.csv` sert de référence, on pourra déduire les numéros SIREN des noms d'entreprise. Elle est issue de l'API data.gouvv. La table `top500verifCom.tsv` set de table d'inputs dont on veut prédire le nom standard d'entreprise. La table est issue d'un copier-coller à partir du site [verif](https://www.verif.com/Hit-parade/01-CA/00-Pays/0-France/).
