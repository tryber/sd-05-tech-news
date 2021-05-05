from tech_news.database import search_news
from collections import Counter


def top_5_news():
    news = search_news({})
    result = sorted(
        news,
        key=lambda item: item["comments_count"] + item["shares_count"],
        reverse=True,
    )
    if len(result) == 0:
        return []
    return [(item["title"], item["url"]) for item in result][:5]


def top_5_categories():
    categories_list = search_news({})
    result = [item["categories"][1] for item in categories_list]
    top_five = Counter(result).most_common(5)
    if len(result) == 0:
        return []
    return top_five
