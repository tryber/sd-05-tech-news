from parsel import Selector
import requests
from time import sleep


def count_shares(text=''):
    text = ''.join(text)
    start = text.find('</svg>')
    end = text.find('Compartilharam\n')
    return int([int(s) for s in text[start:end].split() if s.isdigit()][0])


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        return ""
    else:
        if response.status_code != 200:
            return ""
        sleep(delay)
        return response.text


def digest_content(link_url, article):
    return {
        "url": link_url,
        "title": article.css("#js-article-title::text").get(),
        "timestamp": article.css("#js-article-date").attrib['datetime'],
        "shares_count": count_shares(
          article.css(".tec--toolbar .tec--toolbar__item").getall()
        ),
        "comments_count": int(
          article.css("#js-comments-btn").attrib['data-count']
        ),
        "summary": article.css(
          ".tec--article__body > p::text"
        ).getall()[0].strip(),
        "categories": article.css("#js-categories a::text").getall(),
        "sources": article.css(".z--mb-16 .tec--badge::text").getall(),
        "writer": article.css(".tec--author__info__link::text").get(),
    }


def scrape(fetcher=fetch_content, pages=1):
    base_url = "https://www.tecmundo.com.br/novidades?page=$p"
    results = []
    try:
        for page in range(pages):
            blog_pages = fetcher(base_url.replace("$p", str(page)))
            selector = Selector(text=blog_pages)
            link_list = selector.css("div.tec--list h3 a::attr(href)").getall()
            for link_url in link_list:
                article_page = fetcher(link_url)
                article = Selector(text=article_page)
                results.append(
                  digest_content(link_url, article)
                )
    finally:
        return results
