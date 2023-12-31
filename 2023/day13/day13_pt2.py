# input = 'sample.txt'
input = 'puzzle.txt'


def map_to_decimal(string: str):
  dec_num = 0
  for char in string:
    dec_num *= 2
    dec_num += 1 if char == '#' else 0
  return dec_num
  

from math import log2

def find_reflection(nums):
  n = len(nums)
  mid = 1
  for i in range(1, n, 2):
    rev_nums = nums[i:mid-1:-1]
    diff = [(nums[j], rev_nums[j]) for j in range(mid) if nums[j] != rev_nums[j]]
    if len(diff) == 1:
      xor = diff[0][0] ^ diff[0][1]
      if log2(xor)%1 == 0:
        return mid
    mid += 1
  
  mid = n-1
  for i in range(n-2, -1, -2):
    rev_nums = nums[n:mid-1:-1]
    diff = [(nums[j+i], rev_nums[j]) for j in range(n-mid) if nums[j+i] != rev_nums[j]]
    if len(diff) == 1:
      xor = diff[0][0] ^ diff[0][1]
      if log2(xor)%1 == 0:
        return mid
    mid -= 1

  return 0

def main():
  with open(input) as f:
    content = f.read()
  
  patterns = content.split('\n\n')
  
  res_sum = 0
  
  for pattern in patterns:
    rows = pattern.split('\n')
    nrows = len(rows)
    rows_num = [0 for _ in range(nrows)]
    for i, row in enumerate(rows):
      rows_num[i] = map_to_decimal(row)
    res_sum += find_reflection(rows_num)*100
  
    cols = [list(x) for x in zip(*rows)]
    ncols = len(cols)
    cols_num= [0 for _ in range(ncols)]
    for i, col in enumerate(cols):
      cols_num[i] = map_to_decimal(col)
    res_sum += find_reflection(cols_num)

  print(res_sum)
if __name__ == "__main__":
  main()
