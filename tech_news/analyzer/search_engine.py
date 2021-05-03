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
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
