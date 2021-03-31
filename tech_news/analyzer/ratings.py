from tech_news import database


def top_5_news():
    noticias = database.top5_news_agreggation()
    return [(item["title"], item["url"]) for item in noticias]


def top_5_categories():
    categorias = database.top5_news_categories_aggregation()
    return [categoria["categories"] for categoria in categorias]
