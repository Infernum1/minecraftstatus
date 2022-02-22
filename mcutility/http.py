from aiohttp import ClientSession
from typing import Any


__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self):
        self.session = None

    async def request(self, method: str, endpoint: str, headers: dict[Any, Any]) -> dict[Any, dict[Any, Any]]:
        self.session = ClientSession()
        try:
            resp = await self.session.request(method, endpoint, headers=headers)
        except KeyError:
            await self.session.close()
            return await resp.json()
        await self.session.close()
        return await resp.json()
