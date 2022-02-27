from aiohttp import ClientSession

__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self):
        self.session = None

    async def _request(self, method: str, endpoint: str) -> dict:
        self.session = ClientSession()
        resp = await self.session.request(method, endpoint)
        return resp

    async def _close(self):
        if self.session:
            await self.session.close()
