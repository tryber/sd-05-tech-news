import requests
from parsel import Selector
from time import sleep

Classes = {
    "card": ".tec--card",
    "link": "div.tec--list__item > article > figure > a::attr(href)",
    "title": ".tec--card__title",
    "shares_count": "div.tec--toolbar__item:nth-child(1)::text",
    "comments_count": "#js-comments-btn::attr(data-count)",
    "sources": ".z--mb-16 > div > a::text",
    "categories": "a.tec--badge--primary::text",
    "summary": ".tec--article__body > p:nth-child(1)::text",
}


def fetch_content(url, timeout=3, delay=0.5):
    """
    Seu código deve vir aqui.
    url: url a ser acessada
    timeout: tempo de espera da requisição
    delay: tempo de espera antes de efetuar uma requisição
    """
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException:
        print("deu ruim mano")
        return ""
    else:
        if response.status_code != 200:
            return ""
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    """
    Seu código deve vir aqui.
    fetcher: Função para buscar os dados.
    pages: quantidade de patinas a serem raspadas.
    """
    url = "https://www.tecmundo.com.br/novidadess"
    news_links = []
    all_news = []
    parsed_news = []
    for pageId in range(pages):
        selector = Selector(text=fetcher(url))
        news_links.extend(selector.css(Classes["link"]).getall())
        url += f"?pages={pageId+2}"
    for link in news_links:
        all_news.append({"url": link, "response": fetcher(link)})
    for news in all_news:
        parsed_news.append(parse_news(news))
    return parsed_news


def parse_news(news):
    selector = Selector(text=news["response"])
    title = selector.css("#js-article-title::text").get().strip()
    timestamp = selector.css("#js-article-date::attr(datetime)").get().strip()
    writer = selector.css(".tec--author__info__link::text").get()
    shares_count = selector.css(Classes["shares_count"]).get().strip()
    shares_count = int(shares_count.split()[0])
    summary = selector.css(Classes["summary"]).get().strip()
    comments_count = selector.css(Classes["comments_count"]).get()
    comments_count = int(comments_count)
    sources = selector.css(Classes["sources"]).getall()
    sources = [src for src in sources]
    categories = selector.css(Classes["categories"]).getall()
    return {
        "url": news["url"],
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "summary": summary,
        "comments_count": comments_count,
        "sources": sources,
        "categories": categories,
    }
