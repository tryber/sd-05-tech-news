import csv
from tech_news import database


def csv_exporter(filepath):
    if (not filepath.lower().endswith(".csv")):
        raise ValueError("Formato invalido")

    news = database.find_news()
    with open(filepath, "w") as file:
        file_writer = csv.DictWriter(file, delimiter=";", fieldnames=[
            "url",
            "title",
            "timestamp",
            "writer",
            "shares_count",
            "comments_count",
            "summary",
            "sources",
            "categories",
        ])

        for rows in news:
            for key in rows:
                if type(rows[key]) == list:
                    rows[key] = ",".join(rows[key])
        file_writer.writeheader()
        file_writer.writerows(news)
