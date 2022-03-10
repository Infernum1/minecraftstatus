from aiohttp import ClientSession
from typing import Any


__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self):
        self.session = None

    async def request(self, method: str, endpoint: str) -> dict[Any, dict[Any, Any]]:
        self.session = ClientSession()
        try:
            resp = await self.session.request(method, endpoint)
        except KeyError:
            return await resp
        return await resp
