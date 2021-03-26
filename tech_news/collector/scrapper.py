import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ""
    if response.status_code == 200:
        return response.text
    else:
        return ""


def scrape(fetcher, pages=1):
    base_url = "https://www.tecmundo.com.br/novidades"
    selector = Selector(fetcher(base_url))
    urls = selector.css(".tec--card__info h3 a::attr(href)").getall()
    news_list = []

    for url in urls:
        content = fetcher(url)
        selector = Selector(text=content)
        title = selector.css("#js-article-title::text").get()
        writer = selector.css(".tec--author__info__link::text").get()
        shares_count = selector.css("button::attr(data-count)").get()
        comments_count = selector.css(".tec--btn::attr(data-count)").get()
        timestamp = selector.css(
            ".tec--timestamp__item time::attr(datetime)"
        ).get()
        summary = selector.css(".tec--article__body > p::text").get()
        sources = selector.css(".z--mb-16 > div a::text").getall()
        categories = selector.css("#js-categories a::text").getall()

        news_list.append(
            {
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
        )

    return news_list
