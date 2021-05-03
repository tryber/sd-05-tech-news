from tech_news.database import search_news_agregation


def top_5_news():
    list_result = search_news_agregation(
        [
            {
                "$addFields": {
                    "popularity": {
                        "$add": ["$shares_count", "$comments_count"]
                    }
                }
            },
            {"$sort": {"popularity": -1, "title": 1}},
            {"$limit": 5},
        ]
    )
    list_top5 = []
    if list_result == []:
        return []
    for new in list_result:
        list_top5.append((new["title"], new["url"]))
    return list_top5


def top_5_categories():
    list_result = search_news_agregation(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    list_top5_categories = []
    if list_result == []:
        return []
    for new in list_result:
        list_top5_categories.append((new["_id"]))
    return list_top5_categories
