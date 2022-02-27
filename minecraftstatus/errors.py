
class ServerNotFound(Exception):
    """
    Raised when a server is not found or is offline.
    """
    def __init__(self):
        super().__init__("Server not found or is offline.")

class BadCharacterFormation(Exception):
    """
    Raised when more than 30 characters are passed for some endpoints.
    """
    def __init__(self):
        super().__init__("Too many characters passed. Must be between 1 and 30.")