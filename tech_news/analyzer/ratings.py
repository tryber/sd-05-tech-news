from tech_news import database
from collections import Counter


def top_5_news():
    """Seu código deve vir aqui"""
    news = database.search_news({})
    result = sorted(
        news,
        key=lambda new_count: new_count["comments_count"]
        + new_count["shares_count"],
        reverse=True,
    )
    if len(result) == 0:
        return []
    return [(new["title"], new["url"]) for new in result][:5]


def top_5_categories():
    """Seu código deve vir aqui"""
    news = database.search_news({})
    result = [new["categories"][1] for new in news]
    top_five = Counter(result)
    if len(result) == 0:
        return []
    return sorted(top_five.elements())[:5]
