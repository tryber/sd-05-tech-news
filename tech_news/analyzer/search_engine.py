from tech_news import database
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    news = database.search_news({"title": {"$regex": title, "$options": "-i"}})
    if len(news) == 0:
        return news
    return [(news[0]["title"], news[0]["url"])]


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = database.search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if len(news) == 0:
            return news
    return [(news[0]["title"], news[0]["url"])]


def search_by_source(source):
    """Seu código deve vir aqui"""
    news = database.search_news(
        {"sources": {"$regex": source, "$options": "-i"}}
    )

    if len(news) == 0:
        return news

    return [(news[0]["title"], news[0]["url"])]


def search_by_category(category):
    """Seu código deve vir aqui"""
    news = database.search_news(
        {"categories": {"$regex": category, "$options": "-i"}}
    )

    if len(news) == 0:
        return news
    return [(news[0]["title"], news[0]["url"])]
