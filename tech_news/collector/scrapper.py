import requests
from time import sleep
from parsel import Selector


def fetch_content(url, timeout=3, delay=0.5):
    '''Realiza uma requisição HTTP e retorna conteúdo como resposta.'''

    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)

        if response and response.status_code != 200:
            return ''

        return response.text

    except requests.Timeout:
        return ''


selectors = {
    'title': '.tec--article__header__title::text',
    'timestamp': '#js-article-date::attr(datetime)',
    'writer': 'a.tec--author__info__link::text',
    'shares': '.tec--toolbar__item::text',
    'comments': '#js-comments-btn::attr(data-count)',
    'summary': '.tec--article__body p::text',
    'sources': '.z--mb-16 a::text',
    'categories': '#js-categories a::text'
}


def article_element(url, sel):
    title = sel.css(selectors['title']).get()
    timestamp = sel.css(selectors['timestamp']).get()
    writer = sel.css(selectors['writer']).get()
    shares_count = sel.css(selectors['shares']).re_first(r'\d') or '0'
    comments_count = sel.css(selectors['comments']).get()
    summary = sel.css(selectors['summary']).get()
    sources = sel.css(selectors['sources']).getall()
    categories = sel.css(selectors['categories']).getall()

    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'shares_count': int(shares_count),
        'comments_count': int(comments_count),
        'summary': summary,
        'sources': sources,
        'categories': categories
    }


def scrape(fetcher, pages=1):
    '''Raspagem das informações das últimas notícias TechMundo.'''
    url_news = 'https://www.tecmundo.com.br/novidades?page='
    all_articles = []

    for page in range(pages):
        url = f'{url_news}{page}'
        news_response = fetcher(url)
        news_selector = Selector(text=news_response)
        url_selector = '.tec--list__item .tec--card__title__link::attr(href)'
        news_urls = news_selector.css(url_selector).getall()

        for url in news_urls:
            article_response = fetcher(url)
            article_selector = Selector(text=article_response)
            all_articles.append(article_element(url, article_selector))

    return all_articles

# Honestidade Academica Para melhor organização do código e para atender os
# requisitos do Flake8, utilizei como modelo o PR do Pedro Calado - T05 para
# criar o objeto dos seletores e a função que retornar o objeto de resposta.
