import scrapping_product

# lien de la page à scrapper
url = "https://books.toscrape.com/catalogue/category/books/childrens_11/"
reponse = scrapping_product.requests.get(url)
page = reponse.content

    
# transforme (parse) le HTML en objet BeautifulSoup
soup = scrapping_product.BeautifulSoup(page, "html.parser")

# liste des category et liste des urls des category
cat_list_url = []
cat_list = []

for cat in soup.select('#default > div > div > div > aside > div.side_categories > ul > li > ul > li > a'):
    cat_list_url.append("https://books.toscrape.com/catalogue/category/books/"+ cat.get('href')[3:-10])  
    cat_list.append(cat.get('href')[3:-11])  


print(cat_list_url)
print(cat_list)