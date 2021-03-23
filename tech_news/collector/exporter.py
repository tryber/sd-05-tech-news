from tech_news.database import find_news
import csv


fields = [
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


def csv_exporter(filepath):
    """Seu código deve vir aqui"""

    # (Could not keep try, except & else structure: flake error "too complex")
    # 1/ Prevent main error, available from the start
    # if ".csv" not in filepath:
    # better but both work:
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    # 2/ Take data from bd
    news = find_news()
    # print(news)

    # 3/ Write csv under dict format, with : delimiter & header fields above
    with open(filepath, "w") as file:
        dw = csv.DictWriter(file, delimiter=";", fieldnames=fields)
        for rows in news:
            for key in rows:
                if isinstance(rows[key], list):
                    rows[key] = ",".join(rows[key])
        dw.writeheader()
        dw.writerows(news)

# https://docs.python.org/3/library/csv.html
# https://www.w3schools.com/python/ref_func_isinstance.asp
# https://stackoverflow.com/questions/2982023/how-to-write-header-row-with-csv-dictwriter
