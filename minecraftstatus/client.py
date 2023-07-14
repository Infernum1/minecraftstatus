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
        :return: a :class:`ServerStatus` class instance
        """

        async with HTTPClient() as client:
            resp = await client._request("GET", base_url.format(f"mc/server/status/{ip_address}"))
            data = await resp.json()

        if data["online"] is False:
            raise ServerNotFound(ip_address)

        return ServerStatus(data)

    async def get_server_card(self, ip_address: str, custom_server_name: str = ""):
        """
        :param ip_address: IP address of the server
        :param custom_server_name: A custom server name to be displayed on the server card
        :type ip_address: :class:`str`
        :type custom_server_name: :class:`str`
        :raises `BadTextFormation`: text passed is not between 1-30 characters
        :return: an :class:`io.BytesIO` object co-relating the server card image.
        """
        if len(custom_server_name) == 0:
            custom_server_name = ip_address

        if len(ip_address) > 30 and len(ip_address) < 1:
            raise BadTextFormation()

        async with HTTPClient() as client:
            resp = await client._request(
                "GET", base_url.format(f"mc/server/status/{ip_address}/image?customName={custom_server_name}")
            )
            image = BytesIO(await resp.read())

        return image

    async def achievement(self, achievement: str):
        """
        :param achievement: name of the achievement to display.
        :type achievement: :class:`str`
        :raises BadTextFormation: text passed is not between 1-30 characters
        :return: an :class:`io.BytesIO` object co-relating the achievement image.
        """
        if len(achievement) > 30 and len(achievement) > 1:
            raise BadTextFormation()

        async with HTTPClient() as client:
            resp = await client._request("GET", base_url.format(f"mc/image/achievement/{achievement}"))
            image = BytesIO(await resp.read())

        return image

    async def splash_text(self, text: str):
        """
        :param text: text to display in the splash.
        :type text: :class:`str`
        :raises BadTextFormation: text passed is not between 1-30 characters
        :return: an :class:`io.BytesIO` object co-relating the splash text image.
        """
        if len(text) > 30 and len(text) < 1:
            raise BadTextFormation()

        async with HTTPClient() as client:
            resp = await client._request("GET", base_url.format(f"mc/image/splash/{text}"))
            image = BytesIO(await resp.read())

        return image
