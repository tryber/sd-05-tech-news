import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""

    # 1. No try, codar leitura de arquivo csv
    # incluindo asserts de formatos que queremos
    # e prevendo o delimiter por ; pedido
    try:
        assert ".csv" in filepath
        with open(filepath) as file:
            csv_reader = csv.reader(file, delimiter=";")
            header, *data = csv_reader
            print(data)
            wanted_header = [
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
            assert header == wanted_header
    # 2. Nos except, prever o tratamento de exceções indicadas
    # Com mensagens de erro impostas nos tests do requisito
    except AssertionError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    # 3. No else (executado se tudo correr bem no try), retornar resultado
    else:
        result = [
            {header[i]: content[i] for i in range(len(content))}
            for content in data
        ]
        # fazer corresponder elemento 1 de header com elemento 1 de corpo etc
        # (escrevendo cada etapa, dava erro de csv_importer too difficult)
        return result

# Testado com csv_importer("./correct.csv")
# https://docs.python.org/3/library/exceptions.html erros nativos
