from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    title = {"title": title.title()}
    search = search_news(title)
    if search == []:
        return []
    news = [(search[0]["title"], search[0]["url"])]
    return news


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        search = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if search == []:
            return []
        news = [(search[0]["title"], search[0]["url"])]
        return news


def search_by_source(source):
    """Seu código deve vir aqui"""
    search = search_news({"sources": {"$regex": source, "$options": "i"}})
    if search == []:
        return []
    news = [(search[0]["title"], search[0]["url"])]
    return news


def search_by_category(category):
    """Seu código deve vir aqui"""
    search = search_news({"categories": {"$regex": category, "$options": "i"}})
    if search == []:
        return []
    news = [(search[0]["title"], search[0]["url"])]
    return news
