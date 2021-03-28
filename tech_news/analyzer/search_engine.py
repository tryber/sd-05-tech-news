from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    TITLE = {"title": title.title()}
    news = search_news(TITLE)
    if len(news) == 0:
        return []
    else:
        return [(news[0]["title"], news[0]["url"])]
    return news


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if len(news) == 0:
            return []
        else:
            return [(news[0]["title"], news[0]["url"])]


def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    if len(news) == 0:
        return []
    else:
        return [(news[0]["title"], news[0]["url"])]


def search_by_category(category):
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    if len(news) == 0:
        return []
    else:
        return [(news[0]["title"], news[0]["url"])]
