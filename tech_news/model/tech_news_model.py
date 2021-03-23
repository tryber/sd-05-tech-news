from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")


def connection(base="tech_news"):
    """
    DEFINITIONS:
        base: Database to connect, default is 'tech_news'.
    """
    with MongoClient(host=DB_HOST, port=int(DB_PORT)) as client:
        return client[base]


def find_cursor(
    params={},
    projection={"_id": 0},
    collection="news",
    conn=connection,
    agg=False,
):
    """
    DEFINITIONS:
        params: type DICT, Parâmetros de busca a ser realizada no banco.
        projection: type DICT, default {"_id": 0}
        collection: type STRING, coleção de busca, default 'news'
        conn: type FUNCTION, Conexão a ser usada, default connection
        agg: type BOOLEAN, Define se usa find (False), ou aggregate (True)
    """
    db = conn()
    if agg:
        return list(db[collection].aggregate(params))
    result = list(db[collection].find(params, projection))
    return result
