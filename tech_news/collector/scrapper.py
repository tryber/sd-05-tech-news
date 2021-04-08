import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    else:
        return response.text


def news(url, selector_noticia):
    title = selector_noticia.css("h1.tec--article__header__title::text")
    timestamp = selector_noticia.css(
        "div.tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = selector_noticia.css(".tec--author__info__link::text").get()
    shares_count = (
        selector_noticia.css(".tec--toolbar__item::text").re_first(r"\d")
        or "0"
    )
    comments_count = (
        selector_noticia.css("#js-comments-btn::attr(datacount)").re_first(
            r"\d"
        )
        or "0"
    )
    summary = selector_noticia.css(".tec--article__body p::text").get()
    sources = selector_noticia.css(".z--mb-16 a::text").getall()
    categories = selector_noticia.css("#js-categories a::text").getall()

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
    url_tec = "https://www.tecmundo.com.br/novidades"
    all = []
    for page in range(pages):
        response = fetcher(url_tec)
        selector = Selector(text=response)
        noticias = selector.css(
            "div.tec--list__item > article > figure > a::attr(href)"
        ).getall()
        for noticia in noticias:
            response_noticia = fetcher(noticia)
            selector_noticia = Selector(text=response_noticia)
            all.append(news(noticia, selector_noticia))
    return all
