# Referências:
# https://stackoverflow.com/questions/10610131/checking-if-a-field-contains-a-string
# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python/16870699
# https://stackoverflow.com/questions/10700921/case-insensitive-search-with-in

from tech_news import database
import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""

    news = database.search_news({"title": {"$regex": title, "$options": "i"}})
    return [(item["title"], item["url"]) for item in news]


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news = database.search_news({"timestamp": {"$regex": date}})
        return [(item["title"], item["url"]) for item in news]


def search_by_source(source):
    """Seu código deve vir aqui"""
    news = database.search_news(
        {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}
    )
    return [(item["title"], item["url"]) for item in news]


def search_by_category(category):
    """Seu código deve vir aqui"""
    news = database.search_news(
        {"categories": {"$elemMatch": {"$regex": category, "$options": "i"}}}
    )
    return [(item["title"], item["url"]) for item in news]


if __name__ == "__main__":
    # search_by_title("VAMOSCOMTUDO")
    # print(search_by_date("2020-11-23"))
    # print(search_by_date("2019-12-12"))
    # print(search_by_date("21-12-1980"))
    print(search_by_source("ResetEra"))
    print(search_by_source("fonte_invalida"))
    print(search_by_source("RESETERA"))
