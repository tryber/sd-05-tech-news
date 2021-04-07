from tech_news import database
import csv


def csv_exporter(filepath):
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
    data = database.find_news()
    if not filepath.endswith('.csv'):
        raise ValueError("Formato invalido")
    with open(filepath, mode='w') as file:
        csv_writer = csv.DictWriter(file, fieldnames=headers, delimiter=';')
        for notice in data:
            for key in notice:
                if type(notice[key]) == list:
                    notice[key] = ",".join(notice[key])
        csv_writer.writeheader()
        csv_writer.writerows(data)


# a função acima faz a escrita de dicionários do banco em um arquivo csv
# e verifica chaves que indicam listas e adiciona a "," entre os itens da lista
# fonte: https://github.com/tryber/sd-05-tech-news/blob
# /marina-brcls-tech-news/tech_news/collector/exporter.py
