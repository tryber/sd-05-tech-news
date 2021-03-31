import csv


def csv_importer(filepath):
    if (not filepath.endswith("csv")):
        raise ValueError("Formato invalido")

    try:
        saida = []
        with open(filepath) as file:
            noticias = csv.DictReader(file, delimiter=";")

            for noticia in noticias:
                saida.append(noticia)
        return saida
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")


#   https://docs.python.org/pt-br/3/tutorial/errors.html
#   https://www.kite.com/python/answers/how-to-raise-a-valueerror-in-python
