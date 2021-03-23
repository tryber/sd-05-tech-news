import requests
import time
import parsel


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=timeout)
    except requests.Timeout:
        return ""
    else:
        if response.status_code != 200:
            return ""
        time.sleep(delay)
        return response.text


# https://requests.readthedocs.io/en/master/user/advanced/#timeouts
# https://realpython.com/python-sleep/
# ver exemplos de reqs HTTP com Rate Limit e Time out do course 35-3


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""

    # 1. Preparar constante que será populada
    scrapped_news = []
    # 2. Preparar sistema de paginação
    # Neste caso, melhor com range do que com while porque sabemos onde parar
    for page in range(pages):
        URL_BASE = "https://www.tecmundo.com.br/novidades"
        page_url = f"?page={page}"
        full_url = URL_BASE + page_url
        selector = parsel.Selector(text=fetcher(full_url))
        # (isso porque o fetch_content jà retorna precisamente response.text)
        # 3. Pegar e armazenar cada elemento,
        # mais simples estarem todos dentro da url de detalhes da noticia
        # jà controlando e limpando eles (int, ::text, regexs)
        for url in selector.css(".tec--list__item h3 a::attr(href)").getall():
            selector_new = parsel.Selector(text=fetcher(url))
            title = selector_new.css(
                ".tec--article__header__title::text"
            ).get()
            timestamp = selector_new.css(
                "#js-article-date ::attr(datetime)"
            ).get()
            writer = selector_new.css(".tec--author__info__link ::text").get()
            shares_count_str = selector_new.css(
                    "div.tec--toolbar__item:nth-child(1)::text"
                ).re_first(r"[0-9]+")
            print(f"shares count is :{shares_count_str}")
            shares_count = int(shares_count_str)
            # ao testar, problema "none" porque tag nem sempre presente
            # (aqui escolha de css de contagens é dura porque varia entre news)
            comments_count_str = selector_new.css(
                "#js-comments-btn::text").re_first(r"[0-9]+")
            print(f"comments count is :{comments_count_str}")
            comments_count = int(comments_count_str)
            summary = selector_new.css(".tec--article__body *::text").get()
            sources = selector_new.css(".z--mb-16 a::text").getall()
            categories = selector_new.css(
                "a.tec--badge--primary::text"
            ).getall()
            # 4. Adicionar dados ao array inicial, a cada noticia
            scrapped_news.append(
                {
                    "url": url,
                    "title": title,
                    "timestamp": timestamp,
                    "writer": writer,
                    "shares_count": shares_count,
                    "comments_count": comments_count,
                    "summary": summary,
                    "sources": sources,
                    "categories": categories,
                }
            )
            # aqui deve ser escrito assim repetitivo para ser reconhecido dict
    # 5. Finalmente retornar array populado
    return scrapped_news

# Testado chamando scrape(fetcher=fetch_content, pages=2)

# Honestidade acadêmica, requisito 2:
# 1/ Ajuda do aluno Paulo Dandrea para os selector css,
# PR https://github.com/tryber/sd-05-tech-news/pull/2
# 2/ Uso do modelo course 35-3 "Recursos obtidos à partir de outro recurso"
