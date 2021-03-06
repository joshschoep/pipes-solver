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
    
    def __str__(self):
        return f'({self.x:02}, {self.y:02})'
    
    def __repr__(self):
        return self.__str__()

class Pipe:
    def __init__(self, type: PipeType, direction: Direction, position=Position(1, 1), source=False, selectable=True):
        self.type = type
        self.direction = direction
        self.position = position
        self.source = source
        self.selectable = selectable
        self.validated = False
    
    def __repr__(self) -> str:
        return f'[{"Source" if self.source else "Pipe"}: {self.position} {self.type} {self.direction}]'

    def __str__(self) -> str:
        return f'[ {"Source:" if self.source else "Pipe:  "}\t{self.position}\t{self.type}\t{self.direction}\t]'

    def rotateClockwise(self):
        self.direction += 1
    
    def rotateCounterclockwise(self):
        self.direction -= 1
    
    def getOpenDirections(self) -> list[Direction]:
        if self.type == PipeType.NUB:
            return [self.direction]
        elif self.type == PipeType.LINE:
            return [self.direction, self.direction + 2]
        elif self.type == PipeType.LBAR:
            return [self.direction, self.direction + 1]
        elif self.type == PipeType.TBAR:
            return [self.direction, self.direction + 1, self.direction + 2]
    

    
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
