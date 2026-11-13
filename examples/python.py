import os

from crawlora_chesscom import ChessComClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with ChessComClient(api_key=api_key) as client:
    puzzle = client.puzzle()
    print('puzzle', puzzle)
    puzzle_random = client.puzzle_random()
    print('puzzle_random', puzzle_random)
