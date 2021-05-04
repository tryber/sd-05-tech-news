import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        sleep(delay)
    except requests.exceptions.RequestException:
        return ""
    else:
        return response.text


URL_BASE = "https://www.tecmundo.com.br/novidades"


def scrape(fetcher, pages=1):
    news = []
    count = 1
    while count <= pages:
        response = fetcher(URL_BASE + "?page={count}")
        selector = Selector(text=response)

        for url in selector.css(".tec--card__title a::attr(href)").getall():
            selector_url = Selector(text=fetcher(url))
            news.append(
                {
                    "url": url,
                    "title": selector_url.css(
                        ".tec--article__header__title::text"
                        ).get(),
                    "timestamp": selector_url.css(
                        "#js-article-date::attr(datetime)"
                        ).get(),
                    "writer": selector_url.css(
                        ".tec--author__info__link::text"
                        ).get(),
                    "shares_count": int(
                        selector_url.css(
                            ".tec--toolbar__item::text").re_first(r"[0-9]+")
                        ),
                    "comments_count": int(
                        selector_url.css(
                            "#js-comments-btn::text").re_first(r"[0-9]+")
                        ),
                    "summary": selector_url.css(
                        ".tec--article__body > p::text"
                        ).get(),
                    "sources": selector_url.css(
                        "div.z--mb-16 .tec--badge::text"
                        ).getall(),
                    "categories": selector_url.css(
                        "#js-categories a::text"
                        ).getall(),
                }
            )
        count += 1
    return news
