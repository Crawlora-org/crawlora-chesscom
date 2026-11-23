# Chess.com clients for Crawlora

Official Crawlora client packages for the hosted Chess.com API. Access 26 API endpoints covering puzzles, player and club resources, tournaments, and public team matches from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Chess.com locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Chess.com or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/chesscom`](javascript/README.md)
- Python: [`crawlora-chesscom`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-chesscom`](go.mod)
- Ruby: [`crawlora-chesscom`](ruby/README.md)
- Java: [`net.crawlora:crawlora-chesscom:0.1.1`](java/README.md)
- PHP: [`crawlora/chesscom`](php/README.md)
- Rust: [`crawlora-chesscom`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 26 selected public Chess.com API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/chesscom/club/{slug}` | `chesscom-club` | Get a Chess.com club profile |
| `GET` | `/chesscom/club/{slug}/matches` | `chesscom-club-matches` | List one club’s team matches |
| `GET` | `/chesscom/club/{slug}/members` | `chesscom-club-members` | List one club’s members |
| `GET` | `/chesscom/country/{iso}` | `chesscom-country` | Get Chess.com country metadata |
| `GET` | `/chesscom/live-match/{id}` | `chesscom-match-live` | Get a live Chess.com team match |
| `GET` | `/chesscom/live-match/{id}/{board}` | `chesscom-match-live-board` | Get a live team match board |
| `GET` | `/chesscom/match/{id}` | `chesscom-match` | Get a Chess.com team match |
| `GET` | `/chesscom/match/{id}/{board}` | `chesscom-match-board` | Get a team match board |
| `GET` | `/chesscom/player/{username}` | `chesscom-player` | Get a public Chess.com player profile |
| `GET` | `/chesscom/player/{username}/clubs` | `chesscom-player-clubs` | Get a player’s public clubs |
| `GET` | `/chesscom/player/{username}/games` | `chesscom-player-games` | Get a player’s current Daily Chess games |
| `GET` | `/chesscom/player/{username}/games/archive/{year}/{month}` | `chesscom-player-game-month` | Get a monthly player game archive |
| `GET` | `/chesscom/player/{username}/games/archive/{year}/{month}/pgn` | `chesscom-player-game-month-pgn` | Get a monthly PGN game archive |
| `GET` | `/chesscom/player/{username}/games/archives` | `chesscom-player-game-archives` | List a player’s monthly game archives |
| `GET` | `/chesscom/player/{username}/games/live/{base_time}` | `chesscom-player-live-games-base-time` | Get live games by base time |
| `GET` | `/chesscom/player/{username}/games/live/{base_time}/{increment}` | `chesscom-player-live-games` | Get live games by time control |
| `GET` | `/chesscom/player/{username}/games/to-move` | `chesscom-player-games-to-move` | Get a player’s Daily Chess games to move |
| `GET` | `/chesscom/player/{username}/is-online` | `chesscom-player-is-online` | Get Chess.com player online status |
| `GET` | `/chesscom/player/{username}/matches` | `chesscom-player-matches` | Get a player’s team-match records |
| `GET` | `/chesscom/player/{username}/stats` | `chesscom-player-stats` | Get Chess.com player statistics |
| `GET` | `/chesscom/player/{username}/tournaments` | `chesscom-player-tournaments` | Get a player’s tournament records |
| `GET` | `/chesscom/puzzle` | `chesscom-puzzle` | Chess.com daily puzzle |
| `GET` | `/chesscom/puzzle/random` | `chesscom-puzzle-random` | Chess.com random daily puzzle |
| `GET` | `/chesscom/tournament/{slug}` | `chesscom-tournament` | Get a Chess.com tournament |
| `GET` | `/chesscom/tournament/{slug}/{round}` | `chesscom-tournament-round` | Get a tournament round |
| `GET` | `/chesscom/tournament/{slug}/{round}/{group}` | `chesscom-tournament-round-group` | Get a tournament round group |

## License

MIT. See [LICENSE](LICENSE).
