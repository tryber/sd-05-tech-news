import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        RESPONSE = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    else:
        return RESPONSE.text


def create_news(url, selector):
    TITLE = selector.css(".tec--article__header__title::text").get()
    TIMESTAMP = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    WRITER = selector.css("a.tec--author__info__link::text").get()
    SHARES_COUNT = (
        selector.css(".tec--toolbar__item::text").re_first(r"\d") or "0"
    )
    COMMENTS_COUNT = (
        selector.css("#js-comments-btn::text").re_first(r"\d") or "0"
    )
    SUMMARY = selector.css(".tec--article__body > p::text").get()
    SOURCES = selector.css("div.z--mb-16 .tec--badge::text").getall()
    CATEGORIES = selector.css("#js-categories a::text").getall()
    return {
        "url": url,
        "title": TITLE,
        "timestamp": TIMESTAMP,
        "writer": WRITER,
        "shares_count": int(SHARES_COUNT),
        "comments_count": int(COMMENTS_COUNT),
        "summary": SUMMARY,
        "sources": SOURCES,
        "categories": CATEGORIES,
    }


def scrape(fetcher, pages=1):
    BASE_URL = "https://www.tecmundo.com.br/novidades"
    news_list = []
    for page in range(1, pages + 1):
        SELECTOR = Selector(fetcher(f"{BASE_URL}?page={page}"))
        URLS = SELECTOR.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        for url in URLS:
            SELECTOR = Selector(fetcher(url))
            news_list.append(create_news(url, SELECTOR))
    return news_list
