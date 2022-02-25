from aiohttp import ClientSession



__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self):
        self.session = None

    async def request(self, method: str, endpoint: str) -> dict:
        self.session = ClientSession()
        try:
            resp = await self.session.request(method, endpoint)
        except KeyError:
            return resp
        return resp

    async def close(self):
        if self.session:
            return await self.session.close()