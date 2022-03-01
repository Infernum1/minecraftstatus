__all__ = (
    "ServerNotFound",
    "BadTextFormation",
)


class ServerNotFound(Exception):
    """
    Exception raised when a server is not found or is offline. Has the following attribute:

    Attributes
    ----------
    address: (:class:`str`)the address of the server passed.
    """

    def __init__(self, address: str):
        self.address = address
        super().__init__(f"Server '{self.address}' not found or is offline.")


class BadTextFormation(Exception):
    """
    Exception raised when the characters passed are not between 1 and 30 for some endpoints.
    """

    def __init__(self):
        super().__init__("Character limit is between 1 and 30.")
