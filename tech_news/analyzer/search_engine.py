from tech_news import database
from datetime import datetime


def search_by_title(title):
    search_news = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )

    if len(search_news) == 0:
        return []

    return [(search_news[0]["title"], search_news[0]["url"])]


# https://docs.python.org/3/library/datetime.html
def search_by_date(date):
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            news_collection = []
            search_news = database.search_news({"timestamp": {"$regex": date}})
            print(search_news)

            for news in search_news:
                news_collection.append((news["title"], news["url"]))

            return news_collection
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    search_news = database.search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )

    if len(search_news) == 0:
        return []

    return [(search_news[0]["title"], search_news[0]["url"])]


def search_by_category(category):
    search_news = database.search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )

    if len(search_news) == 0:
        return []

    return [(search_news[0]["title"], search_news[0]["url"])]
