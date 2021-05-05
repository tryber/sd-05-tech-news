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

    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    news = find_news()

    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(header)
        row_list = []

        for field in header:
            if type(news[0][field]) == list:
                string_row = ",".join(news[0][field])
                row_list.append(string_row)
            else:
                row_list.append(news[0][field])
        writer.writerow(row_list)
