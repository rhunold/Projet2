import requests
from bs4 import BeautifulSoup
import csv
from os.path  import basename
import os


#On créer un dossier csv et images pour stocker les données que l'on va scrapper
paths = ["csv", "images"]

for path in paths:
    try:
        os.mkdir(path)
    except OSError:
        print ("La creation du dossier %s n'a pas marché soit parce qu'il y a eu un problème, soit parce qu'il existe déjà." % path)
    else:
        print ("Le dossier %s a été crée." % path)

# lien de la page à scrapper en premier
url = "https://books.toscrape.com/"
reponse = requests.get(url)
page = reponse.content

    
# transforme (parse) le HTML en objet BeautifulSoup
soup = BeautifulSoup(page, "html.parser")

# liste des category et liste des urls des category
category_list_url = []

for category in soup.select('#default > div > div > div > aside > div.side_categories > ul > li > ul > li > a'):
    category_list_url.append(url + category.get('href')[:-10])  


# Boucle principale sur chaque url de category
for category_url in category_list_url[:]:

    # Liste des pages d'une catégorie (incrémenter si présence page suivante)
    url_list = [category_url]

    # fonction pour récupérer les url des livres de la page
    def getLinkList():
        for link in soup.select('h3 > a'):
            link_list.append("http://books.toscrape.com/catalogue/"+ link.get('href')[9:])  
    

    # liste des url des livres de la category
    link_list = []


    # boucle tant qu'il y a de la pagination
    while category_url in url_list:
        reponse = requests.get(category_url)
        page = reponse.content 
        
        # transforme (parse) le HTML en objet BeautifulSoup
        soup = BeautifulSoup(page, "html.parser")

        nextpage = soup.find("li", class_="next")

        if nextpage:
            category_url = url_list[0] + nextpage.find('a')['href']
            url_list.append(category_url)
            
            # for pages with next pagination
            getLinkList()   

        else:
            # if only one page  or last page of categorie (no nextpage)
            getLinkList()                  
            break

        
    # Creation de listes vides pour conserver data scrappées des livres d'une catégory
    title_list = []
    book_url_list = []
    upc_list = []
    image_list = []
    description_list = []
    category_list = []
    stock_list = []
    price_tax_list = []
    price_notax_list = []
    rating_list = []
    
    
    for bookurl in link_list:

        reponse = requests.get(bookurl)
        page = reponse.content
    
        # transforme (parse) le HTML en objet BeautifulSoup
        soup = BeautifulSoup(page, "html.parser")
        
        #  ajout de l'url à une list
        book_url_list.append(bookurl)

        # récupération du titre + ajout list
        title = soup.h1.text
        title_list.append(title)

        # récupération de la categorie + ajout list
        category = soup.select('#default > div > div > ul > li:nth-child(3) > a')[0].text
        category_list.append(category)

        # récupération de la description + ajout list
        description = soup.select('article > p')[0].text      
        description_list.append(description)           

        # récupération du lien de l'image + ajout list
        image = soup.select('#product_gallery > div > div > div > img')[0]['src']
        image = "http://books.toscrape.com" + image[5:]     
        image_list.append(image) 

        # récupération de l'upc + ajout list
        upc = soup.select('tr:nth-child(1) td')[0].text
        upc_list.append(upc)         

        # récupération du prix sans taxe + ajout list
        price_notax = soup.select('tr:nth-child(3) td')[0].text
        price_notax_list.append(price_notax) 

        # récupération du prix avec taxe + ajout list
        price_tax = soup.select('tr:nth-child(4) td')[0].text       
        price_tax_list.append(price_tax)         

        # récupération du stock disponible + ajout list
        stock = soup.select('tr:nth-child(6) td')[0].text        
        stock_list.append(stock)
        
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
        rating_list.append(rating)
    

    # création du fichier csv pour chaque catégorie
    en_tete = ['title', 'product_page_url', 'product_description',
            'universal_product_code', 'price_including_tax', 'price_excluding_tax',
            'number_available', 'review_rating', 'image_url']
    
    with open(paths[0] + '/' + category + '.csv', 'w') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(en_tete)
        # zip permet d'itérer sur deux listes à la fois
        for title, url, description, upc, price_tax, price_notax, category, stock, rating, image in zip(title_list, book_url_list, description_list, upc_list, price_tax_list, price_notax_list, category_list, stock_list, rating_list, image_list):
            writer.writerow([title, url, description, upc, price_tax, price_notax, category, stock, rating, image])             

    # download de l'image de couverture de chaque livre
    for image in image_list:
        with open(paths[1] + '/' + basename(image), "wb") as f:
                f.write(requests.get(image).content)
