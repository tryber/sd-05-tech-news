import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content
from tech_news.collector.scrapper import scrape

from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_source
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.database import create_news


first_menu = [
    "\nSelecione uma das opções a seguir:",
    " 1 - Importar notícias a partir de um arquivo CSV;",
    " 2 - Exportar notícias para CSV;",
    " 3 - Raspar notícias online;",
    " 4 - Sair."
]

sec_menu = [
    "\nSelecione uma das opções a seguir:",
    " 1 - Buscar notícias por título;",
    " 2 - Buscar notícias por data;",
    " 3 - Buscar notícias por fonte;",
    " 4 - Buscar notícias por categoria;",
    " 5 - Listar top 5 notícias;",
    " 6 - Listar top 5 categorias;",
    " 7 - Sair."
]


def collector_menu():
    try:
        option = int(view(first_menu))
    except ValueError:
        print("Opção inválida", file=sys.stderr)
        # return collector_menu()
    else:
        first_switching(option)


def analyzer_menu():
    try:
        option = int(view(sec_menu))
    except ValueError:
        print("Opção inválida", file=sys.stderr)
        # analyzer_menu()
    else:
        sec_switching(option)


def first_switching(option):
    if option == 1:
        selected = option_selected(
            "Digite o nome do arquivo CSV a ser importado:")
        news = csv_importer(selected)
        return print(create_news(news))
        # return csv_importer(selected)

    elif option == 2:
        selected = option_selected(
            "Digite o nome do arquivo CSV a ser exportado:")
        return csv_exporter(selected)

    elif option == 3:
        selected = option_selected(
            "Digite a quantidade de páginas a serem raspadas:")
        news = scrape(fetcher=fetch_content, pages=int(selected))
        return print(create_news(news))

    elif option == 4:
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)


def sec_switching(option):
    try:
        options = {
            "1": first,
            "2": second,
            "3": third,
            "4": forth,
            "5": fifth,
            "6": sixth,
            "7": seventh,
        }

        if not (1 > option > 7):
            option = str(option)
            selected = options.get(option)
            selected()
    except Exception:
        return erro()


def first():
    selected = option_selected(
        "Digite o título:")
    return print(search_by_title(selected))
    # analyzer_menu()


def second():
    selected = option_selected(
        "Digite a data no formato aaaa-mm-dd:")
    return print(search_by_date(selected))
    # analyzer_menu()


def third():
    selected = option_selected(
        "Digite a fonte:")
    return print(search_by_source(selected))
    # analyzer_menu()


def forth():
    selected = option_selected(
        "Digite a categoria:")
    return print(search_by_category(selected))
    # analyzer_menu()


def fifth():
    selected = option_selected(
        "Filtrar por noticias")
    return top_5_news(selected)


def sixth():
    selected = option_selected(
        "Filtrar por categorias")
    return top_5_categories(selected)


def seventh():
    return print("Encerrando script")


def erro():
    return print("Opção inválida", file=sys.stderr)
    # return analyzer_menu()


def view(menu):
    for option in menu:
        print(option)
    return input()


def option_selected(text_supply):
    user_request = str(input(text_supply))
    return user_request
