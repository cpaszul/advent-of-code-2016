from string import ascii_lowercase

DEFAULT_INPUT = 'day4.txt'

def day_4(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    rooms = []
    with open(loc) as f:
        for line in f.readlines():
            room, checksum = line.rstrip(']\n').split('[')
            split = room.split('-')
            room_name, room_id = '-'.join(split[:-1]), int(split[-1])
            rooms.append((room_name, room_id, checksum))
    valid_rooms = [room for room in rooms if is_valid(room[0], room[2])]
    decrypted = {decrypt(room[0], room[1]): room[1] for room in valid_rooms}
    return sum(room[1] for room in valid_rooms), decrypted['northpole object storage']

def is_valid(room_name: str, checksum: str) -> bool:
    letters_used = list(ch for ch in set(room_name) if ch != '-')
    letters_used.sort()
    letters_used.sort(key = lambda ch: room_name.count(ch), reverse = True)
    return ''.join(letters_used[:5]) == checksum

def decrypt(room_name: str, room_id: int) -> str:
    decrypted = ''
    for ch in room_name:
        if ch == '-':
            decrypted += ' '
        else:
            i = ascii_lowercase.index(ch)
            i += room_id
            i %= len(ascii_lowercase)
            decrypted += ascii_lowercase[i]
    return decrypted

if __name__ == '__main__':
    part_1, part_2 = day_4()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
