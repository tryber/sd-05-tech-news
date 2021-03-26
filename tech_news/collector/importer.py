import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    try:
        with open(filepath) as file:
            reader = csv.DictReader(file, delimiter=";")
            body = [content for content in reader]
            return body
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
