import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    keys = [
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
    if filepath.split(".")[1] != "csv":
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        writer_file = csv.DictWriter(file, delimiter=";", fieldnames=keys)
        writer_file.writeheader()
        for news in find_news():
            lista = {
                "url": news["url"],
                "title": news["title"],
                "timestamp": news["timestamp"],
                "writer": news["writer"],
                "shares_count": str(news["shares_count"]),
                "comments_count": str(news["comments_count"]),
                "summary": news["summary"],
                "sources": ",".join(news["sources"]),
                "categories": ",".join(news["categories"]),
            }
            writer_file.writerow(lista)
