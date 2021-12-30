from collections import defaultdict, deque
from itertools import combinations, permutations

DEFAULT_INPUT = 'day24.txt'

def day_24(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    numbers = {}
    distances = defaultdict(dict)
    grid = {}
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            row = row.rstrip()
            for x, cell in enumerate(row):
                grid[(x, y)] = '#' if cell == '#' else '.'
                if cell not in '.#':
                    numbers[cell] = (x, y)
    for a, b in combinations(numbers, 2):
        d = distance(numbers[a], numbers[b], grid)
        distances[a][b] = d
        distances[b][a] = d
    shortest_distance = None
    shortest_distance_2 = None
    for path in permutations((n for n in numbers if n != '0')):
        total = 0
        path = ('0',) + path
        for a, b in zip(path, path[1:]):
            total += distances[a][b]
        total_2 = total + distances[path[-1]]['0']
        if shortest_distance is None:
            shortest_distance = total
        shortest_distance = min(shortest_distance, total)
        if shortest_distance_2 is None:
            shortest_distance_2 = total_2
        shortest_distance_2 = min(shortest_distance_2, total_2)
    return shortest_distance, shortest_distance_2

def distance(point_a: tuple[int, int], point_b: tuple[int, int], grid: dict[tuple[int, int], str]) -> int:
    d = deque([(point_a, 0)])
    seen = set([point_a])
    while d:
        current, current_dist = d.popleft()
        all_adj = adjacent(current)
        for adj in all_adj:
            if adj == point_b:
                return current_dist + 1
            if adj in grid and grid[adj] == '.' and adj not in seen:
                seen.add(adj)
                d.append((adj, current_dist + 1))

def adjacent(point: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = point
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

if __name__ == '__main__':
    part_1, part_2 = day_24()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
