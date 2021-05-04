from tech_news.database import find_news
import csv


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

    with open(filepath, "w") as file:
        if not filepath.endswith("csv"):
            raise ValueError("Formato invalido")
        # É necessário passar o arquivo e o cabeçalho
        writer = csv.DictWriter(file, fieldnames=header, delimiter=";")
        writer.writeheader()
        list_news = find_news()
        for linhas in list_news:
            for key in linhas:
                if type(linhas[key]) == list:
                    linhas[key] = ",".join(linhas[key])
        writer.writerows(list_news)
