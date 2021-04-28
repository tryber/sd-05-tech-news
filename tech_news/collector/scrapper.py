import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException:
        return ""
    else:
        success_status = 200
        if response.status_code != success_status:
            return ""
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    base_url = "https://www.tecmundo.com.br/novidades"
    page_path = "?page="

    news = []
    index = 1
    while index <= pages:
        content = fetcher(f"{base_url}{page_path}{index}")
        selector = Selector(content)
        items = selector.css(".tec--list__item")
        for list_item in items:
            url = list_item.css("h3 a::attr(href)").get()
            details_content = fetcher(url)
            details_selector = Selector(details_content)
            title = details_selector.css("#js-article-title::text").get()
            timestamp = details_selector.css(
                ".tec--timestamp__item time::attr(datetime)"
            ).get()
            writer = details_selector.css(
                ".tec--author__info__link::text"
            ).get()
            shares = details_selector.css("button::attr(data-count)").get()
            comments = details_selector.css(
                ".tec--btn::attr(data-count)"
            ).getall()
            summary = details_selector.css(
                ".tec--article__body > p::text"
            ).get()
            sources = details_selector.css(".z--mb-16 > div a::text").getall()
            categories = details_selector.css(
                "#js-categories a::text"
            ).getall()

            notice = {
                "url": url,
                "title": title,
                "timestamp": timestamp,
                "writer": writer,
                "shares_count": int(shares),
                "comments_count": int(comments[0]),
                "summary": summary,
                "sources": sources,
                "categories": categories,
            }

            news.append(notice)

        index += 1

    print("news length", len(news))
    return news
