import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    if filepath.split('.')[1] != "csv":
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            reader_file = csv.DictReader(file, delimiter=";")
            for text in reader_file:
                result = text
            return [result]
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
