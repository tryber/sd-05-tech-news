# thx to https://realpython.com/python-exceptions/

import csv


def assemble_news(header, news_data):
    news = {}
    for field in header:
        news[field] = news_data[header.index(field)]
    return news


def csv_importer(filepath, assembler=assemble_news):
    """Seu código deve vir aqui"""
    try:
        assert filepath.endswith(".csv")
        with open(filepath) as file:
            reader = csv.reader(file, delimiter=";")
            header, *content = reader
    except AssertionError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        data = []
        for values in content:
            data.append(assembler(header, values))
        return data
