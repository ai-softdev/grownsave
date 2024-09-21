from typing import List


async def get_list_data(model, page: int, limit: int, filter=None, includes: List[str] = None):
    return {
        'data': await model.paginate(page=page, limit=limit, filter=filter, includes=includes),
        'total': await model.count(filter=filter),
        'page': page,
        'limit': limit
    }
