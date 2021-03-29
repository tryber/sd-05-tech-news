import csv


def csv_importer(filepath):
    results = []
    if filepath.split('.')[1] != "csv":
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            reader_file = csv.DictReader(file, delimiter=";")
            for linha in reader_file:
                results.append(linha)
        return results
    except FileNotFoundError:
        raise ValueError(f'Arquivo {filepath} não encontrado')
