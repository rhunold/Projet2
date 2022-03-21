import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "https://books.toscrape.com/catalogue/category/books/childrens_11/"

# Liste des pages d'une catégorie (incrémenter si présence page suivante)
url_list = [url]

# fonction pour récupérer les url des livres de la page
def getLinkList():
    for link in soup.select('h3 > a'):
        link_list.append("http://books.toscrape.com/catalogue/"+ link.get('href')[9:])  
   

# list des url des livres de la category
link_list = []


# tant qu'il y a de la pagination
while url in url_list:
    reponse = requests.get(url)
    page = reponse.content 
    
    # transforme (parse) le HTML en objet BeautifulSoup
    soup = BeautifulSoup(page, "html.parser")

    nextpage = soup.find("li", class_="next")

    if nextpage:
        url = url_list[0] + nextpage.find('a')['href']
        url_list.append(url)
        
        # for pages with  next pagination
        getLinkList()   

    else:      
        break

    # if only one page  or last page of categorie (no nextpage)
    getLinkList()    

print(url_list)
print(len(link_list))


print(link_list)





