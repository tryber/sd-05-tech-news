from tech_news.database import search_news
import datetime


def title_url_tuple_maker(data):

    tuples = []

    for news in data:
        tuples.append((news["title"], news["url"]))

    return tuples


# Case insensitive options
# https://docs.mongodb.com/manual/reference/operator/query/regex/


def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return title_url_tuple_maker(news_list)


def search_by_date(date):
    try:
        # https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python/16870699
        datetime.datetime.strptime(date, "%Y-%m-%d")
        result = search_news({"timestamp": {"$regex": date, "$options": "im"}})

        return title_url_tuple_maker(result)

    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    news_list = search_news({"sources": {"$regex": source, "$options": "i"}})
    return title_url_tuple_maker(news_list)


def search_by_category(category):
    news_list = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    return title_url_tuple_maker(news_list)
