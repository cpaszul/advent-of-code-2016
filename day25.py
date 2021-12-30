DEFAULT_INPUT = 'day25.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        instructions = [list(line.rstrip().split(' ')) for line in f.readlines()]
    val = int(instructions[1][1]) * int(instructions[2][1])
    i = 0
    while True:
        if valid_number(i + val):
            return i
        i += 1

def valid_number(n: int) -> bool:
    b = bin(n)[2:]
    return len(b) % 2 == 0 and b == '10' * (len(b) // 2)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
