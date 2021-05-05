from tech_news import database
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    news = database.search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = database.search_news({"timestamp": {"$regex": date, "$options": "i"}})
    except ValueError:
        raise ValueError("Data inválida")
        if len(news) == 0:
            return []
    return [(new["title"], new["url"]) for new in news]


def search_by_source(source):
    """Seu código deve vir aqui"""
    news = database.search_news({"sources": {"$regex": source, "$options": "i"}})
    if len(news) == 0:
        return []
    return [(new["title"], new["url"]) for new in news]


def search_by_category(category):
    """Seu código deve vir aqui"""
    news = database.search_news({"categories": {"$regex": category, "$options": "i"}})
    if len(news) == 0:
        return []
    return [(new["title"], new["url"]) for new in news]
