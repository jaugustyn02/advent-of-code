input = 'data/sample.txt'
# input = 'data/puzzle.txt'


def main():
    with open(input) as f:
        lines = f.readlines()
        nums = list(map(int, lines[0].split(': ')[1].split()))
        seed_ranges = [[nums[i], nums[i] + nums[i+1], False] for i in range(0, len(nums), 2)]
        print(seed_ranges)
        for line in lines[2:]:
            if line == '\n':
                # print(seed_ranges)
                continue
            if not line[0].isnumeric():
                for i in range(len(seed_ranges)):
                    seed_ranges[i][2] = False
                continue
            
            dest_start, map_start, range_len = map(int, line.split())
            dest_end = dest_start + range_len
            map_end = map_start + range_len
            starts_diff = dest_start - map_start
            for i, value in enumerate(seed_ranges):
                src_start, src_end, was_mapped = value
                # print(src_start, src_end, was_mapped)
                if was_mapped:
                    continue
                if map_start <= src_start < map_end:
                    seed_ranges[i][0] = dest_start
                    seed_ranges[i][2] = True
                    if map_end < src_end:
                        seed_ranges[i][1] = map_end + starts_diff
                        seed_ranges.append([map_end, src_end, False])
                    else:
                        seed_ranges[i][1] = dest_end
                elif map_start < src_end <= map_end:
                    seed_ranges[i][1] = dest_end
                    seed_ranges[i][2] = True
                    if src_start < map_start:
                        seed_ranges[i][0] = map_start + starts_diff
                        seed_ranges.append([src_start, map_start, False])
                    else:
                        seed_ranges[i][0] = dest_start
                # if not seed_was_mapped[i] and src_range <= seed < src_range + range_len:
                    # seeds[i] = seed - src_range + dest_range
                    # seed_was_mapped[i] = True
            
            
        print(min(seed_ranges, key=lambda x: x[0]))
        
        
if __name__ == '__main__':
    main()