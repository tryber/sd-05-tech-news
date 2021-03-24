import csv


def csv_importer(filepath):
    if(not filepath.endswith(".csv")):
        raise ValueError("Formato invalido")

    data_result = []
    try:
        with open(filepath) as file:
            news_reader = csv.DictReader(file, delimiter=";")
            for item in news_reader:
                data_result.append(item)
            return data_result

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
