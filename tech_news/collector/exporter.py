from tech_news.database import find_news
import csv


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    header = [
        'url',
        'title',
        'timestamp',
        'writer',
        'shares_count',
        'comments_count',
        'summary',
        'sources',
        'categories',
    ]
    if filepath.split('.')[1] != "csv":
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        writer = csv.DictWriter(file, delimiter=";", fieldnames=header)
        writer.writeheader()
        for news in find_news():
            result = {
                "url": news["url"],
                "title": news["title"],
                "timestamp": news["timestamp"],
                "writer": news["writer"],
                "shares_count": str(news["shares_count"]),
                "comments_count": str(news["comments_count"]),
                "summary": news["summary"],
                "sources": ",".join(news["sources"]),
                "categories": ",".join(news["categories"])
            }
            writer.writerow(result)
