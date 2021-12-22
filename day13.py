from collections import deque

DEFAULT_INPUT = 'day13.txt'

def day_13(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        favorite_number = int(f.readline())
    grid = {}
    for y in range(55):
        for x in range(55):
            value = x**2 + 3*x + 2*x*y + y + y**2 + favorite_number
            bval = bin(value)[2:]
            if bval.count('1') % 2 == 0:
                grid[(x, y)] = '.'
            else:
                grid[(x, y)] = '#'
    distances = {}
    seen = set()
    d = deque([((1, 1), 0)])
    while d:
        current_location, current_distance = d.popleft()
        if current_location in distances and distances[current_location] <= current_distance:
            continue
        distances[current_location] = current_distance
        seen.add(current_location)
        for neighbor in neighbors(current_location):
            if neighbor in grid and grid[neighbor] == '.' and neighbor not in seen:
                d.append((neighbor, current_distance + 1))
    return distances[(31, 39)], sum(1 for v in distances.values() if v <= 50)

def neighbors(cell: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = cell
    return [(x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1)]

if __name__ == '__main__':
    part_1, part_2 = day_13()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
