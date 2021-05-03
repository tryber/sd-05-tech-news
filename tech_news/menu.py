import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content
from tech_news.collector.scrapper import scrape

from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_source
from tech_news.analyzer.search_engine import search_by_category


first_menu = [
    "\nSelecione uma das opções a seguir:",
    " 1 - Importar notícias a partir de um arquivo CSV;",
    " 2 - Exportar notícias para CSV;",
    " 3 - Raspar notícias online;",
    " 4 - Sair."
]

sec_menu = [
    "\nSelecione uma das opções a seguir:",
    "1 - Buscar notícias por título;",
    "2 - Buscar notícias por data;",
    "3 - Buscar notícias por fonte;",
    "4 - Buscar notícias por categoria;",
    "5 - Listar top 5 notícias;",
    "6 - Listar top 5 categorias;",
    "7 - Sair."
]


def collector_menu():
    try:
        option = int(view(first_menu))
    except ValueError:
        print("Opção inválida", file=sys.stderr)
    else:
        first_switching(option)


def analyzer_menu():
    try:
        option = view(sec_menu)
    except ValueError:
        print("Opção inválida", file=sys.stderr)
    else:
        sec_switching(option)


def first_switching(option):
    if option == 1:
        selected = option_selected(
            "Digite o nome do arquivo CSV a ser importado:")
        print(csv_importer(selected))

    elif option == 2:
        selected = option_selected(
            "Digite o nome do arquivo CSV a ser exportado:")
        return csv_exporter(selected)

    elif option == 3:
        selected = option_selected(
            "Digite a quantidade de páginas a serem raspadas:")
        return scrape(fetch_content, pages=int(selected))

    elif option == 4:
        print("Encerrando script")
        return "Encerrando script"
    else:
        return print("Opção inválida", file=sys.stderr)


def sec_switching(option):
    options = {
        "1": first,
        "2": second,
        "3": third,
        "4": forth,
        "5": fifth,
        "6": sixth,
        "7": seventh,
    }
    selected = options.get(option, "Opção inválida", file=sys.stderr)
    print("teste", selected())
    # ("Opção inválida")


def first():
    # if option == 1:
    selected = option_selected(
        "Digite o título:")
    print(search_by_title(selected))
    analyzer_menu()


def second():
    # if option == 2:
    selected = option_selected(
        "Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(selected))
    analyzer_menu()


def third():
    # if option == 3:
    selected = option_selected(
        "Digite a fonte:")
    print(search_by_source(selected))
    analyzer_menu()


def forth():
    #   if option == 4:
    selected = option_selected(
        "Digite a categoria:")
    print(search_by_category(selected))
    analyzer_menu()


def fifth():
    #   if option == 5:
    selected = option_selected(
        "")
    return selected


def sixth():
    # if option == 6:
    selected = option_selected(
        "")
    return selected


def seventh():
    #   if option == 7:
    # print("Encerrando script")
    return "Encerrando script"


def view(menu):
    for men in menu:
        print(men)
    return input("Opção: ")


def option_selected(text_supply):
    user_request = str(input(text_supply))
    return user_request
