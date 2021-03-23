import csv
from tech_news import database
# https://www.geeksforgeeks.org/writing-csv-files-in-python/


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    news = database.find_news()
    print(news)
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
            for index in rows:
                if isinstance(rows[index], list):
                    rows[index] = ",".join(rows[index])
# https://stackoverflow.com/questions/2982023/how-to-write-header-row-with-csv-dictwriter
        file_writer.writeheader()
        file_writer.writerows(news)
