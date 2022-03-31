# Scrapping de books.toscrape.com
L'objectif est de scrapper des datas et de générer un ou des fichiers csv.

## Créer et installer l'environnement virtuelle
- Clonez le reposotory git dans un dossier local
- Dans votre terminal, allez au dossier local et lancez la commande "python3 -m venv env"
- Dans votre terminal, activez l'environnement virtuelle en lançant la commande "source env/bin/activate"
- Dans votre terminal, lancez la commande "pip install -r requirements.txt"

## Présentation des scripts
On peut :
- Scrapper une page (scrapping_product.py)
- Scrapper toutes les pages produit d'une catégorie (scrapping_category.py)
- Scrapper toutes les pages produit du site (scrapping_final.py)

## Spécificités des scripts
Pour scrapping_product.py et scrapping_category.py, les fichiers csv sont générés dans le même dossier que les scripts.

Pour scrapping_final.py, un csv est généré pour chaque catégorie dans le dossier "csv" qui est généré.
Par ailleurs, le fichier scrapping_final.py va egalement télécharger les images des pages produit et les mettre dans le dossier "images" généré.

## Lancer les scripts
Pour lancer les scripts, il faut écrire dans le terminal :
- "python3 scrapping_product.py"
- "python3 scrapping_category.py"
- "python3 scrapping_final.py"

## Liste d'améliorations possibles
- utiliser les import pour éviter de remettre certaines portions de code dans les 3 scripts
- dans le nom des fichiers csv, remplacer certains caractères par d'autres caractères (un espace est remplacé par un underscore par exemple)
- Renommer les images téléchargées en utilisant le titre du livre (et en remplaçant certains caractères comme l'espace)
- Dans le titre des fichiers csv, indiquer le nombre de livres de la catégorie et la date de création du fichier