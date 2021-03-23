from tech_news import database
from datetime import datetime


def search_by_title(title):
    """Seu código deve vir aqui"""
    # 1/ Use search_news functions from database.py, writing pymongo query
    # & selecting by title & providing case insensitive (option i)
    NEWS = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    # print(NEWS)
    # 2/ Caso nenhuma notícia seja encontrada, retornar lista vazia
    if len(NEWS) == 0:
        return []
    # 3/ Formatar resposta pedida - lista de tuplas [("title", "url")]
    return [(NEWS[0]["title"], NEWS[0]["url"])]


def search_by_date(date):
    # 1/ Same logic & expected result format
    # 2/ But with datetime lib and invalid error
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        # (até sem assert, dispara ValueError se for inconsistente)
        NEWS = database.search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        if len(NEWS) == 0:
            return []
        return [(NEWS[0]["title"], NEWS[0]["url"])]

# Sobre estrutura code, aqui podia ser apenas try except, com else dentro try
# datetime, strptime, formatos https://docs.python.org/3/library/datetime.html


def search_by_source(source):
    """Seu código deve vir aqui"""
    # Same as search_by_title, but by source
    NEWS = database.search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    if len(NEWS) == 0:
        return []
    return [(NEWS[0]["title"], NEWS[0]["url"])]


def search_by_category(category):
    """Seu código deve vir aqui"""
    # Same but by category
    NEWS = database.search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    if len(NEWS) == 0:
        return []
    return [(NEWS[0]["title"], NEWS[0]["url"])]

# https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
# Honestidade acadêmica:
# PR do aluno Felipe Vieira para lembrar da norma de var maiuscula (NEWS)
# https://github.com/tryber/sd-05-tech-news/pull/17/files
# PR do aluno Dandrea para se inspirar com outros jeitos, por ex. usando tuple
# https://github.com/tryber/sd-05-tech-news/pull/2/files
# PR do aluno Cesar para completar entendimento de lógicas e exemplos diversos
# https://github.com/tryber/sd-05-tech-news/pull/18/files
