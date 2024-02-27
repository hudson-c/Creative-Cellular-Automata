from imageio import imread

from Cell import Cell
import config


def next_state(state):
    size = range(config.size)
    new_state = [[Cell() for x in size] for x in size]
    for y in size:
        for x in size:
            cell = state[y][x]
            neighbours = get_neighbours(x, y, state)
            new_state[y][x] = config.apply_rule(cell, neighbours)

    return new_state


def get_neighbours(x, y, state):
    neighbours = []
    for i in range(1, -2, -1):
        for j in range(-1, 2):
            if (i == 0 and j == 0) or (not in_bounds(x + j, y + i)):
                continue
            neighbours.append(state[y + i][x + j])
    return neighbours


def in_bounds(x, y):
    return in_bound(x) and in_bound(y)


def in_bound(i):
    return 0 <= i and i < config.size


def print_state(state):
    print("")
    for row in state:
        print("[ ", ", ".join([str(cell) for cell in row]), " ]", end="\n")
    print("")
