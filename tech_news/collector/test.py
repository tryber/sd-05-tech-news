import requests
from parsel import Selector

response = requests.get("https://www.tecmundo.com.br/novidades")
selector = Selector(text=response.text)
print(selector.css("img.tec--card__thumb__image").getall()[0])
# print(selector)
