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
    url = "https://www.tecmundo.com.br/novidades"
    results = []
    for page in range(pages):
        print(url)
        response = fetcher(url)
        selector = Selector(text=response)
        news_urls = selector.css(
            "div.tec--list__item > article > figure > a::attr(href)"
        ).getall()
        for single_url in news_urls:
            response_new = fetcher(single_url)
            selector_new = Selector(text=response_new)
            build_scrap = builder(selector_new)
            corrected_scrap = correction(
                build_scrap["shares_count"],
                build_scrap["comments_count"],
                build_scrap["summary"],
            )

            new_result = {
                "url": single_url,
                "title": build_scrap["title"],
                "timestamp": build_scrap["timestamp"],
                "writer": build_scrap["writer"],
                "shares_count": corrected_scrap["shares_count"],
                "comments_count": corrected_scrap["comments_count"],
                "summary": corrected_scrap["summary"],
                "sources": build_scrap["sources"],
                "categories": build_scrap["categories"],
            }
            results.append(new_result)
            url += f"?page={page+2}"

    return results


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
