input = 'data/sample.txt'
input = 'data/puzzle.txt'

def main():
    with open(input) as f:
        line = f.readlines()[0].rstrip()
    strings = line.split(',')
    
    res_sum = 0
    for s in strings:
        val = 0
        for c in s:
            val = (val + ord(c))*17%256
        res_sum+=val
    print(res_sum)  
    
    
if __name__ == "__main__":
    main()