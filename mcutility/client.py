from io import BytesIO

from .server_status import ServerStatus
from .http import HTTPClient


__all__ = ("MCStatus",)
base_url = "https://api.iapetus11.me/{}"


class MCStatus(HTTPClient):
    """
    The main MCStatus class.
    """

    def __init__(self) -> None:
        HTTPClient.__init__(self)

    async def get_server(self, ip_address: str):
        """
        Makes a request to the server status endpoint.
        Parameters:
        ----------
        ip_address: IP address of the server.
        Returns:
        -------
        ServerStatus class instance.
        Attributes:
        -----------
        host: The host of the server.
        port: The port of the server.
        is_online: True if the server is online, False otherwise.
        latency: The latency of the server.
        max_players: The maximum players of the server.
        online_players: The online players of the server.
        motd: The message of the day of the server.
        favicon: The base64 data of the favicon of the server.
        game_map: The game map of the server.
        game_mode: The game mode of the server.
        """

        resp = await self.request(
            "GET", base_url.format(f"mc/server/status/{ip_address}")
        )
        resp = await resp.json()
        return ServerStatus(resp)

    async def get_server_card(self, ip_address: str):
        """
        Makes a request to the server-card endpoint.
        Parameters:
        ----------
        ip_address: IP address of the server.
        Returns:
        -------
        io.BytesIO object co-relating the server card.
        """

        res = await self.image_request(
            "GET", base_url.format(f"mc/server/status/{ip_address}/image")
        )
        image = BytesIO(await res.read())
        return image

    async def achievement(self, achievement: str):
        """
        Makes a request to the achievement endpoint.
        Parameters
        ----------
        achievement: name of the achievement to display.
        Returns
        -------
        io.BytesIO object co-relating the achievement image.
        """

        res = await self.request(
            "GET", base_url.format(f"mc/image/achievement/{achievement}")
        )
        image = BytesIO(await res.read())
        return image

    async def splash_text(self, text: str):
        """
        Makes a request to the splash text endpoint.
        Parameters
        ----------
        text: text to display in the splash.
        Returns
        -------
        io.BytesIO object co-relating the splash image.
        """

        res = await self.request("GET", base_url.format(f"mc/image/splash/{text}"))
        image = BytesIO(await res.read())
        return image
