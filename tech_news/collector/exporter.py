import csv
from tech_news import database


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
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
    if filepath.endswith(".csv") is not True:
        raise ValueError("Formato invalido")
    data = database.find_news()
    with open(filepath, "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=headers, delimiter=";")
        csv_writer.writeheader()
        for news in data:
            article = {
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
            csv_writer.writerow(article)
