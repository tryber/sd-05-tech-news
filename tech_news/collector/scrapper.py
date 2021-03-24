import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.RequestException:
        return ""
    else:
        if response.status_code != 200:
            return ""
        return response.text


selectors = {
    "title": ".tec--article__header__title::text",
    "timestamp": "#js-article-date::attr(datetime)",
    "writer": "a.tec--author__info__link::text",
    "shares": ".tec--toolbar__item::text",
    "comments": "#js-comments-btn::attr(data-count)",
    "summary": ".tec--article__body p::text",
    "sources": ".z--mb-16 a::text",
    "categories": "#js-categories a::text",
    "news": ".tec--list__item .tec--card__title__link::attr(href)"
}


def create_element(url, selector):
    title = selector.css(selectors["title"]).get()
    timestamp = selector.css(selectors["timestamp"]).get()
    writer = selector.css(selectors["writer"]).get()
    shares_count = selector.css(selectors["shares"]).re_first(r'\d') or "0"
    comments_count = selector.css(selectors["comments"]).re_first(r'\d') or "0"
    summary = selector.css(selectors["summary"]).get()
    sources = selector.css(selectors["sources"]).getall()
    categories = selector.css(selectors["categories"]).getall()

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
    request_url = "https://www.tecmundo.com.br/novidades?page="
    news_list = []
    for page in range(1, pages + 1):
        url = f"{request_url}{page}"
        news_response = fetcher(url)
        news_selector = Selector(text=news_response)
        news = news_selector.css(selectors["news"]).getall()
        for article in news:
            article_response = fetcher(article)
            article_selector = Selector(text=article_response)
            news_list.append(create_element(article, article_selector))
    return news_list
