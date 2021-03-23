from csv import reader


def csv_importer(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            file_read = reader(file, delimiter=";")
            header, *data = file_read
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        output = []
        dict_list = {}
        for index, value in enumerate(header):
            dict_list[value] = data[0][index]

        output.append(dict_list)
        return output
