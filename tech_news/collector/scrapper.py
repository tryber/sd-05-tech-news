import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except (requests.HTTPError, requests.ReadTimeout):
        return ""
    else:
        return response.text    


def container(url_page, res_article):
    sel_article = Selector(text=res_article)
    title = sel_article.css("#js-article-title::text").get()
    timestamp = sel_article.css("#js-article-date::attr(datetime)").get()
    writer = sel_article.css(".tec--author__info__link::text").get()
    shares_count = sel_article.css(
        "div.tec--toolbar__item:nth-child(1)::text"
    ).get().strip()
    shares_count = int(shares_count.split()[0])
    summary = sel_article.css(
            ".tec--article__body > p:nth-child(1)::text"
    ).get().strip()
    comments_count = sel_article.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    comments_count = int(comments_count)
    sources = sel_article.css(".z--mb-16 .tec--badge::text").getall()
    sources = [source for source in sources]
    categories = sel_article.css("#js-categories a::text").getall()

    return {
        "url": url_page,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "summary": summary,
        "comments_count": comments_count,
        "sources": sources,
        "categories": categories,
    }


def scrape(fetcher=fetch_content, pages=1):
    results = []
    news_url = []
    url_base = "https://www.tecmundo.com.br/novidadess"
    for page in range(pages):
        response = fetcher(url_base)
        select = Selector(text=response)
        news_url.extend(select.css(
            "div.tec--list h3 a::attr(href)"
        ).getall())
        url_base += f"?pages={page+1}"
    for url_page in news_url:
        res_article = fetcher(url_page)
        results.append(container(url_page, res_article))
    return results
