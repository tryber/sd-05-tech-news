import csv


def csv_importer(filepath):
    try:
        assert filepath.endswith(".csv")
        with open(filepath) as file:
            csv_reader = csv.reader(file, delimiter=";")
            header, *data = csv_reader

            ofc_header = [
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

            assert header == ofc_header

    except AssertionError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        """ lógica tirada do repo da Juliette """
        result = [
            {header[i]: content[i] for i in range(len(content))}
            for content in data
        ]

        return result
