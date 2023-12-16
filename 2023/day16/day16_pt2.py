from enum import Enum
from collections import deque

# input = 'data/sample.txt'
input = 'data/puzzle.txt'


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def to_vector(self):
        if self == Direction.UP:
            return (-1, 0)
        elif self == Direction.RIGHT:
            return (0, 1)
        elif self == Direction.DOWN:
            return (1, 0)
        elif self == Direction.LEFT:
            return (0, -1)
    
    def turn_left(self):
        return Direction((self.value - 1) % 4)
    
    def turn_right(self):
        return Direction((self.value + 1) % 4)

beam_mirrors = {
    '/': {
        Direction.UP: Direction.RIGHT,
        Direction.RIGHT: Direction.UP,
        Direction.DOWN: Direction.LEFT,
        Direction.LEFT: Direction.DOWN
    },
    '\\': {
        Direction.UP: Direction.LEFT,
        Direction.RIGHT: Direction.DOWN,
        Direction.DOWN: Direction.RIGHT,
        Direction.LEFT: Direction.UP
    }
}

beam_splitters = {
    '|': {
        Direction.UP: (Direction.UP,),
        Direction.RIGHT: (Direction.UP, Direction.DOWN),
        Direction.DOWN: (Direction.DOWN,),
        Direction.LEFT: (Direction.DOWN, Direction.UP)
    },
    '-': {
        Direction.UP: (Direction.LEFT, Direction.RIGHT),
        Direction.RIGHT: (Direction.RIGHT,),
        Direction.DOWN: (Direction.RIGHT, Direction.LEFT),
        Direction.LEFT: (Direction.LEFT,)
    }
}

class Beam:
    def __init__(self, i, j, direction):
        self.i = i
        self.j = j
        self.direction = direction
        
    def move(self):
        vector = self.direction.to_vector()
        self.i += vector[0]
        self.j += vector[1]

def main():
    with open(input) as f:
        lines = f.readlines()
    
    contraption = [line.strip() for line in lines]
    n = len(contraption)
    m = len(contraption[0])
    beams_grid = [[[False for _ in Direction] for _ in range(m)] for _ in range(n)]
    
    starting_beams = []
    for i in range(n):
        starting_beams.append(Beam(i, 0, Direction.RIGHT))
        starting_beams.append(Beam(i, m - 1, Direction.LEFT))
    for j in range(m):
        starting_beams.append(Beam(0, j, Direction.DOWN))
        starting_beams.append(Beam(n - 1, j, Direction.UP))
    
    max_num_of_energized_tiles = 0
    for beam in starting_beams:
        beams_grid = [[[False for _ in Direction] for _ in range(m)] for _ in range(n)]
        beams_to_check = deque()
        beams_to_check.append(beam)
        while len(beams_to_check) > 0:
            beam = beams_to_check.popleft()
            if beam.i < 0 or beam.i >= n or beam.j < 0 or beam.j >= m:
                continue
            if beams_grid[beam.i][beam.j][beam.direction.value]:
                continue
            
            beams_grid[beam.i][beam.j][beam.direction.value] = True
            
            if contraption[beam.i][beam.j] in beam_splitters:
                for direction in beam_splitters[contraption[beam.i][beam.j]][beam.direction]:
                    new_beam = Beam(beam.i, beam.j, direction)
                    new_beam.move()
                    beams_to_check.append(new_beam)
            else:
                if contraption[beam.i][beam.j] in beam_mirrors:
                    beam.direction = beam_mirrors[contraption[beam.i][beam.j]][beam.direction]
                beam.move()
                beams_to_check.append(beam)
            
        energized_tiles = 0
        for row in beams_grid:
            for tile in row:
                if any(tile):
                    energized_tiles += 1
        max_num_of_energized_tiles = max(max_num_of_energized_tiles, energized_tiles)
        
    print(max_num_of_energized_tiles)
    
    
if __name__ == '__main__':
    main()