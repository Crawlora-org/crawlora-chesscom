import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class ChessComClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  club(params: OperationParamsMap["chesscom-club"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  clubMatches(params: OperationParamsMap["chesscom-club-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  clubMembers(params: OperationParamsMap["chesscom-club-members"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  country(params: OperationParamsMap["chesscom-country"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchLive(params: OperationParamsMap["chesscom-match-live"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchLiveBoard(params: OperationParamsMap["chesscom-match-live-board"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  match(params: OperationParamsMap["chesscom-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchBoard(params: OperationParamsMap["chesscom-match-board"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params: OperationParamsMap["chesscom-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerClubs(params: OperationParamsMap["chesscom-player-clubs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerGames(params: OperationParamsMap["chesscom-player-games"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerGameMonth(params: OperationParamsMap["chesscom-player-game-month"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerGameMonthPgn(params: OperationParamsMap["chesscom-player-game-month-pgn"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerGameArchives(params: OperationParamsMap["chesscom-player-game-archives"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerLiveGamesBaseTime(params: OperationParamsMap["chesscom-player-live-games-base-time"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerLiveGames(params: OperationParamsMap["chesscom-player-live-games"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerGamesToMove(params: OperationParamsMap["chesscom-player-games-to-move"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerIsOnline(params: OperationParamsMap["chesscom-player-is-online"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerMatches(params: OperationParamsMap["chesscom-player-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerStats(params: OperationParamsMap["chesscom-player-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerTournaments(params: OperationParamsMap["chesscom-player-tournaments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  puzzle(params?: OperationParamsMap["chesscom-puzzle"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  puzzleRandom(params?: OperationParamsMap["chesscom-puzzle-random"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournament(params: OperationParamsMap["chesscom-tournament"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentRound(params: OperationParamsMap["chesscom-tournament-round"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentRoundGroup(params: OperationParamsMap["chesscom-tournament-round-group"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  club(params: OperationParamsMap["chesscom-club"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  clubMatches(params: OperationParamsMap["chesscom-club-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  clubMembers(params: OperationParamsMap["chesscom-club-members"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  country(params: OperationParamsMap["chesscom-country"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchLive(params: OperationParamsMap["chesscom-match-live"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchLiveBoard(params: OperationParamsMap["chesscom-match-live-board"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  match(params: OperationParamsMap["chesscom-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchBoard(params: OperationParamsMap["chesscom-match-board"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params: OperationParamsMap["chesscom-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerClubs(params: OperationParamsMap["chesscom-player-clubs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerGames(params: OperationParamsMap["chesscom-player-games"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerGameMonth(params: OperationParamsMap["chesscom-player-game-month"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerGameMonthPgn(params: OperationParamsMap["chesscom-player-game-month-pgn"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerGameArchives(params: OperationParamsMap["chesscom-player-game-archives"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerLiveGamesBaseTime(params: OperationParamsMap["chesscom-player-live-games-base-time"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerLiveGames(params: OperationParamsMap["chesscom-player-live-games"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerGamesToMove(params: OperationParamsMap["chesscom-player-games-to-move"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerIsOnline(params: OperationParamsMap["chesscom-player-is-online"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerMatches(params: OperationParamsMap["chesscom-player-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerStats(params: OperationParamsMap["chesscom-player-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerTournaments(params: OperationParamsMap["chesscom-player-tournaments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  puzzle(params?: OperationParamsMap["chesscom-puzzle"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  puzzleRandom(params?: OperationParamsMap["chesscom-puzzle-random"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournament(params: OperationParamsMap["chesscom-tournament"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentRound(params: OperationParamsMap["chesscom-tournament-round"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentRoundGroup(params: OperationParamsMap["chesscom-tournament-round-group"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  club(...args: OperationRequestArgs<"chesscom-club">): Promise<OperationResponseMap["chesscom-club"]>;
  clubMatches(...args: OperationRequestArgs<"chesscom-club-matches">): Promise<OperationResponseMap["chesscom-club-matches"]>;
  clubMembers(...args: OperationRequestArgs<"chesscom-club-members">): Promise<OperationResponseMap["chesscom-club-members"]>;
  country(...args: OperationRequestArgs<"chesscom-country">): Promise<OperationResponseMap["chesscom-country"]>;
  matchLive(...args: OperationRequestArgs<"chesscom-match-live">): Promise<OperationResponseMap["chesscom-match-live"]>;
  matchLiveBoard(...args: OperationRequestArgs<"chesscom-match-live-board">): Promise<OperationResponseMap["chesscom-match-live-board"]>;
  match(...args: OperationRequestArgs<"chesscom-match">): Promise<OperationResponseMap["chesscom-match"]>;
  matchBoard(...args: OperationRequestArgs<"chesscom-match-board">): Promise<OperationResponseMap["chesscom-match-board"]>;
  player(...args: OperationRequestArgs<"chesscom-player">): Promise<OperationResponseMap["chesscom-player"]>;
  playerClubs(...args: OperationRequestArgs<"chesscom-player-clubs">): Promise<OperationResponseMap["chesscom-player-clubs"]>;
  playerGames(...args: OperationRequestArgs<"chesscom-player-games">): Promise<OperationResponseMap["chesscom-player-games"]>;
  playerGameMonth(...args: OperationRequestArgs<"chesscom-player-game-month">): Promise<OperationResponseMap["chesscom-player-game-month"]>;
  playerGameMonthPgn(...args: OperationRequestArgs<"chesscom-player-game-month-pgn">): Promise<OperationResponseMap["chesscom-player-game-month-pgn"]>;
  playerGameArchives(...args: OperationRequestArgs<"chesscom-player-game-archives">): Promise<OperationResponseMap["chesscom-player-game-archives"]>;
  playerLiveGamesBaseTime(...args: OperationRequestArgs<"chesscom-player-live-games-base-time">): Promise<OperationResponseMap["chesscom-player-live-games-base-time"]>;
  playerLiveGames(...args: OperationRequestArgs<"chesscom-player-live-games">): Promise<OperationResponseMap["chesscom-player-live-games"]>;
  playerGamesToMove(...args: OperationRequestArgs<"chesscom-player-games-to-move">): Promise<OperationResponseMap["chesscom-player-games-to-move"]>;
  playerIsOnline(...args: OperationRequestArgs<"chesscom-player-is-online">): Promise<OperationResponseMap["chesscom-player-is-online"]>;
  playerMatches(...args: OperationRequestArgs<"chesscom-player-matches">): Promise<OperationResponseMap["chesscom-player-matches"]>;
  playerStats(...args: OperationRequestArgs<"chesscom-player-stats">): Promise<OperationResponseMap["chesscom-player-stats"]>;
  playerTournaments(...args: OperationRequestArgs<"chesscom-player-tournaments">): Promise<OperationResponseMap["chesscom-player-tournaments"]>;
  puzzle(...args: OperationRequestArgs<"chesscom-puzzle">): Promise<OperationResponseMap["chesscom-puzzle"]>;
  puzzleRandom(...args: OperationRequestArgs<"chesscom-puzzle-random">): Promise<OperationResponseMap["chesscom-puzzle-random"]>;
  tournament(...args: OperationRequestArgs<"chesscom-tournament">): Promise<OperationResponseMap["chesscom-tournament"]>;
  tournamentRound(...args: OperationRequestArgs<"chesscom-tournament-round">): Promise<OperationResponseMap["chesscom-tournament-round"]>;
  tournamentRoundGroup(...args: OperationRequestArgs<"chesscom-tournament-round-group">): Promise<OperationResponseMap["chesscom-tournament-round-group"]>;
}
export { ChessComClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default ChessComClient;
