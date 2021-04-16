import csv
from tech_news import database


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    noticias = database.find_news()
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
        all = []
        for key in headers:
            if type(noticias[0][key]) == list:
                linha = ",".join(noticias[0][key])
                all.append(linha)
            else:
                all.append(noticias[0][key])
        writer.writerow(all)
