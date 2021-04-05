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


def analyzer_menu():
    """Seu código deve vir aqui"""
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )
    if option == "1":
        result = input("Digite o título:")
        title = search_by_title(result)
        print(title)
    elif option == "2":
        result = input("Digite a data no formato aaaa-mm-dd:")
        date = search_by_date(result)
        print(date)
    elif option == "3":
        result = input("Digite a fonte:")
        source = search_by_source(result)
        print(source)
    elif option == "4":
        result = input("Digite a categoria:")
        category = search_by_category(result)
        print(category)
    elif option == "5":
        result = top_5_news()
        print(result)
    elif option == "6":
        result = top_5_categories()
        print(result)
    elif option == "7":
        print("Encerrando script\n")
        return
    else:
        print("Opção inválida", file=sys.stderr)
        return
