import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        news = find_news()
        fields = list(news[0].keys())
        writer = csv.DictWriter(file, fields, delimiter=";")
        writer.writeheader()

        for item in news:
            for key in item:
                if type(item[key]) == list:
                    item[key] = ",".join(item[key])

        writer.writerows(news)
        file.close()
