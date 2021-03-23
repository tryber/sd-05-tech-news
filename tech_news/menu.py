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
from tech_news.analyzer.ratings import top_5_categories, top_5_news


def collector_menu():
    INPUT = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair.\n"
    )

    if INPUT == "1":
        PATH = input("Digite o nome do arquivo CSV a ser importado:")
        CONTENT = csv_importer(PATH)
        create_news(CONTENT)
    elif INPUT == "2":
        PATH = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(PATH)
    elif INPUT == "3":
        PAGE_QNT = input("Digite a quantidade de páginas a serem raspadas:")
        DATA = scrape(fetcher=fetch_content, pages=int(PAGE_QNT))
        create_news(DATA)
    elif INPUT == "4":
        print("Encerrando script")
    else:
        print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    INPUT = int(input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    ))

    FUNCTIONS = {
        1: lambda title: print(search_by_title(title)),
        2: lambda date: print(search_by_date(date)),
        3: lambda source: print(search_by_source(source)),
        4: lambda category: print(search_by_category(category)),
        5: lambda: print(top_5_news()),
        6: lambda: print(top_5_categories()),
        7: lambda: print("Encerrando script"),
    }

    INPUTS = {
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
    }

    if 0 < INPUT < 5:
        USER_INPUT = input(INPUTS[INPUT])
        FUNCTIONS[INPUT](USER_INPUT)
    elif 4 < INPUT < 8:
        FUNCTIONS[INPUT]()
    else:
        print("Opção inválida", file=sys.stderr)
