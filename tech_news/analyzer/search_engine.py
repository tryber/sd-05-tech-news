from datetime import datetime
from tech_news.database import search_news


# search_news(query): return list(db.news.find(query))
def search_by_title(title):
    # Method The title() method returns a string
    # where the first character in every word is upper case.
    busca = search_news({"title": title.title()})
    if len(busca) == 0:
        return []
    return [(busca[0]["title"], busca[0]["url"])]


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        busca = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if len(busca) == 0:
            return []
        return [(busca[0]["title"], busca[0]["url"])]


def search_by_source(source):
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    # options i - Case insensitivity to match upper and lower cases
    busca = search_news({"sources": {"$regex": source, "$options": "i"}})
    if len(busca) == 0:
        return []
    return [(busca[0]["title"], busca[0]["url"])]


def search_by_category(category):
    busca = search_news({"categories": {"$regex": category, "$options": "i"}})
    if len(busca) == 0:
        return []
    return [(busca[0]["title"], busca[0]["url"])]
