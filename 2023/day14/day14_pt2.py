from itertools import count

input = 'data/sample.txt'
input = 'data/puzzle.txt'


def rotate_matrix( m ):
  return [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]

def print_matrix( m ):
  for r in m:
    print(''.join(r))
  print()

def main():
  with open(input) as f:
    rows = f.readlines()
    
  rows = [[c for c in r.rstrip()] for r in rows]
  rows_set = dict()
  
  wanted_cycle = 1000000000
  end_on_cycle = -1
  for curr_cycle in count(0):
    if curr_cycle == end_on_cycle:
      break
    
    for direction in range(4):
      nrows = len(rows)
      ncols = len(rows[0])
      
      # first highest empty space in column
      T = [0 for _ in range(ncols)]
      
      for i in range(nrows):
        for j in range(ncols):
          char = rows[i][j]
          if char == '#':
            T[j] = i+1
          elif char == 'O':
            # R[T[j]] += 1
            rows[i][j] = '.'
            rows[T[j]][j] = 'O'
            T[j] += 1
       
      rows = rotate_matrix(rows)
    
    if end_on_cycle == -1:
      str_cyc = ''.join([''.join(r) for r in rows])
      if str_cyc in rows_set:
        cycle_start = rows_set[str_cyc]
        cycle_len = curr_cycle - cycle_start
        end_on_cycle = (wanted_cycle - cycle_start) % cycle_len + curr_cycle
      else:
        rows_set[str_cyc] = curr_cycle  
    
  # stones count on each row
  R = [0 for _ in range(nrows)]
  for i in range(nrows):
    for j in range(ncols):
      if rows[i][j] == 'O':
        R[i] += 1
  load = sum([(nrows-i)*R[i] for i in range(nrows)])
  print(load)
    
  
if __name__ == "__main__":
  main()
