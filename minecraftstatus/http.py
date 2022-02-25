from aiohttp import ClientSession
import aiohttp



__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self):
        self.session = None

    async def request(self, method: str, endpoint: str) -> dict:
        async with aiohttp.ClientSession() as self.session:
            async with self.session.request(method, endpoint) as resp:
                return resp
