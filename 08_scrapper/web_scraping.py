from bs4 import BeautifulSoup

import requests

# indica o site que deseja indicar
site = requests.get("https://www.climatempo.com.br/").content

# Esta BAIXANDO DO SITE  o conteudo html do site
soup = BeautifulSoup(site, 'html.parser')

# transforma em string para leitura em python
# print(soup.prettify())

temperatura = soup.find("span", class_="temperature _margin-l-5 -font-13")

print(temperatura.text)

print(soup.a)

for item in soup.find_all('span'):
    print(item.string)


# SITE NAO ESTA MAIS IMPRIMINDO O TEMPO



