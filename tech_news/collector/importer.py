import csv


def csv_importer(filepath):
    data_results = []
    valid_header = [
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

    try:
        assert filepath.endswith(".csv")

        with open(filepath) as file:
            csv_reader = csv.DictReader(file, delimiter=";")
            # print(csv_reader)

            assert csv_reader.fieldnames == valid_header

            for item in csv_reader:
                data_results.append(item)

            return data_results

    # mesmo except para os 2 assertion errors (.csv & header)
    except AssertionError:
        raise ValueError("Formato invalido")

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")

# https://docs.python.org/3/library/exceptions.html#ValueError
