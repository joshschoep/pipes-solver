from math import floor, sqrt
import sys
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from ..types import Direction, Pipe, PipeType

session = HTMLSession()

def get_all_cell_classes(tag):
    return tag.has_attr('class') and 'cell' in tag['class']

makePipe = lambda cellInfo, pos : Pipe(cellInfo[0], cellInfo[1], position=pos)
makeSource = lambda cellInfo, pos : Pipe(cellInfo[0], cellInfo[1], position=pos, source=True)

# All angled and multi-angled pieces are denoted starting from the most counter-clockwise
# open end
cellTypeMap = {
    "pipe0": (PipeType.NONE, Direction.Up),
    "pipe1": (PipeType.NUB, Direction.Right),
    "pipe2": (PipeType.NUB, Direction.Up),
    "pipe3": (PipeType.LBAR, Direction.Up),
    "pipe4": (PipeType.NUB, Direction.Left),

    "pipe5": (PipeType.LINE, Direction.Left),
    "pipe6": (PipeType.LBAR, Direction.Left),
    "pipe7": (PipeType.TBAR, Direction.Left),
    "pipe8": (PipeType.NUB, Direction.Down),

    "pipe9": (PipeType.LBAR, Direction.Right),
    "pipe10": (PipeType.LINE, Direction.Up),
    "pipe11": (PipeType.TBAR, Direction.Up),
    "pipe12": (PipeType.LBAR, Direction.Down),

    "pipe13": (PipeType.TBAR, Direction.Right),
    "pipe14": (PipeType.TBAR, Direction.Down),
}

def getGameBoard(url='https://www.puzzle-pipes.com/') -> list[Pipe]:
    response = session.get(url)
    response.html.render()

    puzzleCells = BeautifulSoup(response.html.find('#game', first=True).html, 'lxml')
    cellClassList = [cell['class'] for cell in puzzleCells.find_all(get_all_cell_classes)]
    rows = cols = int(sqrt(len(cellClassList)))

    cellList = [makeSource(cellTypeMap[classes[2]], (en % cols, floor(en / rows))) if 'source' in classes else makePipe(cellTypeMap[classes[2]], (en % cols, floor(en / rows))) for en, classes in enumerate(cellClassList)]

    return cellList

if __name__ == "__main__":
    for pipe in getGameBoard(sys.argv[1] if len(sys.argv) >= 2 else None):
        print(pipe)