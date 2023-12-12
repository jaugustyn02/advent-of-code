from enum import Enum


input = 'data/puzzle.txt'
# input = 'data/sample.txt'


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    
    def to_vector(self):
        if self == Direction.UP:
            return (-1, 0)
        elif self == Direction.DOWN:
            return (1, 0)
        elif self == Direction.LEFT:
            return (0, -1)
        elif self == Direction.RIGHT:
            return (0, 1)
        else:
            raise ValueError("Invalid direction")
    
PipeDirections = {'|': {Direction.UP: Direction.UP, Direction.DOWN: Direction.DOWN},
                  '-': {Direction.LEFT: Direction.LEFT, Direction.RIGHT: Direction.RIGHT},
                  'L': {Direction.LEFT: Direction.UP, Direction.DOWN: Direction.RIGHT},
                  'J': {Direction.RIGHT: Direction.UP, Direction.DOWN: Direction.LEFT},
                  '7': {Direction.RIGHT: Direction.DOWN, Direction.UP: Direction.LEFT},
                  'F': {Direction.LEFT: Direction.DOWN, Direction.UP: Direction.RIGHT}
                  }



def find_first_direction(grid, start):
    x, y = start
    for direction in Direction:
        vec = direction.to_vector()
        pipe = grid[x + vec[0]][y + vec[1]]
        if pipe == '.':
            continue
        pipe_directions = PipeDirections[pipe]
        if direction in pipe_directions:
            return direction
    return None

def main():
    
    
    with open(input) as f:
        grid = f.readlines()
        start = None
        for x, line in enumerate(grid):
            for y, char in enumerate(line):
                if char == 'S':
                    start = (x, y)
                    break
            if start:
                break
        # print(start)
        direction = find_first_direction(grid, start)
        step_count = 1
        x, y = start
        x += direction.to_vector()[0]
        y += direction.to_vector()[1]
        
        while grid[x][y] != 'S':
            # print(grid[x][y])
            step_count += 1
            direction = PipeDirections[grid[x][y]][direction]
            x += direction.to_vector()[0]
            y += direction.to_vector()[1]
        
        print(step_count//2)
        
        
    
    
    
if __name__ == "__main__":
  main()
