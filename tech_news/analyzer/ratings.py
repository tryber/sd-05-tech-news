from tech_news.database import search_news
from collections import Counter


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
    list_categories = search_news({})
    result = [item["categories"][1] for item in list_categories]
    top_five = Counter(result).most_common(5)
    if len(result) == 0:
        return []
    return top_five
