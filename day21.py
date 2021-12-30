from collections import deque
import re

DEFAULT_INPUT = 'day21.txt'

def part_1(loc: str = DEFAULT_INPUT) -> str:
    password = deque('abcdefgh')
    with open(loc) as f:
        lines = f.readlines()
    for line in lines:
        if m := re.match(r'swap position (\d) with position (\d)', line):
            ind_x = int(m.group(1))
            ind_y = int(m.group(2))
            letter_x = password[ind_x]
            letter_y = password[ind_y]
            password[ind_x] = letter_y
            password[ind_y] = letter_x
        if m := re.match(r'swap letter (\w) with letter (\w)', line):
            letter_x = m.group(1)
            letter_y = m.group(2)
            ind_x = password.index(letter_x)
            ind_y = password.index(letter_y)
            password[ind_x] = letter_y
            password[ind_y] = letter_x
        if m := re.match(r'rotate (left|right) (\d) step', line):
            direction = 1 if m.group(1) == 'right' else -1
            password.rotate(direction * int(m.group(2)))
        if m := re.match(r'rotate based on position of letter (\w)', line):
            ind = password.index(m.group(1))
            amount_to_rotate = 1 + ind + (1 if ind >= 4 else 0)
            password.rotate(amount_to_rotate)
        if m := re.match(r'reverse positions (\d) through (\d)', line):
            start = int(m.group(1))
            end = int(m.group(2))
            password = list(password)
            password = password[:start] + password[start:end + 1][::-1] + password[end + 1:]
            password = deque(password)
        if m := re.match(r'move position (\d) to position (\d)', line):
            start = int(m.group(1))
            end = int(m.group(2))
            password.rotate(-1 * start)
            to_move = password.popleft()
            password.rotate(start)
            password.insert(end, to_move)
    return ''.join(password)
        
def part_2(loc: str = DEFAULT_INPUT) -> str:
    password = deque('fbgdceah')
    with open(loc) as f:
        lines = f.readlines()[::-1]
    for line in lines:
        if m := re.match(r'swap position (\d) with position (\d)', line):
            ind_x = int(m.group(1))
            ind_y = int(m.group(2))
            letter_x = password[ind_x]
            letter_y = password[ind_y]
            password[ind_x] = letter_y
            password[ind_y] = letter_x
        if m := re.match(r'swap letter (\w) with letter (\w)', line):
            letter_x = m.group(1)
            letter_y = m.group(2)
            ind_x = password.index(letter_x)
            ind_y = password.index(letter_y)
            password[ind_x] = letter_y
            password[ind_y] = letter_x
        if m := re.match(r'rotate (left|right) (\d) step', line):
            direction = 1 if m.group(1) == 'left' else -1
            password.rotate(direction * int(m.group(2)))
        if m := re.match(r'rotate based on position of letter (\w)', line):
            guess = password.copy()
            while True:
                if rotate_on_letter(guess.copy(), m.group(1)) == password:
                    password = guess
                    break
                guess.rotate(-1)
        if m := re.match(r'reverse positions (\d) through (\d)', line):
            start = int(m.group(1))
            end = int(m.group(2))
            password = list(password)
            password = password[:start] + password[start:end + 1][::-1] + password[end + 1:]
            password = deque(password)
        if m := re.match(r'move position (\d) to position (\d)', line):
            end = int(m.group(1))
            start = int(m.group(2))
            password.rotate(-1 * start)
            to_move = password.popleft()
            password.rotate(start)
            password.insert(end, to_move)
    return ''.join(password)
    
def rotate_on_letter(password: list[str], letter: str) -> list[str]:
    ind = password.index(letter)
    amount_to_rotate = 1 + ind + (1 if ind >= 4 else 0)
    password.rotate(amount_to_rotate)
    return password
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
