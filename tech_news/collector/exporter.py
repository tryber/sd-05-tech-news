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

        for notice in find_news():
            article = {
                "url": notice["url"],
                "title": notice["title"],
                "timestamp": notice["timestamp"],
                "writer": notice["writer"],
                "shares_count": str(notice["shares_count"]),
                "comments_count": str(notice["comments_count"]),
                "summary": notice["summary"],
                "sources": ",".join(notice["sources"]),
                "categories": ",".join(notice["categories"])
            }

            csv_writer.writerow(article)
        return notice
