from tech_news import database
import csv


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    news = database.find_news()
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
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
        writer.writerow(headers)
        row = []
        for key_name in headers:
            if type(news[0][key_name]) == list:
                string_row = ",".join(news[0][key_name])
                row.append(string_row)
            else:
                row.append(news[0][key_name])
        writer.writerow(row)
