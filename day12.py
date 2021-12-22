DEFAULT_INPUT = 'day12.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    registers = {ch: 0 for ch in 'abcd'}
    with open(loc) as f:
        instructions = [line.rstrip() for line in f.readlines()]
    i = 0
    while 0 <= i < len(instructions):
        inst = instructions[i].split(' ')
        op = inst[0]
        x = inst[1]
        if len(inst) == 3:
            y = inst[2]
        if op == 'cpy':
            if x in 'abcd':
                registers[y] = registers[x]
            else:
                registers[y] = int(x)
        elif op == 'inc':
            registers[x] += 1
        elif op == 'dec':
            registers[x] -= 1
        else:
            value = registers[x] if x in 'abcd' else int(x)
            if value != 0:
                i += int(y) - 1
        i += 1
    return registers['a']
        
            
def part_2(loc: str = DEFAULT_INPUT) -> int:
    registers = {ch: 0 for ch in 'abcd'}
    registers['c'] = 1
    with open(loc) as f:
        instructions = [line.rstrip() for line in f.readlines()]
    i = 0
    while 0 <= i < len(instructions):
        inst = instructions[i].split(' ')
        op = inst[0]
        x = inst[1]
        if len(inst) == 3:
            y = inst[2]
        if op == 'cpy':
            if x in 'abcd':
                registers[y] = registers[x]
            else:
                registers[y] = int(x)
        elif op == 'inc':
            registers[x] += 1
        elif op == 'dec':
            registers[x] -= 1
        else:
            value = registers[x] if x in 'abcd' else int(x)
            if value != 0:
                i += int(y) - 1
        i += 1
    return registers['a']

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
