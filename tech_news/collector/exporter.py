import csv
from tech_news import database


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


def csv_exporter(filepath):
    if filepath.split('.')[1] == 'csv':
        with open(filepath, 'w') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(headers)
            for news in database.find_news():
                row = []
                for keys in headers:
                    row.append(
                        news[keys] if not isinstance(news[keys], list)
                        else ",".join(news[keys])
                    )
                print(row)
                writer.writerow(row)
    else:
        raise ValueError('Formato invalido')
