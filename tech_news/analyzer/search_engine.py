from tech_news import database


def search_by_title(title):
    news = []
    titulo = database.search_news({
        "title": {
            "$regex": title,
            "$options": "i",
        }
    })

    for one in titulo:
        news.append((one["title"], one["url"]))
    return news


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
