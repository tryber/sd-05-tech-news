from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    article = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(header["title"], header["url"]) for header in article]


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
