import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if (not filepath.endswith("csv")):
        raise ValueError("Formato invalido")

    noticias = find_news()

    # abre um arquivo para escrita
    with open(filepath, "w") as file:
        # os valores a serem escritos devem ser dicionários
        header = [
            "url",
            "title",
            "timestamp",
            "writer",
            "shares_count",
            "comments_count",
            "summary",
            "sources",
            "categories"
        ]

        # É necessário passar o arquivo e o cabeçalho
        writer = csv.DictWriter(file, fieldnames=header, delimiter=";")
        writer.writeheader()
        # escreve as linhas de dados
        for noticia in noticias:
            for chave in noticia:
                if (isinstance(noticia[chave], list)):
                    noticia[chave] = ",".join(noticia[chave])
#                    transforma a lista em um formato para o csv

        writer.writerows(noticias)

#   https://docs.python.org/3/library/csv.html
#   https://www.w3schools.com/python/ref_func_isinstance.asp
