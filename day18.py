DEFAULT_INPUT = 'day18.txt'

def day_18(limit: int, loc: str = DEFAULT_INPUT) -> int:
    rows = []
    with open(loc) as f:
        rows.append(f.readline().rstrip())
    while len(rows) < limit:
        rows.append(next_row(rows[-1]))
    return sum(row.count('.') for row in rows)

def next_row(row: str) -> str:
    new = ''
    for i, c in enumerate(row):
        if i == 0:
            left = '.'
        else:
            left = row[i - 1]
        if i == len(row) - 1:
            right = '.'
        else:
            right = row[i + 1]
        if left + c + right in ('^^.', '.^^', '^..', '..^'):
            new += '^'
        else:
            new += '.'
    return new
    
if __name__ == '__main__':
    print('Solution for Part One:', day_18(40))
    print('Solution for Part Two:', day_18(400_000))
