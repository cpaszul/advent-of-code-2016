from collections import deque

DEFAULT_INPUT = 'day19.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        size = int(f.readline())
    d = deque(range(1, size + 1))
    while len(d) > 1:
        d.rotate(-1)
        d.popleft()
    return d[0]
        
def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        size = int(f.readline())
    pow_3 = 1
    while True:
        next_power = 3 ** (pow_3 + 1)
        if next_power == size:
            return 3 ** (pow_3 + 1)
        if next_power > size:
            break
        pow_3 += 1
    result = 1
    n = (3 ** pow_3) + 1
    increment = 1
    while n < size:
        if n == result * 2:
            increment = 2
        result += increment
        n += 1
    return result
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
