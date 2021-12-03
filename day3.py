import re

DEFAULT_INPUT = 'day3.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    pattern = re.compile(r'(\d+)')
    with open(loc) as f:
        triangles = [tuple(map(int, pattern.findall(line)))
                     for line in f.readlines()]
    return sum(1 for tri in triangles if is_valid(tri))

def is_valid(tri: tuple[int, int, int]) -> bool:
    sorted_tri = sorted(tri)
    return sorted_tri[0] + sorted_tri[1] > sorted_tri[2]
            
def part_2(loc: str = DEFAULT_INPUT) -> int:
    pattern = re.compile(r'(\d+)')
    triangles = []
    with open(loc) as f:
        tri_a = ()
        tri_b = ()
        tri_c = ()
        for line in f.readlines():
            a, b, c = map(int, pattern.findall(line))
            tri_a += (a,)
            tri_b += (b,)
            tri_c += (c,)
            if len(tri_a) == 3:
                triangles.append(tri_a)
                triangles.append(tri_b)
                triangles.append(tri_c)
                tri_a = ()
                tri_b = ()
                tri_c = ()
    return sum(1 for tri in triangles if is_valid(tri))

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
