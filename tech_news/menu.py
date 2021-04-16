import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_date,
    search_by_category,
    search_by_title,
    search_by_source,
)
from tech_news.analyzer.ratings import top_5_categories, top_5_news


def collector_menu():
    text = """
Selecione uma das opções a seguir:
1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Raspar notícias online;
4 - Sair. """

    menu = input(text)

    if menu == "1":
        msg = input("Digite o nome do arquivo CSV a ser importado:")
        doc = csv_importer(msg)
        create_news(doc)
    elif menu == "2":
        msg = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(msg)
    elif menu == "3":
        number = int(input("Digite a quantidade de páginas a serem raspadas:"))
        doc = scrape(fetcher=fetch_content, pages=number)
        create_news(doc)
    elif menu == "4":
        print("Encerrando script")
    else:
        sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    text = """
1 - Buscar notícias por título;
2 - Buscar notícias por data;
3 - Buscar notícias por fonte;
4 - Buscar notícias por categoria;
5 - Listar top 5 notícias;
6 - Listar top 5 categorias;
7 - Sair.
    """

    menu = input(text)
    switch(int(menu))


def switch(menu):
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
        int(menu), lambda: sys.stderr.write("Opção inválida\n")
    )
    print(func())


def case_1():
    title = input("Digite o título:")
    print(search_by_title(title))


def case_2():
    date = input("Digite da data no formato aaaa-mm-dd:")
    print(search_by_date(date))


def case_3():
    source = input("Digite a fonte:")
    print(search_by_source(source))


def case_4():
    category = input("Digite a categoria:")
    print(search_by_category(category))


def case_5():
    print(top_5_news())


def case_6():
    print(top_5_categories())


def case_7():
    print("Encerrando script")
