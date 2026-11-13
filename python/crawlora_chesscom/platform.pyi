from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelChesscomPublicDataResponse = TypedDict('ModelChesscomPublicDataResponse', {
    'cache_control': NotRequired[str],
    'data': NotRequired[dict[str, Any]],
    'etag': NotRequired[str],
    'last_modified': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelChesscomPuzzleResponse = TypedDict('ModelChesscomPuzzleResponse', {
    'cache_control': NotRequired[str],
    'data': NotRequired[ModelChesscomPuzzleData],
    'source_url': NotRequired[str],
}, total=False)

ModelChesscomPuzzleData = TypedDict('ModelChesscomPuzzleData', {
    'fen': NotRequired[str],
    'image': NotRequired[str],
    'pgn': NotRequired[str],
    'publish_time': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelChesscomPublicPgnresponse = TypedDict('ModelChesscomPublicPgnresponse', {
    'cache_control': NotRequired[str],
    'content_disposition': NotRequired[str],
    'content_type': NotRequired[str],
    'etag': NotRequired[str],
    'last_modified': NotRequired[str],
    'pgn': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelChesscomCountryProfileResponse = TypedDict('ModelChesscomCountryProfileResponse', {
    'cache_control': NotRequired[str],
    'data': NotRequired[ModelChesscomCountryProfileData],
    'source_url': NotRequired[str],
}, total=False)

ModelChesscomCountryProfileData = TypedDict('ModelChesscomCountryProfileData', {
    '@id': NotRequired[str],
    'code': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ChesscomClubResponse = Any
ChesscomClubParams = TypedDict('ChesscomClubParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

ChesscomClubMatchesResponse = Any
ChesscomClubMatchesParams = TypedDict('ChesscomClubMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

ChesscomClubMembersResponse = Any
ChesscomClubMembersParams = TypedDict('ChesscomClubMembersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

ChesscomCountryResponse = Any
ChesscomCountryParams = TypedDict('ChesscomCountryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'iso': Required[str],
}, total=False)

ChesscomMatchLiveResponse = Any
ChesscomMatchLiveParams = TypedDict('ChesscomMatchLiveParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[int],
}, total=False)

ChesscomMatchLiveBoardResponse = Any
ChesscomMatchLiveBoardParams = TypedDict('ChesscomMatchLiveBoardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[int],
    'board': Required[int],
}, total=False)

ChesscomMatchResponse = Any
ChesscomMatchParams = TypedDict('ChesscomMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[int],
}, total=False)

ChesscomMatchBoardResponse = Any
ChesscomMatchBoardParams = TypedDict('ChesscomMatchBoardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[int],
    'board': Required[int],
}, total=False)

ChesscomPlayerResponse = Any
ChesscomPlayerParams = TypedDict('ChesscomPlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

ChesscomPlayerClubsResponse = Any
ChesscomPlayerClubsParams = TypedDict('ChesscomPlayerClubsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGamesResponse = Any
ChesscomPlayerGamesParams = TypedDict('ChesscomPlayerGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGameMonthResponse = Any
ChesscomPlayerGameMonthParams = TypedDict('ChesscomPlayerGameMonthParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
    'year': Required[str],
    'month': Required[str],
}, total=False)

ChesscomPlayerGameMonthPgnResponse = Any
ChesscomPlayerGameMonthPgnParams = TypedDict('ChesscomPlayerGameMonthPgnParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
    'year': Required[str],
    'month': Required[str],
}, total=False)

ChesscomPlayerGameArchivesResponse = Any
ChesscomPlayerGameArchivesParams = TypedDict('ChesscomPlayerGameArchivesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

ChesscomPlayerLiveGamesBaseTimeResponse = Any
ChesscomPlayerLiveGamesBaseTimeParams = TypedDict('ChesscomPlayerLiveGamesBaseTimeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
    'base_time': Required[int],
}, total=False)

ChesscomPlayerLiveGamesResponse = Any
ChesscomPlayerLiveGamesParams = TypedDict('ChesscomPlayerLiveGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
    'base_time': Required[int],
    'increment': Required[int],
}, total=False)

ChesscomPlayerGamesToMoveResponse = Any
ChesscomPlayerGamesToMoveParams = TypedDict('ChesscomPlayerGamesToMoveParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

ChesscomPlayerIsOnlineResponse = Any
ChesscomPlayerIsOnlineParams = TypedDict('ChesscomPlayerIsOnlineParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

ChesscomPlayerMatchesResponse = Any
ChesscomPlayerMatchesParams = TypedDict('ChesscomPlayerMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

ChesscomPlayerStatsResponse = Any
ChesscomPlayerStatsParams = TypedDict('ChesscomPlayerStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

ChesscomPlayerTournamentsResponse = Any
ChesscomPlayerTournamentsParams = TypedDict('ChesscomPlayerTournamentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

ChesscomPuzzleResponse = Any
ChesscomPuzzleParams = TypedDict('ChesscomPuzzleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ChesscomPuzzleRandomResponse = Any
ChesscomPuzzleRandomParams = TypedDict('ChesscomPuzzleRandomParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

ChesscomTournamentResponse = Any
ChesscomTournamentParams = TypedDict('ChesscomTournamentParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
}, total=False)

ChesscomTournamentRoundResponse = Any
ChesscomTournamentRoundParams = TypedDict('ChesscomTournamentRoundParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'round': Required[int],
}, total=False)

ChesscomTournamentRoundGroupResponse = Any
ChesscomTournamentRoundGroupParams = TypedDict('ChesscomTournamentRoundGroupParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'slug': Required[str],
    'round': Required[int],
    'group': Required[int],
}, total=False)

class ChesscomGroup:
    @overload
    def club(self, **params: Unpack[ChesscomClubStreamParams]) -> BinaryIO: ...
    @overload
    def club(self, **params: Unpack[ChesscomClubTextResponseParams]) -> str: ...
    @overload
    def club(self, **params: Unpack[ChesscomClubDefaultParams]) -> ChesscomClubResponse: ...
    @overload
    def club_matches(self, **params: Unpack[ChesscomClubMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def club_matches(self, **params: Unpack[ChesscomClubMatchesTextResponseParams]) -> str: ...
    @overload
    def club_matches(self, **params: Unpack[ChesscomClubMatchesDefaultParams]) -> ChesscomClubMatchesResponse: ...
    @overload
    def club_members(self, **params: Unpack[ChesscomClubMembersStreamParams]) -> BinaryIO: ...
    @overload
    def club_members(self, **params: Unpack[ChesscomClubMembersTextResponseParams]) -> str: ...
    @overload
    def club_members(self, **params: Unpack[ChesscomClubMembersDefaultParams]) -> ChesscomClubMembersResponse: ...
    @overload
    def country(self, **params: Unpack[ChesscomCountryStreamParams]) -> BinaryIO: ...
    @overload
    def country(self, **params: Unpack[ChesscomCountryTextResponseParams]) -> str: ...
    @overload
    def country(self, **params: Unpack[ChesscomCountryDefaultParams]) -> ChesscomCountryResponse: ...
    @overload
    def match_live(self, **params: Unpack[ChesscomMatchLiveStreamParams]) -> BinaryIO: ...
    @overload
    def match_live(self, **params: Unpack[ChesscomMatchLiveTextResponseParams]) -> str: ...
    @overload
    def match_live(self, **params: Unpack[ChesscomMatchLiveDefaultParams]) -> ChesscomMatchLiveResponse: ...
    @overload
    def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardStreamParams]) -> BinaryIO: ...
    @overload
    def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardTextResponseParams]) -> str: ...
    @overload
    def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardDefaultParams]) -> ChesscomMatchLiveBoardResponse: ...
    @overload
    def match(self, **params: Unpack[ChesscomMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[ChesscomMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[ChesscomMatchDefaultParams]) -> ChesscomMatchResponse: ...
    @overload
    def match_board(self, **params: Unpack[ChesscomMatchBoardStreamParams]) -> BinaryIO: ...
    @overload
    def match_board(self, **params: Unpack[ChesscomMatchBoardTextResponseParams]) -> str: ...
    @overload
    def match_board(self, **params: Unpack[ChesscomMatchBoardDefaultParams]) -> ChesscomMatchBoardResponse: ...
    @overload
    def player(self, **params: Unpack[ChesscomPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[ChesscomPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[ChesscomPlayerDefaultParams]) -> ChesscomPlayerResponse: ...
    @overload
    def player_clubs(self, **params: Unpack[ChesscomPlayerClubsStreamParams]) -> BinaryIO: ...
    @overload
    def player_clubs(self, **params: Unpack[ChesscomPlayerClubsTextResponseParams]) -> str: ...
    @overload
    def player_clubs(self, **params: Unpack[ChesscomPlayerClubsDefaultParams]) -> ChesscomPlayerClubsResponse: ...
    @overload
    def player_games(self, **params: Unpack[ChesscomPlayerGamesStreamParams]) -> BinaryIO: ...
    @overload
    def player_games(self, **params: Unpack[ChesscomPlayerGamesTextResponseParams]) -> str: ...
    @overload
    def player_games(self, **params: Unpack[ChesscomPlayerGamesDefaultParams]) -> ChesscomPlayerGamesResponse: ...
    @overload
    def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthStreamParams]) -> BinaryIO: ...
    @overload
    def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthTextResponseParams]) -> str: ...
    @overload
    def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthDefaultParams]) -> ChesscomPlayerGameMonthResponse: ...
    @overload
    def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnStreamParams]) -> BinaryIO: ...
    @overload
    def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnTextResponseParams]) -> str: ...
    @overload
    def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnDefaultParams]) -> ChesscomPlayerGameMonthPgnResponse: ...
    @overload
    def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesStreamParams]) -> BinaryIO: ...
    @overload
    def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesTextResponseParams]) -> str: ...
    @overload
    def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesDefaultParams]) -> ChesscomPlayerGameArchivesResponse: ...
    @overload
    def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeStreamParams]) -> BinaryIO: ...
    @overload
    def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeTextResponseParams]) -> str: ...
    @overload
    def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeDefaultParams]) -> ChesscomPlayerLiveGamesBaseTimeResponse: ...
    @overload
    def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesStreamParams]) -> BinaryIO: ...
    @overload
    def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesTextResponseParams]) -> str: ...
    @overload
    def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesDefaultParams]) -> ChesscomPlayerLiveGamesResponse: ...
    @overload
    def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveStreamParams]) -> BinaryIO: ...
    @overload
    def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveTextResponseParams]) -> str: ...
    @overload
    def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveDefaultParams]) -> ChesscomPlayerGamesToMoveResponse: ...
    @overload
    def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineStreamParams]) -> BinaryIO: ...
    @overload
    def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineTextResponseParams]) -> str: ...
    @overload
    def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineDefaultParams]) -> ChesscomPlayerIsOnlineResponse: ...
    @overload
    def player_matches(self, **params: Unpack[ChesscomPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_matches(self, **params: Unpack[ChesscomPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    def player_matches(self, **params: Unpack[ChesscomPlayerMatchesDefaultParams]) -> ChesscomPlayerMatchesResponse: ...
    @overload
    def player_stats(self, **params: Unpack[ChesscomPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_stats(self, **params: Unpack[ChesscomPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def player_stats(self, **params: Unpack[ChesscomPlayerStatsDefaultParams]) -> ChesscomPlayerStatsResponse: ...
    @overload
    def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsTextResponseParams]) -> str: ...
    @overload
    def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsDefaultParams]) -> ChesscomPlayerTournamentsResponse: ...
    @overload
    def puzzle(self, **params: Unpack[ChesscomPuzzleStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle(self, **params: Unpack[ChesscomPuzzleTextResponseParams]) -> str: ...
    @overload
    def puzzle(self, **params: Unpack[ChesscomPuzzleDefaultParams]) -> ChesscomPuzzleResponse: ...
    @overload
    def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomTextResponseParams]) -> str: ...
    @overload
    def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomDefaultParams]) -> ChesscomPuzzleRandomResponse: ...
    @overload
    def tournament(self, **params: Unpack[ChesscomTournamentStreamParams]) -> BinaryIO: ...
    @overload
    def tournament(self, **params: Unpack[ChesscomTournamentTextResponseParams]) -> str: ...
    @overload
    def tournament(self, **params: Unpack[ChesscomTournamentDefaultParams]) -> ChesscomTournamentResponse: ...
    @overload
    def tournament_round(self, **params: Unpack[ChesscomTournamentRoundStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_round(self, **params: Unpack[ChesscomTournamentRoundTextResponseParams]) -> str: ...
    @overload
    def tournament_round(self, **params: Unpack[ChesscomTournamentRoundDefaultParams]) -> ChesscomTournamentRoundResponse: ...
    @overload
    def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupTextResponseParams]) -> str: ...
    @overload
    def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupDefaultParams]) -> ChesscomTournamentRoundGroupResponse: ...

