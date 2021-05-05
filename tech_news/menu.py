import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
# from tech_news.database import create_news
from tech_news.analyzer.search_engine import search_by_title, search_by_date
from tech_news.analyzer.search_engine import search_by_source
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_categories, top_5_news


def create_news():
    pass


def collector_menu():
    print("Selecione uma das opções a seguir:")
    print(" 1 - Importar notícias a partir de um arquivo CSV;")
    print(" 2 - Exportar notícias para CSV;")
    print(" 3 - Raspar notícias online;")
    print(" 4 - Sair.")
    options = input()
    if options == "1":
        print("Digite o nome do arquivo CSV a ser importado:")
        import_data = input()
        create_news(csv_importer(import_data))
    elif options == "2":
        print("Digite o nome do arquivo CSV a ser exportado:")
        export_data = input()
        csv_exporter(export_data)
    elif options == "3":
        print("Digite a quantidade de páginas a serem raspadas:")
        pages_number = input()
        create_news(scrape(fetcher=fetch_content, pages=int(pages_number)))
    elif options == "4":
        sys.stdout.write("Encerrando script\n")
    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    print("Selecione uma das opções a seguir:")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por fonte;")
    print(" 4 - Buscar notícias por categoria;")
    print(" 5 - Listar top 5 notícias;")
    print(" 6 - Listar top 5 categorias;")
    print(" 7 - Sair.")
    options = input()
    if options == "1":
        search_by_title(input())
    elif options == "2":
        search_by_date(input())
    elif options == "3":
        search_by_source(input())
    elif options == "4":
        search_by_category(input())
    elif options == "5":
        top_5_news(input())
    elif options == "6":
        top_5_categories(input())
    elif options == "7":
        sys.stdout.write("Encerrando script\n")
    else:
        sys.stderr.write("Opção inválida\n")
