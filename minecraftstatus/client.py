from io import BytesIO
from typing import Any
from urllib.parse import quote

from .server_status import ServerStatus
from .http import HTTPClient
from .errors import BadTextFormation, ServerNotFound

all = ("MCStatus", "ServerNotFound", "BadTextFormation")

BASE_URL = "https://api.iapetus11.me/{}"


class MCStatus(HTTPClient):
    """
    Asynchronous client for interacting with [api.iapetus.me](https://github.com/Iapetus-11/api.iapetus11.me)

    ???+ example "Usage Example"
        ```python
        import asyncio
        from minecraftstatus import MCStatus

        async def main():
            async with MCStatus() as client:
                status = await client.get_server("play.hypixel.com")
            print(status.host, status.port)

        if __name__ == "__main__":
            asyncio.run(main())
        ```
    """

    def __init__(self):
        super().__init__()

    async def __aenter__(self) -> "MCStatus":
        await self.open()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        await self.close()

    async def get_server(self, ip_address: str) -> ServerStatus:
        """
        Retrieve the status of a Minecraft server.

        Args:
            ip_address (str): The IP address or hostname of the Minecraft server.

        Returns:
            ServerStatus: An instance containing the server's status details.

        Raises:
            ServerNotFound: If the server is not found or is offline.

        ???+ example "Usage Example"
            ```python
            async with MCStatus() as client:
                status = await client.get_server("play.hypixel.com")
                print(status.host, status.port)
            ```
        """
        endpoint = BASE_URL.format(f"mc/server/status/{quote(ip_address)}")
        response = await self._request("GET", endpoint)
        data = await response.json()

        if not data.get("online", False):
            raise ServerNotFound(ip_address)

        return ServerStatus(data)

    async def get_server_card(self, ip_address: str, custom_server_name: str = None) -> BytesIO:
        """
        Generate a server card image for a Minecraft server.

        Args:
            ip_address (str): The IP address or hostname of the Minecraft server.
            custom_server_name (str, optional): Custom name to be displayed on the server card.
                Defaults to the provided IP address if not specified.

        Returns:
            BytesIO: A byte-stream object containing the server card image.

        Raises:
            BadTextFormation: If the provided text is not between 1 and 30 characters.

        ???+ example "Usage Example"
            ```python
            async with MCStatus() as client:
                image_stream = await client.get_server_card("play.hypixel.com", "My Server")

            # Use image_stream as needed (e.g., save to file)
            ```

        ???+ example "Server Card Example"
            ![Server Card Example](/images/server_card.png)

        """
        server_name = custom_server_name or ip_address
        if not (1 <= len(server_name) <= 30):
            raise BadTextFormation()

        endpoint = BASE_URL.format(f"mc/server/status/{quote(ip_address)}/image?customName={quote(server_name)}")
        response = await self._request("GET", endpoint)
        return BytesIO(await response.read())

    async def achievement(self, achievement_text: str) -> BytesIO:
        """
        Generate an image for a Minecraft achievement.

        Args:
            achievement_text (str): The name of the achievement to display (must be 1 to 30 characters).

        Returns:
            BytesIO: A byte-stream object containing the achievement image.

        Raises:
            BadTextFormation: If the achievement text is not within the 1-30 character limit.

        ???+ example "Usage Example"
            ```python
            async with MCStatus() as client:
                image_stream = await client.achievement("Mom, get the camera!!!")

            # Use image_stream as needed
            ```

        ???+ example "Achievement Image Example"
            ![Achievement Image Example](/images/achievement.png)

        """
        if not (1 <= len(achievement_text) <= 30):
            raise BadTextFormation()

        endpoint = BASE_URL.format(f"mc/image/achievement/{quote(achievement_text)}")
        response = await self._request("GET", endpoint)
        return BytesIO(await response.read())

    async def splash_text(self, text: str) -> BytesIO:
        """
        Generate a splash text image for Minecraft.

        Args:
            text (str): The text to display (must be between 1 and 30 characters).

        Returns:
            BytesIO: A byte-stream object containing the splash text image.

        Raises:
            BadTextFormation: If the text does not meet the required length.

        ???+ example "Usage Example"
            ```python
            async with MCStatus() as client:
                image_stream = await client.splash_text(text)

            # Use image_stream as needed
            ```

        ???+ example "Splash Text Example"
            ![Splash Text Example](/images/splash_text.png)
        """
        if not (1 <= len(text) <= 30):
            raise BadTextFormation()

        endpoint = BASE_URL.format(f"mc/image/splash/{quote(text)}")
        response = await self._request("GET", endpoint)
        return BytesIO(await response.read())
