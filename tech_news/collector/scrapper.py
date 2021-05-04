import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        res = requests.get(url, timeout=timeout)
    except requests.RequestException:
        return ""
    else:
        if res.status_code != 200:
            return ""
    sleep(delay)
    return res.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    links = []
    news_url = "https://www.tecmundo.com.br/novidades"


def get_links(url, fetcher):
    selector = Selector(fetcher(url))
    array_selector = selector.css(
        'div.tec--list__item > article > figure > a::attr(href)').getall()
    return array_selector
