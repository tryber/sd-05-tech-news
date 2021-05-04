import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    if filepath.endswith(".csv") is not True:
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            reading = csv.DictReader(file, delimiter=";")
            archive = []
            for archive in reading:
                values = archive
                return [values]
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
