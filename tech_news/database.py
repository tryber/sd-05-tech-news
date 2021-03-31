from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def create_news(data):
    db.news.insert_many(data)


def insert_or_update(notice):
    return (
        db.news.update_one(
            {"url": notice["url"]}, {"$set": notice}, upsert=True
        ).upserted_id
        is not None
    )


def find_news():
    return list(db.news.find({}, {"_id": False}))


def search_news(query):
    return list(db.news.find(query))


def top5_news_agreggation():
    return list(db.news.aggregate([
        {"$addFields":
            {"somaSocial": {"$add": ["$comments_count", "$shares_count"]}}},
        {"$sort": {"somaSocial": -1, "title": 1}},
        {"$limit": 5},
        ]))


def top5_news_categories_aggregation():
    return list(db.news.aggregate([
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories"}},
        {"$sort": {"_id": 1}},
        {"$limit": 5},
        {"$project": {"_id": 0, "categories": "$_id"}}
        ]))

#   https://docs.mongodb.com/manual/reference/operator/aggregation/group/
#   https://docs.mongodb.com/manual/reference/operator/aggregation/unwind/
#   https://docs.mongodb.com/manual/reference/operator/projection/positional/
