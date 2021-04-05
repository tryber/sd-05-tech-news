import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_source,
    search_by_title,
)


def collector_menu():
    """Seu código deve vir aqui"""
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Importar notícias a partir de um arquivo CSV;\n"
        " 2 - Exportar notícias para CSV;\n"
        " 3 - Raspar notícias online;\n"
        " 4 - Sair."
    )

    if option == "1":
        file_path = input("Digite o nome do arquivo CSV a ser importado:")
        file_content = csv_importer(file_path)
        create_news(file_content)
    elif option == "2":
        file_path = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(file_path)
    elif option == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        data = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(data)
    elif option == "4":
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)


def getInput():
    return input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )


def optionOne():
    result = input("Digite o título:")
    title = search_by_title(result)
    print(title)


def optionTwo():
    result = input("Digite a data no formato aaaa-mm-dd:")
    date = search_by_date(result)
    print(date)


def optionThree():
    result = input("Digite a fonte:")
    source = search_by_source(result)
    print(source)


def optionFour():
    result = input("Digite a categoria:")
    category = search_by_category(result)
    print(category)


def optionFive():
    result = top_5_news()
    print(result)


def optionSix():
    result = top_5_categories()
    print(result)


def optionSeven():
    print("Encerrando script\n")


def analyzer_menu():
    option = getInput()
    switcher = {
        "1": optionOne,
        "2": optionTwo,
        "3": optionThree,
        "4": optionFour,
        "5": optionFive,
        "6": optionSix,
        "7": optionSeven,
    }
    switcher.get(option, lambda: print("Opção inválida", file=sys.stderr))()