OperationId = Literal[
    'chesscom-club',
    'chesscom-club-matches',
    'chesscom-club-members',
    'chesscom-country',
    'chesscom-match-live',
    'chesscom-match-live-board',
    'chesscom-match',
    'chesscom-match-board',
    'chesscom-player',
    'chesscom-player-clubs',
    'chesscom-player-games',
    'chesscom-player-game-month',
    'chesscom-player-game-month-pgn',
    'chesscom-player-game-archives',
    'chesscom-player-live-games-base-time',
    'chesscom-player-live-games',
    'chesscom-player-games-to-move',
    'chesscom-player-is-online',
    'chesscom-player-matches',
    'chesscom-player-stats',
    'chesscom-player-tournaments',
    'chesscom-puzzle',
    'chesscom-puzzle-random',
    'chesscom-tournament',
    'chesscom-tournament-round',
    'chesscom-tournament-round-group',
]

class CrawloraClient:
    chesscom: ChesscomGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-club'],
        params: ChesscomClubParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomClubResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-club-matches'],
        params: ChesscomClubMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomClubMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-club-members'],
        params: ChesscomClubMembersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomClubMembersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-country'],
        params: ChesscomCountryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomCountryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-match-live'],
        params: ChesscomMatchLiveParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomMatchLiveResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-match-live-board'],
        params: ChesscomMatchLiveBoardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomMatchLiveBoardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-match'],
        params: ChesscomMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-match-board'],
        params: ChesscomMatchBoardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomMatchBoardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player'],
        params: ChesscomPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-clubs'],
        params: ChesscomPlayerClubsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerClubsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-games'],
        params: ChesscomPlayerGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-game-month'],
        params: ChesscomPlayerGameMonthParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGameMonthResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-game-month-pgn'],
        params: ChesscomPlayerGameMonthPgnParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGameMonthPgnResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-game-archives'],
        params: ChesscomPlayerGameArchivesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGameArchivesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-live-games-base-time'],
        params: ChesscomPlayerLiveGamesBaseTimeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerLiveGamesBaseTimeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-live-games'],
        params: ChesscomPlayerLiveGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerLiveGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-games-to-move'],
        params: ChesscomPlayerGamesToMoveParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGamesToMoveResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-is-online'],
        params: ChesscomPlayerIsOnlineParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerIsOnlineResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-matches'],
        params: ChesscomPlayerMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-stats'],
        params: ChesscomPlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-player-tournaments'],
        params: ChesscomPlayerTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerTournamentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-puzzle'],
        params: ChesscomPuzzleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPuzzleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-puzzle-random'],
        params: ChesscomPuzzleRandomParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPuzzleRandomResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-tournament'],
        params: ChesscomTournamentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomTournamentResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-tournament-round'],
        params: ChesscomTournamentRoundParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomTournamentRoundResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['chesscom-tournament-round-group'],
        params: ChesscomTournamentRoundGroupParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomTournamentRoundGroupResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-club'],
        params: ChesscomClubParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomClubResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-club-matches'],
        params: ChesscomClubMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomClubMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-club-members'],
        params: ChesscomClubMembersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomClubMembersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-country'],
        params: ChesscomCountryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomCountryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-match-live'],
        params: ChesscomMatchLiveParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomMatchLiveResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-match-live-board'],
        params: ChesscomMatchLiveBoardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomMatchLiveBoardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-match'],
        params: ChesscomMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-match-board'],
        params: ChesscomMatchBoardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomMatchBoardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player'],
        params: ChesscomPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-clubs'],
        params: ChesscomPlayerClubsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerClubsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-games'],
        params: ChesscomPlayerGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-game-month'],
        params: ChesscomPlayerGameMonthParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGameMonthResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-game-month-pgn'],
        params: ChesscomPlayerGameMonthPgnParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGameMonthPgnResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-game-archives'],
        params: ChesscomPlayerGameArchivesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGameArchivesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-live-games-base-time'],
        params: ChesscomPlayerLiveGamesBaseTimeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerLiveGamesBaseTimeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-live-games'],
        params: ChesscomPlayerLiveGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerLiveGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-games-to-move'],
        params: ChesscomPlayerGamesToMoveParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerGamesToMoveResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-is-online'],
        params: ChesscomPlayerIsOnlineParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerIsOnlineResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-matches'],
        params: ChesscomPlayerMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-stats'],
        params: ChesscomPlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-player-tournaments'],
        params: ChesscomPlayerTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPlayerTournamentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-puzzle'],
        params: ChesscomPuzzleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPuzzleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-puzzle-random'],
        params: ChesscomPuzzleRandomParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomPuzzleRandomResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-tournament'],
        params: ChesscomTournamentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomTournamentResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-tournament-round'],
        params: ChesscomTournamentRoundParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomTournamentRoundResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['chesscom-tournament-round-group'],
        params: ChesscomTournamentRoundGroupParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> ChesscomTournamentRoundGroupResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class ChessComClient(CrawloraClient):
    def __enter__(self) -> ChessComClient: ...
    @overload
    def club(self, **params: Unpack[ChesscomClubStreamParams]) -> BinaryIO: ...
    @overload
    def club(self, **params: Unpack[ChesscomClubTextResponseParams]) -> str: ...
    @overload
    def club(self, **params: Unpack[ChesscomClubDefaultParams]) -> ChesscomClubResponse: ...
    @overload
    def club_matches(self, **params: Unpack[ChesscomClubMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def club_matches(self, **params: Unpack[ChesscomClubMatchesTextResponseParams]) -> str: ...
    @overload
    def club_matches(self, **params: Unpack[ChesscomClubMatchesDefaultParams]) -> ChesscomClubMatchesResponse: ...
    @overload
    def club_members(self, **params: Unpack[ChesscomClubMembersStreamParams]) -> BinaryIO: ...
    @overload
    def club_members(self, **params: Unpack[ChesscomClubMembersTextResponseParams]) -> str: ...
    @overload
    def club_members(self, **params: Unpack[ChesscomClubMembersDefaultParams]) -> ChesscomClubMembersResponse: ...
    @overload
    def country(self, **params: Unpack[ChesscomCountryStreamParams]) -> BinaryIO: ...
    @overload
    def country(self, **params: Unpack[ChesscomCountryTextResponseParams]) -> str: ...
    @overload
    def country(self, **params: Unpack[ChesscomCountryDefaultParams]) -> ChesscomCountryResponse: ...
    @overload
    def match_live(self, **params: Unpack[ChesscomMatchLiveStreamParams]) -> BinaryIO: ...
    @overload
    def match_live(self, **params: Unpack[ChesscomMatchLiveTextResponseParams]) -> str: ...
    @overload
    def match_live(self, **params: Unpack[ChesscomMatchLiveDefaultParams]) -> ChesscomMatchLiveResponse: ...
    @overload
    def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardStreamParams]) -> BinaryIO: ...
    @overload
    def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardTextResponseParams]) -> str: ...
    @overload
    def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardDefaultParams]) -> ChesscomMatchLiveBoardResponse: ...
    @overload
    def match(self, **params: Unpack[ChesscomMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[ChesscomMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[ChesscomMatchDefaultParams]) -> ChesscomMatchResponse: ...
    @overload
    def match_board(self, **params: Unpack[ChesscomMatchBoardStreamParams]) -> BinaryIO: ...
    @overload
    def match_board(self, **params: Unpack[ChesscomMatchBoardTextResponseParams]) -> str: ...
    @overload
    def match_board(self, **params: Unpack[ChesscomMatchBoardDefaultParams]) -> ChesscomMatchBoardResponse: ...
    @overload
    def player(self, **params: Unpack[ChesscomPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[ChesscomPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[ChesscomPlayerDefaultParams]) -> ChesscomPlayerResponse: ...
    @overload
    def player_clubs(self, **params: Unpack[ChesscomPlayerClubsStreamParams]) -> BinaryIO: ...
    @overload
    def player_clubs(self, **params: Unpack[ChesscomPlayerClubsTextResponseParams]) -> str: ...
    @overload
    def player_clubs(self, **params: Unpack[ChesscomPlayerClubsDefaultParams]) -> ChesscomPlayerClubsResponse: ...
    @overload
    def player_games(self, **params: Unpack[ChesscomPlayerGamesStreamParams]) -> BinaryIO: ...
    @overload
    def player_games(self, **params: Unpack[ChesscomPlayerGamesTextResponseParams]) -> str: ...
    @overload
    def player_games(self, **params: Unpack[ChesscomPlayerGamesDefaultParams]) -> ChesscomPlayerGamesResponse: ...
    @overload
    def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthStreamParams]) -> BinaryIO: ...
    @overload
    def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthTextResponseParams]) -> str: ...
    @overload
    def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthDefaultParams]) -> ChesscomPlayerGameMonthResponse: ...
    @overload
    def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnStreamParams]) -> BinaryIO: ...
    @overload
    def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnTextResponseParams]) -> str: ...
    @overload
    def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnDefaultParams]) -> ChesscomPlayerGameMonthPgnResponse: ...
    @overload
    def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesStreamParams]) -> BinaryIO: ...
    @overload
    def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesTextResponseParams]) -> str: ...
    @overload
    def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesDefaultParams]) -> ChesscomPlayerGameArchivesResponse: ...
    @overload
    def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeStreamParams]) -> BinaryIO: ...
    @overload
    def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeTextResponseParams]) -> str: ...
    @overload
    def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeDefaultParams]) -> ChesscomPlayerLiveGamesBaseTimeResponse: ...
    @overload
    def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesStreamParams]) -> BinaryIO: ...
    @overload
    def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesTextResponseParams]) -> str: ...
    @overload
    def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesDefaultParams]) -> ChesscomPlayerLiveGamesResponse: ...
    @overload
    def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveStreamParams]) -> BinaryIO: ...
    @overload
    def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveTextResponseParams]) -> str: ...
    @overload
    def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveDefaultParams]) -> ChesscomPlayerGamesToMoveResponse: ...
    @overload
    def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineStreamParams]) -> BinaryIO: ...
    @overload
    def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineTextResponseParams]) -> str: ...
    @overload
    def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineDefaultParams]) -> ChesscomPlayerIsOnlineResponse: ...
    @overload
    def player_matches(self, **params: Unpack[ChesscomPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_matches(self, **params: Unpack[ChesscomPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    def player_matches(self, **params: Unpack[ChesscomPlayerMatchesDefaultParams]) -> ChesscomPlayerMatchesResponse: ...
    @overload
    def player_stats(self, **params: Unpack[ChesscomPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def player_stats(self, **params: Unpack[ChesscomPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def player_stats(self, **params: Unpack[ChesscomPlayerStatsDefaultParams]) -> ChesscomPlayerStatsResponse: ...
    @overload
    def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsTextResponseParams]) -> str: ...
    @overload
    def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsDefaultParams]) -> ChesscomPlayerTournamentsResponse: ...
    @overload
    def puzzle(self, **params: Unpack[ChesscomPuzzleStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle(self, **params: Unpack[ChesscomPuzzleTextResponseParams]) -> str: ...
    @overload
    def puzzle(self, **params: Unpack[ChesscomPuzzleDefaultParams]) -> ChesscomPuzzleResponse: ...
    @overload
    def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomTextResponseParams]) -> str: ...
    @overload
    def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomDefaultParams]) -> ChesscomPuzzleRandomResponse: ...
    @overload
    def tournament(self, **params: Unpack[ChesscomTournamentStreamParams]) -> BinaryIO: ...
    @overload
    def tournament(self, **params: Unpack[ChesscomTournamentTextResponseParams]) -> str: ...
    @overload
    def tournament(self, **params: Unpack[ChesscomTournamentDefaultParams]) -> ChesscomTournamentResponse: ...
    @overload
    def tournament_round(self, **params: Unpack[ChesscomTournamentRoundStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_round(self, **params: Unpack[ChesscomTournamentRoundTextResponseParams]) -> str: ...
    @overload
    def tournament_round(self, **params: Unpack[ChesscomTournamentRoundDefaultParams]) -> ChesscomTournamentRoundResponse: ...
    @overload
    def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupTextResponseParams]) -> str: ...
    @overload
    def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupDefaultParams]) -> ChesscomTournamentRoundGroupResponse: ...

class AsyncChessComClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncChessComClient: ...
    chesscom: _AsyncChesscomGroup
    @overload
    async def club(self, **params: Unpack[ChesscomClubStreamParams]) -> BinaryIO: ...
    @overload
    async def club(self, **params: Unpack[ChesscomClubTextResponseParams]) -> str: ...
    @overload
    async def club(self, **params: Unpack[ChesscomClubDefaultParams]) -> ChesscomClubResponse: ...
    @overload
    async def club_matches(self, **params: Unpack[ChesscomClubMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def club_matches(self, **params: Unpack[ChesscomClubMatchesTextResponseParams]) -> str: ...
    @overload
    async def club_matches(self, **params: Unpack[ChesscomClubMatchesDefaultParams]) -> ChesscomClubMatchesResponse: ...
    @overload
    async def club_members(self, **params: Unpack[ChesscomClubMembersStreamParams]) -> BinaryIO: ...
    @overload
    async def club_members(self, **params: Unpack[ChesscomClubMembersTextResponseParams]) -> str: ...
    @overload
    async def club_members(self, **params: Unpack[ChesscomClubMembersDefaultParams]) -> ChesscomClubMembersResponse: ...
    @overload
    async def country(self, **params: Unpack[ChesscomCountryStreamParams]) -> BinaryIO: ...
    @overload
    async def country(self, **params: Unpack[ChesscomCountryTextResponseParams]) -> str: ...
    @overload
    async def country(self, **params: Unpack[ChesscomCountryDefaultParams]) -> ChesscomCountryResponse: ...
    @overload
    async def match_live(self, **params: Unpack[ChesscomMatchLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def match_live(self, **params: Unpack[ChesscomMatchLiveTextResponseParams]) -> str: ...
    @overload
    async def match_live(self, **params: Unpack[ChesscomMatchLiveDefaultParams]) -> ChesscomMatchLiveResponse: ...
    @overload
    async def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardStreamParams]) -> BinaryIO: ...
    @overload
    async def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardTextResponseParams]) -> str: ...
    @overload
    async def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardDefaultParams]) -> ChesscomMatchLiveBoardResponse: ...
    @overload
    async def match(self, **params: Unpack[ChesscomMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[ChesscomMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[ChesscomMatchDefaultParams]) -> ChesscomMatchResponse: ...
    @overload
    async def match_board(self, **params: Unpack[ChesscomMatchBoardStreamParams]) -> BinaryIO: ...
    @overload
    async def match_board(self, **params: Unpack[ChesscomMatchBoardTextResponseParams]) -> str: ...
    @overload
    async def match_board(self, **params: Unpack[ChesscomMatchBoardDefaultParams]) -> ChesscomMatchBoardResponse: ...
    @overload
    async def player(self, **params: Unpack[ChesscomPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[ChesscomPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[ChesscomPlayerDefaultParams]) -> ChesscomPlayerResponse: ...
    @overload
    async def player_clubs(self, **params: Unpack[ChesscomPlayerClubsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_clubs(self, **params: Unpack[ChesscomPlayerClubsTextResponseParams]) -> str: ...
    @overload
    async def player_clubs(self, **params: Unpack[ChesscomPlayerClubsDefaultParams]) -> ChesscomPlayerClubsResponse: ...
    @overload
    async def player_games(self, **params: Unpack[ChesscomPlayerGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_games(self, **params: Unpack[ChesscomPlayerGamesTextResponseParams]) -> str: ...
    @overload
    async def player_games(self, **params: Unpack[ChesscomPlayerGamesDefaultParams]) -> ChesscomPlayerGamesResponse: ...
    @overload
    async def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthStreamParams]) -> BinaryIO: ...
    @overload
    async def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthTextResponseParams]) -> str: ...
    @overload
    async def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthDefaultParams]) -> ChesscomPlayerGameMonthResponse: ...
    @overload
    async def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnStreamParams]) -> BinaryIO: ...
    @overload
    async def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnTextResponseParams]) -> str: ...
    @overload
    async def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnDefaultParams]) -> ChesscomPlayerGameMonthPgnResponse: ...
    @overload
    async def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesTextResponseParams]) -> str: ...
    @overload
    async def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesDefaultParams]) -> ChesscomPlayerGameArchivesResponse: ...
    @overload
    async def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeStreamParams]) -> BinaryIO: ...
    @overload
    async def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeTextResponseParams]) -> str: ...
    @overload
    async def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeDefaultParams]) -> ChesscomPlayerLiveGamesBaseTimeResponse: ...
    @overload
    async def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesTextResponseParams]) -> str: ...
    @overload
    async def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesDefaultParams]) -> ChesscomPlayerLiveGamesResponse: ...
    @overload
    async def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveStreamParams]) -> BinaryIO: ...
    @overload
    async def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveTextResponseParams]) -> str: ...
    @overload
    async def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveDefaultParams]) -> ChesscomPlayerGamesToMoveResponse: ...
    @overload
    async def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineStreamParams]) -> BinaryIO: ...
    @overload
    async def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineTextResponseParams]) -> str: ...
    @overload
    async def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineDefaultParams]) -> ChesscomPlayerIsOnlineResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[ChesscomPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[ChesscomPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[ChesscomPlayerMatchesDefaultParams]) -> ChesscomPlayerMatchesResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[ChesscomPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[ChesscomPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[ChesscomPlayerStatsDefaultParams]) -> ChesscomPlayerStatsResponse: ...
    @overload
    async def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsTextResponseParams]) -> str: ...
    @overload
    async def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsDefaultParams]) -> ChesscomPlayerTournamentsResponse: ...
    @overload
    async def puzzle(self, **params: Unpack[ChesscomPuzzleStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle(self, **params: Unpack[ChesscomPuzzleTextResponseParams]) -> str: ...
    @overload
    async def puzzle(self, **params: Unpack[ChesscomPuzzleDefaultParams]) -> ChesscomPuzzleResponse: ...
    @overload
    async def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomTextResponseParams]) -> str: ...
    @overload
    async def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomDefaultParams]) -> ChesscomPuzzleRandomResponse: ...
    @overload
    async def tournament(self, **params: Unpack[ChesscomTournamentStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament(self, **params: Unpack[ChesscomTournamentTextResponseParams]) -> str: ...
    @overload
    async def tournament(self, **params: Unpack[ChesscomTournamentDefaultParams]) -> ChesscomTournamentResponse: ...
    @overload
    async def tournament_round(self, **params: Unpack[ChesscomTournamentRoundStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_round(self, **params: Unpack[ChesscomTournamentRoundTextResponseParams]) -> str: ...
    @overload
    async def tournament_round(self, **params: Unpack[ChesscomTournamentRoundDefaultParams]) -> ChesscomTournamentRoundResponse: ...
    @overload
    async def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupTextResponseParams]) -> str: ...
    @overload
    async def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupDefaultParams]) -> ChesscomTournamentRoundGroupResponse: ...

