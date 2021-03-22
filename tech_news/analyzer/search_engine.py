import re
from tech_news.database import search_news


def search_by_title(title):
    q = {"title": {"$regex": title, "$options": "i"}}
    news = []
    for article in search_news(q):
        news.append((article['title'], article['url']))
    return news


def search_by_date(date):
    date_format = re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}')
    if not date_format.match(date):
        raise ValueError('Data inválida')
    q = {"timestamp": {"$regex": date}}
    news = []
    for article in search_news(q):
        news.append((article['title'], article['url']))
    return news


def search_by_source(source):
    q = {"sources": {"$regex": source, "$options": "i"}}
    news = []
    for article in search_news(q):
        news.append((article['title'], article['url']))
    return news


def search_by_category(category):
    q = {"categories": {"$regex": category, "$options": "i"}}
    news = []
    for article in search_news(q):
        news.append((article['title'], article['url']))
    return news
