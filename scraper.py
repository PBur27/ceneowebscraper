import requests
from bs4 import BeautifulSoup


product_code = 99105003
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"

response = requests.get(url)
page = BeautifulSoup(response.text, "html.parser")
opinions = page.select("div.js_product-review")

for opinion in opinions:
    print(opinion["data-entry-id"])

#print(page.prettify())