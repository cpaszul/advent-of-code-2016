import re
from collections import namedtuple

DEFAULT_INPUT = 'day15.txt'

Disc = namedtuple('Disc', ['number', 'cycle', 'start'])

def part_1(loc: str = DEFAULT_INPUT) -> int:
    discs = []
    r = re.compile(r'Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+)')
    with open(loc) as f:
        for line in f.readlines():
            m = r.match(line)
            number = int(m.group(1))
            cycle = int(m.group(2))
            start = int(m.group(3))
            discs.append(Disc(number, cycle, start))
    t = 0
    while True:
        if all((t + disc.number + disc.start) % disc.cycle == 0 for disc in discs):
            return t
        t += 1

def part_2(loc: str = DEFAULT_INPUT) -> int:
    discs = []
    r = re.compile(r'Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+)')
    with open(loc) as f:
        for line in f.readlines():
            m = r.match(line)
            number = int(m.group(1))
            cycle = int(m.group(2))
            start = int(m.group(3))
            discs.append(Disc(number, cycle, start))
    discs.append(Disc(len(discs) + 1, 11, 0))
    t = 0
    while True:
        if all((t + disc.number + disc.start) % disc.cycle == 0 for disc in discs):
            return t
        t += 1
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
