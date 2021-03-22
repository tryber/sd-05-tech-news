import csv


def csv_importer(filepath):
    if ".csv" not in filepath:
        raise ValueError("Formato invalido")

    try:
        with open(filepath) as file:
            header_to_assert = [
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

            reader = csv.reader(file, delimiter=";")

            header, *data = reader

            if header_to_assert != header:
                raise ValueError("Formato invalido")

        return [
            {header[i]: info[i] for i in range(len(info))} for info in data
        ]
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
