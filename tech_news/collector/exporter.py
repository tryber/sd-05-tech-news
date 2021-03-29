import csv
# from pymongo import MongoClient
from tech_news.database import find_news


def csv_exporter(filepath):
    # DB_HOST = config("DB_HOST", default="localhost")
    # DB_PORT = config("DB_PORT", default="27017")
    # with client = MongoClient(host=DB_HOST, port=int(DB_PORT))
    #    db = client.tech_news
    # comentei estrutura do try excerpt para fugir do "too complex" do flake
    # try:
    #     assert filepath.endswith('.csv')
    # except AssertionError:
    #     raise ValueError("Formato invalido")
    if not filepath.endswith('.csv'):
        raise ValueError("Formato invalido")
    # else:
    with open(filepath, "w") as file:
        headers = [
            "url",
            "title",
            "timestamp",
            "writer",
            "shares_count",
            "comments_count",
            "summary",
            "sources",
            "categories",
        ]
        writer = csv.DictWriter(file, delimiter=";", fieldnames=headers)
        writer.writeheader()
        news = find_news()
        for rows in news:
            for key in rows:
                if isinstance(rows[key], list):
                    rows[key] = ",".join(rows[key])
        writer.writerows(news)

# transparencia academica: conversei com colegas que sugeriram os artigos:
# https://stackoverflow.com/questions/2982023/how-to-write-header-row-with-csv-dictwriter
# https://www.w3schools.com/python/ref_func_isinstance.asp
