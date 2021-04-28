import csv


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath, 'r') as file:
            data = csv.DictReader(file, delimiter=";")
            for row in data:
                return [row]

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
