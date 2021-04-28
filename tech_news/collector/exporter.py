import csv
from tech_news import database


def csv_exporter(filepath):

    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
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

    with open(filepath, "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")

        news_db = database.find_news()
        for new in news_db:
            for chave in new:
                if type(new[chave]) == list:
                    new[chave] = ",".join(new[chave])

        csv_writer.writeheader()
        csv_writer.writerows(news_db)
