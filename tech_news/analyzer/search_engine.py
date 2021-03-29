from datetime import datetime
from tech_news.database import search_news
# from pymongo import MongoClient
# from decouple import config

# DB_HOST = config("DB_HOST", default="localhost")
# DB_PORT = config("DB_PORT", default="27017")

# client = MongoClient(host=DB_HOST, port=int(DB_PORT))
# db = client.tech_news


def search_by_title(title):
    insensitive_title = {"title": {"$regex": title, "$options": "i"}}
    # news = list(db.news.find(insensitive_title))
    news = search_news(insensitive_title)
    resultado = []
    for noticia in news:
        resultado.append((noticia['title'], noticia['url']))
    return resultado


def search_by_date(date):
    try:
        format = "%Y-%m-%d"
        datetime.strptime(date, format)
        news = search_news({"timestamp": {"$regex": date, "$options": "im"}})
        # print(news)
    except ValueError:
        raise ValueError("Data inválida")
    else:
        resultado = []
        for noticia in news:
            resultado.append((noticia['title'], noticia['url']))
        return resultado


def search_by_source(source):
    insensitive_sources = {"sources": {"$regex": source, "$options": "i"}}
    news = search_news(insensitive_sources)
    resultado = []
    for noticia in news:
        resultado.append((noticia['title'], noticia['url']))
    return resultado


def search_by_category(category):
    insens_categories = {"categories": {"$regex": category, "$options": "i"}}
    # news = list(db.news.find(insensitiveTitle))
    news = search_news(insens_categories)
    resultado = []
    for noticia in news:
        resultado.append((noticia['title'], noticia['url']))
    return resultado

# transparencia academica:
# aprendi os regex com o colega paulo d'andrea e a referencia
# https://docs.mongodb.com/manual/reference/operator/query/regex/
