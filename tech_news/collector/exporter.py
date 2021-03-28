from tech_news import database
import csv


def csv_exporter(filepath):
    valid_header = [
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

    # para conseguir acessar o banco é preciso inicializar o mongo no terminal
    # > sudo service mongod start
    news = database.find_news()

    # try:
    # assert filepath.endswith(".csv")
    # /\ tinha feito assim, mas precisei abandonar esse método
    #    por conta do flake8 (too complex)
    #
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    with open(filepath, "w") as file:
        csv_writer = csv.DictWriter(
            file, fieldnames=valid_header, delimiter=";"
        )

        for rows in news:
            for key in rows:
                # print(key, '--------- chaves')
                if type(rows[key]) == list:
                    # print(rows[key], '--- antes')
                    rows[key] = ",".join(rows[key])
                    # print(rows[key], '--- depois')

        csv_writer.writeheader()
        csv_writer.writerows(news)
        # print(news)

    # except AssertionError:
    #     raise ValueError("Formato invalido")
