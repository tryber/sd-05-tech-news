from parsel import Selector
import requests
from time import sleep


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ''
    else:
        return response.text


def scrape(fetcher, pages=1):
    site_url = 'https://www.tecmundo.com.br/novidades'
    news_to_return = []

    for page in range(1, pages + 1):
        if (page > 1):
            final_url = "{url}?page={page}".format(url=site_url, page=page)
        else:
            final_url = site_url

        selector = Selector(fetcher(final_url))
        found_urls = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()

        for found_url in found_urls:
            selector = Selector(fetcher(found_url))
            news_to_return.append(construct_news_object(found_url, selector))

    return news_to_return


def construct_news_object(url, selector):
    title = selector.css(
        ".tec--article__header__title::text"
    ).get()

    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = selector.css(
        "a.tec--author__info__link::text"
    ).get()

    shares_count = int(selector.css(
        ".tec--toolbar__item::text"
    ).re_first(r"\d") or "0")

    comments_count = int(selector.css(
        "#js-comments-btn::text"
    ).re_first(r"\d") or "0")

    summary = selector.css(
        ".tec--article__body > p::text"
    ).get()

    sources = selector.css(
        "div.z--mb-16 .tec--badge::text"
    ).getall()

    categories = selector.css(
        "#js-categories a::text"
    ).getall()

    news_object = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }
    return news_object
