from typing import Any
from .client import MCStatus

class ServerStatus(MCStatus):
    def __init__(self, resp: str) -> None:
        self.resp = resp

    @property
    def host(self) -> str:
        """
        Returns the host of the server.
        Returns
        -------
        str
        """
        return self.resp["host"]

    @property
    def port(self) -> int:
        """
        Returns the port of the server.
        Returns
        -------
        int or None
        """
        return self.resp["port"]

    @property
    def is_online(self) -> bool:
        """
        Checks if the server is online.
        Returns
        -------
        bool: True if the server is online, False otherwise.
        """
        return self.resp["online"]

    @property
    def latency(self) -> int:
        """
        Returns the latency of the server.
        Returns
        -------
        int: latency in milliseconds, -1 if the server is offline.
        """
        return self.resp["latency"]

    @property
    def max_players(self) -> int:
        """
        Returns the maximum players of the server.
        Returns
        -------
        int or None
        """
        return self.resp["max_players"]
    
    @property
    def favicon(self) -> str:
        """
        Returns base64 data of the favicon of the server.
        Returns
        -------
        str or None
        """
        return self.resp["favicon"]
        
    @property
    def version_info(self) -> dict[Any, Any]:
        """
        Returns the version info of the server.
        Returns
        -------
        dict[Any, Any]
        """
        return self.resp["version"]

    @property
    def online_players(self) -> list[str]:
        """
        Returns a list of the online players of the server.
        Returns
        -------
        list[str]
        """
        return self.resp["players"]

    @property
    def online_player_count(self) -> int:
        """
        Returns the online player count of the server.
        Returns
        -------
        int or None
        """
        return self.resp["online_players"]

    @property
    def clean_motd(self) -> str:
        """
        Returns the clean message of the day (MOTD) of the server.
        Returns
        -------
        str or None
        """
        return self.resp["motd_clean"]
    
    @property
    def motd(self) -> str:
        """
        Returns the message of the day (MOTD) of the server.
        Returns
        -------
        str or None
        """
        return self.resp["motd"]
    
    @property
    def gamemode(self) -> str:
        """
        Returns the game mode of the server.
        Returns
        -------
        str or None
        """
        return self.resp["gamemode"]
    
    @property
    def game_map(self) -> str:
        """
        Returns the game map of the server.
        Returns
        -------
        str or None
        """
        return self.resp["map"]
