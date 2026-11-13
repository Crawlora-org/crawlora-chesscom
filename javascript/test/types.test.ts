import { ChessComClient } from "../src/index.js";

const client = new ChessComClient({ apiKey: "test-key" });
void client.club({"slug": "sample"});
void client.request("chesscom-club", {"slug": "sample"});
const streamResponse: Promise<Response> = client.request("chesscom-club", {"slug": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("chesscom-club", {"slug": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.club({"slug": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("chesscom-club", {"slug": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("chesscom-club", {"slug": "sample"}, { responseType: "text" });
void rawText;


void client.puzzle();
void client.request("chesscom-puzzle");
// @ts-expect-error The selected operation requires its documented params.
void client.club();
