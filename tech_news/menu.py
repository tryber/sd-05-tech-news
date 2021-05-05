import sys
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


def collector_menu():
    options = (
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair.\n"
    )

    option = input(options)

    if option == "1":
        pathfile = input("Digite o nome do arquivo CSV a ser importado:")
        dados = csv_importer(pathfile)
        create_news(dados)
    elif option == "2":
        pathfile = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(pathfile)
    elif option == "3":
        number_of_pages = int(
            input("Digite a quantidade de páginas a serem raspadas:"))
        dados = scrape(fetcher=fetch_content, pages=number_of_pages)
        create_news(dados)
    elif option == "4":
        print("Encerrando script")
    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    options = (
        "Selecione uma das opções a seguir:\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    option = input(options)

    menu = {
        1: lambda: search_by_title(input("Digite o título:")),
        2: lambda: search_by_date(
            input("Digite a data no formato aaaa-mm-dd:")
        ),
        3: lambda: search_by_source(input("Digite a fonte:")),
        4: lambda: search_by_category(input("Digite a categoria:")),
        5: lambda: top_5_news(),
        6: lambda: top_5_categories(),
        7: lambda: print("Encerrando script")
    }

    try:
        return menu[int(option)]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
