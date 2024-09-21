import random
from datetime import datetime, timedelta
from typing import List


def random_date(start: str, end: str):
    start_date = datetime.strptime(start, '%Y-%m-%d').date()
    end_date = datetime.strptime(end, '%Y-%m-%d').date()
    time_delta = end_date - start_date
    random_days = random.randrange(time_delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date


def random_datetime(start: datetime.date, end: datetime.date):
    time_delta = end - start
    random_days = random.randrange(time_delta.days)
    random_seconds = random.randint(0, 86400)
    return start + timedelta(days=random_days, seconds=random_seconds)


async def get_list_data(model, page: int, limit: int, filter=None, includes: List[str] = None):
    return {
        'data': await model.paginate(page=page, limit=limit, filter=filter, includes=includes),
        'total': await model.count(filter=filter),
        'page': page,
        'limit': limit
    }
