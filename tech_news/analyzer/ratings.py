from tech_news.database import search_news


def top_5_news():
    search = search_news({})
    new_list = sorted(
        search,
        key=lambda x: x["comments_count"] + x["shares_count"],
        # para ordenar do maior para o menor
        reverse=True,
    )
    if len(new_list) == 0:
        return []
    return [(item["title"], item["url"]) for item in new_list][:5]
    # forma de fazer map no python
    # https://www.w3schools.com/python/python_tuples.asp
    # https://stackoverflow.com/questions/403421/how-to-sort
    # -a-list-of-objects-based-on-an-attribute-of-the-objects


def top_5_categories():
    """Seu código deve vir aqui"""
