"""Typed Chess.com client for the Crawlora hosted API."""

from .platform import ChessComClient, AsyncChessComClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = ChessComClient
AsyncClient = AsyncChessComClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Chess.com'
PLATFORM = 'chesscom'
CONTRACT_REVISION = 'sha256:24942ed44f40dfeeb9e9c8cb74152690adfab8ebe286196ee747524c2007a928'

__all__ = [
    "ChessComClient", "AsyncChessComClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
