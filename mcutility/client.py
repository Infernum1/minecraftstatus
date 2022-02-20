
from .server import ServerStatus
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
        Makes a request to the Minecraft status endpoint.
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
        favicon: The base64 data of the favicon of the server..
        game_map: The game map of the server.
        game_mode: The game mode of the server.
        """

        resp = await self.request(
            "GET", base_url.format(f"mc/server/status/{ip_address}")
        )
        return ServerStatus(resp)
