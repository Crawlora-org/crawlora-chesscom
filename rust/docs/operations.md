# Crawlora Chess.com Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `26`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| chesscom | `chesscom.club` | `chesscom-club` | `GET /chesscom/club/{slug}` | `slug` (path String required) | `ApiKeyAuth` | `ChesscomClubResponse` |  |
| chesscom | `chesscom.club_matches` | `chesscom-club-matches` | `GET /chesscom/club/{slug}/matches` | `slug` (path String required) | `ApiKeyAuth` | `ChesscomClubMatchesResponse` |  |
| chesscom | `chesscom.club_members` | `chesscom-club-members` | `GET /chesscom/club/{slug}/members` | `slug` (path String required) | `ApiKeyAuth` | `ChesscomClubMembersResponse` |  |
| chesscom | `chesscom.country` | `chesscom-country` | `GET /chesscom/country/{iso}` | `iso` (path String required) | `ApiKeyAuth` | `ChesscomCountryResponse` |  |
| chesscom | `chesscom.match_live` | `chesscom-match-live` | `GET /chesscom/live-match/{id}` | `id` (path i64 required) | `ApiKeyAuth` | `ChesscomMatchLiveResponse` |  |
| chesscom | `chesscom.match_live_board` | `chesscom-match-live-board` | `GET /chesscom/live-match/{id}/{board}` | `id` (path i64 required)<br>`board` (path i64 required) | `ApiKeyAuth` | `ChesscomMatchLiveBoardResponse` |  |
| chesscom | `chesscom.match_` | `chesscom-match` | `GET /chesscom/match/{id}` | `id` (path i64 required) | `ApiKeyAuth` | `ChesscomMatchResponse` |  |
| chesscom | `chesscom.match_board` | `chesscom-match-board` | `GET /chesscom/match/{id}/{board}` | `id` (path i64 required)<br>`board` (path i64 required) | `ApiKeyAuth` | `ChesscomMatchBoardResponse` |  |
| chesscom | `chesscom.player` | `chesscom-player` | `GET /chesscom/player/{username}` | `username` (path String required) | `ApiKeyAuth` | `ChesscomPlayerResponse` |  |
| chesscom | `chesscom.player_clubs` | `chesscom-player-clubs` | `GET /chesscom/player/{username}/clubs` | `username` (path String required) | `ApiKeyAuth` | `ChesscomPlayerClubsResponse` |  |
| chesscom | `chesscom.player_games` | `chesscom-player-games` | `GET /chesscom/player/{username}/games` | `username` (path String required) | `ApiKeyAuth` | `ChesscomPlayerGamesResponse` |  |
| chesscom | `chesscom.player_game_month` | `chesscom-player-game-month` | `GET /chesscom/player/{username}/games/archive/{year}/{month}` | `username` (path String required)<br>`year` (path String required)<br>`month` (path String required) | `ApiKeyAuth` | `ChesscomPlayerGameMonthResponse` |  |
| chesscom | `chesscom.player_game_month_pgn` | `chesscom-player-game-month-pgn` | `GET /chesscom/player/{username}/games/archive/{year}/{month}/pgn` | `username` (path String required)<br>`year` (path String required)<br>`month` (path String required) | `ApiKeyAuth` | `ChesscomPlayerGameMonthPgnResponse` |  |
| chesscom | `chesscom.player_game_archives` | `chesscom-player-game-archives` | `GET /chesscom/player/{username}/games/archives` | `username` (path String required) | `ApiKeyAuth` | `ChesscomPlayerGameArchivesResponse` |  |
| chesscom | `chesscom.player_live_games_base_time` | `chesscom-player-live-games-base-time` | `GET /chesscom/player/{username}/games/live/{base_time}` | `username` (path String required)<br>`base_time` (path i64 required) | `ApiKeyAuth` | `ChesscomPlayerLiveGamesBaseTimeResponse` |  |
| chesscom | `chesscom.player_live_games` | `chesscom-player-live-games` | `GET /chesscom/player/{username}/games/live/{base_time}/{increment}` | `username` (path String required)<br>`base_time` (path i64 required)<br>`increment` (path i64 required) | `ApiKeyAuth` | `ChesscomPlayerLiveGamesResponse` |  |
| chesscom | `chesscom.player_games_to_move` | `chesscom-player-games-to-move` | `GET /chesscom/player/{username}/games/to-move` | `username` (path String required) | `ApiKeyAuth` | `ChesscomPlayerGamesToMoveResponse` |  |
| chesscom | `chesscom.player_is_online` | `chesscom-player-is-online` | `GET /chesscom/player/{username}/is-online` | `username` (path String required) | `ApiKeyAuth` | `ChesscomPlayerIsOnlineResponse` |  |
| chesscom | `chesscom.player_matches` | `chesscom-player-matches` | `GET /chesscom/player/{username}/matches` | `username` (path String required) | `ApiKeyAuth` | `ChesscomPlayerMatchesResponse` |  |
| chesscom | `chesscom.player_stats` | `chesscom-player-stats` | `GET /chesscom/player/{username}/stats` | `username` (path String required) | `ApiKeyAuth` | `ChesscomPlayerStatsResponse` |  |
| chesscom | `chesscom.player_tournaments` | `chesscom-player-tournaments` | `GET /chesscom/player/{username}/tournaments` | `username` (path String required) | `ApiKeyAuth` | `ChesscomPlayerTournamentsResponse` |  |
| chesscom | `chesscom.puzzle` | `chesscom-puzzle` | `GET /chesscom/puzzle` | none | `ApiKeyAuth` | `ChesscomPuzzleResponse` |  |
| chesscom | `chesscom.puzzle_random` | `chesscom-puzzle-random` | `GET /chesscom/puzzle/random` | none | `ApiKeyAuth` | `ChesscomPuzzleRandomResponse` |  |
| chesscom | `chesscom.tournament` | `chesscom-tournament` | `GET /chesscom/tournament/{slug}` | `slug` (path String required) | `ApiKeyAuth` | `ChesscomTournamentResponse` |  |
| chesscom | `chesscom.tournament_round` | `chesscom-tournament-round` | `GET /chesscom/tournament/{slug}/{round}` | `slug` (path String required)<br>`round` (path i64 required) | `ApiKeyAuth` | `ChesscomTournamentRoundResponse` |  |
| chesscom | `chesscom.tournament_round_group` | `chesscom-tournament-round-group` | `GET /chesscom/tournament/{slug}/{round}/{group}` | `slug` (path String required)<br>`round` (path i64 required)<br>`group` (path i64 required) | `ApiKeyAuth` | `ChesscomTournamentRoundGroupResponse` |  |
