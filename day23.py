DEFAULT_INPUT = 'day23.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    registers = {ch: 0 for ch in 'abcd'}
    registers['a'] = 7
    def get_value(x: str) -> int:
        if x in 'abcd':
            return registers[x]
        return int(x)
    instructions = []
    with open(loc) as f:
        instructions = [list(line.rstrip().split(' ')) for line in f.readlines()]
    i = 0
    while 0 <= i < len(instructions):
        if len(instructions[i]) == 2:
            op, x = instructions[i]
        else:
            op, x, y = instructions[i]
        if op == 'cpy':
            if y in 'abcd':
                registers[y] = get_value(x)
        elif op == 'inc':
            registers[x] += 1
        elif op == 'dec':
            registers[x] -= 1
        elif op == 'jnz':
            if get_value(x) != 0:
                i += get_value(y) - 1
        else:
            target_index = i + get_value(x)
            if 0 <= target_index < len(instructions):
                target = instructions[target_index]
                if len(target) == 2:
                    if target[0] == 'inc':
                        target[0] = 'dec'
                    else:
                        target[0] = 'inc'
                else:
                    if target[0] == 'jnz':
                        target[0] = 'cpy'
                    else:
                        target[0] = 'jnz'
        i += 1
    return registers['a']
  
def part_2(loc: str = DEFAULT_INPUT) -> int:
    registers = {ch: 0 for ch in 'abcd'}
    registers['a'] = 12
    def get_value(x: str) -> int:
        if x in 'abcd':
            return registers[x]
        return int(x)
    instructions = []
    with open(loc) as f:
        instructions = [list(line.rstrip().split(' ')) for line in f.readlines()]
    i = 0
    #possibly input-dependent?
    instructions[4] = ['mul', 'a', 'd', 'b']
    instructions[5] = ['cpy', '0', 'c']
    instructions[6] = ['cpy', '0', 'd']
    instructions[7] = ['jnz', '0', '0']
    instructions[8] = ['jnz', '0', '0']
    instructions[9] = ['jnz', '0', '0']
    while 0 <= i < len(instructions):
        if len(instructions[i]) == 2:
            op, x = instructions[i]
        elif len(instructions[i]) == 3:
            op, x, y = instructions[i]
        else:
            op, x, y, z = instructions[i]
        if op == 'cpy':
            if y in 'abcd':
                registers[y] = get_value(x)
        elif op == 'inc':
            registers[x] += 1
        elif op == 'dec':
            registers[x] -= 1
        elif op == 'jnz':
            if get_value(x) != 0:
                i += get_value(y) - 1
        elif op == 'mul':
            registers[x] = get_value(y) * get_value(z)
        else:
            target_index = i + get_value(x)
            if 0 <= target_index < 4 or 10 <= target_index < len(instructions):
                target = instructions[target_index]
                if len(target) == 2:
                    if target[0] == 'inc':
                        target[0] = 'dec'
                    else:
                        target[0] = 'inc'
                else:
                    if target[0] == 'jnz':
                        target[0] = 'cpy'
                    else:
                        target[0] = 'jnz'
        i += 1
    return registers['a']
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
