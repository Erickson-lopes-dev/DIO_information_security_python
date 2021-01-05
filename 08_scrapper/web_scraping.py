from bs4 import BeautifulSoup

import requests

# indica o site que deseja indicar
site = requests.get("http://tempo.clic.com.br/sp/itapecerica-da-serra").content

# Esta BAIXANDO DO SITE  o conteudo html do site
soup = BeautifulSoup(site, 'html.parser')

# transforma em string para leitura em python
# print(soup.prettify())

temperatura = soup.find("span", class_="temperature_now")

print(temperatura.text)