class _AsyncChesscomGroup:
    @overload
    async def club(self, **params: Unpack[ChesscomClubStreamParams]) -> BinaryIO: ...
    @overload
    async def club(self, **params: Unpack[ChesscomClubTextResponseParams]) -> str: ...
    @overload
    async def club(self, **params: Unpack[ChesscomClubDefaultParams]) -> ChesscomClubResponse: ...
    @overload
    async def club_matches(self, **params: Unpack[ChesscomClubMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def club_matches(self, **params: Unpack[ChesscomClubMatchesTextResponseParams]) -> str: ...
    @overload
    async def club_matches(self, **params: Unpack[ChesscomClubMatchesDefaultParams]) -> ChesscomClubMatchesResponse: ...
    @overload
    async def club_members(self, **params: Unpack[ChesscomClubMembersStreamParams]) -> BinaryIO: ...
    @overload
    async def club_members(self, **params: Unpack[ChesscomClubMembersTextResponseParams]) -> str: ...
    @overload
    async def club_members(self, **params: Unpack[ChesscomClubMembersDefaultParams]) -> ChesscomClubMembersResponse: ...
    @overload
    async def country(self, **params: Unpack[ChesscomCountryStreamParams]) -> BinaryIO: ...
    @overload
    async def country(self, **params: Unpack[ChesscomCountryTextResponseParams]) -> str: ...
    @overload
    async def country(self, **params: Unpack[ChesscomCountryDefaultParams]) -> ChesscomCountryResponse: ...
    @overload
    async def match_live(self, **params: Unpack[ChesscomMatchLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def match_live(self, **params: Unpack[ChesscomMatchLiveTextResponseParams]) -> str: ...
    @overload
    async def match_live(self, **params: Unpack[ChesscomMatchLiveDefaultParams]) -> ChesscomMatchLiveResponse: ...
    @overload
    async def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardStreamParams]) -> BinaryIO: ...
    @overload
    async def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardTextResponseParams]) -> str: ...
    @overload
    async def match_live_board(self, **params: Unpack[ChesscomMatchLiveBoardDefaultParams]) -> ChesscomMatchLiveBoardResponse: ...
    @overload
    async def match(self, **params: Unpack[ChesscomMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[ChesscomMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[ChesscomMatchDefaultParams]) -> ChesscomMatchResponse: ...
    @overload
    async def match_board(self, **params: Unpack[ChesscomMatchBoardStreamParams]) -> BinaryIO: ...
    @overload
    async def match_board(self, **params: Unpack[ChesscomMatchBoardTextResponseParams]) -> str: ...
    @overload
    async def match_board(self, **params: Unpack[ChesscomMatchBoardDefaultParams]) -> ChesscomMatchBoardResponse: ...
    @overload
    async def player(self, **params: Unpack[ChesscomPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[ChesscomPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[ChesscomPlayerDefaultParams]) -> ChesscomPlayerResponse: ...
    @overload
    async def player_clubs(self, **params: Unpack[ChesscomPlayerClubsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_clubs(self, **params: Unpack[ChesscomPlayerClubsTextResponseParams]) -> str: ...
    @overload
    async def player_clubs(self, **params: Unpack[ChesscomPlayerClubsDefaultParams]) -> ChesscomPlayerClubsResponse: ...
    @overload
    async def player_games(self, **params: Unpack[ChesscomPlayerGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_games(self, **params: Unpack[ChesscomPlayerGamesTextResponseParams]) -> str: ...
    @overload
    async def player_games(self, **params: Unpack[ChesscomPlayerGamesDefaultParams]) -> ChesscomPlayerGamesResponse: ...
    @overload
    async def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthStreamParams]) -> BinaryIO: ...
    @overload
    async def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthTextResponseParams]) -> str: ...
    @overload
    async def player_game_month(self, **params: Unpack[ChesscomPlayerGameMonthDefaultParams]) -> ChesscomPlayerGameMonthResponse: ...
    @overload
    async def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnStreamParams]) -> BinaryIO: ...
    @overload
    async def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnTextResponseParams]) -> str: ...
    @overload
    async def player_game_month_pgn(self, **params: Unpack[ChesscomPlayerGameMonthPgnDefaultParams]) -> ChesscomPlayerGameMonthPgnResponse: ...
    @overload
    async def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesTextResponseParams]) -> str: ...
    @overload
    async def player_game_archives(self, **params: Unpack[ChesscomPlayerGameArchivesDefaultParams]) -> ChesscomPlayerGameArchivesResponse: ...
    @overload
    async def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeStreamParams]) -> BinaryIO: ...
    @overload
    async def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeTextResponseParams]) -> str: ...
    @overload
    async def player_live_games_base_time(self, **params: Unpack[ChesscomPlayerLiveGamesBaseTimeDefaultParams]) -> ChesscomPlayerLiveGamesBaseTimeResponse: ...
    @overload
    async def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesTextResponseParams]) -> str: ...
    @overload
    async def player_live_games(self, **params: Unpack[ChesscomPlayerLiveGamesDefaultParams]) -> ChesscomPlayerLiveGamesResponse: ...
    @overload
    async def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveStreamParams]) -> BinaryIO: ...
    @overload
    async def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveTextResponseParams]) -> str: ...
    @overload
    async def player_games_to_move(self, **params: Unpack[ChesscomPlayerGamesToMoveDefaultParams]) -> ChesscomPlayerGamesToMoveResponse: ...
    @overload
    async def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineStreamParams]) -> BinaryIO: ...
    @overload
    async def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineTextResponseParams]) -> str: ...
    @overload
    async def player_is_online(self, **params: Unpack[ChesscomPlayerIsOnlineDefaultParams]) -> ChesscomPlayerIsOnlineResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[ChesscomPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[ChesscomPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[ChesscomPlayerMatchesDefaultParams]) -> ChesscomPlayerMatchesResponse: ...
    @overload
    async def player_stats(self, **params: Unpack[ChesscomPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_stats(self, **params: Unpack[ChesscomPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def player_stats(self, **params: Unpack[ChesscomPlayerStatsDefaultParams]) -> ChesscomPlayerStatsResponse: ...
    @overload
    async def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsTextResponseParams]) -> str: ...
    @overload
    async def player_tournaments(self, **params: Unpack[ChesscomPlayerTournamentsDefaultParams]) -> ChesscomPlayerTournamentsResponse: ...
    @overload
    async def puzzle(self, **params: Unpack[ChesscomPuzzleStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle(self, **params: Unpack[ChesscomPuzzleTextResponseParams]) -> str: ...
    @overload
    async def puzzle(self, **params: Unpack[ChesscomPuzzleDefaultParams]) -> ChesscomPuzzleResponse: ...
    @overload
    async def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomTextResponseParams]) -> str: ...
    @overload
    async def puzzle_random(self, **params: Unpack[ChesscomPuzzleRandomDefaultParams]) -> ChesscomPuzzleRandomResponse: ...
    @overload
    async def tournament(self, **params: Unpack[ChesscomTournamentStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament(self, **params: Unpack[ChesscomTournamentTextResponseParams]) -> str: ...
    @overload
    async def tournament(self, **params: Unpack[ChesscomTournamentDefaultParams]) -> ChesscomTournamentResponse: ...
    @overload
    async def tournament_round(self, **params: Unpack[ChesscomTournamentRoundStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_round(self, **params: Unpack[ChesscomTournamentRoundTextResponseParams]) -> str: ...
    @overload
    async def tournament_round(self, **params: Unpack[ChesscomTournamentRoundDefaultParams]) -> ChesscomTournamentRoundResponse: ...
    @overload
    async def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupTextResponseParams]) -> str: ...
    @overload
    async def tournament_round_group(self, **params: Unpack[ChesscomTournamentRoundGroupDefaultParams]) -> ChesscomTournamentRoundGroupResponse: ...

ChesscomClubDefaultParams = TypedDict('ChesscomClubDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

ChesscomClubTextResponseParams = TypedDict('ChesscomClubTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

ChesscomClubStreamParams = TypedDict('ChesscomClubStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

ChesscomClubMatchesDefaultParams = TypedDict('ChesscomClubMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

ChesscomClubMatchesTextResponseParams = TypedDict('ChesscomClubMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

ChesscomClubMatchesStreamParams = TypedDict('ChesscomClubMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

ChesscomClubMembersDefaultParams = TypedDict('ChesscomClubMembersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

ChesscomClubMembersTextResponseParams = TypedDict('ChesscomClubMembersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

ChesscomClubMembersStreamParams = TypedDict('ChesscomClubMembersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

ChesscomCountryDefaultParams = TypedDict('ChesscomCountryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'iso': Required[str],
}, total=False)

ChesscomCountryTextResponseParams = TypedDict('ChesscomCountryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'iso': Required[str],
}, total=False)

ChesscomCountryStreamParams = TypedDict('ChesscomCountryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'iso': Required[str],
}, total=False)

ChesscomMatchLiveDefaultParams = TypedDict('ChesscomMatchLiveDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[int],
}, total=False)

ChesscomMatchLiveTextResponseParams = TypedDict('ChesscomMatchLiveTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[int],
}, total=False)

ChesscomMatchLiveStreamParams = TypedDict('ChesscomMatchLiveStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[int],
}, total=False)

ChesscomMatchLiveBoardDefaultParams = TypedDict('ChesscomMatchLiveBoardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[int],
    'board': Required[int],
}, total=False)

ChesscomMatchLiveBoardTextResponseParams = TypedDict('ChesscomMatchLiveBoardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[int],
    'board': Required[int],
}, total=False)

ChesscomMatchLiveBoardStreamParams = TypedDict('ChesscomMatchLiveBoardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[int],
    'board': Required[int],
}, total=False)

ChesscomMatchDefaultParams = TypedDict('ChesscomMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[int],
}, total=False)

ChesscomMatchTextResponseParams = TypedDict('ChesscomMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[int],
}, total=False)

ChesscomMatchStreamParams = TypedDict('ChesscomMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[int],
}, total=False)

ChesscomMatchBoardDefaultParams = TypedDict('ChesscomMatchBoardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[int],
    'board': Required[int],
}, total=False)

ChesscomMatchBoardTextResponseParams = TypedDict('ChesscomMatchBoardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[int],
    'board': Required[int],
}, total=False)

