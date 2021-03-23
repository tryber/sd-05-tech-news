from tech_news import database
from datetime import datetime


REGEX = "$regex"
OPTIONS = "$options"


def search_by_title(title):
    NEWS = database.search_news({"title": {REGEX: title, OPTIONS: "-i"}})
    if len(NEWS) == 0:
        return NEWS

    return [(NEWS[0]["title"], NEWS[0]["url"])]


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")

        NEWS = database.search_news({"timestamp": {REGEX: date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if len(NEWS) == 0:
            return NEWS
        return [(NEWS[0]["title"], NEWS[0]["url"])]


def search_by_source(source):
    NEWS = database.search_news({"sources": {REGEX: source, OPTIONS: "-i"}})

    if len(NEWS) == 0:
        return NEWS

    return [(NEWS[0]["title"], NEWS[0]["url"])]


def search_by_category(category):
    NEWS = database.search_news(
        {"categories": {REGEX: category, OPTIONS: "-i"}}
    )

    if len(NEWS) == 0:
        return NEWS

    return [(NEWS[0]["title"], NEWS[0]["url"])]
