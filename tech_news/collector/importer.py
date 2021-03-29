import csv


def csv_importer(filepath):

    try:
        assert filepath.endswith(".csv")
        results = []

        with open(filepath) as file:
            news = csv.DictReader(file, delimiter=";")
            headers = [
                "url",
                "title",
                "timestamp",
                "writer",
                "shares_count",
                "comments_count",
                "summary",
                "sources",
                "categories",
            ]
            assert news.fieldnames == headers
            for new in news:
                results.append(new)

            return results

    except AssertionError:
        raise ValueError("Formato invalido")

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
