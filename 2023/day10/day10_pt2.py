from enum import Enum

# input = 'data/puzzle.txt'
input = 'data/sample2.txt'


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
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
        
    def next_direction(self, clockwise=True):
        if clockwise:
            return Direction((self.value + 1) % len(Direction))
        else:
            return Direction((self.value - 1) % len(Direction))
        
    
PipeDirections = {'|': {Direction.UP: Direction.UP, Direction.DOWN: Direction.DOWN},
                  '-': {Direction.LEFT: Direction.LEFT, Direction.RIGHT: Direction.RIGHT},
                  'L': {Direction.LEFT: Direction.UP, Direction.DOWN: Direction.RIGHT},
                  'J': {Direction.RIGHT: Direction.UP, Direction.DOWN: Direction.LEFT},
                  '7': {Direction.RIGHT: Direction.DOWN, Direction.UP: Direction.LEFT},
                  'F': {Direction.LEFT: Direction.DOWN, Direction.UP: Direction.RIGHT}
                  }

all_direction_vectors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def find_initial_direction(grid, x, y):
    for direction in Direction:
        vec = direction.to_vector()
        tile = grid[x + vec[0]][y + vec[1]]
        if tile == '.':
            continue
        neighbour_pipe = tile
        if direction in PipeDirections[neighbour_pipe].keys():
            return direction
    return


def mark_as_inside(grid, grid2, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return
    if grid2[x][y] == 2 or grid2[x][y] == 1:
        return
    grid2[x][y] = 1
    for vec in all_direction_vectors:
        x2 = x + vec[0]
        y2 = y + vec[1]
        if x2 < 0 or x2 >= len(grid) or y2 < 0 or y2 >= len(grid[0]):
            continue
        if grid2[x2][y2] == 2 or grid2[x2][y2] == 1:
            continue
        
        mark_as_inside(grid, grid2, x2, y2)
    return


def main():
    with open(input) as f:
        grid = f.readlines()
        
    for i in range(len(grid)):
        grid[i] = grid[i].rstrip()
    
    # Find start
    start = None
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == 'S':
                start = (x, y)
                break
        if start:
            break


    # Find loop, mark it as 2, and define loop turning direction (clockwise or counter-clockwise)
    clockwise_turns_count = 0
    counter_clockwise_turns_count = 0
    
    x, y = start
    direction = find_initial_direction(grid, x, y)
    
    marked_grid = [[0 for _ in range(len(line.rstrip()))] for line in grid]
    marked_grid[x][y] = 2 # mark start as part of the loop
    
    x += direction.to_vector()[0]
    y += direction.to_vector()[1]
    while grid[x][y] != 'S':
        marked_grid[x][y] = 2
        new_direction = PipeDirections[grid[x][y]][direction]
        
        if new_direction == direction.next_direction(True):
            clockwise_turns_count += 1
        elif new_direction == direction.next_direction(False):
            counter_clockwise_turns_count += 1
        
        direction = new_direction
        x += direction.to_vector()[0]
        y += direction.to_vector()[1]
    
    loop_is_clockwise = clockwise_turns_count > counter_clockwise_turns_count


    # Mark inside of the loop as 1
    x, y = start
    direction = find_initial_direction(grid, x, y)
    
    # print(x, y, direction, loop_is_clockwise, direction.next_direction(loop_is_clockwise).to_vector())
    
    x += direction.to_vector()[0]
    y += direction.to_vector()[1]
    while grid[x][y] != 'S':
        vec = direction.next_direction(loop_is_clockwise).to_vector()
        mark_as_inside(grid, marked_grid, x+vec[0], y+vec[1])
        direction = PipeDirections[grid[x][y]][direction]
        x += direction.to_vector()[0]
        y += direction.to_vector()[1]
    vec = direction.next_direction(loop_is_clockwise).to_vector()
    mark_as_inside(grid, marked_grid, x+vec[0], y+vec[1])
    
    # for x, line in enumerate(marked_grid):
    #     for y, num in enumerate(line):
    #         if num == 0:
    #             char = ' '
    #         elif num == 1:
    #             char = '*'
    #         else:
    #             # char = 'X'
    #             char = grid[x][y]
    #         print(char, end='')
    #     print()
    
    
    # Count 1s (tiles inside of the loop)
    one_count = 0
    for line in marked_grid:
        for char in line:
            if char == 1:
                one_count += 1
    print(one_count)
    return
        
if __name__ == "__main__":
  main()
