DEFAULT_INPUT = 'day16.txt'

def day_16(length: int, loc: str = DEFAULT_INPUT) -> str:
    with open(loc) as f:
        state = f.readline().rstrip()
    while len(state) < length:
        state = next_state(state)
    state = state[:length]
    checksum = generate_checksum(state)
    while len(checksum) % 2 == 0:
        checksum = generate_checksum(checksum)
    return checksum
    
def next_state(a: str) -> str:
    b = ''.join('1' if c == '0' else '0' for c in a[::-1])
    return a + '0' + b

def generate_checksum(chars: str) -> str:
    checksum = ''
    for i in range(0, len(chars) - 1, 2):
        pair = chars[i:i + 2]
        if pair[0] == pair[1]:
            checksum += '1'
        else:
            checksum += '0'
    return checksum
    
if __name__ == '__main__':
    print('Solution for Part One:', day_16(272))
    print('Solution for Part Two:', day_16(35651584))
