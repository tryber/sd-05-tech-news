import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    campos = [
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
    with open(filepath, "w") as arq:
        escreve_arq = csv.DictWriter(arq, delimiter=";", fieldnames=campos)
        escreve_arq.writeheader()
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
            escreve_arq.writerow(lista)
