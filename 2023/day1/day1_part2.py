digit_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                  'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def main():
    sum = 0
    with open('data/puzzle_input.txt') as f:
        for line in f:
            # Search for verbal digits
            left_digit_index = len(line)
            left_digit_value = None
            right_digit_index = -1
            right_digit_value = None
            for key, val in digit_dict.items():
                index = line.find(key)
                if index != -1 and index < left_digit_index:
                    left_digit_index = index
                    left_digit_value = val
                    
                index = line.rfind(key)
                if index != -1 and index > right_digit_index:
                    right_digit_index = index
                    right_digit_value = val
            
            # Search for numeric digit
            for i in range(len(line)):
                if line[i].isnumeric():
                    if i < left_digit_index:
                        left_digit_value = ord(line[i])-ord('0')
                    break
                
            for i in range(len(line)-1, -1, -1):
                if line[i].isnumeric():
                    if i > right_digit_index:
                        right_digit_value = ord(line[i])-ord('0')
                    break
            sum += 10*left_digit_value + right_digit_value
    print(sum)


if __name__ == '__main__':
    main()
