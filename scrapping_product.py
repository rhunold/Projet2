import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
reponse = requests.get(url)
page = reponse.content

# affiche la page HTML
# print(page)

# transforme (parse) le HTML en objet BeautifulSoup
soup = BeautifulSoup(page, "html.parser")


#  ajout de l'url à une list
url_list = [url]

# récupération du titre + ajout list
title = soup.h1.text
title_list = [title]

# récupération de la categorie + ajout list
category = soup.select('#default > div > div > ul > li:nth-child(3) > a')[0].text
category_list = [category]

# récupération de la description + ajout list
description = soup.select('article > p')[0].text
description_list = [description]


# récupération du lien de l'image + ajout list
image = soup.select('#product_gallery > div > div > div > img')[0]['src']
image = "http://books.toscrape.com" + image[5:]
image_list = [image]

# récupération de l'upc + ajout list
upc = soup.select('tr:nth-child(1) td')[0].text
upc_list = [upc]


# récupération du prix sans taxe + ajout list
price_notax = soup.select('tr:nth-child(3) td')[0].text
price_notax_list = [price_notax]


# récupération du prix avec taxe + ajout list
price_tax = soup.select('tr:nth-child(4) td')[0].text
price_tax_list = [price_tax]

# récupération du stock disponible + ajout list
stock = soup.select('tr:nth-child(6) td')[0].text
stock_list = [stock]

# récupération review rating + ajout list
if soup.select('p.One'):
    rating = 1
elif soup.select('p.Two'):
    rating = 2   
elif soup.select('p.Three'):
    rating = 3
elif soup.select('p.Four'):
    rating = 4  
else:
    rating = 5 
rating_list = [rating]  



# création du fichier scrapping_product.csv

en_tete = ['title', 'product_page_url', 'product_description',
           'universal_product_code', 'price_including_tax', 'price_excluding_tax',
           'number_available', 'review_rating', 'image_url']
with open('scrapping_product.csv', 'w') as fichier_csv:
	writer = csv.writer(fichier_csv, delimiter=',')
	writer.writerow(en_tete)
	# zip permet d'itérer sur deux listes à la fois
	for title, url, description, upc, price_tax, price_notax, category, stock, rating, image in zip(title_list, url_list, description_list, upc_list, price_tax_list, price_notax_list, category_list, stock_list, rating_list, image_list):
		writer.writerow([title, url, description, upc, price_tax, price_notax, category, stock, rating, image])






