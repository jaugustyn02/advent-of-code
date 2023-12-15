# input = 'data/sample.txt'
input = 'data/puzzle.txt'

springs, damaged_groups = None, None
memo = {}


def permutations_num(spring_i, group_id, damaged_len, spring_sub=None):
    if (spring_i, group_id, damaged_len, spring_sub) in memo:
        return memo[(spring_i, group_id, damaged_len, spring_sub)]

    if spring_i == len(springs):
        if group_id == len(damaged_groups):
            return 1
        if group_id == len(damaged_groups) - 1 and damaged_groups[group_id] == damaged_len:
            return 1
        return 0

    spring = springs[spring_i] if spring_sub is None else spring_sub

    if spring == '.':
        if damaged_len == 0:
            res = permutations_num(spring_i + 1, group_id, 0)
            memo[(spring_i, group_id, damaged_len, spring_sub)] = res
            return res
        if damaged_len != damaged_groups[group_id]:
            return 0
        res = permutations_num(spring_i + 1, group_id + 1, 0)
        memo[(spring_i, group_id, damaged_len, spring_sub)] = res
        return res
    if spring == '#':
        if group_id == len(damaged_groups):
            return 0
        if damaged_groups[group_id] == damaged_len:
            return 0
        res = permutations_num(spring_i + 1, group_id, damaged_len + 1)
        memo[(spring_i, group_id, damaged_len, spring_sub)] = res
        return res

    res = permutations_num(spring_i, group_id, damaged_len, '.') \
           + permutations_num(spring_i, group_id, damaged_len, '#')
    memo[(spring_i, group_id, damaged_len, spring_sub)] = res
    return res


def main():
    global springs, damaged_groups, memo
    with open(input, 'r') as f:
        lines = f.readlines()

    res_sum = 0
    for i, line in enumerate(lines):
        memo = {}
        springs, damaged_groups = line.rstrip().split()
        damaged_groups = list(map(int, damaged_groups.split(',')))

        num_of_copies = 5
        springs = '?'.join([springs]*num_of_copies)
        damaged_groups = damaged_groups*num_of_copies

        res_sum += permutations_num(0, 0, 0)
    print(res_sum)


if __name__ == '__main__':
    main()
