from collections import defaultdict

input = 'data/puzzle.txt'
# input = 'data/sample.txt'

def main():
    adjecent_to_gear = defaultdict(list)
    sum = 0
    gear_id = 0
    with open(input) as f:
        for row, line in enumerate(f):
            for col, c in enumerate(line.rstrip()):
                if c == '*':
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            adjecent_to_gear[(row+i, col+j)].append(gear_id)
                    gear_id += 1
                    
    gear_adjecent_nums = [[] for _ in range(gear_id)]
    with open(input) as f:
        for row, line in enumerate(f):
            num = 0
            is_adjecent_to = set()
            for col, c in enumerate(line.rstrip()):
                if c.isnumeric():
                    num *= 10
                    num += ord(c) - ord('0')
                    
                    for gear_id in adjecent_to_gear[(row, col)]:
                        if gear_id not in is_adjecent_to:
                            is_adjecent_to.add(gear_id)
                else:
                    for gear_id in is_adjecent_to:
                        gear_adjecent_nums[gear_id].append(num)
                        
                    num = 0
                    is_adjecent_to = set()
                    
            for gear_id in is_adjecent_to:
                gear_adjecent_nums[gear_id].append(num)
                
    for nums in gear_adjecent_nums:
        if len(nums) == 2:
            sum += nums[0] * nums[1]
    print(sum)

if __name__ == '__main__':
    main()