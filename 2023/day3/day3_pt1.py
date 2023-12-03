from collections import defaultdict

input = 'data/puzzle.txt'
# input = 'data/sample.txt'

def main():
    adjecent_to_symbol = defaultdict(bool)
    sum = 0
    with open(input) as f:
        for row, line in enumerate(f):
            for col, c in enumerate(line.rstrip()):
                if not c.isnumeric() and c != '.':
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            adjecent_to_symbol[(row+i, col+j)] = True
                            
    with open(input) as f:
        for row, line in enumerate(f):
            num = 0
            is_adjecent = False
            for col, c in enumerate(line.rstrip()):
                if c.isnumeric():
                    num *= 10
                    num += ord(c) - ord('0')
                    if adjecent_to_symbol[(row, col)]:
                        is_adjecent = True
                else:
                    if is_adjecent:
                        sum += num
                    num = 0
                    is_adjecent = False
            if is_adjecent:
                sum += num
    print(sum)

if __name__ == '__main__':
    main()