import csv


def csv_importer(filepath):
    """Importa um arquivo CSV e retorna os dados como objeto."""

    ext = filepath[-3:]
    # valid_header = [
    #     'url',
    #     'title',
    #     'timestamp',
    #     'writer',
    #     'shares_count',
    #     'comments_count',
    #     'summary',
    #     'sources',
    #     'categories'
    # ]

    if (ext != 'csv'):
        raise ValueError('Formato invalido')

    try:
        with open(filepath) as file:
            # Conteúdo Course - Manipulando arquivos CSV
            csv_reader = csv.DictReader(file, delimiter=";")
            data_result = []

            # Opcional, teste não pede essa verificação.
            # Coloca-lá gerou um aumento de complexidade que
            # o Flake8 não permite.
            #
            # if csv_reader.fieldnames != valid_header:
            #     raise ValueError('Cabeçalhos não compativeis')

            for row in csv_reader:
                data_result.append(row)

            return data_result

    except FileNotFoundError:
        raise ValueError(f'Arquivo {filepath} não encontrado')
