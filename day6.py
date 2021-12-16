from collections import Counter

DEFAULT_INPUT = 'day6.txt'

def day_6(loc: str = DEFAULT_INPUT) -> tuple[str, str]:
    counters = [Counter() for _ in range(8)]
    with open(loc) as f:
        for line in f.readlines():
            for i, ch in enumerate(line.rstrip()):
                counters[i][ch] += 1
    part_1_res, part_2_res = '', ''
    for count in counters:
        part_1_res += count.most_common()[0][0]
        part_2_res += count.most_common()[-1][0]
    return part_1_res, part_2_res

if __name__ == '__main__':
    part_1, part_2 = day_6()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
