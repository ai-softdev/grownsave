import random
from datetime import datetime, timedelta
from typing import List


def random_date(start:str, end:str):
    start_date = datetime.strptime(start, '%Y-%m-%d').date()
    end_date = datetime.strptime(end, '%Y-%m-%d').date()
    time_delta = end_date - start_date
    random_days = random.randrange(time_delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date


def random_datetime(start: str, end: str):
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')
    time_delta = end_date - start_date
    random_days = random.randrange(time_delta.days)
    random_seconds = random.randint(0, 86400)
    random_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return random_date


async def get_list_data(model, page: int, limit: int, filter=None, includes: List[str] = None):
    return {
        'data': await model.paginate(page=page, limit=limit, filter=filter, includes=includes),
        'total': await model.count(filter=filter),
        'page': page,
        'limit': limit
    }
