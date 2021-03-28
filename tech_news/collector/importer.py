import csv


def csv_importer(filepath):
    news = []
    try:
        assert filepath.endswith("csv")
        with open(filepath) as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                news.append(row)
        print(news)
        return news
    except AssertionError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
