from collections import Counter

DEFAULT_INPUT = 'day7.txt'

def day_7(loc: str = DEFAULT_INPUT) -> tuple[str, str]:
    lines = []
    with open(loc) as f:
        for line in f.readlines():
            line = line.rstrip()
            inside, outside = [], []
            split = line.split('[')
            for s in split:
                if ']' not in s:
                    outside.append(s)
                else:
                    inside.append(s.split(']')[0])
                    outside.append(s.split(']')[1])
            lines.append((inside, outside))
    return sum(1 for line in lines if p1_valid(line)), \
           sum(1 for line in lines if p2_valid(line))

def p1_valid(line: tuple[list[str], list[str]]) -> bool:
    inside, outside = line
    return any(has_abba(s) for s in outside) and not any(has_abba(s) for s in inside)

def has_abba(s: str) -> bool:
    for a, b, c, d in zip(s, s[1:], s[2:], s[3:]):
        if a == d and b == c and a != b:
            return True
    return False

def p2_valid(line: tuple[list[str], list[str]]) -> bool:
    inside, outside = line
    babs = set()
    for s in outside:
        for a, b, c in zip(s, s[1:], s[2:]):
            if a == c and a != b:
                babs.add(b + a + b)
    return any(any(bab in s for bab in babs)
               for s in inside)

if __name__ == '__main__':
    part_1, part_2 = day_7()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
