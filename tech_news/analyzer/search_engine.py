from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):

    news = search_news({"title": {"$regex": title, "$options": "i"}})
    print(news)
    return [(item["title"], item["url"]) for item in news]


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")

    if len(news) == 0:
        return []

    return [(item["title"], item["url"]) for item in news]


def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    if len(news) == 0:
        return []
    return [(item["title"], item["url"]) for item in news]


def search_by_category(category):
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    if len(news) == 0:
        return []
    return [(item["title"], item["url"]) for item in news]
