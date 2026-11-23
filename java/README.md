# Crawlora Chess.com API client for Java

The official Java client for Crawlora's hosted Chess.com API. It exposes 26 endpoints covering puzzles, player and club resources, tournaments, and public team matches. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-chesscom</artifactId>
  <version>0.1.1</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-java-console) to get an API key.

```java
import net.crawlora.chesscom.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.puzzle(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Chess.com API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-chesscom)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-java-api-docs)
