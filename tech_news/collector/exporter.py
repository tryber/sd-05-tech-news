import csv
from tech_news.database import find_news


def csv_exporter(filepath):

    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    with open(filepath, "w") as file:
        csv_writer = csv.DictWriter(file, delimiter=";", fieldnames=[
            'url',
            'title',
            'timestamp',
            'writer',
            'shares_count',
            'comments_count',
            'summary',
            'sources',
            'categories',
        ])
        csv_writer.writeheader()

        for news in find_news():
            article = {
                "url": news["url"],
                "title": news["title"],
                "timestamp": news["timestamp"],
                "writer": news["writer"],
                "shares_count": str(news["shares_count"]),
                "comments_count": str(news["comments_count"]),
                "summary": news["summary"],
                "sources": ",".join(news["sources"]),
                "categories": ",".join(news["categories"])
            }

            csv_writer.writerow(article)
