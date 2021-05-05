import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.Timeout:
        return ""
    else:
        return response.text


def get_news(unique_link, selector):
    return {
        "url": unique_link,
        "title": selector.css("#js-article-title::text").get().strip(),
        "timestamp": selector.css("#js-article-date::attr(datetime)")
        .get()
        .strip(),
        "writer": selector.css(".tec--author__info__link::text").get(),
        "shares_count": int(
            selector.css(".tec--toolbar__item:nth-child(1)::text")
            .get()
            .strip()
            .split()[0]
        ),
        "comments_count": int(
            selector.css("#js-comments-btn::attr(data-count)").get().strip()
        ),
        "summary": selector.css(".tec--article__body > p:nth-child(1)::text")
        .get()
        .strip(),
        "sources": selector.css(".z--mb-16 > div > a::text").getall(),
        "categories": selector.css("#js-categories > a::text").getall(),
    }


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    basic_url = "https://www.tecmundo.com.br/novidades"
    req = basic_url
    all_news = []
    for page in range(1, pages + 1):
        url = req
        res = fetcher(url)
        selectors = Selector(text=res)
        link_selector = selectors.css(
            "div.tec--list__item > article > figure > a::attr(href)"
        ).getall()
        for link in link_selector:
            response = fetcher(link)
            select = Selector(text=response)
            all_news.append(get_news(link, select))
        req = f"{basic_url}?page={page}"
    return all_news


# TRANSPARENCIA = feito com sid, zambelli e Yoshi
