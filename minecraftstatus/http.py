from aiohttp import ClientSession

__all__ = ("HTTPClient",)


class HTTPClient:
    def __init__(self):
        self.session = None

    async def open(self):
        self.session = ClientSession()

    async def close(self):
        if self.session:
            await self.session.close()

        self.session = None

    async def _request(self, method: str, endpoint: str) -> dict:
        if self.session:
            resp = await self.session.request(method, endpoint)
            return resp

        raise RuntimeError("There was no open session found. Call .open() or use this class as a context manager")

    async def __aenter__(self):
        await self.open()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.close()
