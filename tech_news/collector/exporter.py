from tech_news.database import find_news
import csv

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
    if ".csv" not in filepath:
        raise ValueError("Formato invalido")

    news_list = find_news()

    with open(filepath, "w") as file:
        csvWriter = csv.DictWriter(file, fieldnames=header, delimiter=";")

        print(news_list)

        for news_dict in news_list:
            for key in news_dict:
                if type(news_dict[key]) == list:
                    news_dict[key] = ",".join(news_dict[key])

        csvWriter.writeheader()
        csvWriter.writerows(news_list)
