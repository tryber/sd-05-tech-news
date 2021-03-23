import csv
# https://app.betrybe.com/course/computer-science/python/entrada-saida/conteudos/manipulando-arquivos-csv?use_case=side_bar


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            result = []
            file_reader = csv.DictReader(file, delimiter=";")
            for content in file_reader:
                result.append(content)
            return result
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
