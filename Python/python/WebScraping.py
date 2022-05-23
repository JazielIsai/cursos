# Realizaremos WebScraping
import requests
from bs4 import BeautifulSoup

# Realizo un webScraping a mi pagina obteniendo todos los links
page = requests.get("https://isai-dev.com/").text

# Creates a BeautifulSoup object
soup = BeautifulSoup(page, 'html.parser')

# Pull all instances of <a> tag
tag_a = soup.find_all("a")

# clears data of all tags
for tag in tag_a:
    nav = tag.contents[0]
    fullLink = tag.get("href")
    print(tag)
    print(fullLink)