ChesscomMatchBoardStreamParams = TypedDict('ChesscomMatchBoardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[int],
    'board': Required[int],
}, total=False)

ChesscomPlayerDefaultParams = TypedDict('ChesscomPlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerTextResponseParams = TypedDict('ChesscomPlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerStreamParams = TypedDict('ChesscomPlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerClubsDefaultParams = TypedDict('ChesscomPlayerClubsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerClubsTextResponseParams = TypedDict('ChesscomPlayerClubsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerClubsStreamParams = TypedDict('ChesscomPlayerClubsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGamesDefaultParams = TypedDict('ChesscomPlayerGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGamesTextResponseParams = TypedDict('ChesscomPlayerGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGamesStreamParams = TypedDict('ChesscomPlayerGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGameMonthDefaultParams = TypedDict('ChesscomPlayerGameMonthDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
    'year': Required[str],
    'month': Required[str],
}, total=False)

ChesscomPlayerGameMonthTextResponseParams = TypedDict('ChesscomPlayerGameMonthTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
    'year': Required[str],
    'month': Required[str],
}, total=False)

ChesscomPlayerGameMonthStreamParams = TypedDict('ChesscomPlayerGameMonthStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
    'year': Required[str],
    'month': Required[str],
}, total=False)

ChesscomPlayerGameMonthPgnDefaultParams = TypedDict('ChesscomPlayerGameMonthPgnDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
    'year': Required[str],
    'month': Required[str],
}, total=False)

