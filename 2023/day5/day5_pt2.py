# input = 'data/sample.txt'
input = 'data/puzzle.txt'


def main():
    with open(input) as f:
        lines = f.readlines()
        nums = list(map(int, lines[0].split(': ')[1].split()))
        seed_ranges = [[nums[i], nums[i] + nums[i+1], False] for i in range(0, len(nums), 2)]
        for line in lines[1:]:
            if line == '\n':
                continue
            if not line[0].isnumeric():
                for i in range(len(seed_ranges)):
                    seed_ranges[i][2] = False
                continue
            
            dest_start, src_start, range_len = map(int, line.split())
            dest_end = dest_start + range_len
            src_end = src_start + range_len
            starts_diff = dest_start - src_start
            for i, value in enumerate(seed_ranges):
                seed_start, seed_end, was_mapped = value
                if was_mapped:
                    continue
                if seed_start < src_start < seed_end:
                    seed_ranges[i][0] = dest_start
                    seed_ranges.append([seed_start, src_start, False])
                elif src_start <= seed_start < src_end:
                    seed_ranges[i][0] = seed_start + starts_diff
                if seed_start < src_end < seed_end:
                    seed_ranges[i][1] = dest_end
                    seed_ranges[i][2] = True
                    seed_ranges.append([src_end, seed_end, False])
                elif src_start < seed_end <= src_end:
                    seed_ranges[i][1] = seed_end + starts_diff
                    seed_ranges[i][2] = True

        print(min(seed_ranges, key=lambda x: x[0])[0])
        
        
if __name__ == '__main__':
    main()