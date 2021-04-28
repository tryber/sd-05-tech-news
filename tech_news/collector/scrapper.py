"""LETS GET STARTED"""
import requests
import time
# from parse1 import Selector


# types = {
#     "link": "div.tec--list__item > article > figure > a::attr(href)",
#     "title": ".tec--article__header__title::text",
#     "timestamp": "#js-article-date::attr(datetime)",
#     "writer": ".tec--author__info__link::text",
#     "shares_count": ".tec--toolbar__item::text",
#     "comments_count": "#js-comments-btn::attr(data-count)",
#     "summary": ".tec--article__body p::text",
#     "sources": ".z--mb-16 a::text",
#     "categories": "#js-categories a::text",
# }


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        res = requests.get(url, timeout=timeout)
        time.sleep(delay)

        if res.status_code != 200:
            return ""

        return res.text

    except requests.Timeout:

        return ""


# def generator(url, types):
#     title = types.css(types["title"]).get()
#     timestamp = types.css(types["timestamp"]).get()
#     writer = types.css(types["writer"]).get()
#     shares_count = types.css(types["shares_count"]).re_first(r'\d') or "0"
#     comments_count = types.css(types["comments_count"]).get()
#     summary = types.css(types["summary"]).get()
#     sources = types.css(types["sources"]).getall()
#     categories = types.css(types["categories"]).getall()

#     return {
#         "url": url,
#         "title": title,
#         "timestamp": timestamp,
#         "writes": writer,
#         "shares_count": int(shares_count),
#         "comments_count": int(comments_count),
#         "summary": summary,
#         "sources": sources,
#         "categories": categories,
#     }


# def scrape(fetcher, pages=1):
#     """Seu código deve vir aqui"""
#     list = []
#     link = "https://www.tecmundo.com.br/novidades?page="

#     for page in range(pages):
#         res = fetcher(link)
#         selector = Selector(text=res)
#         news = selector.css(types.link).getall()

#         for new in news:
#             res_new = fetcher(new)
#             selector_new = Selector(text=res_new)
#             list.append(generator(new, selector_new))

#     return list
