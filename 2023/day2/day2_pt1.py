

def main():
    sum = 0
    cube_color_num = {'red': 12, 'green': 13, 'blue': 14}
    with open('data/puzzle_input.txt') as file:
        for game_index, set in enumerate(file):
            possible = True
            sets = set.strip().split(': ')[1].split('; ')
            for set in sets:
                for cube in set.split(', '):
                    num, color = cube.split(' ')
                    if int(num) > cube_color_num[color]:
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                sum += game_index + 1
    print(sum)

if __name__ == '__main__':
    main()