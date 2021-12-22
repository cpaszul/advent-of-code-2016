DEFAULT_INPUT = 'day20.txt'

def day_20(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        ranges = [tuple(map(int, line.split('-'))) for line in f.readlines()]
    ranges.sort(key=lambda t:t[0])
    i = 0
    while i < len(ranges) - 1:
        current = ranges[i]
        next_range = ranges[i + 1]
        if next_range[0] <= (current[1] + 1):
            ranges[i] = (current[0], max(current[1], next_range[1]))
            ranges.pop(i + 1)
        else:
            i += 1
    smallest_valid = ranges[0][1] + 1
    total_valid = 0
    for a, b in zip(ranges, ranges[1:]):
        total_valid += b[0] - a[1] - 1
    return smallest_valid, total_valid
    
if __name__ == '__main__':
    part_1, part_2 = day_20()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
