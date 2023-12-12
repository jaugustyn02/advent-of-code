
input = 'data/puzzle.txt'
# input = 'data/sample.txt'


def replace_dict(string, dictionary):
    for i, j in dictionary.items():
        string = string.replace(i, j)
    return string


def main():
  with open(input) as f:
    lines = f.readlines()
    moves = lines[0].rstrip()
    navigation = {}
    for line in lines[2:]:
        src, left_dest, right_dest = replace_dict(line.rstrip(), {' ': '', '(':'', ')':'', '=':' ', ',':' '}).split()
        navigation[src] = (left_dest, right_dest)
        
    curr_pos = 'AAA'
    no_moves = 0
    while True:
        for move in moves:
            no_moves += 1
            if move == 'L':
                curr_pos = navigation[curr_pos][0]
            else:
                curr_pos = navigation[curr_pos][1]

            if curr_pos == 'ZZZ':
                print(no_moves)
                return    
    
if __name__ == "__main__":
  main()
