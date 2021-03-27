import csv


def read_file(filepath):
    with open(filepath, "r") as file:
        csv_reader = csv.reader(file, delimiter=";", quotechar='"')
        headers, *data = csv_reader
    return headers, data


def format_news(row, headers, news_list):
    news_dict = {}
    for index in range(len(row)):
        news_dict[headers[index]] = row[index]
    news_list.append(news_dict)
    return news_list


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    try:
        assert filepath.endswith(".csv")
        headers, data = read_file(filepath)
    except AssertionError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        news_list = []
        for row in data:
            news_list = format_news(row, headers, news_list)
        return news_list
