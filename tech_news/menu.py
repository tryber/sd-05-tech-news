import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content, scrape
from tech_news.database import create_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import (
    top_5_news,
    top_5_categories,
)


def op_func():
    ops = 'Selecione uma das opções a seguir:\n'
    op1 = ' 1 - Buscar notícias por título;\n'
    op2 = ' 2 - Buscar notícias por data;\n'
    op3 = ' 3 - Buscar notícias por fonte;\n'
    op4 = ' 4 - Buscar notícias por categoria;\n'
    op5 = ' 5 - Listar top 5 notícias;\n'
    op6 = ' 6 - Listar top 5 categorias;\n'
    op7 = ' 7 - Sair.\n'
    opcoes = ops + op1 + op2 + op3 + op4 + op5 + op6 + op7
    return input(opcoes)


def collector_menu():
    ops = 'Selecione uma das opções a seguir:\n '
    op1 = '1 - Importar notícias a partir de um arquivo CSV;\n '
    op2 = '2 - Exportar notícias para CSV;\n '
    op3 = '3 - Raspar notícias online;\n '
    op4 = '4 - Sair.\n '
    opcoes = ops + op1 + op2 + op3 + op4
    opcao = input(opcoes)
    if opcao == '1':
        path = input('Digite o nome do arquivo CSV a ser importado:\n')
        news = csv_importer(path)
        return create_news(news)
    elif opcao == '2':
        name = input('Digite o nome do arquivo CSV a ser exportado:\n')
        return csv_exporter(name)
    elif opcao == '3':
        pages = input('Digite a quantidade de páginas a serem raspadas:\n')
        result = scrape(fetcher=fetch_content, pages=int(pages))
        return create_news(result)
    elif opcao == '4':
        print('Encerrando script')
    else:
        sys.stderr.write('Opção inválida\n')


def op1():
    title = input('Digite o título:\n')
    return search_by_title(title)


def op2():
    date = input('Digite a data no formato aaaa-mm-dd:\n')
    return search_by_date(date)


def op3():
    source = input('Digite a fonte:\n')
    return search_by_source(source)


def op4():
    category = input('Digite a categoria:\n')
    return search_by_category(category)


def op5():
    return top_5_news()


def op6():
    return top_5_categories()


def op7():
    print('Encerrando script')


def analyzer_menu():
    opcao = int(op_func())
    switch = {
        1: op1,
        2: op2,
        3: op3,
        4: op4,
        5: op5,
        6: op6,
        7: op7,
    }
    switch[opcao]()
