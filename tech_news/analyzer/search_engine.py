from datetime import datetime
from ..database import search_news


def search_by_key(key, query):
    result = search_news({key: {"$regex": query, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]


def search_by_title(title):
    return search_by_key("title", title)


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return search_by_key("timestamp", date)
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    return search_by_key("sources", source)


def search_by_category(category):
    return search_by_key("categories", category)
