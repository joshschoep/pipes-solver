import sys
from scrape import getGameBoard
from solve import solve
from validate import validate

board = getGameBoard(sys.argv[1] if len(sys.argv) >= 2 else 'https://www.puzzle-pipes.com/')

for node in board:
    print(node)

print("Should be false: ", validate(board))

solve(board)
for node in board:
    print(node)

print("Should be true: ", validate(board))