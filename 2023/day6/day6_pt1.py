
input = 'puzzle.txt'
# input = 'sample.txt'
from math import ceil

def main():
  n_sum = 1
  with open(input) as f:
    lines = f.readlines()
    times = map(int, " ".join(lines[0].split(':')[1].split()).split())
    dists = map(int, " ".join(lines[1].split(':')[1].split()).split())
    for t, d in zip(times, dists):
      if t**2 > 4*d:
        x = (t - (t**2 - 4*d)**0.5) / 2.0
        n = t - 2*ceil(x) + 1
        if (x == int(x)): n -= 2
        n_sum *= n
  print(n_sum)

if __name__ == "__main__":
  main()
