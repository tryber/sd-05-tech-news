import csv
from tech_news import database


def format_csv_row(data):
    formated_data = []
    for item in data:
        if type(item) == list:
            item = ",".join(item)
        formated_data.append(item)
    return formated_data


def write_csv(filepath, data):
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")

        headers = [
            "url",
            "title",
            "timestamp",
            "writer",
            "shares_count",
            "comments_count",
            "summary",
            "sources",
            "categories",
        ]

        writer.writerow(headers)

        for news in data:
            news_values = format_csv_row(news.values())
            writer.writerow(news_values)


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    try:
        assert filepath.endswith(".csv")
        news = database.find_news()
        write_csv(filepath, news)

    except AssertionError:
        raise ValueError("Formato invalido")


if __name__ == "__main__":
    csv_exporter("output.csv")
