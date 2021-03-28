import pymongo
from tech_news.database import db


def top_5_news():
    """Busca as 5 noticias com mais compartilhamentos e curtidas."""

    top_five = []

    # https://stackoverflow.com/questions/8109122/
    #
    # Metodo find_news, do tech_news.database, não permite adição do sort.
    # Necessário importar o database e realizar um novo find.
    #
    news = (db.news.find({}).sort([
        ('shares_count', pymongo.DESCENDING),
        ('comments_count', pymongo.DESCENDING),
        ('title', pymongo.ASCENDING)
    ]).limit(5))

    for new in news:
        top_five.append((new['title'], new['url']))

    return top_five


def top_5_categories():
    """Seu código deve vir aqui"""
