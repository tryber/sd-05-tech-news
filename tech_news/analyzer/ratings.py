from tech_news.database import db, client


def top_5_news():
    results = []
    search_results = list(
        db.news.aggregate(
            [
                {
                    "$addFields": {
                        "count": {
                            "$sum": ["$shares_count", "$comments_count"]
                        }
                    }
                },
                {"$sort": {"count": -1, "title": 1}},
                {"$limit": 5},
            ]
        )
    )
    client.close()
    for news in search_results:
        results.append((news["title"], news["url"]))

    return results


def top_5_categories():
    results = []
    search_results = list(
        db.news.aggregate(
            [
                {"$unwind": "$categories"},
                {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
                {"$sort": {"count": -1, "_id": 1}},
                {"$limit": 5},
            ]
        )
    )
    client.close()
    for news in search_results:
        results.append((news["_id"]))

    return results
