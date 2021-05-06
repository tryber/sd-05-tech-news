from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

def connection(base="tech_news"):
    with MongoClient(host=DB_HOST, port=int(DB_PORT)) as client:
        return client[base]

def find_cursor(
    agg=False,
    collection="news",
    conn=connection,
    params={},
    projection={"_id": 0},
):
    db = conn()
    if agg:
        return list(db[collection].aggregate(params))
    result = list(db[collection].find(params, projection))
    return result