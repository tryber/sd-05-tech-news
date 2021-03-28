import csv
from tech_news import database


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    news = database.find_news()
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
        writer = csv.DictWriter(file, delimiter=";", fieldnames=headers)
        for rows in news:
            for key in rows:
                if type(rows[key]) == list:
                    rows[key] = ",".join(rows[key])
        writer.writeheader()
        writer.writerows(news)
