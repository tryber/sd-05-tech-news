import csv


def csv_importer(filepath):
    if (not filepath.endswith("csv")):
        raise ValueError("Formato invalido")
    try:
        noticias = []
        with open(filepath) as file:
            all = csv.DictReader(file, delimiter=";")

            for one in all:
                noticias.append(one)
        return noticias
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
