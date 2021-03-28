import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    news = []
    try:
        assert filepath.endswith("csv")
        with open(filepath) as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                news.append(row)
        return news
    except AssertionError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
