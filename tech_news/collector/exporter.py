import csv
from tech_news.database import find_news


def csv_exporter(filepath):
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
