from hashlib import md5
from collections import deque

DEFAULT_INPUT = 'day17.txt'

def day_17(loc: str = DEFAULT_INPUT) -> tuple[str, int]:
    valid = 'bcdef'
    with open(loc) as f:
        passcode = f.readline().rstrip()
    initial_state = ((0, 0), '')
    d = deque([initial_state])
    solutions = []
    while d:
        cell, path, = d.popleft()
        if cell == (3, 3):
            solutions.append(path)
        else:
            x, y = cell
            h = md5((passcode + path).encode()).hexdigest()[:4]
            if h[0] in valid and y != 0:
                new_state = ((x, y - 1), path + 'U')
                d.append(new_state)
            if h[1] in valid and y != 3:
                new_state = ((x, y + 1), path + 'D')
                d.append(new_state)
            if h[2] in valid and x != 0:
                new_state = ((x - 1, y), path + 'L')
                d.append(new_state)
            if h[3] in valid and x != 3:
                new_state = ((x + 1, y), path + 'R')
                d.append(new_state)
    return solutions[0], len(solutions[-1])
    
if __name__ == '__main__':
    part_1, part_2 = day_17()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
