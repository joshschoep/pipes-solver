from math import sqrt
from int_types import Direction, Pipe, PipeType
from validate import getNodeInDirection

def nodeIsOnEdgeOrCorner(node: Pipe, rows: int):
    return node.position.x == 0 or node.position.x == rows-1 or node.position.y == 0 or node.position.y == rows-1

def recurseValidation(board: list[Pipe], node: Pipe, rows: int, nfrom: Pipe, dfrom: Direction):
    if not dfrom or nfrom:
        for direction in node.getOpenDirections():
            newNode = getNodeInDirection(board, node, direction)
            if newNode.valid:
                continue
            recurseValidation(board, newNode, rows, node, direction + 2)
    
    if node.type == PipeType.LINE or node.type == PipeType.NUB:
        while(node.direction != dfrom):
            node.rotateClockwise()
        node.valid = True
        if(node.type == PipeType.LINE):
            newNode = getNodeInDirection(board, node, node.direction + 2)
            if not newNode.valid:
                recurseValidation(board, newNode, rows, node, node.direction + 4)
        


def turnLInCorner(board, node: Pipe, rows, corner: Direction):
    while node.direction != corner:
        node.rotateClockwise()
    node.valid = True
    recurseValidation(board, node, rows, None, None)

def turnSideTsAndIs(board: list[Pipe], node: Pipe, rows: int):
    direction = Direction.Down
    if node.position.x == 0:
        direction = Direction.Right
    elif node.position.x == rows-1:
        direction = Direction.Left
    elif node.position.y == rows-1:
        direction = Direction.Up
    
    while node.direction != direction - 1:
        node.rotateClockwise()
    node.valid = True
    # recurseValidation(board, node, rows, None, None)

def solve(board: list[Pipe]):
    rows = int(sqrt(len(board)))
    #start with corners and edges
    if(board[0].type == PipeType.LBAR):
        turnLInCorner(board, board[0], rows, Direction.Right)
    if(board[rows-1].type == PipeType.LBAR):
        turnLInCorner(board, board[rows-1], rows, Direction.Down)
    if(board[rows*rows-rows].type == PipeType.LBAR):
        turnLInCorner(board, board[rows*rows-rows], rows, Direction.Up)
    if(board[rows*rows-1].type == PipeType.LBAR):
        turnLInCorner(board, board[rows*rows-1], rows, Direction.Left)
    
    for en, node in enumerate(board):
        if(en == 0 or en == rows-1 or en == rows*rows-rows or en == rows*rows-1):
            continue
        
        if(nodeIsOnEdgeOrCorner(node, rows) and (node.type == PipeType.LINE or node.type == PipeType.TBAR)):
            turnSideTsAndIs(board, node, rows)
    



