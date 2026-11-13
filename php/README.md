# Crawlora Chess.com API client for PHP (`crawlora/chesscom`)

This PHP package calls Crawlora's hosted Chess.com API at `https://api.crawlora.net/api/v1`. It exposes 26 endpoints covering puzzles, player and club resources, tournaments, and public team matches. It does not call or scrape Chess.com directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/chesscom
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Chesscom\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("chesscom-club", ['slug' => 'sample-id']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 26 API operations.

## Supported Chess.com API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-chesscom). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/docs/usage.md).
