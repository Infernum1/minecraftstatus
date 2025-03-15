from typing import Any, Optional
from aiohttp import ClientSession

all = ("HTTPClient",)


class HTTPClient:
    """
    A simple asynchronous HTTP client wrapper using aiohttp.
    """

    def __init__(self) -> None:
        self.session: Optional[ClientSession] = None

    async def open(self) -> None:
        """
        Open a new aiohttp ClientSession.
        """
        self.session = ClientSession()

    async def close(self) -> None:
        """
        Close the aiohttp ClientSession.
        """
        if self.session:
            await self.session.close()
            self.session = None

    async def _request(self, method: str, endpoint: str) -> Any:
        """
        Make an HTTP request.

        Args:
            method (str): The HTTP method (e.g., "GET", "POST").
            endpoint (str): The API endpoint URL.

        Raises:
            RuntimeError: If no open session is found.
            aiohttp.ClientResponseError: If the response status is not 200.

        Returns:
            aiohttp.ClientResponse: The response object.
        """
        if not self.session:
            raise RuntimeError("No open session found. Call open() or use the client as a context manager.")

        response = await self.session.request(method, endpoint)
        response.raise_for_status()
        return response
