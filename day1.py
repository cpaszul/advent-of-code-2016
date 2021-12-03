DEFAULT_INPUT = 'day1.txt'

def day_1(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        moves = f.readline().split(', ')
    seen = set()
    repeat = None
    dx, dy = 0, -1
    x, y = 0, 0
    seen.add((x, y))
    for move in moves:
        turn, n = move[0], int(move[1:])
        if turn == 'R':
            dx, dy = -1 * dy, dx
        else:
            dx, dy = dy, -1 * dx
        for _ in range(n):
            x += dx
            y += dy
            if (x, y) in seen and repeat is None:
                repeat = x, y
            seen.add((x, y))
    return abs(x) + abs(y), abs(repeat[0]) + abs(repeat[1])
    
                    

if __name__ == '__main__':
    part_1, part_2 = day_1()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
