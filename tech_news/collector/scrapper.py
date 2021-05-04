import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        resp = requests.get(url, timeout=timeout)
    except requests.RequestException:
        return ""
    else:
        if resp.status_code != 200:
            return ""
        sleep(delay)
        return resp.text


def scrape(fetcher, pages=1):
    links_all = []
    url_base = "https://www.tecmundo.com.br/novidades"


def get_links(url, fetcher):
    selector = Selector(fetcher(url))
    return selector.css(
        'div.tec--list__item > article > figure > a::attr(href)'
        ).getall()
