input = 'sample.txt'
# input = 'puzzle.txt'


def map_to_decimal(string: str):
  dec_num = 0
  for char in string:
    dec_num *= 2
    dec_num += 1 if char == '#' else 0
  return dec_num
  

def find_reflection(nums):
  n = len(nums)
  mid = 1
  for i in range(1, n, 2):
    rev_nums = nums[i:mid-1:-1]
    # print(nums[0:mid], nums[i:mid-1:-1])
    diff = [(nums[j], nums[j]) for j in range(mid)]
    print(diff)
    if nums[0:mid] == nums[i:mid-1:-1]:
      return mid
    mid += 1
  
  mid = n-1
  for i in range(n-2, -1, -2):
    if nums[i:mid] == nums[n:mid-1:-1]:
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
    # print(rows_num)
    res_sum += find_reflection(rows_num)*100
  
    cols = [list(x) for x in zip(*rows)]
    ncols = len(cols)
    cols_num= [0 for _ in range(ncols)]
    for i, col in enumerate(cols):
      cols_num[i] = map_to_decimal(col)
    # print(cols_num)
    res_sum += find_reflection(cols_num)
  # print(patterns)
  print(res_sum)
if __name__ == "__main__":
  main()
