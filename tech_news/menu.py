import sys

from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import (
    top_5_news,
    top_5_categories,
)

from tech_news.database import create_news

RESULT = {"error": "Opção inválida", "exit": "Encerrando script\n"}

menu_colector = (
    "Selecione uma das opções a seguir:\n"
    " 1 - Importar notícias a partir de um arquivo CSV;\n"
    " 2 - Exportar notícias para CSV;\n"
    " 3 - Raspar notícias online;\n"
    " 4 - Sair.\n"
)

analyze_messages = {
    "1": "Digite o título:",
    "2": "Digite a data no formato aaaa-mm-dd:",
    "3": "Digite a fonte:",
    "4": "Digite a categoria:",
}


def execute_option(answer):
    if answer == "1":
        option = input("Digite o nome do arquivo CSV a ser importado:")
        data = csv_importer(option)
        create_news(data)
    elif answer == "3":
        print(">>>> item 3")
        option = int(input("Digite a quantidade de páginas a serem raspadas:"))
        data = scrape(fetcher=fetch_content, pages=option)
        create_news(data)
    elif answer == "2":
        print("Digite o nome do arquivo CSV a ser exportado:")
        option = input()
        csv_exporter(option)


def collector_menu():
    """Seu código deve vir aqui"""
    print(">>>> to no colector")
    answer = input(menu_colector)
    if answer not in ["1", "2", "3", "4"]:
        print(RESULT["error"], file=sys.stderr)
    if answer == "4":
        print(RESULT["exit"])
    else:
        execute_option(answer)


execute_analyze = {
    "1": lambda x: search_by_title(x),
    "2": lambda x: search_by_date(x),
    "3": lambda x: search_by_source(x),
    "4": lambda x: search_by_category(x),
    "5": lambda _: top_5_news(),
    "6": lambda _: top_5_categories(),
    "7": lambda _: print("Encerrando script\n"),
}


def analyzer_menu():
    """Seu código deve vir aqui"""
    answer = input(
        "Selecione uma das opções a seguir:\n"
        + " 1 - Buscar notícias por título;\n"
        + " 2 - Buscar notícias por data;\n"
        + " 3 - Buscar notícias por fonte;\n"
        + " 4 - Buscar notícias por categoria;\n"
        + " 5 - Listar top 5 notícias;\n"
        + " 6 - Listar top 5 categorias;\n"
        + " 7 - Sair."
    )
    issue = RESULT['error']
    if answer in execute_analyze.keys():
        resp = input(analyze_messages.get(answer))
        issue = execute_analyze.get(answer)(resp)
    else:
        print("Opção inválida", file=sys.stderr)
