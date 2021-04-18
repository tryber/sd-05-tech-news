from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    collect_titles = search_news({"title": {"$regex": title, "$options": "i"}})
    if collect_titles == []:
        return []
    search_title = []
    for item in collect_titles:
        search_title.append((item["title"], item["url"]))
    return search_title


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        collect_date = search_news({"timestamp": {"$regex": date}})
        if collect_date == []:
            return []
        news_by_date = []
        for item in collect_date:
            news_by_date.append((item["title"], item["url"]))
        return news_by_date
    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    """Seu código deve vir aqui"""
    collect_source = search_news({
        "sources":
            {"$regex": source, "$options": "i"}
    })
    if collect_source == []:
        return []
    search_title = []
    for item in collect_source:
        search_title.append((item["title"], item["url"]))
    return search_title


def search_by_category(category):
    """Seu código deve vir aqui"""
    collect_category = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    if collect_category == []:
        return []
    search_title = []
    for item in collect_category:
        search_title.append((item["title"], item["url"]))
    return search_title
