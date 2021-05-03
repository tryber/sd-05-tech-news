from tech_news import database
from datetime import datetime


def search_by_title(title):
    by_title = database.search_news(
        {"title": {"$regex": title, "$options": "-i"}})
    # for news in by_title:
    if len(by_title) == 0:
        return []
    return [(by_title[0]["title"], by_title[0]["url"])]


def search_by_date(date):
    response = []
    try:
        datetime.strptime(date, "%Y-%m-%d")
        # print(date_checked)
    except ValueError:
        raise ValueError("Data inválida")
    else:
        by_date = database.search_news({"timestamp": {"$regex": date}})
        if len(by_date) == 0:
            return []
        for news in by_date:
            response.append((news["title"], news["url"]))
        return response


def search_by_source(source):
    by_source = database.search_news(
        {"sources": {"$regex": source, "$options": "-i"}})
    # for news in by_title:
    if len(by_source) == 0:
        return []
    return [(by_source[0]["title"], by_source[0]["url"])]


def search_by_category(category):
    by_category = database.search_news(
        {"categories": {"$regex": category, "$options": "-i"}})
    # for news in by_title:
    if len(by_category) == 0:
        return []
    return [(by_category[0]["title"], by_category[0]["url"])]
