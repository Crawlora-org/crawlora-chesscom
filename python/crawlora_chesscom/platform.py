"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class ChessComClient(CrawloraClient):
    """Synchronous Chess.com API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-chesscom-python/0.1.1')
        super().__init__(*args, **kwargs)

    def club(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-club', params, response_type=response_type, timeout=timeout, headers=headers)

    def club_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-club-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def club_members(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-club-members', params, response_type=response_type, timeout=timeout, headers=headers)

    def country(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-country', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-match-live', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_live_board(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-match-live-board', params, response_type=response_type, timeout=timeout, headers=headers)

    def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_board(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-match-board', params, response_type=response_type, timeout=timeout, headers=headers)

    def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_clubs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-clubs', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_game_month(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-game-month', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_game_month_pgn(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-game-month-pgn', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_game_archives(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-game-archives', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_live_games_base_time(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-live-games-base-time', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_live_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-live-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_games_to_move(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-games-to-move', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_is_online(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-is-online', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-player-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    def puzzle(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-puzzle', params, response_type=response_type, timeout=timeout, headers=headers)

    def puzzle_random(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-puzzle-random', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-tournament', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_round(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-tournament-round', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_round_group(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('chesscom-tournament-round-group', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncChessComClient(AsyncCrawloraClient):
    """Asynchronous Chess.com API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-chesscom-python/0.1.1')
        super().__init__(*args, **kwargs)

    async def club(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-club', params, response_type=response_type, timeout=timeout, headers=headers)

    async def club_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-club-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def club_members(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-club-members', params, response_type=response_type, timeout=timeout, headers=headers)

    async def country(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-country', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-match-live', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_live_board(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-match-live-board', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_board(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-match-board', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_clubs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-clubs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_game_month(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-game-month', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_game_month_pgn(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-game-month-pgn', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_game_archives(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-game-archives', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_live_games_base_time(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-live-games-base-time', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_live_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-live-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_games_to_move(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-games-to-move', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_is_online(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-is-online', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-player-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def puzzle(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-puzzle', params, response_type=response_type, timeout=timeout, headers=headers)

    async def puzzle_random(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-puzzle-random', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-tournament', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_round(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-tournament-round', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_round_group(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('chesscom-tournament-round-group', params, response_type=response_type, timeout=timeout, headers=headers)
