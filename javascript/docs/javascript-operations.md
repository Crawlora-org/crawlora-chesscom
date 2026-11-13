# Crawlora Chess.com JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `26`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| chesscom | `chesscom.club` | `chesscom-club` | `GET /chesscom/club/{slug}` | `slug` (path string required) | `ApiKeyAuth` | `ChesscomClubResponse` |  |
| chesscom | `chesscom.clubMatches` | `chesscom-club-matches` | `GET /chesscom/club/{slug}/matches` | `slug` (path string required) | `ApiKeyAuth` | `ChesscomClubMatchesResponse` |  |
| chesscom | `chesscom.clubMembers` | `chesscom-club-members` | `GET /chesscom/club/{slug}/members` | `slug` (path string required) | `ApiKeyAuth` | `ChesscomClubMembersResponse` |  |
| chesscom | `chesscom.country` | `chesscom-country` | `GET /chesscom/country/{iso}` | `iso` (path string required) | `ApiKeyAuth` | `ChesscomCountryResponse` |  |
| chesscom | `chesscom.matchLive` | `chesscom-match-live` | `GET /chesscom/live-match/{id}` | `id` (path number required) | `ApiKeyAuth` | `ChesscomMatchLiveResponse` |  |
| chesscom | `chesscom.matchLiveBoard` | `chesscom-match-live-board` | `GET /chesscom/live-match/{id}/{board}` | `id` (path number required)<br>`board` (path number required) | `ApiKeyAuth` | `ChesscomMatchLiveBoardResponse` |  |
| chesscom | `chesscom.match` | `chesscom-match` | `GET /chesscom/match/{id}` | `id` (path number required) | `ApiKeyAuth` | `ChesscomMatchResponse` |  |
| chesscom | `chesscom.matchBoard` | `chesscom-match-board` | `GET /chesscom/match/{id}/{board}` | `id` (path number required)<br>`board` (path number required) | `ApiKeyAuth` | `ChesscomMatchBoardResponse` |  |
| chesscom | `chesscom.player` | `chesscom-player` | `GET /chesscom/player/{username}` | `username` (path string required) | `ApiKeyAuth` | `ChesscomPlayerResponse` |  |
| chesscom | `chesscom.playerClubs` | `chesscom-player-clubs` | `GET /chesscom/player/{username}/clubs` | `username` (path string required) | `ApiKeyAuth` | `ChesscomPlayerClubsResponse` |  |
| chesscom | `chesscom.playerGames` | `chesscom-player-games` | `GET /chesscom/player/{username}/games` | `username` (path string required) | `ApiKeyAuth` | `ChesscomPlayerGamesResponse` |  |
| chesscom | `chesscom.playerGameMonth` | `chesscom-player-game-month` | `GET /chesscom/player/{username}/games/archive/{year}/{month}` | `username` (path string required)<br>`year` (path string required)<br>`month` (path string required) | `ApiKeyAuth` | `ChesscomPlayerGameMonthResponse` |  |
| chesscom | `chesscom.playerGameMonthPgn` | `chesscom-player-game-month-pgn` | `GET /chesscom/player/{username}/games/archive/{year}/{month}/pgn` | `username` (path string required)<br>`year` (path string required)<br>`month` (path string required) | `ApiKeyAuth` | `ChesscomPlayerGameMonthPgnResponse` |  |
| chesscom | `chesscom.playerGameArchives` | `chesscom-player-game-archives` | `GET /chesscom/player/{username}/games/archives` | `username` (path string required) | `ApiKeyAuth` | `ChesscomPlayerGameArchivesResponse` |  |
| chesscom | `chesscom.playerLiveGamesBaseTime` | `chesscom-player-live-games-base-time` | `GET /chesscom/player/{username}/games/live/{base_time}` | `username` (path string required)<br>`base_time` (path number required) | `ApiKeyAuth` | `ChesscomPlayerLiveGamesBaseTimeResponse` |  |
| chesscom | `chesscom.playerLiveGames` | `chesscom-player-live-games` | `GET /chesscom/player/{username}/games/live/{base_time}/{increment}` | `username` (path string required)<br>`base_time` (path number required)<br>`increment` (path number required) | `ApiKeyAuth` | `ChesscomPlayerLiveGamesResponse` |  |
| chesscom | `chesscom.playerGamesToMove` | `chesscom-player-games-to-move` | `GET /chesscom/player/{username}/games/to-move` | `username` (path string required) | `ApiKeyAuth` | `ChesscomPlayerGamesToMoveResponse` |  |
| chesscom | `chesscom.playerIsOnline` | `chesscom-player-is-online` | `GET /chesscom/player/{username}/is-online` | `username` (path string required) | `ApiKeyAuth` | `ChesscomPlayerIsOnlineResponse` |  |
| chesscom | `chesscom.playerMatches` | `chesscom-player-matches` | `GET /chesscom/player/{username}/matches` | `username` (path string required) | `ApiKeyAuth` | `ChesscomPlayerMatchesResponse` |  |
| chesscom | `chesscom.playerStats` | `chesscom-player-stats` | `GET /chesscom/player/{username}/stats` | `username` (path string required) | `ApiKeyAuth` | `ChesscomPlayerStatsResponse` |  |
| chesscom | `chesscom.playerTournaments` | `chesscom-player-tournaments` | `GET /chesscom/player/{username}/tournaments` | `username` (path string required) | `ApiKeyAuth` | `ChesscomPlayerTournamentsResponse` |  |
| chesscom | `chesscom.puzzle` | `chesscom-puzzle` | `GET /chesscom/puzzle` | none | `ApiKeyAuth` | `ChesscomPuzzleResponse` |  |
| chesscom | `chesscom.puzzleRandom` | `chesscom-puzzle-random` | `GET /chesscom/puzzle/random` | none | `ApiKeyAuth` | `ChesscomPuzzleRandomResponse` |  |
| chesscom | `chesscom.tournament` | `chesscom-tournament` | `GET /chesscom/tournament/{slug}` | `slug` (path string required) | `ApiKeyAuth` | `ChesscomTournamentResponse` |  |
| chesscom | `chesscom.tournamentRound` | `chesscom-tournament-round` | `GET /chesscom/tournament/{slug}/{round}` | `slug` (path string required)<br>`round` (path number required) | `ApiKeyAuth` | `ChesscomTournamentRoundResponse` |  |
| chesscom | `chesscom.tournamentRoundGroup` | `chesscom-tournament-round-group` | `GET /chesscom/tournament/{slug}/{round}/{group}` | `slug` (path string required)<br>`round` (path number required)<br>`group` (path number required) | `ApiKeyAuth` | `ChesscomTournamentRoundGroupResponse` |  |
