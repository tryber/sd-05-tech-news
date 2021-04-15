import pymongo
from tech_news.database import db


def top_5_news():
    top_five = []
    news = (db.news.find({}).sort([
        ('shares_count', pymongo.DESCENDING),
        ('comments_count', pymongo.DESCENDING),
        ('title', pymongo.ASCENDING)
    ]).limit(5))

    for one in news:
        top_five.append((one['title'], one['url']))
   
    return top_five


def top_5_categories():
    """Seu código deve vir aqui"""
