from tech_news import database
from datetime import datetime


def search_by_title(title):
    news = []
    titulo = database.search_news(
        {
            "title": {
                "$regex": title,
                "$options": "i",
            }
        }
    )

    for one in titulo:
        news.append((one["title"], one["url"]))
    return news


def search_by_date(date):
    news = []
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news = database.search_news({"timestamp": {"$regex": date}})
    return [(one["title"], one["url"]) for one in news]


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
