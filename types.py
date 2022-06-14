from enum import Enum, IntEnum

class PipeType(Enum):
    NUB = 0
    LBAR = 1
    LINE = 2
    TBAR = 3
    NONE = 4

class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

    def __add__(self, other: int):
        return Direction((self.value + other) % 4)
    
    def __sub__(self, other: int):
        return Direction((self.value - other) % 4)



class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Pipe:
    def __init__(self, type: PipeType, direction: Direction, position=Position(1, 1), source=False, selectable=True):
        self.type = type
        self.direction = direction
        self.position = position
        self.source = source
        self.selectable = selectable
    
    def __str__(self) -> str:
        return f'[{"Source" if self.source else "Pipe"}: {self.type} {self.direction}]\n'

    def __repr__(self) -> str:
        return self.__str__()

    def rotateClockwise(self):
        self.direction += 1
    
    def rotateCounterclockwise(self):
        self.direction -= 1
    

    
if __name__ == "__main__":
    print('Running tests for types.py')
    pipe1 = Pipe(PipeType.NUB, Direction.Down)
    pipe1.rotateClockwise()
    assert(pipe1.direction == Direction.Left)
    pipe1.rotateClockwise()
    assert(pipe1.direction == Direction.Up)

    pipe2 = Pipe(PipeType.TBAR, Direction.Up)
    pipe2.rotateCounterclockwise()
    assert(Direction.Left == pipe2.direction)
    pipe2.rotateCounterclockwise()
    assert(Direction.Down == pipe2.direction)
    pipe2.rotateClockwise()
    assert(Direction.Left == pipe2.direction)
    print('Success!')
