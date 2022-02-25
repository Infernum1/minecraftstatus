from aiohttp import ClientSession
import aiohttp



__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self):
        self.session = None

    async def request(self, method: str, endpoint: str) -> dict:
        self.session = ClientSession()
        resp = await self.session.request(method, endpoint)
        await self.session.close()
        return await resp
