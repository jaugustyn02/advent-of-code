

def main():
    sum = 0
    with open('data/puzzle_input.txt') as f:
        for line in f:
            for c in line:
                if c.isnumeric():
                    digit1 = ord(c)-ord('0')
                    break
            for i in range(len(line)-1, -1, -1):
                if line[i].isnumeric():
                    sum += 10*digit1 + ord(line[i])-ord('0')
                    break
    print(sum)


if __name__ == '__main__':
    main()
