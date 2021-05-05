import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        return ''
    else:
        if response.status_code != 200:
            return ''
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    base_url = 'https://www.tecmundo.com.br/novidades'
    scrapper_info = []

    for page_id in range(pages):
        url_page = f"?page={page_id}"
        full_url = base_url + url_page
        selector = Selector(text=fetcher(full_url))
        for link in selector.css(".tec--list__item h3 a::attr(href)").getall():
            individual_request = Selector(text=fetcher(link))
            title = individual_request.css(
                ".tec--article__header__title::text"
            ).get()
            timestamp = individual_request.css(
                "#js-article-date ::attr(datetime)"
            ).get()
            writer = individual_request.css(
                 ".tec--author__info__link ::text"
            ).get()
            shares_count = individual_request.css(
                    "div.tec--toolbar__item:nth-child(1)::text"
            ).re_first(r"[0-9]+")
            comments_count = individual_request.css(
                    "#js-comments-btn::text"
            ).re_first(r"[0-9]+")
            summary = individual_request.css(
                ".tec--article__body *::text"
            ).get()
            sources = individual_request.css(
                ".z--mb-16 a::text"
            ).getall()
            categories = individual_request.css(
                "a.tec--badge--primary::text"
            ).getall()

            scrapper_info.append(
                {
                    "url": link,
                    "title": title,
                    "timestamp": timestamp,
                    "writer": writer,
                    "shares_count": int(shares_count),
                    "comments_count": int(comments_count),
                    "summary": summary,
                    "sources": sources,
                    "categories": categories,
                }
            )

    return scrapper_info
