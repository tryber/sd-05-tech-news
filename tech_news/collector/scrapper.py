import requests
import time
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    request = requests.get(url, timeout=timeout)
    time.sleep(delay)
    status = request.status_code
    if status != 200:
        return ""
    return request.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    link = "https://www.tecmundo.com.br/novidades"
    results = []
    for page in range(1, pages+1):
        request = fetcher(f"{link}?page={page}")
        # print("url", f"{link}?page={page}")
        selector = Selector(text=request)
        list_news = selector.css(
            ".tec--list__item h3 a::attr(href)").getall()
        for each_news in list_news:
            response = fetcher(each_news)
            selector = Selector(text=response)
            url = each_news
            results.append(output_news(selector, url))
    return results


def output_news(selector, url):
    new = {}
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    writer = selector.css(
        "#js-author-bar p a.tec--author__info__link::text").get()
    summary = selector.css(
        ".tec--article__body p *::text").get()
    sources = selector.css("div.z--mb-16 div a::text").getall()

    shares_count = selector.css(".tec--toolbar__item::text").get()
    shares_count = to_number(str(shares_count).replace(" Compartilharam", ""))

    comments_count = selector.css(
        ".tec--toolbar__item #js-comments-btn::attr(data-count)").get()
    comments_count = to_number(comments_count)

    categories = selector.css("#js-categories a::text").getall()
    # print(title)
    new["url"] = url
    new["title"] = title
    new["timestamp"] = timestamp
    new["writer"] = writer
    new["shares_count"] = comments_count
    new["comments_count"] = comments_count
    new["summary"] = summary
    new["sources"] = sources
    new["categories"] = categories
    return new


def to_number(num):
    try:
        number = int(num)
    except Exception:
        number = 0
    finally:
        return number
