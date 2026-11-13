package net.crawlora.chesscom;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Chess.com endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 26;
    public static final List<String> OPERATION_IDS = List.of(
            "chesscom-club",
            "chesscom-club-matches",
            "chesscom-club-members",
            "chesscom-country",
            "chesscom-match",
            "chesscom-match-board",
            "chesscom-match-live",
            "chesscom-match-live-board",
            "chesscom-player",
            "chesscom-player-clubs",
            "chesscom-player-game-archives",
            "chesscom-player-game-month",
            "chesscom-player-game-month-pgn",
            "chesscom-player-games",
            "chesscom-player-games-to-move",
            "chesscom-player-is-online",
            "chesscom-player-live-games",
            "chesscom-player-live-games-base-time",
            "chesscom-player-matches",
            "chesscom-player-stats",
            "chesscom-player-tournaments",
            "chesscom-puzzle",
            "chesscom-puzzle-random",
            "chesscom-tournament",
            "chesscom-tournament-round",
            "chesscom-tournament-round-group"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("chesscom-club", new Operation("chesscom-club", "GET", "/chesscom/club/{slug}", Map.ofEntries(Map.entry("slug", new Param("slug", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-club-matches", new Operation("chesscom-club-matches", "GET", "/chesscom/club/{slug}/matches", Map.ofEntries(Map.entry("slug", new Param("slug", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-club-members", new Operation("chesscom-club-members", "GET", "/chesscom/club/{slug}/members", Map.ofEntries(Map.entry("slug", new Param("slug", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-country", new Operation("chesscom-country", "GET", "/chesscom/country/{iso}", Map.ofEntries(Map.entry("iso", new Param("iso", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-match-live", new Operation("chesscom-match-live", "GET", "/chesscom/live-match/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-match-live-board", new Operation("chesscom-match-live-board", "GET", "/chesscom/live-match/{id}/{board}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "integer", List.of(), "csv")), Map.entry("board", new Param("board", "path", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-match", new Operation("chesscom-match", "GET", "/chesscom/match/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-match-board", new Operation("chesscom-match-board", "GET", "/chesscom/match/{id}/{board}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "integer", List.of(), "csv")), Map.entry("board", new Param("board", "path", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player", new Operation("chesscom-player", "GET", "/chesscom/player/{username}", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-clubs", new Operation("chesscom-player-clubs", "GET", "/chesscom/player/{username}/clubs", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-games", new Operation("chesscom-player-games", "GET", "/chesscom/player/{username}/games", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-game-month", new Operation("chesscom-player-game-month", "GET", "/chesscom/player/{username}/games/archive/{year}/{month}", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv")), Map.entry("year", new Param("year", "path", true, "string", List.of(), "csv")), Map.entry("month", new Param("month", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-game-month-pgn", new Operation("chesscom-player-game-month-pgn", "GET", "/chesscom/player/{username}/games/archive/{year}/{month}/pgn", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv")), Map.entry("year", new Param("year", "path", true, "string", List.of(), "csv")), Map.entry("month", new Param("month", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-game-archives", new Operation("chesscom-player-game-archives", "GET", "/chesscom/player/{username}/games/archives", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-live-games-base-time", new Operation("chesscom-player-live-games-base-time", "GET", "/chesscom/player/{username}/games/live/{base_time}", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv")), Map.entry("base_time", new Param("base_time", "path", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-live-games", new Operation("chesscom-player-live-games", "GET", "/chesscom/player/{username}/games/live/{base_time}/{increment}", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv")), Map.entry("base_time", new Param("base_time", "path", true, "integer", List.of(), "csv")), Map.entry("increment", new Param("increment", "path", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-games-to-move", new Operation("chesscom-player-games-to-move", "GET", "/chesscom/player/{username}/games/to-move", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-is-online", new Operation("chesscom-player-is-online", "GET", "/chesscom/player/{username}/is-online", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-matches", new Operation("chesscom-player-matches", "GET", "/chesscom/player/{username}/matches", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-stats", new Operation("chesscom-player-stats", "GET", "/chesscom/player/{username}/stats", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-player-tournaments", new Operation("chesscom-player-tournaments", "GET", "/chesscom/player/{username}/tournaments", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-puzzle", new Operation("chesscom-puzzle", "GET", "/chesscom/puzzle", Map.of(), List.of("application/json")));
        operations.put("chesscom-puzzle-random", new Operation("chesscom-puzzle-random", "GET", "/chesscom/puzzle/random", Map.of(), List.of("application/json")));
        operations.put("chesscom-tournament", new Operation("chesscom-tournament", "GET", "/chesscom/tournament/{slug}", Map.ofEntries(Map.entry("slug", new Param("slug", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-tournament-round", new Operation("chesscom-tournament-round", "GET", "/chesscom/tournament/{slug}/{round}", Map.ofEntries(Map.entry("slug", new Param("slug", "path", true, "string", List.of(), "csv")), Map.entry("round", new Param("round", "path", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("chesscom-tournament-round-group", new Operation("chesscom-tournament-round-group", "GET", "/chesscom/tournament/{slug}/{round}/{group}", Map.ofEntries(Map.entry("slug", new Param("slug", "path", true, "string", List.of(), "csv")), Map.entry("round", new Param("round", "path", true, "integer", List.of(), "csv")), Map.entry("group", new Param("group", "path", true, "integer", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Chess.com operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object club(Map<String, ?> params) { return request("chesscom-club", params); }
    public Object clubMatches(Map<String, ?> params) { return request("chesscom-club-matches", params); }
    public Object clubMembers(Map<String, ?> params) { return request("chesscom-club-members", params); }
    public Object country(Map<String, ?> params) { return request("chesscom-country", params); }
    public Object matchLive(Map<String, ?> params) { return request("chesscom-match-live", params); }
    public Object matchLiveBoard(Map<String, ?> params) { return request("chesscom-match-live-board", params); }
    public Object match(Map<String, ?> params) { return request("chesscom-match", params); }
    public Object matchBoard(Map<String, ?> params) { return request("chesscom-match-board", params); }
    public Object player(Map<String, ?> params) { return request("chesscom-player", params); }
    public Object playerClubs(Map<String, ?> params) { return request("chesscom-player-clubs", params); }
    public Object playerGames(Map<String, ?> params) { return request("chesscom-player-games", params); }
    public Object playerGameMonth(Map<String, ?> params) { return request("chesscom-player-game-month", params); }
    public Object playerGameMonthPgn(Map<String, ?> params) { return request("chesscom-player-game-month-pgn", params); }
    public Object playerGameArchives(Map<String, ?> params) { return request("chesscom-player-game-archives", params); }
    public Object playerLiveGamesBaseTime(Map<String, ?> params) { return request("chesscom-player-live-games-base-time", params); }
    public Object playerLiveGames(Map<String, ?> params) { return request("chesscom-player-live-games", params); }
    public Object playerGamesToMove(Map<String, ?> params) { return request("chesscom-player-games-to-move", params); }
    public Object playerIsOnline(Map<String, ?> params) { return request("chesscom-player-is-online", params); }
    public Object playerMatches(Map<String, ?> params) { return request("chesscom-player-matches", params); }
    public Object playerStats(Map<String, ?> params) { return request("chesscom-player-stats", params); }
    public Object playerTournaments(Map<String, ?> params) { return request("chesscom-player-tournaments", params); }
    public Object puzzle(Map<String, ?> params) { return request("chesscom-puzzle", params); }
    public Object puzzleRandom(Map<String, ?> params) { return request("chesscom-puzzle-random", params); }
    public Object tournament(Map<String, ?> params) { return request("chesscom-tournament", params); }
    public Object tournamentRound(Map<String, ?> params) { return request("chesscom-tournament-round", params); }
    public Object tournamentRoundGroup(Map<String, ?> params) { return request("chesscom-tournament-round-group", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
