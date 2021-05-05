import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        res = requests.get(url, timeout=timeout)
    except requests.RequestException:
        return ""
    else:
        if res.status_code != 200:
            return ""
    sleep(delay)
    return res.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    links = []
    news_url = "https://www.tecmundo.com.br/novidades"
    url_dinamic = news_url
    for page_index in range(pages):
        links.extend(get_links(url_dinamic, fetcher))
        url_dinamic = news_url + "?pages=" + str(page_index + 2)
        result = []
    for unique_link in links:
        text = fetcher(unique_link)
        result.append(get_news(text, unique_link))
    return result


def get_news(text, unique_link):
    selector = Selector(text)
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


def get_links(url, fetcher):
    selector = Selector(fetcher(url))
    array_selector = selector.css(
        "div.tec--list__item > article > figure > a::attr(href)"
    ).getall()
    return array_selector
