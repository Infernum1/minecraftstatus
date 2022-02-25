from aiohttp import ClientSession
import aiohttp



__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self):
        self.session = None

    async def request(self, method: str, endpoint: str) -> dict:
        self.session = ClientSession()
        try:
            resp = await self.session.request(method, endpoint)
        except KeyError:
            await self.session.close()
            return resp
        await self.session.close()
        return resp
