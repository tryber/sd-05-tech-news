from tech_news.database import search_news


def top_5_news():
    # compatilhamentos e comentarios
    busca = search_news({})
    # https://stackoverflow.com/questions/403421/
    # how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
    newlist = sorted(
        busca,
        key=lambda x: x["comments_count"] + x["shares_count"],
        reverse=True,
    )
    if len(newlist) == 0:
        return []
    # https://www.w3schools.com/python/python_tuples.asp
    return [(news["title"], news["url"]) for news in newlist][:5]


def top_5_categories():
    """Seu código deve vir aqui"""
