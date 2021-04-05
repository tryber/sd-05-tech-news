import csv

def csv_importer(filepath):
    try:
        assert filepath.endswith('.csv')
        with open(filepath) as file:
            filepath_reader = csv.reader(file, delimiter=";")
            header, *data = filepath_reader
    except AssertionError:
        raise ValueError("Formato invalido")
    except FileNotFoundError:
        raise ValueError(f'Arquivo {filepath} não encontrado')
    else:
        newArr = []
        for item in data:
            newArr.append(dict(zip(header, item)))
        return newArr
