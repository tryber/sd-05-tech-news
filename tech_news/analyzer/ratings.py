from operator import itemgetter
from tech_news.model import tech_news_model

cursor = tech_news_model.find_cursor
PROJECTION = {"_id": False, "title": True, "url": True}


def top_5_news():
    """Seu código deve vir aqui"""
    agg_search = [
        {
            "$project": {
                "_id": 0,
                "title": 1,
                "url": 1,
                "total": 1,
                "comments_count": 1,
                "shares_count": 1,
            }
        }
    ]
    agg_search.append(
        {
            "$addFields": {
                "total": {"$add": ["$comments_count", "$shares_count"]}
            }
        }
    )
    agg_search.append({"$sort": {"total": -1, "title": 1}})
    agg_search.append({"$limit": 5})

    search = cursor(params=agg_search, agg=True)
    if len(search) == 0:
        return []
    result = [(item["title"], item["url"]) for item in search]
    return result


def top_5_categories():
    """Seu código deve vir aqui"""
    get_categories = cursor(projection={"categories": True, "_id": False})
    cat = []
    for item in get_categories:
        cat.extend(item['categories'])
    contagem = {key: cat.count(key) for key in set(cat)}
    categories = [
        k for k, v in sorted(contagem.items(), key=itemgetter(1, 0))
    ]
    return categories[:5]
