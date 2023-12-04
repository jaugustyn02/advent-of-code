
from collections import defaultdict

# input = 'data/sample.txt'
input = 'data/puzzle.txt'

def main():
  card_instances = defaultdict(int)
  with open(input) as f:
    lines = f.readlines()
    for card_index, line in enumerate(lines):
      winning, mine = line[:-1].split(':')[1].split('|')
      winning_set = set([int(num) for num in ' '.join(winning.split()).split()])
      mine = [int(num) for num in ' '.join(mine.split()).split()]
      
      win_count = 0
      for num in mine:
        if(num in winning_set):
          win_count += 1
          
      card_instances[card_index] += 1
      instances = card_instances[card_index]
      for following_card_index in range(card_index + 1, min(card_index + win_count + 1, len(lines))):
        # print(f"card {card_index+1} wins {instances} copies of card {following_card_index+1}")
        card_instances[following_card_index] += instances
  # print(card_instances.items())
  print(sum(card_instances.values()))


if __name__ == "__main__":
  main()
