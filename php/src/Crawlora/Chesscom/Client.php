<?php

declare(strict_types=1);

namespace Crawlora\Chesscom;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'chesscom';
    public const VERSION = '0.1.1';
    public const OPERATION_COUNT = 26;
    public const OPERATION_IDS = ["chesscom-club", "chesscom-club-matches", "chesscom-club-members", "chesscom-country", "chesscom-match", "chesscom-match-board", "chesscom-match-live", "chesscom-match-live-board", "chesscom-player", "chesscom-player-clubs", "chesscom-player-game-archives", "chesscom-player-game-month", "chesscom-player-game-month-pgn", "chesscom-player-games", "chesscom-player-games-to-move", "chesscom-player-is-online", "chesscom-player-live-games", "chesscom-player-live-games-base-time", "chesscom-player-matches", "chesscom-player-stats", "chesscom-player-tournaments", "chesscom-puzzle", "chesscom-puzzle-random", "chesscom-tournament", "chesscom-tournament-round", "chesscom-tournament-round-group"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"chesscom-club": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-club", "method": "GET", "params": [{"description": "Chess.com club URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}], "path": "/chesscom/club/{slug}", "pathParams": ["slug"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-club-matches": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-club-matches", "method": "GET", "params": [{"description": "Chess.com club URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}], "path": "/chesscom/club/{slug}/matches", "pathParams": ["slug"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-club-members": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-club-members", "method": "GET", "params": [{"description": "Chess.com club URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}], "path": "/chesscom/club/{slug}/members", "pathParams": ["slug"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-country": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-country", "method": "GET", "params": [{"description": "Two-character uppercase ISO country code or documented Chess.com region code", "in": "path", "name": "iso", "required": true, "type": "string", "x-example": "IT"}], "path": "/chesscom/country/{iso}", "pathParams": ["iso"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-match": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-match", "method": "GET", "params": [{"description": "Positive Chess.com team match ID", "in": "path", "name": "id", "required": true, "type": "integer"}], "path": "/chesscom/match/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-match-board": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-match-board", "method": "GET", "params": [{"description": "Positive Chess.com team match ID", "in": "path", "name": "id", "required": true, "type": "integer"}, {"description": "Source board number", "in": "path", "name": "board", "required": true, "type": "integer"}], "path": "/chesscom/match/{id}/{board}", "pathParams": ["id", "board"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-match-live": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-match-live", "method": "GET", "params": [{"description": "Positive Chess.com live team match ID", "in": "path", "name": "id", "required": true, "type": "integer"}], "path": "/chesscom/live-match/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-match-live-board": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-match-live-board", "method": "GET", "params": [{"description": "Positive Chess.com live team match ID", "in": "path", "name": "id", "required": true, "type": "integer"}, {"description": "Source board number", "in": "path", "name": "board", "required": true, "type": "integer"}], "path": "/chesscom/live-match/{id}/{board}", "pathParams": ["id", "board"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-clubs": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-clubs", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/clubs", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-game-archives": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-game-archives", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games/archives", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-game-month": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-game-month", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}, {"description": "Four-digit game-end year", "in": "path", "name": "year", "required": true, "type": "string"}, {"description": "Game-end month, 1 through 12", "in": "path", "name": "month", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games/archive/{year}/{month}", "pathParams": ["username", "year", "month"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-game-month-pgn": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-game-month-pgn", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}, {"description": "Four-digit game-end year", "in": "path", "name": "year", "required": true, "type": "string"}, {"description": "Game-end month, 1 through 12", "in": "path", "name": "month", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games/archive/{year}/{month}/pgn", "pathParams": ["username", "year", "month"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-games": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-games", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-games-to-move": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-games-to-move", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/games/to-move", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-is-online": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-is-online", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/is-online", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-live-games": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-live-games", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}, {"description": "Base time in seconds", "in": "path", "name": "base_time", "required": true, "type": "integer"}, {"description": "Increment in seconds", "in": "path", "name": "increment", "required": true, "type": "integer"}], "path": "/chesscom/player/{username}/games/live/{base_time}/{increment}", "pathParams": ["username", "base_time", "increment"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-live-games-base-time": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-live-games-base-time", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}, {"description": "Base time in seconds", "in": "path", "name": "base_time", "required": true, "type": "integer"}], "path": "/chesscom/player/{username}/games/live/{base_time}", "pathParams": ["username", "base_time"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-matches": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-matches", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/matches", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-stats": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-stats", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/stats", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-player-tournaments": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-player-tournaments", "method": "GET", "params": [{"description": "Chess.com username", "in": "path", "name": "username", "required": true, "type": "string"}], "path": "/chesscom/player/{username}/tournaments", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-puzzle": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-puzzle", "method": "GET", "params": [], "path": "/chesscom/puzzle", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-puzzle-random": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-puzzle-random", "method": "GET", "params": [], "path": "/chesscom/puzzle/random", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-tournament": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-tournament", "method": "GET", "params": [{"description": "Chess.com tournament URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}], "path": "/chesscom/tournament/{slug}", "pathParams": ["slug"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-tournament-round": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-tournament-round", "method": "GET", "params": [{"description": "Chess.com tournament URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}, {"description": "Source round number", "in": "path", "name": "round", "required": true, "type": "integer"}], "path": "/chesscom/tournament/{slug}/{round}", "pathParams": ["slug", "round"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "chesscom-tournament-round-group": {"bodyParam": null, "bodyRequired": false, "id": "chesscom-tournament-round-group", "method": "GET", "params": [{"description": "Chess.com tournament URL ID", "in": "path", "name": "slug", "required": true, "type": "string"}, {"description": "Source round number", "in": "path", "name": "round", "required": true, "type": "integer"}, {"description": "Source group number", "in": "path", "name": "group", "required": true, "type": "integer"}], "path": "/chesscom/tournament/{slug}/{round}/{group}", "pathParams": ["slug", "round", "group"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-chesscom-php/0.1.1',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function club(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-club", $params, $responseType);
    }
    public function club_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-club-matches", $params, $responseType);
    }
    public function club_members(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-club-members", $params, $responseType);
    }
    public function country(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-country", $params, $responseType);
    }
    public function match_live(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-match-live", $params, $responseType);
    }
    public function match_live_board(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-match-live-board", $params, $responseType);
    }
    public function match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-match", $params, $responseType);
    }
    public function match_board(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-match-board", $params, $responseType);
    }
    public function player(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player", $params, $responseType);
    }
    public function player_clubs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-clubs", $params, $responseType);
    }
    public function player_games(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-games", $params, $responseType);
    }
    public function player_game_month(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-game-month", $params, $responseType);
    }
    public function player_game_month_pgn(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-game-month-pgn", $params, $responseType);
    }
    public function player_game_archives(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-game-archives", $params, $responseType);
    }
    public function player_live_games_base_time(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-live-games-base-time", $params, $responseType);
    }
    public function player_live_games(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-live-games", $params, $responseType);
    }
    public function player_games_to_move(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-games-to-move", $params, $responseType);
    }
    public function player_is_online(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-is-online", $params, $responseType);
    }
    public function player_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-matches", $params, $responseType);
    }
    public function player_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-stats", $params, $responseType);
    }
    public function player_tournaments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-player-tournaments", $params, $responseType);
    }
    public function puzzle(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-puzzle", $params, $responseType);
    }
    public function puzzle_random(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-puzzle-random", $params, $responseType);
    }
    public function tournament(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-tournament", $params, $responseType);
    }
    public function tournament_round(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-tournament-round", $params, $responseType);
    }
    public function tournament_round_group(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("chesscom-tournament-round-group", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
