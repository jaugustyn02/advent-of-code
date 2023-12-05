# input = 'data/sample.txt'
input = 'data/puzzle.txt'


def main():
    with open(input) as f:
        lines = f.readlines()
        seeds = list(map(int, lines[0].split(': ')[1].split()))
        seed_was_mapped: list[bool] = [False] * len(seeds)
        for line in lines[2:]:
            if line == '\n':
                continue
            if not line[0].isnumeric():
                for i in range(len(seeds)):
                    seed_was_mapped[i] = False
                continue
            
            dest_range, src_range, range_len = map(int, line.split())
            for i, seed in enumerate(seeds):
                if not seed_was_mapped[i] and src_range <= seed < src_range + range_len:
                    seeds[i] = seed - src_range + dest_range
                    seed_was_mapped[i] = True
            
        print(min(seeds))
        
        
if __name__ == '__main__':
    main()