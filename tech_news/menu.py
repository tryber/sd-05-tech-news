import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content, scrape
from tech_news.database import create_news


ops = 'Selecione uma das opções a seguir:\n '
op1 = '1 - Importar notícias a partir de um arquivo CSV;\n '
op2 = '2 - Exportar notícias para CSV;\n '
op3 = '3 - Raspar notícias online;\n '
op4 = '4 - Sair.\n '
opcoes = ops + op1 + op2 + op3 + op4


def collector_menu():
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


def analyzer_menu():
    """Seu código deve vir aqui"""
