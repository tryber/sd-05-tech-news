import csv
from tech_news import database


def csv_exporter(filepath):
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
    try:
        assert filepath.endswith("csv")
        with open(filepath, "w") as file:
            csv_writer = csv.DictWriter(
                file, delimiter=";", fieldnames=headers
            )
            csv_writer.writeheader()
            for news in database.find_news():
                news_data = {
                    "url": news["url"],
                    "title": news["title"],
                    "timestamp": news["timestamp"],
                    "writer": news["writer"],
                    "shares_count": news["shares_count"],
                    "comments_count": news["comments_count"],
                    "summary": news["summary"],
                    "sources": ",".join(news["sources"]),
                    "categories": ",".join(news["categories"]),
                }
                csv_writer.writerow(news_data)
    except AssertionError:
        raise ValueError("Formato invalido")
