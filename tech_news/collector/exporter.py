import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    header = [
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
    if filepath.endswith(".csv") is not True:
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        csv_file = csv.DictWriter(file, delimiter=";", fieldnames=header)
        csv_file.writeheader()
        for noticia in find_news():
            data = {
                "url": noticia["url"],
                "title": noticia["title"],
                "timestamp": noticia["timestamp"],
                "writer": noticia["writer"],
                "shares_count": str(noticia["shares_count"]),
                "comments_count": str(noticia["comments_count"]),
                "summary": noticia["summary"],
                "sources": ",".join(noticia["sources"]),
                "categories": ",".join(noticia["categories"]),
            }         
            csv_file.writerow(data)
