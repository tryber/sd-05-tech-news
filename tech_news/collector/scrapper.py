import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text
    finally:
        sleep(delay)


def content(string):
    if string is None:
        return 0
    return int(string)


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    news = []
    URL_BASE = "https://www.tecmundo.com.br/novidades"
    for index in range(1, pages + 1):
        url = URL_BASE + f"?page={index}"
        response_text = fetcher(url)
        selector = Selector(text=response_text)
        pages_url = selector.css(
            "h3.tec--card__title a.tec--card__title__link::attr(href)"
        ).getall()

        for page in pages_url:
            page_info = {}
            page_text = fetcher(page)
            page_selector = Selector(text=page_text)
            page_info["url"] = page
            page_info["title"] = page_selector.css(
                ".tec--article__header__title::text"
            ).get()
            page_info["timestamp"] = page_selector.css(
                "#js-article-date::attr(datetime)"
            ).get()
            page_info["writer"] = page_selector.css(
                ".tec--author__info__link::text"
            ).get()
            page_info["shares_count"] = content(
                page_selector.css(
                    "nav.tec--toolbar > div.tec--toolbar__item::text"
                ).re_first("\\d+")
            )

            page_info["comments_count"] = content(
                page_selector.css("#js-comments-btn::attr(data-count)").get()
            )

            page_info["summary"] = page_selector.css(
                ".tec--article__body > p:nth-child(1)::text"
            ).get()
            page_info["sources"] = page_selector.css(
                ".z--mb-16 > div > a::text"
            ).getall()
            page_info["categories"] = page_selector.css(
                "#js-categories > a::text"
            ).getall()
            news.append(page_info)

    return news
