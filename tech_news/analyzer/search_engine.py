from tech_news.model import tech_news_model

cursor = tech_news_model.find_cursor
PROJECTION = {"_id": False, "title": True, "url": True}

def validate_date(date):
    year, month, day = date.split("-")
    try:
        assert len(year) == 4
        assert len(month) == 2
        assert len(day) == 2
    except AssertionError:
        raise ValueError("Invalid date")
    else:
        return date

def search_by_title(title):
    PARAMS = {"title": {"$regex": f".*{title}.*", "$options": "i"}}
    search = cursor(params=PARAMS, projection=PROJECTION)
    if len(search) == 0:
        return []
    result = [tuple(reversed(item.values())) for item in search]
    return result

def search_by_date(date, validator=validate_date):
    valid_date = validator(date)
    PARAMS = {"timestamp": {"$regex": f"^{valid_date}"}}
    search = cursor(params=PARAMS, projection=PROJECTION)
    if len(search) == 0:
        return []
    result = [tuple(reversed(item.values())) for item in search]
    return result

def search_by_source(source):
    PARAMS = {"sources": {"$regex": source, "$options": "i"}}
    search = cursor(params=PARAMS, projection=PROJECTION)
    if len(search) == 0:
        return []
    result = [tuple(reversed(item.values())) for item in search]
    return result

def search_by_category(category):
    PARAMS = {"categories": {"$regex": category, "$options": "i"}}
    search = cursor(params=PARAMS, projection=PROJECTION)
    if len(search) == 0:
        return []
    result = [tuple(reversed(item.values())) for item in search]
    return result