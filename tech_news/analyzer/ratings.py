from tech_news.database import db

""" inspirado no repo do Rafael Leite """


def top_5_news():
    aggregation = list(db.news.aggregate([
        {"$addFields":
            {"somaSocial": {"$add": ["$comments_count", "$shares_count"]}}},
        {"$sort": {"somaSocial": -1, "title": 1}},
        {"$limit": 5},
        ]))
    return [(item["title"], item["url"]) for item in aggregation]


def top_5_categories():
    aggregation = list(db.news.aggregate([
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories"}},
        {"$sort": {"_id": 1}},
        {"$limit": 5},
        {"$project": {"_id": 0, "categories": "$_id"}}
        ]))
    return [item["categories"] for item in aggregation]
