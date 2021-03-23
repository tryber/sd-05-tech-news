import requests
from time import sleep
from parsel import Selector


BASE_URL = "https://www.tecmundo.com.br/novidades?page="


ELEMENTS = {
    "title": ".tec--article__header__title::text",
    "time": "#js-article-date::attr(datetime)",
    "writer": "a.tec--author__info__link::text",
    "share": ".tec--toolbar__item::text",
    "comments": "#js-comments-btn::attr(data-count)",
    "summary": ".tec--article__body p::text",
    "sources": ".z--mb-16 .tec--badge::text",
    "categories": "#js-categories a::text"
}


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except (requests.HTTPError, requests.exceptions.ReadTimeout):
        print("Nothing found.")
        return ""
    else:
        if response.status_code != 200:
            return ""
        return response.text


def parse_elements(url, selector):
    title = selector.css(ELEMENTS["title"]).get()
    time = selector.css(ELEMENTS["time"]).get()
    writer = selector.css(ELEMENTS["writer"]).get()
    shares_count = selector.css(ELEMENTS["share"]).re_first(r'\d') or "0"
    comments_count = selector.css(ELEMENTS["comments"]).get() or "0"
    summary = selector.css(ELEMENTS["summary"]).extract_first()
    sources = selector.css(ELEMENTS["sources"]).getall()
    categories = selector.css(ELEMENTS["categories"]).getall()

    return {
        "url": url,
        "title": title,
        "timestamp": time,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


def parse_content(urls, fetcher):
    content = []

    for url in urls:
        page = fetcher(url)
        selector = Selector(page)
        content.append(parse_elements(url, selector))

    return content


def scrape(fetcher, pages=1):
    result = []

    for page in range(1, pages + 1):
        fetch_page = fetcher(BASE_URL + str(page))
        content = Selector(fetch_page)
        urls = content.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
            ).getall()
        result.extend(parse_content(urls, fetcher))

    return result
