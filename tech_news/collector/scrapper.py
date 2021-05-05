import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        resp = requests.get(url, timeout=timeout)
    except requests.RequestException:
        return ""
    else:
        if resp.status_code != 200:
            return ""
        sleep(delay)
        return resp.text


def scrape(fetcher, pages=1):
    links_all = []
    url_base = "https://www.tecmundo.com.br/novidades"
    url_dynamic = url_base
    for page_index in range(pages):
        array_link = get_links(url_dynamic, fetcher)
        links_all.extend(array_link)
        url_dynamic = url_base + "?pages=" + str(page_index + 2)
    result = []
    for link_page in links_all:
        text = fetcher(link_page)
        result.append(get_news(text, link_page))
    return result


def get_links(url, fetcher):
    selector = Selector(fetcher(url))
    return selector.css(
        'div.tec--list__item > article > figure > a::attr(href)'
        ).getall()


def get_news(text, link_page):
    selector = Selector(text)
    return {
        "url": link_page,
        "title": selector.css('#js-article-title::text').get().strip(),
        "timestamp": selector.css(
            '#js-article-date::attr(datetime)').get().strip(),
        "writer": selector.css(
            '.tec--author__info__link::text').get(),
        "shares_count": int(
            selector.css(
                'div.tec--toolbar__item:nth-child(1)::text'
            ).get().strip().split()[0]
        ),
        "comments_count": int(
            selector.css(
                '#js-comments-btn::attr(data-count)').get().strip()
        ),
        "summary": selector.css(
            '.tec--article__body > p:nth-child(1)::text'
            ).get().strip(),
        "sources": selector.css(
            'div.z--mb-16 > div > a::text'
            ).getall(),
        "categories": selector.css(
            '#js-categories > a::text'
            ).getall()
    }
