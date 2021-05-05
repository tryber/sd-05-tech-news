from tech_news.database import search_news
# from collections import Counter


def top_5_news():
    """Seu código deve vir aqui"""
    popular_news = search_news({})
    result = sorted(
        popular_news,
        key=lambda item: item["comments_count"] + item["shares_count"],
        reverse=True,
    )
    if len(result) == 0:
        return []

    return [(item["title"], item["url"]) for item in result][:5]
    # [:5] limit 5 results


def top_5_categories():
    """Seu código deve vir aqui"""
