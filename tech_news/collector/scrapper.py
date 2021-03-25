import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    else:
        if response.status_code != 200:
            return ""
        return response.text


def scrape(fetcher=fetch_content, pages=1):
    """Seu código deve vir aqui"""
    content_list = []
    url_base = "https://www.tecmundo.com.br/novidades"
    for index in range(1, pages+1):
        respon = fetcher(f"{url_base}?page={index}")
        selector = Selector(respon)
        href = selector.css(".tec--card__title__link::attr(href)").getall()

        for link in href:
            detail_response = fetcher(link)
            detail_selector = Selector(detail_response)
            title = detail_selector.css(
                ".tec--article__header__title::text"
                ).get()
            timestamp = detail_selector.css(
                "#js-article-date::attr(datetime)"
                ).get()
            writer = detail_selector.css(
                ".tec--author__info__link::text"
            ).get()
            shares_count = detail_selector.css(
                ".tec--toolbar__item::text"
                ).re_first(r"\d") or "0"
            comments_count = detail_selector.css(
                "#js-comments-btn::text"
                ).re_first(r"\d") or "0"
            summary = detail_selector.css(
                ".tec--article__body > p::text"
                ).get()
            sources = detail_selector.css(
                "div.z--mb-16 .tec--badge::text"
                ).getall()
            categories = detail_selector.css(
                "#js-categories a::text"
                ).getall()
            assembly = {
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
            content_list.append(assembly)
    return content_list
