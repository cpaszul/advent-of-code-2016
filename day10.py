from collections import defaultdict
import re

DEFAULT_INPUT = 'day10.txt'

def day_10(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    value_pattern = re.compile(r'value (\d+) goes to bot (\d+)')
    comp_pattern = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    bots = defaultdict(list)
    outputs = {}
    part_1_res = None
    while lines:
        to_run = []
        for line in lines:
            if (m := value_pattern.match(line)):
                value, bot = map(int, (m.group(1), m.group(2)))
                bots[bot].append(value)
            else:
                m = comp_pattern.match(line)
                giver = int(m.group(1))
                if len(bots[giver]) == 2:
                    a_bot = m.group(2) == 'bot'
                    a_num = int(m.group(3))
                    b_bot = m.group(4) == 'bot'
                    b_num = int(m.group(5))
                    low = min(bots[giver])
                    high = max(bots[giver])
                    if low == 17 and high == 61:
                        part_1_res = giver
                    if a_bot:
                        bots[a_num].append(low)
                    else:
                        outputs[a_num] = low
                    if b_bot:
                        bots[b_num].append(high)
                    else:
                        outputs[b_num] = high
                else:
                    to_run.append(line)
        lines = to_run
    return part_1_res, outputs[0] * outputs[1] * outputs[2]

if __name__ == '__main__':
    part_1, part_2 = day_10()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
