from tech_news.database import search_news


def top_5_news():
    """Seu código deve vir aqui"""
    list_news = search_news({})
    result = sorted(
        list_news,
        key=lambda new_count: new_count["comments_count"]
        + new_count["shares_count"],
        reverse=True,
    )
    if len(result) == 0:
        return []
    return [(item["title"], item["url"]) for item in result][:5]


def top_5_categories():
    """Seu código deve vir aqui"""
