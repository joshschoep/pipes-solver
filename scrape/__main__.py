import sys
from scrape.scrape import getGameBoard

print(getGameBoard(sys.argv[1] if len(sys.argv) >= 2 else None))