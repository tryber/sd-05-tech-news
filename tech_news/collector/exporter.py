from tech_news import database
import csv


def csv_exporter(filepath):
    """Escreve um arquivo CSV com dados do MongoDB."""

    # Uso do Try, Assert e Except resulta em
    # erro no Flake8, por "too complex (6)".
    # assert filepath.endswith('.csv')
    # except AssertionError:
    #     raise ValueError('Formato invalido')
    if (not filepath.endswith('.csv')):
        raise ValueError('Formato invalido')

    header = [
        'url',
        'title',
        'timestamp',
        'writer',
        'shares_count',
        'comments_count',
        'summary',
        'sources',
        'categories'
    ]

    news = database.find_news()

    with open(filepath, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=header, delimiter=';')

        for rows in news:
            for key in rows:
                # print(key, 'key -------')
                if type(rows[key]) == list:
                    # print(rows[key], 'antes')
                    rows[key] = ",".join(rows[key])
                    # print(rows[key], 'depois')
        writer.writeheader()
        writer.writerows(news)
