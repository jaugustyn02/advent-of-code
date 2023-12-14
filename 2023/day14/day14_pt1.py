import numpy as np

# input = 'sample.txt'
input = 'puzzle.txt'


def main():
  with open(input) as f:
    rows = f.readlines()
    nrows = len(rows)
    ncols = len(rows[0].rstrip())
    
    # stones count on each row
    R = [0 for _ in range(nrows)]
    # first highest empty space in column
    T = [0 for _ in range(ncols)]
    
    for i in range(nrows):
      for j in range(ncols):
        char = rows[i][j]
        if char == '#':
          T[j] = i+1
        elif char == 'O':
          R[T[j]] += 1
          T[j] += 1
          
    print(sum([(nrows-i)*R[i] for i in range(nrows)]))
  
if __name__ == "__main__":
  main()
