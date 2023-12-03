

def main():
    sum = 0
    with open('data/puzzle_input.txt') as file:
        for game_index, set in enumerate(file):
            sets = set.strip().split(': ')[1].split('; ')
            cube_color_max_num = {'red': 0, 'green': 0, 'blue': 0} 
            for set in sets:
                for cube in set.split(', '):
                    num, color = cube.split(' ')
                    if int(num) > cube_color_max_num[color]:
                        cube_color_max_num[color] = int(num)
            mul = 1
            for val in cube_color_max_num.values():
                mul *= val
            sum += mul
    print(sum)

if __name__ == '__main__':
    main()