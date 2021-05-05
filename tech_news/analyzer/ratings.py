from tech_news.database import search_news
from collections import Counter


def top_5_news():
    """Seu código deve vir aqui"""
    news = search_news({})
    result = sorted(
        news,
        key=lambda item: item["comments_count"] + item["shares_count"],
        reverse=True
    )

    if len(result) == 0:
        return []

    listing_top5 = [(item["title"], item["url"]) for item in result][:5]

    return listing_top5


def top_5_categories():
    """Seu código deve vir aqui"""
    categories = search_news({})
    result = [item["categories"][1] for item in categories]

    top5 = Counter(result).most_common(5)

    if len(result) == 0:
        return []
    return top5
