import csv


def csv_importer(filepath):
    if (not filepath.lower().endswith(".csv")):
        raise ValueError("Formato invalido")
    try:
        with open(filepath, "r") as file:
            data_result = []
            file_reader = csv.DictReader(file, delimiter=";")
            for data in file_reader:
                data_result.append(data)
            return data_result
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
