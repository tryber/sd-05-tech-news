from tech_news import database
import datetime


def search_by_title(title):
    data = database.search_news({"title": {"$regex": title, "$options": "i"}})
    if data == []:
        return []
    news = []
    for item in data:
        news.append((item["title"], item["url"]))
    return news


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        data = database.search_news({"timestamp": {"$regex": date}})
        if data == []:
            return []
        news = []
        for item in data:
            news.append((item["title"], item["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    return news


def search_by_source(source):
    data = database.search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    if data == []:
        return []
    news = []
    for item in data:
        news.append((item["title"], item["url"]))
    return news


def search_by_category(category):
    data = database.search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    if data == []:
        return []
    news = []
    for item in data:
        news.append((item["title"], item["url"]))
    return news
