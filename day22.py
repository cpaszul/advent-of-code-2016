from itertools import permutations
from collections import deque
import re

DEFAULT_INPUT = 'day22.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    nodes = {}
    with open(loc) as f:
        f.readline()
        f.readline()
        for line in f.readlines():
            digits = re.findall(r'(\d+)', line)
            x, y, size, used, avail, _ = map(int, digits)
            nodes[(x, y)] = (size, used, avail)
    return sum(1 for node_a, node_b in permutations(nodes.values(), 2) if valid_pair(node_a, node_b))

def valid_pair(node_a: tuple[int, int, int], node_b: tuple[int, int, int]) -> bool:
    return node_a[1] and node_a[1] < node_b[2]
            
        
def part_2(loc: str = DEFAULT_INPUT) -> int:
    nodes = {}
    walls = []
    max_x = -1
    max_y = -1
    with open(loc) as f:
        f.readline()
        f.readline()
        for line in f.readlines():
            digits = re.findall(r'(\d+)', line)
            x, y, size, used, avail, _ = map(int, digits)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            nodes[(x, y)] = (size, used, avail)
            if size >= 500:
                walls.append((x, y))
            if used == 0:
                empty = (x, y)
    target_data = (max_x, 0)
    d = deque([((empty, target_data), 0)])
    seen = set([(empty, target_data)])
    while d:
        state, moves = d.popleft()
        empty_cell, target_data = state
        for adj in adjacent(empty_cell, max_x, max_y):
            if adj not in walls:
                if adj == target_data:
                    new_state = (target_data, empty_cell)
                else:
                    new_state = (adj, target_data)
                if new_state[1] == (0, 0):
                    return moves + 1
                if new_state not in seen:
                    d.append((new_state, moves + 1))
                    seen.add(new_state)

def adjacent(cell: tuple[int, int], max_x: int, max_y: int) -> list[tuple[int, int]]:
    x, y = cell
    unfiltered = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [(i, j) for i, j in unfiltered if 0 <= i <= max_x and 0 <= j <= max_y]

def draw(nodes: dict):
    max_x = max(nodes, key=lambda t:t[0])[0]
    max_y = max(nodes, key=lambda t:t[1])[1]
    rows = []
    for y in range(max_y + 1):
        row = ''
        for x in range(max_x + 1):
            if nodes[(x, y)][0] > 500:
                row += '#'
            elif nodes[(x, y)][1] == 0:
                row += '_'
            elif (x, y) == (max_x, 0):
                row += 'G'
            else:
                row += '.'
        rows.append(row)
    print('\n'.join(rows))
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
