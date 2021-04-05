import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException:
        print("Oops!  That was no valid number.  Try again...")
        return ''
    else:
        if response.status_code != 200:
            return ''
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    list_news = []
    page = 1
    while page <= pages:
        res = fetcher("https://www.tecmundo.com.br/novidades" + "?page={page}")
        selector = Selector(text=res)
        for url in selector.css(".tec--list__item h3 a::attr(href)").getall():
            selector_url = Selector(text=fetcher(url))
            list_news.append(
                {
                    "url": url,
                    "title": selector_url.css(
                        ".tec--article__header__title::text"
                    ).get(),
                    "timestamp": selector_url.css(
                        ".tec--timestamp__item time::attr(datetime)"
                    ).get(),
                    "writer": selector_url.css(
                        ".tec--author__info__link::text"
                    ).get(),
                    "shares_count": int(
                        selector_url.css(".tec--toolbar__item::text").re_first(
                            r"[0-9]+"
                        )
                    ),
                    "comments_count": int(
                        selector_url.css("#js-comments-btn::text").re_first(
                            r"[0-9]+"
                        )
                    ),
                    "summary": selector_url.css(
                        ".tec--article__body *::text"
                    ).get(),
                    "sources": selector_url.css(".z--mb-16 a::text").getall(),
                    "categories": selector_url.css(
                        "#js-categories a::text"
                    ).getall(),
                }
            )
        page += 1
    return list_news
