from tech_news import database
from datetime import datetime


def search_by_title(title):
    search = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    if len(search) == 0:
        return []

    news = []
    for new in search:
        news.append((new["title"], new["url"]))
    return news


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        search = database.search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if len(search) == 0:
            return []

        news = []
        for new in search:
            news.append((new["title"], new["url"]))
        return news


def search_by_source(source):
    search = database.search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )

    if len(search) == 0:
        return []

    news = []
    for new in search:
        news.append((new["title"], new["url"]))
    return news


def search_by_category(category):
    search = database.search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )

    if len(search) == 0:
        return []

    news = []
    for new in search:
        news.append((new["title"], new["url"]))
    return news
