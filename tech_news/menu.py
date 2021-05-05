import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news


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
    """Seu código deve vir aqui"""
