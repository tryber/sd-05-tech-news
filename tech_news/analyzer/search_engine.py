from tech_news import database
from datetime import datetime


def search_by_title(title):
    #   ref1
    noticias = []
    pesquisa_por_titulo = database.search_news({
        "title": {
            "$regex": title,
            "$options": "i",
        }
    })

    for item in pesquisa_por_titulo:
        noticias.append((item["title"], item["url"]))
    return noticias


def search_by_date(date):
    #   2020-11-23 - exemplo
    #   ref2:
    noticias = []
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        noticias = database.search_news({
            "timestamp": {
                "$regex": date
            }
        })
    return [(item["title"], item["url"]) for item in noticias]


def search_by_source(source):
    noticias = database.search_news({
        "sources": {
            "$regex": source,
            "$options": "i",
        }
    })
    return [(item["title"], item["url"]) for item in noticias]


def search_by_category(category):
    noticias = database.search_news({
        "categories": {
            "$regex": category,
            "$options": "i",
        }
    })
    return [(item["title"], item["url"]) for item in noticias]


#   ref1: https://docs.mongodb.com/manual/reference/operator/query/regex/
#   ref2: https://www.programiz.com/python-programming/datetime/strptime
#   https://docs.mongodb.com/manual/reference/operator/query/in/
