import csv


def csv_importer(filepath):
    try:
        assert filepath.endswith('.csv')
        with open(filepath) as file:
            arquivo = csv.reader(file, delimiter=';', quotechar='"')
            header, *data = arquivo
            # print(data)
            correct_header = [
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
            assert header == correct_header
    except AssertionError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f'Arquivo {filepath} não encontrado')
    except OSError:
        raise ValueError("Formato invalido")
    else:
        result = [
            {header[indice]: content[indice] for indice in range(len(content))}
            for content in data
        ]
        return result