ChesscomPlayerGameMonthPgnTextResponseParams = TypedDict('ChesscomPlayerGameMonthPgnTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
    'year': Required[str],
    'month': Required[str],
}, total=False)

ChesscomPlayerGameMonthPgnStreamParams = TypedDict('ChesscomPlayerGameMonthPgnStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
    'year': Required[str],
    'month': Required[str],
}, total=False)

ChesscomPlayerGameArchivesDefaultParams = TypedDict('ChesscomPlayerGameArchivesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGameArchivesTextResponseParams = TypedDict('ChesscomPlayerGameArchivesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGameArchivesStreamParams = TypedDict('ChesscomPlayerGameArchivesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerLiveGamesBaseTimeDefaultParams = TypedDict('ChesscomPlayerLiveGamesBaseTimeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
    'base_time': Required[int],
}, total=False)

ChesscomPlayerLiveGamesBaseTimeTextResponseParams = TypedDict('ChesscomPlayerLiveGamesBaseTimeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
    'base_time': Required[int],
}, total=False)

ChesscomPlayerLiveGamesBaseTimeStreamParams = TypedDict('ChesscomPlayerLiveGamesBaseTimeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
    'base_time': Required[int],
}, total=False)

ChesscomPlayerLiveGamesDefaultParams = TypedDict('ChesscomPlayerLiveGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
    'base_time': Required[int],
    'increment': Required[int],
}, total=False)

