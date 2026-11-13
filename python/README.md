# crawlora-chesscom — Chess.com API client for Python

Python client for Crawlora's hosted Chess.com API. It exposes 26 API endpoints covering puzzles, player and club resources, tournaments, and public team matches. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-python-homepage); the package does not run a browser or scrape
Chess.com locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Chess.com or its owners.

## Install

```sh
python -m pip install crawlora-chesscom
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=chesscom-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_chesscom import ChessComClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with ChessComClient(api_key=api_key) as client:
    result_1 = client.puzzle()
    print(result_1)
    result_2 = client.puzzle_random()
    print(result_2)
```

The package also exports `Client` as an alias for `ChessComClient`. Operation
methods are available directly in snake_case and through the `chesscom`
group. The async package client is `AsyncChessComClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_chesscom import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.puzzle()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/examples/python.py) for a complete usage example.

## Supported Chess.com API endpoints

This package exposes every route below through direct snake_case methods and the `chesscom` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-chesscom/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
