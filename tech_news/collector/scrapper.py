import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)

    except requests.RequestException:
        return ""

    else:

        if response.status_code != 200:
            return ""

        sleep(delay)
        return response.text


itens = {
    "card": ".tec--card",
    "link": "div.tec--list__item > article > figure > a::attr(href)",
    "title": ".tec--card__title",
    "shares_count": "div.tec--toolbar__item:nth-child(1)::text",
    "comments_count": "#js-comments-btn::attr(data-count)",
    "sources": ".z--mb-16 > div > a::text",
    "categories": "a.tec--badge--primary::text",
    "summary": ".tec--article__body > p:nth-child(1)::text",
}


def scraper(texto):
    seletor = Selector(text=texto["texto"])
    datetime = seletor.css("#js-article-date::attr(datetime)").get().strip()
    s = seletor.css(itens["shares_count"]).get().strip()
    c = seletor.css("#js-comments-btn::attr(data-count)").get().strip()
    m = seletor.css(itens["sources"]).getall()
    return {
        "url": texto["url"],
        "title": seletor.css("#js-article-title::text").get().strip(),
        "timestamp": datetime,
        "writer": seletor.css(".tec--author__info__link::text").get(),
        "shares_count": int(s.split()[0]),
        "comments_count": int(c),
        "summary": seletor.css(itens["summary"]).get()
        .strip(),
        "sources": [source for source in m],
        "categories": seletor.css("a.tec--badge--primary::text").getall()
    }


def scrape(fetcher, pages=1):
    url = "https://www.tecmundo.com.br/novidadess"
    page_links = []
    texts_links = []
    result = []
    # Get all links per page
    for page_num in range(pages):
        seletor = Selector(text=fetcher(url))
        page_links.extend(seletor.css(itens["link"]).getall())
        url += f'?pages={page_num+2}'
    for link in page_links:
        texts_links.append({"texto": fetcher(link), "url": link})
    for text in texts_links:
        result.append(scraper(text))
    return result