ChesscomPlayerLiveGamesTextResponseParams = TypedDict('ChesscomPlayerLiveGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
    'base_time': Required[int],
    'increment': Required[int],
}, total=False)

ChesscomPlayerLiveGamesStreamParams = TypedDict('ChesscomPlayerLiveGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
    'base_time': Required[int],
    'increment': Required[int],
}, total=False)

ChesscomPlayerGamesToMoveDefaultParams = TypedDict('ChesscomPlayerGamesToMoveDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGamesToMoveTextResponseParams = TypedDict('ChesscomPlayerGamesToMoveTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerGamesToMoveStreamParams = TypedDict('ChesscomPlayerGamesToMoveStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerIsOnlineDefaultParams = TypedDict('ChesscomPlayerIsOnlineDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerIsOnlineTextResponseParams = TypedDict('ChesscomPlayerIsOnlineTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerIsOnlineStreamParams = TypedDict('ChesscomPlayerIsOnlineStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerMatchesDefaultParams = TypedDict('ChesscomPlayerMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerMatchesTextResponseParams = TypedDict('ChesscomPlayerMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerMatchesStreamParams = TypedDict('ChesscomPlayerMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerStatsDefaultParams = TypedDict('ChesscomPlayerStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerStatsTextResponseParams = TypedDict('ChesscomPlayerStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerStatsStreamParams = TypedDict('ChesscomPlayerStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerTournamentsDefaultParams = TypedDict('ChesscomPlayerTournamentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerTournamentsTextResponseParams = TypedDict('ChesscomPlayerTournamentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

ChesscomPlayerTournamentsStreamParams = TypedDict('ChesscomPlayerTournamentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

ChesscomPuzzleDefaultParams = TypedDict('ChesscomPuzzleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

ChesscomPuzzleTextResponseParams = TypedDict('ChesscomPuzzleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

ChesscomPuzzleStreamParams = TypedDict('ChesscomPuzzleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

ChesscomPuzzleRandomDefaultParams = TypedDict('ChesscomPuzzleRandomDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

ChesscomPuzzleRandomTextResponseParams = TypedDict('ChesscomPuzzleRandomTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

ChesscomPuzzleRandomStreamParams = TypedDict('ChesscomPuzzleRandomStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

ChesscomTournamentDefaultParams = TypedDict('ChesscomTournamentDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
}, total=False)

ChesscomTournamentTextResponseParams = TypedDict('ChesscomTournamentTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
}, total=False)

ChesscomTournamentStreamParams = TypedDict('ChesscomTournamentStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
}, total=False)

ChesscomTournamentRoundDefaultParams = TypedDict('ChesscomTournamentRoundDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'round': Required[int],
}, total=False)

ChesscomTournamentRoundTextResponseParams = TypedDict('ChesscomTournamentRoundTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'round': Required[int],
}, total=False)

ChesscomTournamentRoundStreamParams = TypedDict('ChesscomTournamentRoundStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'round': Required[int],
}, total=False)

ChesscomTournamentRoundGroupDefaultParams = TypedDict('ChesscomTournamentRoundGroupDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'slug': Required[str],
    'round': Required[int],
    'group': Required[int],
}, total=False)

ChesscomTournamentRoundGroupTextResponseParams = TypedDict('ChesscomTournamentRoundGroupTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'slug': Required[str],
    'round': Required[int],
    'group': Required[int],
}, total=False)

ChesscomTournamentRoundGroupStreamParams = TypedDict('ChesscomTournamentRoundGroupStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'slug': Required[str],
    'round': Required[int],
    'group': Required[int],
}, total=False)
