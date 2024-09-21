from aiohttp import ClientSession

class Methods:
    GET = 'get'
    POST = 'post'
    PATCH = 'patch'
    PUT = 'put'
    DELETE = 'delete'


async def make_request(method, url, data=None, headers=None):
    async with ClientSession() as session:
        if method == Methods.GET:
            async with session.get(url) as response:
                return await response.json()

        elif method == Methods.POST:
            async with session.post(url, data=data, headers=headers) as response:
                return await response.json()

        elif method == Methods.PATCH:
            async with session.patch(url, data=data, headers=headers) as response:
                return await response.json()

        elif method == Methods.PUT:
            async with session.put(url, data=data, headers=headers) as response:
                return await response.json()

        elif method == Methods.DELETE:
            async with session.delete(url, headers=headers) as response:
                return await response.json()


class AsyncRequest:
    async def get(self, **kwargs):
        return await make_request(method=Methods.GET, **kwargs)
    async def post(self, **kwargs):
        return await make_request(method=Methods.POST, **kwargs)
    async def patch(self, **kwargs):
        return await make_request(method=Methods.PATCH, **kwargs)
    async def put(self, **kwargs):
        return await make_request(method=Methods.PUT, **kwargs)
    async def delete(self, **kwargs):
        return await make_request(method=Methods.DELETE, **kwargs)


request = AsyncRequest()
