import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    collection = []
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
        for each_row in data:
            assembly = {
                "url": each_row[0],
                "title": each_row[1],
                "timestamp": each_row[2],
                "writer": each_row[3],
                "shares_count": each_row[4],
                "comments_count": each_row[5],
                "summary": each_row[6],
                "sources": each_row[7],
                "categories": each_row[8]
            }
            collection.append(assembly)
    return collection
