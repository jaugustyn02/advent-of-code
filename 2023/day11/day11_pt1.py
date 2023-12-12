import numpy as np

# input = 'sample.txt'
input = 'puzzle.txt'


def calc_distance(g1, g2):
  return abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])


def main():
  with open(input) as f:
    lines = f.readlines()
    
  space_grid = [[0 if char == '.' else 1 for char in row.rstrip()] for row in lines]
  
  nrows = len(space_grid)
  ncols = len(space_grid[0])

  expanded_rows = [1-min(sum(row), 1) for row in space_grid]
  expanded_cols = [1-min(sum([space_grid[j][i] for j in range(nrows)]), 1) for i in range(ncols)]
  
  fixed_rows = [0 for i in range(nrows)]
  fixed_cols = [0 for i in range(ncols)]
  
  for i in range(1, nrows):
    fixed_rows[i] = expanded_rows[i-1] + fixed_rows[i-1] + 1
  for i in range(1, ncols):
    fixed_cols[i] = expanded_cols[i-1] + fixed_cols[i-1] + 1
    
  
  galaxies = []
  for i, row in enumerate(space_grid):
    for j, char in enumerate(row):
      if space_grid[i][j] == 1:
        galaxies.append((fixed_rows[i], fixed_cols[j]))
  
  
  ngalaxies = len(galaxies)
  dist_sum = 0
  for i in range(ngalaxies):
    for j in range(i+1, ngalaxies):
      dist_sum += calc_distance(galaxies[i], galaxies[j])
  
  print(dist_sum)
if __name__ == "__main__":
  main()
