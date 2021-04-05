from tech_news import database


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
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
