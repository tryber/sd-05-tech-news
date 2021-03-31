import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories, top_5_news


def collector_menu():
    mensagem = '''
Selecione uma das opções a seguir:
 1 - Importar notícias a partir de um arquivo CSV;
 2 - Exportar notícias para CSV;
 3 - Raspar notícias online;
 4 - Sair.'''
    option = input(mensagem)

    if option == "1":
        pathfile = input("Digite o nome do arquivo CSV a ser importado:")
        dados = csv_importer(pathfile)
        create_news(dados)
    elif option == "2":
        pathfile = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(pathfile)
    elif option == "3":
        quantidade = int(
            input("Digite a quantidade de páginas a serem raspadas:"))
        dados = scrape(fetcher=fetch_content, pages=quantidade)
        create_news(dados)
    elif option == "4":
        print("Encerrando script")
    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    mensagem = '''
Selecione uma das opções a seguir:
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.'''
    option = input(mensagem)
    switch(int(option))


def switch(option):

    switcher = {
        1: case_1,
        2: case_2,
        3: case_3,
        4: case_4,
        5: case_5,
        6: case_6,
        7: case_7,
    }
    func = switcher.get(
        int(option), lambda: sys.stderr.write("Opção inválida\n"))
    print(func())


def case_1():
    titulo = input("Digite o título:")
    print(search_by_title(titulo))


def case_2():
    data = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(data))


def case_3():
    source = input("Digite a fonte:")
    print(search_by_source(source))


def case_4():
    categoria = input("Digite a categoria:")
    print(search_by_category(categoria))


def case_5():
    print(top_5_news())


def case_6():
    print(top_5_categories())


def case_7():
    print("Encerrando script")

#   https://codesource.io/ways-to-implement-python-switch-case-statement/
#   https://jaxenter.com/implement-switch-case-statement-python-138315.html
