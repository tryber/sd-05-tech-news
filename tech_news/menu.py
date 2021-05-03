import sys


def collector_menu():
    um, dois, tres, quatro = [1, 2, 3, 4]

    print("\nSelecione uma das opções a seguir:")
    print(f" {um} - Importar notícias a partir de um arquivo CSV;")
    print(f" {dois} - Exportar notícias para CSV;")
    print(f" {tres} - Raspar notícias online;")
    print(f" {quatro} - Sair.")

    try:
        selected = ""
        option = int(input())
    except ValueError:
        print("Opção inválida", file=sys.stderr)
    else:
        if option == um:
            selected = option_selected(
                "Digite o nome do arquivo CSV a ser importado:")
            return selected

        elif option == dois:
            selected = option_selected(
                "Digite o nome do arquivo CSV a ser exportado:")
            return selected

        elif option == tres:
            selected = option_selected(
                "Digite a quantidade de páginas a serem raspadas:")
            return selected

        elif option == quatro:
            print("Encerrando script")
            return
        else:
            print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""


def option_selected(text_supply):
    user_request = input(text_supply)
    return user_request
