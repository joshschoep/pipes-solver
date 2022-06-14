import sys
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from ..types import Direction, Pipe, PipeType

session = HTMLSession()

def get_all_cell_classes(tag):
    return tag.has_attr('class') and 'cell' in tag['class']

makePipe = lambda cellInfo : Pipe(cellInfo[0], cellInfo[1])
makeSource = lambda cellInfo : Pipe(cellInfo[0], cellInfo[1], source=True)

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
    response = session.get('https://www.puzzle-pipes.com/')
    response.html.render()

    puzzleCells = BeautifulSoup(response.html.find('#game', first=True).html, 'lxml')
    cellList = [makeSource(cellTypeMap[cell['class'][2]]) if "source" in cell['class'] else makePipe(cellTypeMap[cell['class'][2]]) for cell in puzzleCells.find_all(get_all_cell_classes)]
    return cellList

if __name__ == "__main__":
    print(getGameBoard(sys.argv[1] if len(sys.argv) >= 2 else None))