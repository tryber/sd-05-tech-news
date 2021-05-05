import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news


def collector_menu():
    """Seu código deve vir aqui"""
    print("Selecione uma das opções a seguir:")
    print(" 1 - Importar notícias a partir de um arquivo CSV;")
    print(" 2 - Exportar notícias para CSV;")
    print(" 3 - Raspar notícias online;")
    print(" 4 - Sair.")
    value_input = input()
    if value_input == "1":
        print("Digite o nome do arquivo CSV a ser importado:")
        import_csv = input()
        create_news(csv_importer(import_csv))

    elif value_input == "2":
        print("Digite o nome do arquivo CSV a ser exportado:")
        export_csv = input()
        csv_exporter(export_csv)

    elif value_input == "3":
        print("Digite a quantidade de páginas a serem raspadas:")
        number_pages = input()
        create_news(scrape(fetcher=fetch_content, pages=int(number_pages)))

    elif value_input == "4":
        sys.stdout.write("Encerrando script\n")
    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    """Seu código deve vir aqui"""
