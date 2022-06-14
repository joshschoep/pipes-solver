import sys
from scrape import getGameBoard

for pipe in getGameBoard(sys.argv[1] if len(sys.argv) >= 2 else 'https://www.puzzle-pipes.com/'):
    print(pipe)