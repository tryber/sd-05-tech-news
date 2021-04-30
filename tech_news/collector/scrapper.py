"""LETS GET STARTED"""
import requests
from time import sleep
from parsel import Selector


types = {
    "title": ".tec--article__header__title::text",
    "timestamp": "#js-article-date::attr(datetime)",
    "writer": ".tec--author__info__link::text",
    "shares_count": ".tec--toolbar__item::text",
    "comments_count": "#js-comments-btn::attr(data-count)",
    "summary": ".tec--article__body p::text",
    "sources": ".z--mb-16 a::text",
    "categories": "#js-categories a::text",
}


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)

        if response.status_code != 200:
            return ""

        return response.text

    except requests.Timeout:

        return ""


def generator(url, selector):
    title = selector.css(types["title"]).get()
    timestamp = selector.css(types["timestamp"]).get()
    writer = selector.css(types["writer"]).get()
    shares_count = selector.css(types["shares_count"]).re_first(r'\d') or "0"
    comments_count = selector.css(types["comments_count"]).get()
    summary = selector.css(types["summary"]).get()
    sources = selector.css(types["sources"]).getall()
    categories = selector.css(types["categories"]).getall()

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
    """Seu código deve vir aqui"""
    list = []
    link = "https://www.tecmundo.com.br/novidades?page="

    for page in range(pages):
        url = f'{link}{page}'
        res = fetcher(url)
        selector = Selector(text=res)
        selector_url = '.tec--list__item .tec--card__title__link::attr(href)'
        news = selector.css(selector_url).getall()

        for new in news:
            res_new = fetcher(new)
            selector_new = Selector(text=res_new)
            list.append(generator(new, selector_new))

    return list
