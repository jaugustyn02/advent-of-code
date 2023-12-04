# input = 'data/sample.txt'
input = 'data/puzzle.txt'

def main():
  result_sum = 0
  with open(input) as f:
    for line in f:
      count = -1
      winning, mine = line[:-1].split(':')[1].split('|')
      winning_set = set([int(num) for num in ' '.join(winning.split()).split()])
      mine = [int(num) for num in ' '.join(mine.split()).split()]
      for num in mine:
        if(num in winning_set):
          count += 1
      result_sum += 2**count if count > -1 else 0
  print(result_sum)
  
if __name__ == "__main__":
  main()
