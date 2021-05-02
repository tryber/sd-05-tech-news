import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    expected_header = ["url", "title", "timestamp", "writer", "shares_count", "comments_count", "summary", "sources", "categories"]
    results = []
    new = dict()
    try:
        # print("header: ")
        with open(filepath) as file:
            # response = csv.DictReader(file, delimiter=";")
            file_readed = csv.reader(file, delimiter=";")
            header, *data = file_readed
            # for new in response:
            #     # print("data: ", new)
            #     results.append(new.items())

    except FileNotFoundError:
        if not filepath.endswith("csv"):
            raise ValueError("Formato invalido")
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        if not filepath.endswith("csv"):
            raise ValueError("Formato invalido")
        for idx in expected_header:
            if idx not in header:
                raise ValueError("Some header of the file is missing")
        for idx in range(len(header)):
            new["url"] = data[0][0]
            new["title"] = data[0][1]
            new["timestamp"] = data[0][2]
            new["writer"] = data[0][3]
            new["shares_count"] = data[0][4]
            new["comments_count"] = data[0][5]
            new["summary"] = data[0][6]
            new["sources"] = data[0][7]
            new["categories"] = data[0][8]
        results.append(new)
    return results
