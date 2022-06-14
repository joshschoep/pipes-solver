import sys
from scrape import getGameBoard
from validate import validate

board = getGameBoard(sys.argv[1] if len(sys.argv) >= 2 else 'https://www.puzzle-pipes.com/')

for node in board:
    print(node)

print("Should be false: ", validate(board))