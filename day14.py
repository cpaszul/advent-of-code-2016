from hashlib import md5
from functools import cache

DEFAULT_INPUT = 'day14.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        salt = f.readline().rstrip()
    i = 0
    found_keys = 0
    while True:
        hashed = get_hash(salt, i)
        triple = None
        for a, b, c in zip(hashed, hashed[1:], hashed[2:]):
            if triple is None and a == b == c:
                triple = a
        if triple:
            target = triple * 5
            for index in range(i + 1, i + 1002):
                if target in get_hash(salt, index):
                    found_keys += 1
                    if found_keys == 64:
                        return i
                    break
        i += 1

@cache
def get_hash(salt: str, index: int) -> str:
    return md5((salt + str(index)).encode()).hexdigest()

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        salt = f.readline().rstrip()
    i = 0
    found_keys = 0
    while True:
        hashed = get_stretched_hash(salt, i)
        triple = None
        for a, b, c in zip(hashed, hashed[1:], hashed[2:]):
            if triple is None and a == b == c:
                triple = a
        if triple:
            target = triple * 5
            for index in range(i + 1, i + 1002):
                if target in get_stretched_hash(salt, index):
                    found_keys += 1
                    if found_keys == 64:
                        return i
                    break
        i += 1

@cache
def get_stretched_hash(salt: str, index: int) -> str:
    value = salt + str(index)
    for _ in range(2017):
        value = md5(value.encode()).hexdigest()
    return value
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
