from .client import *
from .errors import *
from .server_status import *

__version__ = "0.0.7"
__author__ = "Infernum1"
__title__ = "minecraftstatus"
__copyright__ = "Copyright (c) 2022 Infernum1"
__summary__ = "minecraftstatus is an asynchronous wrapper for https://api.iapetus11.me."
__all__ = ("MCStatus", "HTTPClient", "ServerStatus", "ServerNotFound", "BadTextFormation")
