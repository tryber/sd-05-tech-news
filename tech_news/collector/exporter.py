import csv
from pymongo import MongoClient
from tech_news.model import tech_news_model

NEW_NOTICE = {
    "url": "https://www.tecmundo.com.br/brincadeira-levadaserio.htm",
    "title": "Yakuza Like a Dragon era beat em up",
    "timestamp": "2020-11-23T11:00:01",
    "writer": "André Luis Dias Custodio",
    "shares_count": 0,
    "comments_count": 0,
    "summary": "Sumario da noticia",
    "sources": ["ResetEra"],
    "categories": ["Plataformas", "PC", "Console"],
}


cursor = tech_news_model.find_cursor


def parse_list(data):
    new_data = []
    for item in data:
        if type(item) is list:
            new_data.append(",".join(item))
        else:
            new_data.append(item)
    return new_data


def csv_exporter(filepath, cur=cursor):
    """Seu código deve vir aqui"""
    try:
        assert filepath.endswith('.csv')
    except AssertionError:
        raise ValueError("Formato invalido")
    else:
        all_news = []
        news = cur()
        headers = [field for field in news[0].keys()]
        all_news.extend([content.values() for content in news])
        with open(filepath, "w") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(headers)
            for row in all_news:
                writer.writerow(parse_list(row))
        return all_news


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.tech_news
        db.news.delete_many({})
        db.news.insert_one(NEW_NOTICE)
        print(csv_exporter("kyle.csv"))
