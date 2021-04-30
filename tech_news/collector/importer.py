import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    extension = filepath[-3:]
    header_ok = [
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

    if extension != "csv":
        raise ValueError("Formato invalido")

    try:
        with open(filepath) as file:
            read_csv = csv.reader(file, delimiter=";")
            header, *data = read_csv

            if header != header_ok:
                raise ValueError("Cabeçalhos não compativeis")

            data_final = [
                {header[i]: content[i] for i in range(len(content))}
                for content in data
            ]

            return data_final

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
