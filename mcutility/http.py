from aiohttp import ClientSession

from typing import Any


__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self) -> None:
        self.session = None

    async def request(self, method: str, endpoint: str) -> dict[Any, Any]:
        self.session = ClientSession()
        try:
            resp = await self.session.request(method, endpoint)
        except KeyError:
            await self.session.close()
            return await resp.json()
        await self.session.close()
        return await resp.json()

    async def image_request(self, method: str, endpoint: str):
        self.session = ClientSession()
        try:
            resp = await self.session.request(method, endpoint)
        except KeyError:
            await self.session.close()
            return await resp
        await self.session.close()
        return await resp
