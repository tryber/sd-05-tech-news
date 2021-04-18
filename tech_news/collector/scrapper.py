import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        sleep(delay)
    except requests.exceptions.RequestException:
        return ""
    else:
        return response.text


def scrape_new(url, selector):
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    writer = selector.css("a.tec--author__info__link::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d")
    if shares_count is None:
        shares_count = "0"
    comments_count = selector.css("#js-comments-btn::text").re_first(r"\d")
    if comments_count is None:
        comments_count = "0"
    summary = selector.css(".tec--article__body > p::text").get()
    sources = selector.css("div.z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories a::text").getall()
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
    """Seu código deve vir aqui"""
    news = []
    for pages in range(1, pages + 1):
        selector = Selector(
            fetcher(f"https://www.tecmundo.com.br/novidades?page={pages}")
            )
        get_url = selector.css(
            ".tec--list__item .tec--card__title__link::attr(href)"
        ).getall()
        for url in get_url:
            selector = Selector(fetcher(url))
            news.append(scrape_new(url, selector))
    return news
