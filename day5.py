from hashlib import md5

DEFAULT_INPUT = 'day5.txt'

def part_1(loc: str = DEFAULT_INPUT) -> str:
    with open(loc) as f:
        door_id = f.readline().rstrip()
    i = 0
    password = ''
    while len(password) < 8:
        d = (door_id + str(i)).encode()
        m = md5(d).hexdigest()
        if m.startswith('00000'):
            password += m[5]
        i += 1
    return password
        
            
def part_2(loc: str = DEFAULT_INPUT) -> str:
    with open(loc) as f:
        door_id = f.readline().rstrip()
    i = 0
    password = [None] * 8
    while None in password:
        d = (door_id + str(i)).encode()
        m = md5(d).hexdigest()
        if m.startswith('00000'):
            if m[5] in '01234567' and password[int(m[5])] is None:
                password[int(m[5])] = m[6]
        i += 1
    return ''.join(password)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
