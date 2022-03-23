# Scrapping de books.toscrape.com
L'objectif est de scrapper des datas et de générer un ou des fichiers csv.

## Présentation des scripts
On peut :
- Scrapper une page (scrapping_product.py)
- Scrapper toutes les pages produit d'une catégorie (scrapping_category.py)
- Scrapper toutes les pages produit du site (scrapping_final.py)

## Spécificités des scripts
Pour scrapping_product.py et scrapping_category.py, les fichiers csv sont générés dans le même dossier que les scripts.

Pour scrapping_final.py, un csv est généré pour chaque catégorie dans le dossier "csv" qui est généré.
Par ailleurs, le fichier scrapping_final.py va egalement télécharger les images des pages produit et les mettre dans le dossier "images".

## Liste d'améliorations possibles

- utiliser les import pour éviter de remettre certaines portions de code dans les 3 scripts
- dans le nom des fichiers csv, remplacer certains caractères par d'autres caractères (un espace est remplacé par un underscore par exemple)
- Renommer les images téléchargé en utilisant le titre du livre (et en remplaçant certains caractères comme l'espace)
- Dans le titre des fichiers csv, indiquer le nombre de livre de la catégorie et la date de création du fichier