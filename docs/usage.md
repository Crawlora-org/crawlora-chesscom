# Chess.com API endpoint reference and client usage

This reference lists all 26 public Chess.com API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/chesscom`, `crawlora-chesscom`, and `crawlora-chesscom` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Chess.com locally; Crawlora is independent from and not endorsed by Chess.com or its owners.

The package tracks the public API contract revision `sha256:bb52aafac634d8bd443235e38fe6f1e7503b53f83d9e87a10df59858337a4628` bundled with release `0.1.1`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `chesscom`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `club` | `club` | `chesscom.club` | `GET /chesscom/club/{slug}` | `slug` (path, required) | Get a Chess.com club profile |
| `clubMatches` | `club_matches` | `chesscom.club_matches` | `GET /chesscom/club/{slug}/matches` | `slug` (path, required) | List one club’s team matches |
| `clubMembers` | `club_members` | `chesscom.club_members` | `GET /chesscom/club/{slug}/members` | `slug` (path, required) | List one club’s members |
| `country` | `country` | `chesscom.country` | `GET /chesscom/country/{iso}` | `iso` (path, required) | Get Chess.com country metadata |
| `match` | `match` | `chesscom.match_` | `GET /chesscom/match/{id}` | `id` (path, required) | Get a Chess.com team match |
| `matchBoard` | `match_board` | `chesscom.match_board` | `GET /chesscom/match/{id}/{board}` | `id` (path, required), `board` (path, required) | Get a team match board |
| `matchLive` | `match_live` | `chesscom.match_live` | `GET /chesscom/live-match/{id}` | `id` (path, required) | Get a live Chess.com team match |
| `matchLiveBoard` | `match_live_board` | `chesscom.match_live_board` | `GET /chesscom/live-match/{id}/{board}` | `id` (path, required), `board` (path, required) | Get a live team match board |
| `player` | `player` | `chesscom.player` | `GET /chesscom/player/{username}` | `username` (path, required) | Get a public Chess.com player profile |
| `playerClubs` | `player_clubs` | `chesscom.player_clubs` | `GET /chesscom/player/{username}/clubs` | `username` (path, required) | Get a player’s public clubs |
| `playerGameArchives` | `player_game_archives` | `chesscom.player_game_archives` | `GET /chesscom/player/{username}/games/archives` | `username` (path, required) | List a player’s monthly game archives |
| `playerGameMonth` | `player_game_month` | `chesscom.player_game_month` | `GET /chesscom/player/{username}/games/archive/{year}/{month}` | `username` (path, required), `year` (path, required), `month` (path, required) | Get a monthly player game archive |
| `playerGameMonthPgn` | `player_game_month_pgn` | `chesscom.player_game_month_pgn` | `GET /chesscom/player/{username}/games/archive/{year}/{month}/pgn` | `username` (path, required), `year` (path, required), `month` (path, required) | Get a monthly PGN game archive |
| `playerGames` | `player_games` | `chesscom.player_games` | `GET /chesscom/player/{username}/games` | `username` (path, required) | Get a player’s current Daily Chess games |
| `playerGamesToMove` | `player_games_to_move` | `chesscom.player_games_to_move` | `GET /chesscom/player/{username}/games/to-move` | `username` (path, required) | Get a player’s Daily Chess games to move |
| `playerIsOnline` | `player_is_online` | `chesscom.player_is_online` | `GET /chesscom/player/{username}/is-online` | `username` (path, required) | Get Chess.com player online status |
| `playerLiveGames` | `player_live_games` | `chesscom.player_live_games` | `GET /chesscom/player/{username}/games/live/{base_time}/{increment}` | `username` (path, required), `base_time` (path, required), `increment` (path, required) | Get live games by time control |
| `playerLiveGamesBaseTime` | `player_live_games_base_time` | `chesscom.player_live_games_base_time` | `GET /chesscom/player/{username}/games/live/{base_time}` | `username` (path, required), `base_time` (path, required) | Get live games by base time |
| `playerMatches` | `player_matches` | `chesscom.player_matches` | `GET /chesscom/player/{username}/matches` | `username` (path, required) | Get a player’s team-match records |
| `playerStats` | `player_stats` | `chesscom.player_stats` | `GET /chesscom/player/{username}/stats` | `username` (path, required) | Get Chess.com player statistics |
| `playerTournaments` | `player_tournaments` | `chesscom.player_tournaments` | `GET /chesscom/player/{username}/tournaments` | `username` (path, required) | Get a player’s tournament records |
| `puzzle` | `puzzle` | `chesscom.puzzle` | `GET /chesscom/puzzle` | — | Chess.com daily puzzle |
| `puzzleRandom` | `puzzle_random` | `chesscom.puzzle_random` | `GET /chesscom/puzzle/random` | — | Chess.com random daily puzzle |
| `tournament` | `tournament` | `chesscom.tournament` | `GET /chesscom/tournament/{slug}` | `slug` (path, required) | Get a Chess.com tournament |
| `tournamentRound` | `tournament_round` | `chesscom.tournament_round` | `GET /chesscom/tournament/{slug}/{round}` | `slug` (path, required), `round` (path, required) | Get a tournament round |
| `tournamentRoundGroup` | `tournament_round_group` | `chesscom.tournament_round_group` | `GET /chesscom/tournament/{slug}/{round}/{group}` | `slug` (path, required), `round` (path, required), `group` (path, required) | Get a tournament round group |

## Client forms

- JavaScript: import `ChessComClient` (also exported as `Client`) from `@crawlora-org/chesscom`; use `new ChessComClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `ChessComClient` (also exported as `Client`) from `crawlora_chesscom`; use `with ChessComClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncChessComClient`, used with `async with` and `await`.
- Rust: add `crawlora-chesscom` with Cargo; import `Client` and the generated operation parameter struct, then call `client.chesscom.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
