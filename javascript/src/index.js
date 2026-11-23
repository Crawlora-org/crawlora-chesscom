import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class ChessComClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-chesscom-js/0.1.1" });
    this["club"] = (...args) => this.request("chesscom-club", ...args);
    this["clubMatches"] = (...args) => this.request("chesscom-club-matches", ...args);
    this["clubMembers"] = (...args) => this.request("chesscom-club-members", ...args);
    this["country"] = (...args) => this.request("chesscom-country", ...args);
    this["matchLive"] = (...args) => this.request("chesscom-match-live", ...args);
    this["matchLiveBoard"] = (...args) => this.request("chesscom-match-live-board", ...args);
    this["match"] = (...args) => this.request("chesscom-match", ...args);
    this["matchBoard"] = (...args) => this.request("chesscom-match-board", ...args);
    this["player"] = (...args) => this.request("chesscom-player", ...args);
    this["playerClubs"] = (...args) => this.request("chesscom-player-clubs", ...args);
    this["playerGames"] = (...args) => this.request("chesscom-player-games", ...args);
    this["playerGameMonth"] = (...args) => this.request("chesscom-player-game-month", ...args);
    this["playerGameMonthPgn"] = (...args) => this.request("chesscom-player-game-month-pgn", ...args);
    this["playerGameArchives"] = (...args) => this.request("chesscom-player-game-archives", ...args);
    this["playerLiveGamesBaseTime"] = (...args) => this.request("chesscom-player-live-games-base-time", ...args);
    this["playerLiveGames"] = (...args) => this.request("chesscom-player-live-games", ...args);
    this["playerGamesToMove"] = (...args) => this.request("chesscom-player-games-to-move", ...args);
    this["playerIsOnline"] = (...args) => this.request("chesscom-player-is-online", ...args);
    this["playerMatches"] = (...args) => this.request("chesscom-player-matches", ...args);
    this["playerStats"] = (...args) => this.request("chesscom-player-stats", ...args);
    this["playerTournaments"] = (...args) => this.request("chesscom-player-tournaments", ...args);
    this["puzzle"] = (...args) => this.request("chesscom-puzzle", ...args);
    this["puzzleRandom"] = (...args) => this.request("chesscom-puzzle-random", ...args);
    this["tournament"] = (...args) => this.request("chesscom-tournament", ...args);
    this["tournamentRound"] = (...args) => this.request("chesscom-tournament-round", ...args);
    this["tournamentRoundGroup"] = (...args) => this.request("chesscom-tournament-round-group", ...args);
  }
}

export { ChessComClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.1";
export default ChessComClient;
