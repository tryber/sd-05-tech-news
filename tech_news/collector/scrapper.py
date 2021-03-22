import requests
from time import sleep
from parsel import Selector

URL_BASE = "https://www.tecmundo.com.br/novidades"


def fetch_content(url, timeout=3, delay=0.5):

    try:
        response = requests.get(url, timeout=timeout)

    except requests.ReadTimeout:
        # print("readTImeout")
        return ""

    if response.status_code and response.status_code == 200:
        # print(response)
        sleep(delay)
        # print('returning response text')
        return response.text

    else:
        return ""


def scrape(fetcher, pages=1):
    list_news = []
    page = 1

    while page <= pages:
        response_text = fetcher(URL_BASE + "?page={page}")
        selector = Selector(text=response_text)

        for url in selector.css(".tec--list__item h3 a::attr(href)").getall():
            selector_url = Selector(text=fetcher(url))
            title = selector_url.css(
                ".tec--article__header__title::text"
            ).get()

            timestamp = selector_url.css(
                "#js-article-date ::attr(datetime)"
            ).get()

            author = selector_url.css(".tec--author__info__link ::text").get()

            shares_count = int(
                selector_url.css(
                    "div.tec--toolbar__item:nth-child(1)::text"
                ).re_first(r"[0-9]+")
            )

            comments_count = int(
                selector_url.css("#js-comments-btn::text").re_first(r"[0-9]+")
            )

            summary = selector_url.css(".tec--article__body *::text").get()

            sources = selector_url.css(".z--mb-16 a::text").getall()

            categories = selector_url.css(
                "a.tec--badge--primary::text"
            ).getall()

            list_news.append(
                {
                    "url": url,
                    "title": title,
                    "timestamp": timestamp,
                    "writer": author,
                    "shares_count": shares_count,
                    "comments_count": comments_count,
                    "summary": summary,
                    "sources": sources,
                    "categories": categories,
                }
            )
        page += 1
    return list_news


# print(scrape(fetcher=fetch_content, pages=2)[1])
