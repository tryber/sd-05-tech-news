from tech_news.database import find_news
import csv


def csv_exporter(filepath):
    # print(list_news)
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
        # new = {
        #         "url": linhas["url"],
        #         "title": linhas["title"],
        #         "timestamp": linhas["timestamp"],
        #         "writer": linhas["writer"],
        #         "shares_count": linhas["shares_count"],
        #         "comments_count": linhas["comments_count"],
        #         "summary": linhas["summary"],
        #         "sources": linhas["sources"],
        #         "categories": linhas["categories"],
        #         }
        # novo_arquivo.writelines("\n\nEste arquivo foi criado via script.")
        # novo_arquivo.writelines("\nEsta é a segunda linha do
        # arquivo que foi criado via script.\n")

    # finally:
    #     # será sempre executado, independentemente de erro
    #     print("Tentativa de abrir arquivo")
