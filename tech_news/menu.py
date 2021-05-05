import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category
)
from tech_news.analyzer.ratings import top_5_categories, top_5_news


def collector_menu():
    """Seu código deve vir aqui"""
    print("Selecione uma das opções a seguir:")
    print(" 1 - Importar notícias a partir de um arquivo CSV;")
    print(" 2 - Exportar notícias para CSV;")
    print(" 3 - Raspar notícias online;")
    print(" 4 - Sair.")

    value = input()

    if value == "1":
        print("Digite o nome do arquivo CSV a ser importado:")
        import_csv = input()
        create_news(csv_importer(import_csv))

    elif value == "2":
        print("Digite o nome do arquivo CSV a ser exportado:")
        export_csv = input()
        csv_exporter(export_csv)

    elif value == "3":
        print("Digite a quantidade de páginas a serem raspadas:")
        pages = input()
        create_news(scrape(fetcher=fetch_content, pages=int(pages)))

    elif value == "4":
        sys.stdout.write("Encerrando script\n")

    else:
        sys.stderr.write("Opção inválida\n")


def part1(value):
    if value == "1":
        search_by_title(input())

    elif value == "2":
        search_by_date(input())

    elif value == "3":
        search_by_source(input())

    elif value == "4":
        search_by_category(input())


def analyzer_menu():
    """Seu código deve vir aqui"""
    print("Selecione uma das opções a seguir:")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por fonte;")
    print(" 4 - Buscar notícias por categoria;")
    print(" 5 - Listar top 5 notícias;")
    print(" 6 - Listar top 5 categorias;")
    print(" 7 - Sair.")

    value = input()

    part1(value)

    if value == "5":
        top_5_news(input())

    elif value == "6":
        top_5_categories(input())

    elif value == "7":
        sys.stdout.write("Encerrando script\n")

    else:
        sys.stderr.write("Opção inválida\n")
