import csv
from tech_news.database import find_news


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


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    news = find_news()
    if filepath.split('.')[1] != 'csv':
        raise ValueError('Formato invalido')
    with open(filepath, 'w') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(header)
        for each in news:
            print(each)
            row = [
                each["url"],
                each["title"],
                each["timestamp"],
                each["writer"],
                each["shares_count"],
                each["comments_count"],
                each["summary"],
                ",".join(each["sources"]),
                ",".join(each["categories"]),
            ]
            writer.writerow(row)
