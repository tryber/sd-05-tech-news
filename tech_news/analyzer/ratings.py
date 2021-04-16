import pymongo
from tech_news.database import db
from bson.son import SON


def top_5_news():
    top_five = []
    news = (
        db.news.find({})
        .sort(
            [
                ("shares_count", pymongo.DESCENDING),
                ("comments_count", pymongo.DESCENDING),
                ("title", pymongo.ASCENDING),
            ]
        )
        .limit(5)
    )

    for one in news:
        top_five.append((one["title"], one["url"]))

    return top_five


def top_5_categories():
    top_five = []
    cat = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": SON([("count", 1), ("_id", 1)])},
            {"$limit": 5},
        ]
    )

    for one in cat:
        top_five.append((one["_id"]))

    return top_five
