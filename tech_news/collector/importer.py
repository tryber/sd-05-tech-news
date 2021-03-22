import csv


def assign_data(data, header):
    results = []
    for row in data:
        article = {}
        counter = 0
        for keys in header:
            article[keys] = row[counter]
            counter += 1
        results.append(article)
    return results


def csv_importer(filepath):
    try:
        assert filepath.split('.')[1] == 'csv'
        with open(filepath) as file:
            beach_status_reader = csv.reader(
              file, delimiter=";", quotechar='"'
            )
            header, *data = beach_status_reader
    except AssertionError:
        raise ValueError('Formato invalido')
    except FileNotFoundError:
        raise ValueError(f'Arquivo {filepath} não encontrado')
    else:
        return assign_data(data, header)
