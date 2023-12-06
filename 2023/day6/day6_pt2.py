
input = 'puzzle.txt'
# input = 'sample.txt'
from math import ceil

def main():
  with open(input) as f:
    lines = f.readlines()
    t = int("".join(lines[0].split(':')[1].split()))
    d = int("".join(lines[1].split(':')[1].split()))
    if t**2 > 4*d:
      x = (t - (t**2 - 4*d)**0.5) / 2.0
      n = t - 2*ceil(x) + 1
      if (x == int(x)): n -= 2
  print(n)

if __name__ == "__main__":
  main()
