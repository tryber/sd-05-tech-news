from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories
import sys


def collector_secondary_menu(opt_input):
    options = {
        1: "Digite o nome do arquivo CSV a ser importado:",
        2: "Digite o nome do arquivo CSV a ser exportado:",
        3: "Digite a quantidade de páginas a serem raspadas:",
        4: "Encerrando script",
        5: "Opção inválida",
    }

    if opt_input > 4 or opt_input < 1:
        print(options[5], file=sys.stderr)
        return

    print(options[opt_input])


def collector_menu():
    print(
        """Selecione uma das opções a seguir:
        1 - Importar notícias a partir de um arquivo CSV;
        2 - Exportar notícias para CSV;
        3 - Raspar notícias online;
        4 - Sair."""
    )
    try:
        opt_input = int(input())
    except ValueError:
        opt_input = 5

    collector_secondary_menu(opt_input)

    if opt_input > 3:
        return

    param_input = input()
    functions = {
        1: csv_importer,
        2: csv_exporter,
        3: lambda n: scrape(fetcher=fetch_content, pages=int(n)),
    }
    result = functions[opt_input](param_input)
    if opt_input == 3 or opt_input == 1:
        create_news(result)


def analyzer_secondary_menu(opt_input):
    options = {
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
        7: "Encerrando script",
        8: "Opção inválida",
    }
    if opt_input > 7 or opt_input < 1:
        print(options[8], file=sys.stderr)
        return

    print(options[opt_input])


def analyzer_menu():
    print(
        """Selecione uma das opções a seguir:

        1 - Buscar notícias por título;
        2 - Buscar notícias por data;
        3 - Buscar notícias por fonte;
        4 - Buscar notícias por categoria;
        5 - Listar top 5 notícias;
        6 - Listar top 5 categorias;
        7 - Sair."""
    )
    try:
        opt_input = int(input())
    except ValueError:
        opt_input = 8

    functions = {
        1: search_by_title,
        2: search_by_date,
        3: search_by_source,
        4: search_by_category,
        5: top_5_news,
        6: top_5_categories,
    }

    if opt_input < 5 or opt_input > 6:
        analyzer_secondary_menu(opt_input)
        if opt_input > 6 or opt_input < 1:
            return
        param_input = input()
        result = functions[opt_input](param_input)
    else:
        result = functions[opt_input]()

    print(result)
