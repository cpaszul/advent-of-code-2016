DEFAULT_INPUT = 'day2.txt'

PART_1_GRID = {(-1, -1): '1',
               ( 0, -1): '2',
               ( 1, -1): '3',
               (-1,  0): '4',
               ( 0,  0): '5',
               ( 1,  0): '6',
               (-1,  1): '7',
               ( 0,  1): '8',
               ( 1,  1): '9'}

PART_2_GRID = {(2, -2): '1',
               (1, -1): '2',
               (2, -1): '3',
               (3, -1): '4',
               (0,  0): '5',
               (1,  0): '6',
               (2,  0): '7',
               (3,  0): '8',
               (4,  0): '9',
               (1,  1): 'A',
               (2,  1): 'B',
               (3,  1): 'C',
               (2,  2): 'D'}

def day_2(loc: str = DEFAULT_INPUT) -> tuple[str, str]:
    with open(loc) as f:
        moves = [line.rstrip() for line in f.readlines()]
    return solve(moves, PART_1_GRID), solve(moves, PART_2_GRID)

def solve(moves: list[str], grid: dict[tuple[int, int], str]) -> str:
    res = ''
    x, y = 0, 0
    m = {'R': ( 1,  0),
         'L': (-1,  0),
         'U': ( 0, -1),
         'D': ( 0,  1)}
    for move in moves:
        for char in move:
            dx, dy = m[char]
            if (x + dx, y + dy) in grid:
                x += dx
                y += dy
        res += grid[(x, y)]
    return res

if __name__ == '__main__':
    part_1, part_2 = day_2()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
