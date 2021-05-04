from tech_news.database import filter_top_5_news


def top_5_news():
    """Seu código deve vir aqui"""
    top_5 = filter_top_5_news()
    topi = []
    if len(top_5) == 0:
        return []
    for top in top_5:
        topi.append((top["title"], top["url"]))
    return topi


def top_5_categories():
    """Seu código deve vir aqui"""
#     
