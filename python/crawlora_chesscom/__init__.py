"""Typed Chess.com client for the Crawlora hosted API."""

from .platform import ChessComClient, AsyncChessComClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = ChessComClient
AsyncClient = AsyncChessComClient
__version__ = '0.1.1'
DISPLAY_NAME = 'Chess.com'
PLATFORM = 'chesscom'
CONTRACT_REVISION = 'sha256:bb52aafac634d8bd443235e38fe6f1e7503b53f83d9e87a10df59858337a4628'

__all__ = [
    "ChessComClient", "AsyncChessComClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
