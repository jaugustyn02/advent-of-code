# input = 'data/sample.txt'
input = 'data/puzzle.txt'


springs, damaged_groups = None, None


def permutations_num(spring_i, group_id, damaged_len, spring_sub = None):
    if spring_i == len(springs):
        if group_id == len(damaged_groups):
            return 1
        if group_id == len(damaged_groups) - 1 and damaged_groups[group_id] == damaged_len:
            return 1
        return 0

    spring = springs[spring_i] if spring_sub is None else spring_sub

    if spring == '.':
        if damaged_len == 0:
            return permutations_num(spring_i + 1, group_id, 0)
        if damaged_len != damaged_groups[group_id]:
            return 0
        return permutations_num(spring_i + 1, group_id + 1, 0)
    if spring == '#':
        if group_id == len(damaged_groups):
            return 0
        if damaged_groups[group_id] == damaged_len:
            return 0
        return permutations_num(spring_i + 1, group_id, damaged_len + 1)

    return permutations_num(spring_i, group_id, damaged_len, '.')\
        + permutations_num(spring_i, group_id, damaged_len, '#')


def main():
    global springs, damaged_groups
    with open(input, 'r') as f:
        lines = f.readlines()

    res_sum = 0
    for i, line in enumerate(lines):
        springs, damaged_groups = line.rstrip().split()
        damaged_groups = list(map(int, damaged_groups.split(',')))

        res_sum += permutations_num(0, 0, 0)
    print(res_sum)
    
if __name__ == '__main__':
    main()
