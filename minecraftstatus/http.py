from aiohttp import ClientSession
import aiohttp



__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self):
        self.session = None

    async def _request(self, method: str, endpoint: str) -> dict:
        self.session = ClientSession()
        try:
            resp = await self.session.request(method, endpoint)
        except KeyError:
            return resp
        return resp

    async def _close(self):
        if self.session:
            self.session.close()