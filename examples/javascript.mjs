import { ChessComClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new ChessComClient({ apiKey });

  const puzzle = await client.puzzle({  });
  console.log("puzzle", puzzle);
  const puzzleRandom = await client.puzzleRandom({  });
  console.log("puzzleRandom", puzzleRandom);
