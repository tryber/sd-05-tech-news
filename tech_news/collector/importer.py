import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""

    if filepath.endswith(".csv") is not True:
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            storage = csv.DictReader(file, delimiter=";")
            content = []
            for data in storage:
                content.append(data)
                return content
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")


# Testado manualmente com csv_importer("file_csv.csv")
# file csv já existente no projeto
