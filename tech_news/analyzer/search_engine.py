from tech_news import database
from datetime import datetime


def search_by_title(title):
    search_title = database.search_news({
        "title": {
            "$regex": title,
            "$options": "i",
        }
    })
    notices_list = []
    for item in search_title:
        notices_list.append((item['title'], item['url']))
    return notices_list


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        search_date = database.search_news({
            'timestamp': {
                '$regex': date
             }
        })
        notices_list = []
        for item in search_date:
            notices_list.append((item['title'], item['url']))
        return notices_list


def search_by_source(source):
    search_source = database.search_news({
        "sources": {
            "$regex": source,
            "$options": "i",
        }
    })
    notices_list = []
    for item in search_source:
        notices_list.append((item['title'], item['url']))
    return notices_list


def search_by_category(category):
    search_category = database.search_news({
        "categories": {
            "$regex": category,
            "$options": "i",
        }
    })
    notices_list = []
    for item in search_category:
        notices_list.append((item['title'], item['url']))
    return notices_list
