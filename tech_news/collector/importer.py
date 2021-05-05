import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    if filepath.endswith(".csv") is not True:
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            csv_reader = csv.DictReader(file, delimiter=";")
            row = []
            for row in csv_reader:
                values = row
                return [values]
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
