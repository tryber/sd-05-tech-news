import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    expected_header = [
        "url", "title", "timestamp", "writer", "shares_count",
        "comments_count", "summary", "sources", "categories"]
    results = []
    try:
        with open(filepath) as file:
            file_readed = csv.reader(file, delimiter=";")
            header, *data = file_readed
            data = data[0]
    except FileNotFoundError:
        if not filepath.endswith("csv"):
            raise ValueError("Formato invalido")
        raise ValueError(f"Arquivo {filepath} não encontrado")
    else:
        final_result(filepath, expected_header, header, data, results)
    return results


def final_result(filepath, expected_header, header, data, results):
    if not filepath.endswith("csv"):
        raise ValueError("Formato invalido")
    for idx in expected_header:
        if idx not in header:
            raise ValueError("Some header of the file is missing")
    for idx in range(len(header)):
        new = {}
        new["url"] = data[0]
        new["title"] = data[1]
        new["timestamp"] = data[2]
        new["writer"] = data[3]
        new["shares_count"] = data[4]
        new["comments_count"] = data[5]
        new["summary"] = data[6]
        new["sources"] = data[7]
        new["categories"] = data[8]
    results.append(new)
