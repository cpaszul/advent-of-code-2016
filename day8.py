import re

DEFAULT_INPUT = 'day8.txt'

def day_8(loc: str = DEFAULT_INPUT) -> tuple[str, list[list[str]]]:
    grid = [['.'] * 50 for _ in range(6)]
    rect = re.compile(r'rect (\d+)x(\d+)')
    rot = re.compile(r'rotate (row y|column x)=(\d+) by (\d+)')
    with open(loc) as f:
        for line in f.readlines():
            if (m := rect.match(line)):
                a = int(m.group(1))
                b = int(m.group(2))
                for y in range(b):
                    for x in range(a):
                        grid[y][x] = '#'
            else:
                m = rot.match(line)
                row = m.group(1) == 'row y'
                a = int(m.group(2))
                b = int(m.group(3))
                if row:
                    rotate_row(grid, a, b)
                else:
                    rotate_column(grid, a, b)
    return sum(row.count('#') for row in grid), grid

def rotate_column(grid: list[list[str]], col_x: int, amount: int):
    col = []
    for y in range(6):
        col.append(grid[y][col_x])
    for y in range(6):
        target = y - amount
        target %= 6
        grid[y][col_x] = col[target]

def rotate_row(grid: list[list[str]], row_y: int, amount: int):
    row = grid[row_y].copy()
    for x in range(50):
        target = x - amount
        target %= 50
        grid[row_y][x] = row[target]

if __name__ == '__main__':
    part_1, part_2 = day_8()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:')
    print('\n'.join(''.join(row) for row in part_2))
