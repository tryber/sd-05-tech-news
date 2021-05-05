import csv


def csv_importer(filepath):
    if filepath.endswith(".csv") is not True:
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            csv_file = csv.DictReader(file, delimiter=";")
            datas = [data for data in csv_file]
        return datas
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
