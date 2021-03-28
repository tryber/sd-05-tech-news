from tech_news import database
import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    title_news = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    filtered_news = []
    for news in title_news:
        filtered_news.append((news['title'], news['url']))
    return filtered_news


def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        year, month, day = date.split('-')
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news_by_date = database.search_news({"timestamp": {"$regex": date}})
        return([(news["title"], news["url"]) for news in news_by_date])


def search_by_source(source):
    """Seu código deve vir aqui"""
    source_news = database.search_news(
        {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}
    )
    return [(news["title"], news["url"]) for news in source_news]


def search_by_category(category):
    """Seu código deve vir aqui"""
    category_news = database.search_news(
        {"categories": {"$elemMatch": {"$regex": category, "$options": "i"}}}
    )
    return [(news["title"], news["url"]) for news in category_news]
