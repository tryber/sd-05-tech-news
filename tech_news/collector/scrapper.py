from parsel import Selector
from time import sleep
import requests


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)

        if response.status_code != 200:
            return ""

        return response.text

    except requests.Timeout:
        return ""

# https://realpython.com/python-sleep/


selectors = {
    "title": ".tec--article__header__title::text",
    "timestamp": "#js-article-date::attr(datetime)",
    "writer": ".tec--author__info__link::text",
    "shares_count": ".tec--toolbar__item::text",
    "comments_count": "#js-comments-btn::attr(data-count)",
    "summary": ".tec--article__body p::text",
    "sources": ".z--mb-16 a::text",
    "categories": "#js-categories a::text",
}


def generate_element(url, selector):
    title = selector.css(selectors["title"]).get()
    timestamp = selector.css(selectors["timestamp"]).get()
    writer = selector.css(selectors["writer"]).get()
    shares_count = selector.css(
        selectors["shares_count"]
    ).re_first(r'\d') or "0"
    comments_count = selector.css(selectors["comments_count"]).get()
    summary = selector.css(selectors["summary"]).get()
    sources = selector.css(selectors["sources"]).getall()
    categories = selector.css(selectors["categories"]).getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


def scrape(fetcher, pages=1):
    basic_url = "https://www.tecmundo.com.br/novidades?page="
    news_list = []

    for page in range(pages):
        url = f"{basic_url}{page}"
        response_fetched = fetcher(url)

        general_selector = Selector(text=response_fetched)
        urls = general_selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()

        for url in urls:
            arcticle_response = fetcher(url)
            arcticle_selector = Selector(text=arcticle_response)
            news_list.append(generate_element(url, arcticle_selector))

    return news_list

# honestidade acadêmica:
# para deixar o código mais limpo e atender ao limite de caracteres por linha,
# utilizei a mesma organização do colega Pedro Calado, criando o
# dicionário "selectors" e função "generate_element" a exemplo dele.
