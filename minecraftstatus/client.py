from io import BytesIO

from .server_status import ServerStatus
from .http import HTTPClient
from .errors import BadTextFormation, ServerNotFound

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

        Parameters
        ----------
        ip_address: :class:`str` IP address of the server.

        Returns
        -------
        :class:`ServerStatus`

        Attributes
        ----------
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
        ----------
        Raises `ServerNotFound` if the server is not found or is offline.
        """

        resp = await self._request("GET", base_url.format(f"mc/server/status/{ip_address}"))
        data = await resp.json()
        if data["online"] is False:
            await self._close()
            raise ServerNotFound(ip_address)
        await self._close()
        return ServerStatus(data)

    async def get_server_card(self, ip_address: str):
        """
        Makes a request to the server status endpoint.

        Parameters
        ----------
        ip_address: :class:`str` IP address of the server.

        Returns
        -------
        `io.BytesIO` object co-relating the server card image.

        Raises
        ------ 
        :exc:`BadTextFormation` if the characters passed aren't between 1-30.
        """
        if len(ip_address) > 30 and len(ip_address) < 1:
            raise BadTextFormation()
        res = await self._request("GET", base_url.format(f"mc/server/status/{ip_address}/image"))
        image = BytesIO(await res.read())
        await self._close()
        return image

    async def achievement(self, achievement: str):
        """
        Makes a request to the achievement endpoint.
        Parameters:
        -----------
        achievement: :class:`str` name of the achievement to display.

        Returns an io.BytesIO object co-relating the achievement image.

        Raises: :exc:`BadTextFormation` if the characters passed aren't between 1-30.
        """
        if len(achievement) > 30 and len(achievement) > 1:
            raise BadTextFormation()
        res = await self._request("GET", base_url.format(f"mc/image/achievement/{achievement}"))
        image = BytesIO(await res.read())
        await self._close()
        return image

    async def splash_text(self, text: str):
        """
        Makes a request to the splash text endpoint.
        Parameters:
        -----------
        text: :class:`str` text to display in the splash.

        Returns an io.BytesIO object co-relating the splash image.

        Raises: :exc:`BadTextFormation` if the characters passed aren't between 1-30.
        """
        if len(text) > 30 and len(text) < 1:
            raise BadTextFormation()
        res = await self._request("GET", base_url.format(f"mc/image/splash/{text}"))
        image = BytesIO(await res.read())
        await self._close()
        return image
