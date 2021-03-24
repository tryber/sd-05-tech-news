# Organizei/refatorei com ajuda do repo do Rodrigo
import requests
from parsel import Selector
from time import sleep


URL = 'https://www.tecmundo.com.br/novidades'


def fetch_content(url=URL, timeout=3, delay=0.5, page=1):
    try:
        response = requests.get(url, timeout=timeout)
        if (response.status_code != 200):
            return ''
        sleep(delay)
        return response.text
    except OSError:
        print('Deu algum erro')
        return ''


def scrape(fetcher, pages=1):
    url = "https://www.tecmundo.com.br/novidades"
    main_list = []
    for page in range(pages):
        resp = fetcher(url=url)
        selector = Selector(text=resp)
        h3 = 'h3[class=tec--card__title]'
        classe = 'a.tec--card__title__link::attr(href)'
        trash_list = selector.css(f'{h3} {classe}').extract()
        print(len(trash_list))
        for x in trash_list:
            response = fetcher(url=x)
            selector2 = Selector(text=response)
            build_scrap = builder(selector2)
            corrected_scrap = correction(
                build_scrap["shares_count"],
                build_scrap["comments_count"],
                build_scrap["summary"],
            )

            new_result = {
                "url": x,
                "title": build_scrap["title"],
                "timestamp": build_scrap["timestamp"],
                "writer": build_scrap["writer"],
                "shares_count": corrected_scrap["shares_count"],
                "comments_count": corrected_scrap["comments_count"],
                "summary": corrected_scrap["summary"],
                "sources": build_scrap["sources"],
                "categories": build_scrap["categories"],
            }
            main_list.append(new_result)
            url += f"?page={page+2}"
    print(main_list)
    return main_list


def correction(shares_count, comments_count, summary):
    if shares_count and shares_count[0] != "":
        shares_count = int("".join(shares_count))
    else:
        shares_count = 0
    if comments_count and comments_count != "None":
        comments_count = int(comments_count)
    else:
        comments_count = 0
    if summary != "":
        summary = "".join(summary)

    return {
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
    }


def builder(selector_new):
    title = selector_new.css("h1.tec--article__header__title::text").get()

    timestamp = selector_new.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()

    writer = selector_new.css(
        "div.tec--author__info a.tec--author__info__link::text"
    ).get()

    shares_count = selector_new.css("div.tec--toolbar__item::text").re(r"\d")

    comments_count = selector_new.css(
        "div.tec--toolbar__item button.tec--btn::attr(data-count)"
    ).get()

    summary = selector_new.css(
        "div.tec--article__body p:first-child *::text"
    ).getall()

    sources = selector_new.css(
        ".z--mb-16 > div > a::text"
    ).getall()
    categories = selector_new.css("#js-categories > a::text").getall()

    return {
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


scrape(fetcher=fetch_content, pages=1)
