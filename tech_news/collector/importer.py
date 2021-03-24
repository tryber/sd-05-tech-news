import csv


def csv_importer(filepath):
    if filepath.split('.')[1] == 'csv':
        try:
            with open(filepath, 'r') as news:
                ler = csv.reader(news, delimiter=';')
                header, *data = ler
        except FileNotFoundError:
            raise ValueError(f"Arquivo {filepath} não encontrado")
        else:
            output = []
            lista = {}
            for index, value in enumerate(header):
                lista[value] = data[0][index]

            output.append(lista)
            return output
    else:
        raise ValueError("Formato invalido")
