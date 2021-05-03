from tech_news.database import search_news


def search_by_title(title):

    news = search_news({"title": {"$regex": title, "$options": "i"}})
    print(news)
    return [(item["title"], item["url"]) for item in news]


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
