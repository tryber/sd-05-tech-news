from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    article = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(header["title"], header["url"]) for header in article]


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    if len(news) == 0:
        return []
    return [(item["title"], item["url"]) for item in news]


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
