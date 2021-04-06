from tech_news import database


def top_5_news():
    top_5 = database.top_5_news_aggregation()
    notice_list = []
    for item in top_5:
        notice_list.append((item['title'], item['url']))
    return notice_list


def top_5_categories():
    """Seu código deve vir aqui"""
