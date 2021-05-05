import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content 
from tech_news.database import create_news


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
    """Seu código deve vir aqui"""
