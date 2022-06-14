from math import sqrt
from tokenize import Pointfloat
from int_types import Direction, Pipe, PipeType, Position

def validate(board: list[Pipe]):
    source = None
    for pipe in board:
        pipe.validated = False
        if pipe.source:
            pipe.validated = True
            source = pipe
    if not source:
        return False
    
    return validateNodeRecursive(board, source)

def getNodeInDirection(board: list[Pipe], node: Pipe, direction: Direction):
    rows = int(sqrt(len(board)))
    if direction == Direction.Up:
        return board[(node.position.y - 1) * rows + node.position.x]
    elif direction == Direction.Right:
        return board[node.position.y * rows + node.position.x + 1]
    elif direction == Direction.Down:
        return board[(node.position.y + 1) * rows + node.position.x]
    elif direction == Direction.Left:
        return board[node.position.y * rows + node.position.x - 1]

def validateNodeRecursive(board: list[Pipe], node: Pipe):
    directions = node.getOpenDirections()
    node.validated = True
    print(f'Checking node {node} in directions {directions}')
    
    for direction in directions:
        try:
            newNode = getNodeInDirection(board, node, direction)
        except:
            print(f'Node in direction {direction} threw error')
            return False
        
        if not (direction + 2) in newNode.getOpenDirections():
            print(f'Node in direction {direction} was not connected to new node {node} with directions {newNode.getOpenDirections()}')
            return False
        
        if newNode.validated:
            print(f'Node in direction {direction} was already validated')
            continue
        
        if not validateNodeRecursive(board, newNode):
            print(f'Node recursion failed')
            return False
    print(f'All nodes for {node} succeeded')
    return True

if __name__ == "__main__":
    board = [
        Pipe(PipeType.NUB, Direction.Down, Position(0, 0)),
        Pipe(PipeType.NUB, Direction.Down, Position(1, 0)),
        Pipe(PipeType.LBAR, Direction.Up, Position(0, 1)),
        Pipe(PipeType.LBAR, Direction.Left, Position(1, 1), source=True)
    ]
    print(validate(board))