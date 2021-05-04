from tech_news.database import search_news


def top_5_news():
    list_news = search_news({})
    resultado = sorted(
        list_news,
        key=lambda item: item["comments_count"] + item["shares_count"],
        reverse=True
        )
    if len(resultado) == 0:
        return []
    return [(item["title"], item["url"]) for item in resultado][:5]




def top_5_categories():
    
