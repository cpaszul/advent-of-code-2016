DEFAULT_INPUT = 'day9.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        s = f.readline().rstrip()
    expanded = 0
    i = 0
    in_marker = False
    marker_data = ''
    while i < len(s):
        ch = s[i]
        if in_marker:
            if ch == ')':
                repeat_chars, repeat_amount = map(int, marker_data.split('x'))
                expanded += repeat_chars * repeat_amount
                i += repeat_chars
                marker_data = ''
                in_marker = False
            else:
                marker_data += ch
        else:
            if ch == '(':
                in_marker = True
            else:
                expanded += 1
        i += 1
    return expanded
              
def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        s = f.readline().rstrip()
    return expand(s)

def expand(s: str) -> int:
    expanded = 0
    i = 0
    in_marker = False
    marker_data = ''
    while i < len(s):
        ch = s[i]
        if in_marker:
            if ch == ')':
                repeat_chars, repeat_amount = map(int, marker_data.split('x'))
                chars_to_repeat = s[i + 1:i + repeat_chars + 1]
                expanded += expand(chars_to_repeat) * repeat_amount
                i += repeat_chars
                marker_data = ''
                in_marker = False
            else:
                marker_data += ch
        else:
            if ch == '(':
                in_marker = True
            else:
                expanded += 1
        i += 1
    return expanded

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
