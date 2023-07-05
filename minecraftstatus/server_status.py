from io import BytesIO

__all__ = ("ServerStatus",)


class ServerStatus:
    def __init__(self, resp):
        self.resp = resp

    """
    The ServerStatus class is used to return the data through :class:`MCStatus`.
    """

    @property
    def host(self) -> str:
        """
        The host name of the server. (same as the IP address)\n
        Returns:
        :class:`str`
        """
        return self.resp["host"]

    @property
    def port(self) -> int:
        """
        The port the server is running on. (usually 25565)\n
        Returns:
        :class:`int` or :class:`None`
        """
        return self.resp["port"]

    @property
    def is_online(self) -> bool:
        """
        Checks if the server is online.\n
        Returns:
        :class:`bool`: True if the server is online, False otherwise.
        """
        return self.resp["online"]

    @property
    def latency(self) -> int:
        """
        The latency of the server.\n
        Returns:
        :class:`int`: latency in milliseconds, -1 if the server is offline.
        """
        return self.resp["latency"]

    @property
    def max_players(self) -> int:
        """
        The maximum players a server can accommodate.\n
        Returns:
        :class:`int` or :class:`None`
        """
        return self.resp["max_players"]

    @property
    def favicon(self) -> BytesIO:
        """
        The server favicon
        Returns:
        :class:`io.BytesIO` object or :class:`None`
        """
        if self.resp["favicon"]:
            data = bytes(self.resp["favicon"], "utf-8")
            favicon = BytesIO(data)
            return favicon
        return None

    @property
    def version_info(self) -> dict:
        """
        The descriptive version info of the server.\n
        Returns:
        :class:`dict[Any, Any]`
        """
        return self.resp["version"]

    @property
    def online_players(self) -> list:
        """
        A list of dicts of the online players of the server and their UUID/XUID.\n
        Returns:
        :class:`list[dict[str, str]]`
        """
        return self.resp["players"]

    @property
    def online_player_count(self) -> int:
        """
        The online player count of the server.\n
        Returns:
        :class:`int` or :class:`None`
        """
        return self.resp["online_players"]

    @property
    def clean_motd(self) -> str:
        """
        The clean message of the day (MOTD) of the server. (without the color codes)\n
        Returns:
        :class:`str` or :class:`None`
        """
        return self.resp["motd_clean"]

    @property
    def motd(self) -> str:
        """
        The message of the day (MOTD) of the server. (along with the colour codes)\n
        Returns:
        :class:`str` or :class:`None`
        """
        return self.resp["motd"]

    @property
    def gamemode(self) -> str:
        """
        The game mode of the server.
        Returns:
        :class:`str` or :class:`None`
        """
        return self.resp["gamemode"]

    @property
    def game_map(self) -> str:
        """
        The game map of the server.
        Returns:
        :class:`str` or :class:`None`
        """
        return self.resp["map"]
