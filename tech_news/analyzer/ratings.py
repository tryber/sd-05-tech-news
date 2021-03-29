# from tech_news.database import find_news


# def top_5_news():
#     news = find_news()
#     totalizer = []
#     for art in news:
#         totalizer.append(
#             {
#                 'title': art['title'],
#                 'url': art['url'],
#                 'total': (art['comments_count']+art['shares_count'])},
#         )
#         # totalizer.append({'total': (art['comments_count']+art['shares_count'])})

#     print(totalizer)
#     def myFunc(e):
#         return e['total']
#     sorted = totalizer.sort(key=myFunc)
#     # https://www.w3schools.com/python/ref_list_sort.asp
#     # limited = sorted[:5]
#     print(sorted)
#     resultado = []
#     for noticia in sorted:
#         resultado.append((noticia['title'], noticia['url']))
    
#     return resultado

# def top_5_categories():
#     """Seu código deve vir aqui"""
