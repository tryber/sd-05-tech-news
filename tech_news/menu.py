import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content
from tech_news.collector.scrapper import scrape


# except AttributeError:
#         raise AttributeError(file=sys.stderr)
def collector_menu():
    try:
        view()
        option = int(input("Opção: "))
    except ValueError:
        print("Opção inválida", file=sys.stderr)
    else:
        switching(option)
        # if option == 1:
        #     selected = option_selected(
        #         "Digite o nome do arquivo CSV a ser importado:")
        #     print(csv_importer(selected))

        # elif option == 2:
        #     selected = option_selected(
        #         "Digite o nome do arquivo CSV a ser exportado:")
        #     return csv_exporter(selected)

        # elif option == 3:
        #     selected = option_selected(
        #         "Digite a quantidade de páginas a serem raspadas:")
        #     return scrape(fetch_content, pages=int(selected))

        # elif option == 4:
        #     print("Encerrando script")
        #     return "Encerrando script"
        # else:
        #     return print("Opção inválida", file=sys.stderr)


def switching(option):
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


def view():
    print("\nSelecione uma das opções a seguir:")
    print(" 1 - Importar notícias a partir de um arquivo CSV;")
    print(" 2 - Exportar notícias para CSV;")
    print(" 3 - Raspar notícias online;")
    print(" 4 - Sair.")


def option_selected(text_supply):
    user_request = str(input(text_supply))
    return user_request


def analyzer_menu():
    """Seu código deve vir aqui"""
