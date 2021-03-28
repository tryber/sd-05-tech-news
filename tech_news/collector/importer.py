import csv


def csv_importer(filepath):

    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    data = []
    try:
        with open(filepath) as file:
            read_news = csv.DictReader(file, delimiter=";")
            for item in read_news:
                data.append(item)
            return data

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
