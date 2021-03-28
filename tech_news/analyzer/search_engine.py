from tech_news import database
from datetime import datetime


def search_by_title(title):
    # A busca deve ser case insensitive
    # e deve retornar uma lista de lista de tuplas [("title", "url")];
    NEWS = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    # Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
    if len(NEWS) == 0:
        return []
    return [(NEWS[0]["title"], NEWS[0]["url"])]


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        # A busca deve retornar uma lista de tuplas [("title", "url")];
        NEWS = database.search_news({"timestamp": {"$regex": date}})
    except ValueError:
        # A data deve estar no formato "aaaa-mm-dd" e deve ser válida.
        # Caso seja inválida, uma exceção deve ser lançada Data inválida.
        raise ValueError("Data inválida")
    else:
        if len(NEWS) == 0:
            return []
        return [(NEWS[0]["title"], NEWS[0]["url"])]


def search_by_source(source):
    # A busca deve ser case insensitive
    # e deve retornar uma lista de tuplas [("title", "url")];
    NEWS = database.search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    # Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
    if len(NEWS) == 0:
        return []
    return [(NEWS[0]["title"], NEWS[0]["url"])]


def search_by_category(category):
    # A busca deve ser case insensitive
    # e deve retornar uma lista de tuplas [("title", "url")];
    NEWS = database.search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    # Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
    if len(NEWS) == 0:
        return []
    return [(NEWS[0]["title"], NEWS[0]["url"])]
