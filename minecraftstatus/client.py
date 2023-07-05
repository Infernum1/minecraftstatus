from io import BytesIO

from .server_status import ServerStatus
from .http import HTTPClient
from .errors import BadTextFormation, ServerNotFound

__all__ = ("MCStatus", "ServerNotFound", "BadTextFormation")  # docs don't properly work without this
base_url = "https://api.iapetus11.me/{}"


class MCStatus(HTTPClient):
    """
    The main MCStatus class.
    """

    def __init__(self) -> None:
        HTTPClient.__init__(self)

    async def get_server(self, ip_address: str):
        """
        :param ip_address: IP address of the server
        :type ip_address: :class:`str`
        :raises ServerNotFound: server not found or is offline
        :return: a :class:`ServerStatus` class instance with the following attributes

        Attributes
        ----------
        host: Returns the host of the server or `None` (:class:`str`)
        port: Returns the port of the server or `None` (:class:`int`).
        is_online: Returns :class:`True` if the server is online, :class:`False` otherwise (:class:`bool`).
        latency: Returns the latency of the server (:class:`int`).
        max_players: Returns the maximum players allowed in the server (:class:`int`).
        online_players: Returns the current online players of the server (:class:`int`).
        motd: Returns the message of the day of the server (:class:`str`).
        clean_motd: Returns the **clean** message of the day of the server (:class:`str`).
        favicon: Returns an io.BytesIO object co-relating the server favicon (:class:`BytesIO`).
        game_map: Returns the game map of the server (:class:`str`).
        game_mode: Returns the game mode of the server (:class:`str`).
        """

        resp = await self._request("GET", base_url.format(f"mc/server/status/{ip_address}"))
        data = await resp.json()
        if data["online"] is False:
            await self._close()
            raise ServerNotFound(ip_address)

        await self._close()
        return ServerStatus(data)

    async def get_server_card(self, ip_address: str, custom_server_name: str = ""):
        """
        :param ip_address: IP address of the server
        :param custom_server_name: A custom server name to be displayed on the server card
        :type ip_address: :class:`str`
        :type custom_server_name: :class:`str`
        :raises `BadTextFormation`: text passed is not between 1-30 characters
        :return: an io.BytesIO object co-relating the server card image.
        """
        if len(custom_server_name) == 0:
            custom_server_name = ip_address

        if len(ip_address) > 30 and len(ip_address) < 1:
            raise BadTextFormation()

        res = await self._request(
            "GET", base_url.format(f"mc/server/status/{ip_address}/image?customName={custom_server_name}")
        )
        image = BytesIO(await res.read())
        await self._close()
        return image

    async def achievement(self, achievement: str):
        """
        :param achievement: name of the achievement to display.
        :type achievement: :class:`str`
        :raises BadTextFormation: text passed is not between 1-30 characters
        :return: an io.BytesIO object co-relating the achievement image.
        """
        if len(achievement) > 30 and len(achievement) > 1:
            raise BadTextFormation()

        res = await self._request("GET", base_url.format(f"mc/image/achievement/{achievement}"))
        image = BytesIO(await res.read())
        await self._close()
        return image

    async def splash_text(self, text: str):
        """
        :param text: text to display in the splash.
        :type text: :class:`str`
        :raises BadTextFormation: text passed is not between 1-30 characters
        :return: an io.BytesIO object co-relating the splash text image.
        """
        if len(text) > 30 and len(text) < 1:
            raise BadTextFormation()

        res = await self._request("GET", base_url.format(f"mc/image/splash/{text}"))
        image = BytesIO(await res.read())
        await self._close()
        return image
