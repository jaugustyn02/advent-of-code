
input = 'data/puzzle.txt'
# input = 'data/sample_pt2.txt'


def replace_dict(string, dictionary):
    for i, j in dictionary.items():
        string = string.replace(i, j)
    return string


def NWD(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
  with open(input) as f:
    lines = f.readlines()
    moves = lines[0].rstrip()
    navigation = {}
    for line in lines[2:]:
        src, left_dest, right_dest = replace_dict(line.rstrip(), {' ': '', '(':'', ')':'', '=':' ', ',':' '}).split()
        navigation[src] = (left_dest, right_dest)
        
    
    src_positions = [src for src in navigation.keys() if src.endswith('A')]
    nww = 0
    for curr_pos in src_positions:
        no_moves = 0
        while not curr_pos.endswith('Z'):
            for move in moves:
                no_moves += 1
                if move == 'L':
                    curr_pos = navigation[curr_pos][0]
                else:
                    curr_pos = navigation[curr_pos][1]
                
                if curr_pos.endswith('Z'):
                    break
                
        nww = nww * no_moves // NWD(nww, no_moves) if nww != 0 else no_moves
    
    print(nww)
                    
    
    
if __name__ == "__main__":
  main()
