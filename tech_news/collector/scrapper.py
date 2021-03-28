import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        return ""
    else:
        code_success = 200
        if response.status_code != code_success:
            return ""
        return response.text

    finally:
        sleep(delay)


def scrape(fetcher, pages=1):
    news = []
    URL_BASE = "https://www.tecmundo.com.br/novidades"
    for index in range(1, pages + 1):
        url = URL_BASE + f"?page={index}"
        response_text = fetcher(url)
        selector = Selector(text=response_text)
        news_links = selector.css(
            "h3.tec--card__title a.tec--card__title__link::attr(href)"
        ).getall()
        for page in news_links:
            news_selector = Selector(text=fetcher(page))
            news_title = news_selector.css(
                ".tec--article__header__title::text"
            ).get()
            news_data = news_selector.css(
                "#js-article-date ::attr(datetime)"
            ).get()
            news_author = news_selector.css(
                ".tec--author__info__link ::text"
            ).get()
            news_shares_count = (
                news_selector.css("div.tec--toolbar__item::text").re_first(
                    "\\d+"
                )
                or "0"
            )
            news_comments_count = (
                news_selector.css("#js-comments-btn::attr(data-count)").get()
                or "0"
            )
            news_summary = news_selector.css(
                ".tec--article__body *::text"
            ).get()
            news_sources = news_selector.css(
                ".z--mb-16 a::text"
            ).getall()
            news_categories = news_selector.css(
                "a.tec--badge--primary::text"
            ).getall()

            news.append(
                {
                    "url": page,
                    "title": news_title,
                    "timestamp": news_data,
                    "writer": news_author,
                    "shares_count": int(news_shares_count),
                    "comments_count": int(news_comments_count),
                    "summary": news_summary,
                    "sources": news_sources,
                    "categories": news_categories,
                }
            )
    return news
