from collections import deque, namedtuple
from functools import cache
import itertools
import re

#from https://docs.python.org/3.9/library/itertools.html#itertools-recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

State = namedtuple('State', ['floors', 'elevator'])
Item = namedtuple('Item', ['name', 'type'])

DEFAULT_INPUT = 'day11.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    gen_pattern = re.compile(r'(\w+) generator')
    microchip_pattern = re.compile(r'(\w+)-compatible')
    initial_floors = []
    with open(loc) as f:
        for line in f.readlines():
            contents = set()
            if f := gen_pattern.findall(line):
                for gen in f:
                    contents.add(Item(gen, 'G'))
            if f := microchip_pattern.findall(line):
                for microchip in f:
                    contents.add(Item(microchip, 'M'))
            initial_floors.append(frozenset(contents))
    initial_floors = tuple(initial_floors)
    initial_state = State(initial_floors, 0)
    seen = set([initial_state])
    d = deque([(initial_state, 0, [initial_state])])
    while d:
        state, moves, history = d.popleft()
        potential_moves = []
        if state.elevator != 0:
            potential_moves.append(-1)
        if state.elevator != 3:
            potential_moves.append(1)
        for m in potential_moves:
            new_elevator = state.elevator + m
            items_to_move = [frozenset(items) for items in powerset(state.floors[state.elevator])
                             if len(items) in (1, 2)]
            for item_set in items_to_move:
                new_floors = []
                for i, floor in enumerate(state.floors):
                    if i == new_elevator:
                        new_floors.append(floor | item_set)
                    elif i == state.elevator:
                        new_floors.append(floor - item_set)
                    else:
                        new_floors.append(floor)
                new_floors = tuple(new_floors)
                new_state = State(new_floors, new_elevator)
                if winning_floors(new_floors):
                    #print_history(history + [new_state])
                    return moves + 1
                if valid_floors(new_floors) and new_state not in seen:
                    seen.add(new_state)
                    d.append((new_state, moves + 1, history + [new_state]))

def winning_floors(floors: tuple[frozenset[Item]]) -> bool:
    return not any(floors[:3])

@cache
def valid_floors(floors: tuple[frozenset[Item]]) -> bool:
    return all(valid_floor(floor) for floor in floors)

@cache
def valid_floor(floor: frozenset[Item]) -> bool:
    microchips = set(item.name for item in floor if item.type == 'M')
    generators = set(item.name for item in floor if item.type == 'G')
    for m in microchips:
        if generators and m not in generators:
            return False
    return True
 
def part_2(loc: str = DEFAULT_INPUT) -> int:
    gen_pattern = re.compile(r'(\w+) generator')
    microchip_pattern = re.compile(r'(\w+)-compatible')
    initial_floors = []
    with open(loc) as f:
        for i, line in enumerate(f.readlines()):
            contents = set()
            if f := gen_pattern.findall(line):
                for gen in f:
                    contents.add(Item(gen, 'G'))
            if f := microchip_pattern.findall(line):
                for microchip in f:
                    contents.add(Item(microchip, 'M'))
            if i == 0:
                contents |= set([Item('elerium', 'G'), Item('elerium', 'M'),
                                 Item('dilithium', 'G'), Item('dilithium', 'M')])
            initial_floors.append(frozenset(contents))
    initial_floors = tuple(initial_floors)
    initial_state = State(initial_floors, 0)
    seen = set([initial_state])
    d = deque([(initial_state, 0, [initial_state])])
    while d:
        state, moves, history = d.popleft()
        potential_moves = []
        if state.elevator != 0:
            potential_moves.append(-1)
        if state.elevator != 3:
            potential_moves.append(1)
        for m in potential_moves:
            new_elevator = state.elevator + m
            items_to_move = [frozenset(items) for items in powerset(state.floors[state.elevator])
                             if len(items) in (1, 2)]
            for item_set in items_to_move:
                new_floors = []
                for i, floor in enumerate(state.floors):
                    if i == new_elevator:
                        new_floors.append(floor | item_set)
                    elif i == state.elevator:
                        new_floors.append(floor - item_set)
                    else:
                        new_floors.append(floor)
                new_floors = tuple(new_floors)
                new_state = State(new_floors, new_elevator)
                if winning_floors(new_floors):
                    #print_history(history + [new_state])
                    return moves + 1
                if valid_floors(new_floors) and new_state not in seen:
                    seen.add(new_state)
                    d.append((new_state, moves + 1, history + [new_state]))

#Part two takes a very long time to run, (~20 minutes)
#but it does work
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
