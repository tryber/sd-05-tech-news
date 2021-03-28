from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    """Retorna o titulo e url das noticias encontradas."""

    news = []
    news_by_title = search_news({
        'title': {
            '$regex': title,
            '$options': 'i'
        }
    })

    for new in news_by_title:
        news.append((new['title'], new['url']))

    return news


def search_by_date(date):
    """Busca o título e url de uma notícia, a partir da data."""

    news = []

    try:
        # https://stackoverflow.com/questions/16870663
        datetime.strptime(date, '%Y-%m-%d')

        news_by_date = search_news({
            'timestamp': {
                '$regex': date
            }
        })

        for new in news_by_date:
            news.append((new['title'], new['url']))

        return news

    except ValueError:
        raise ValueError('Data inválida')


def search_by_source(source):
    """Busca o título e url de uma notícia, a partir da fonte."""

    news = []
    news_by_source = search_news({
        'sources': {
            '$regex': source,
            '$options': 'i'
        }
    })

    for new in news_by_source:
        news.append((new['title'], new['url']))

    return news


def search_by_category(category):
    """Busca pelo título e url de uma notícia, a partir da categoria."""

    news = []
    news_by_category = search_news({
        'categories': {
            '$regex': category,
            '$options': 'i'
        }
    })

    for new in news_by_category:
        news.append((new['title'], new['url']))

    return news
