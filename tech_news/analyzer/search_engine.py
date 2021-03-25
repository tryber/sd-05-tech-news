import re
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    result = []
    allNews = search_news({"title": {"$regex": title, "$options": "i"}})
    for each in allNews:
        result.append((each["title"], each["url"]))
    return result


def search_by_date(date):
    """Seu código deve vir aqui"""
    date_format = re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}')
    if not date_format.match(date):
        raise ValueError('Data inválida')
    result = []
    allNews = search_news({"timestamp": {"$regex": date}})
    for each in allNews:
        result.append((each["title"], each["url"]))
    return result


def search_by_source(source):
    """Seu código deve vir aqui"""
    result = []
    allNews = search_news({"sources": {"$regex": source, "$options": "i"}})
    for each in allNews:
        result.append((each["title"], each["url"]))
    return result


def search_by_category(category):
    """Seu código deve vir aqui"""
    result = []
    allNews = search_news({
        "categories": {"$regex": category, "$options": "i"}
        })
    for each in allNews:
        result.append((each["title"], each["url"]))
    return result
