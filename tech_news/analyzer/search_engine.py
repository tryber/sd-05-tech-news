from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    result = search_news({"title": title.title()})
    return [(one["title"], one["url"]) for one in result]


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        result = search_news({"timestamp": {"$regex": date}})
        return [(one["title"], one["url"]) for one in result]
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""
    result = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(one["title"], one["url"]) for one in result]


def search_by_category(category):
    """Seu código deve vir aqui"""
    result = search_news({"categories": {"$regex": category, "$options": "i"}})
    return [(one["title"], one["url"]) for one in result]
