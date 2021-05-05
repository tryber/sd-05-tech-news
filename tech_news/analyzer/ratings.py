from tech_news.database import search_news


def top_5_news():
    news = search_news({})
    result = sorted(
        news,
        key=lambda item: item["comments_count"] + item["shares_count"],
        reverse=true,
    )
    if len(result) == 0:
        return []
    return [(item["title"], item["url"]) for item in result][:5]


def top_5_categories():