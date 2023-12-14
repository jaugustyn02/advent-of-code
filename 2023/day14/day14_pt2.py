import numpy as np

input = 'sample.txt'
# input = 'puzzle.txt'


def rotate_matrix( m ):
  return [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]


def main():
  with open(input) as f:
    rows = f.readlines()
    rows = [[c for c in r.rstrip()] for r in rows]
    
    for _ in range(10):
      for cycle in range(4):
        for r in rows:
          print(r)
        print()
        
        nrows = len(rows)
        ncols = len(rows[0])
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
              rows[T[j]][j] = 'O'
              rows[i][j] = '.'
              T[j] += 1
              
        rows = rotate_matrix(rows)
          
    # print(R)
    # print([(nrows-i)*R[i] for i in range(nrows)])
    print(sum([(nrows-i)*R[i] for i in range(nrows)]))
  
if __name__ == "__main__":
  main()
