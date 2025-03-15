from io import BytesIO

all = ("ServerStatus",)


class ServerStatus:
    def __init__(self, data: dict) -> None:
        self.data = data

    @property
    def host(self) -> str:
        """
        Get the host name of the server

        Returns:
            str: The host name (same as the IP address)
        """
        return self.data.get("host", "")

    @property
    def port(self) -> int:
        """
        Get the port the server is running on

        Returns:
            int: The port number, -1 if not available
        """
        return self.data.get("port", -1)

    @property
    def is_online(self) -> bool:
        """
        Check if the server is online

        Returns:
            bool: True if the server is online, False otherwise
        """
        return self.data.get("online", False)

    @property
    def latency(self) -> int:
        """
        Get the latency of the server

        Returns:
            int: Latency in milliseconds, -1 if the server is offline
        """
        return self.data.get("latency", -1)

    @property
    def max_players(self) -> int:
        """
        Get the maximum players the server can accommodate

        Returns:
            int: The maximum number of players
        """
        return self.data.get("max_players", 0)

    @property
    def favicon(self) -> BytesIO:
        """
        Get the server favicon

        Returns:
            BytesIO: An io.BytesIO object containing the favicon, or None if not available
        """
        favicon_data = self.data.get("favicon")
        if favicon_data:
            return BytesIO(favicon_data.encode("utf-8"))
        return None

    @property
    def version_info(self) -> dict:
        """
        Get the descriptive version info of the server

        Returns:
            dict: The version information
        """
        return self.data.get("version", {})

    @property
    def online_players(self) -> list:
        """
        Get a list of online players on the server

        Returns:
            list: A list of dictionaries containing player information
        """
        return self.data.get("players", [])

    @property
    def online_player_count(self) -> int:
        """
        Get the online player count of the server

        Returns:
            int: The number of online players
        """
        return self.data.get("online_players", 0)

    @property
    def clean_motd(self) -> str:
        """
        Get the clean Message Of The Day (MOTD) of the server

        Returns:
            str: The clean MOTD (without color codes)
        """
        return self.data.get("motd_clean", "")

    @property
    def motd(self) -> str:
        """
        Get the message of the day (MOTD) of the server

        Returns:
            str: The MOTD (with color codes)
        """
        return self.data.get("motd", "")

    @property
    def gamemode(self) -> str:
        """
        Get the game mode of the server

        Returns:
            str: The game mode
        """
        return self.data.get("gamemode", "")

    @property
    def game_map(self) -> str:
        """
        Get the game map of the server

        Returns:
            str: The game map
        """
        return self.data.get("map", "")
