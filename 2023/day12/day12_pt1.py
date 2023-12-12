input = 'data/sample.txt'
# input = 'data/puzzle.txt'

# Sample input:
#   #.#.### 1,1,3
#   .#...#....###. 1,1,3
#   .#.###.#.###### 1,3,1,6
#   ####.#...#... 4,1,1
#   #....######..#####. 1,6,5
#   .###.##....# 3,2,1
    
def main():
    with open(input, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        springs, damaged_groups = line.rstrip().split()
        springs = ''.join(springs.replace('.', ' ')).split()
        
        damaged_groups = list(map(int, damaged_groups.split(',')))
        print(springs, damaged_groups)
    
    
if __name__ == '__main__':
    main()