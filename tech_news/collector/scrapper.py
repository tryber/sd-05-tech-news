import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
    except requests.Timeout:
        return ""
    else:
        if (response.status_code != 200):
            return ""
        sleep(delay)
        return response.text


def scrape(fetcher, pages=1):
    url = "https://www.tecmundo.com.br/novidades"
    saida = []
    for page in range(pages):
        response = fetcher(url)
        selector = Selector(text=response)
        lista_noticias = selector.css(
            "div.tec--list__item > article > figure > a::attr(href)"
            ).getall()
#        print(lista_noticias)
        for url_noticia in lista_noticias:
            print(url_noticia)
            response_noticia = fetcher(url_noticia)
            selector_noticia = Selector(text=response_noticia)
            saida.append(retorna_objeto(url_noticia, selector_noticia))
    return saida


def retorna_objeto(url, selector_noticia):
    title = selector_noticia.css("h1.tec--article__header__title::text").get()
    # print("eis o title:", title)

    timestamp = selector_noticia.css(
        "div.tec--timestamp__item time::attr(datetime)"
        ).get()
    # print("eis o timestamp", timestamp)

    writer = selector_noticia.css(".tec--author__info__link::text").get()
    # print("eis o writer", writer)

    shares_count = selector_noticia.css(
        ".tec--toolbar__item::text"
        ).re_first(r"\d") or "0"
    # print("eis o shares_count", shares_count)

    comments_count = selector_noticia.css(
        "#js-comments-btn::attr(datacount)"
        ).re_first(r"\d") or "0"
    # print("eis o comments_count", comments_count)

    summary = selector_noticia.css(".tec--article__body p::text").get()
    # print("eis o summary", summary)

    sources = selector_noticia.css(".z--mb-16 a::text").getall()
    # print("eis o sources", sources)

    categories = selector_noticia.css("#js-categories a::text").getall()
    # print("eis o categories", categories)

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories
    }

#   https://parsel.readthedocs.io/en/latest/usage.html - re_first
#   página que contem o compartilhar:
#   https://www.tecmundo.com.br/software/204759-windows-10-veja-desabilitar-bing-buscas-sistema.htm
#   http://turing.com.br/material/regex/introducao.html
