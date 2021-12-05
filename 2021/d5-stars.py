import time
from helpers import *

t = time.time()

input = mypath + "d5-input.txt"
with open(input) as f:
    vents_raw = [c.split(" -> ") for c in f.read().split("\n")]
    all_vent_coords = [[tuple(map(int, xy.split(","))) for xy in c] for c in vents_raw]

# Part 1
def coords(vent):
    return vent[0][0], vent[0][1], vent[1][0], vent[1][1]


def isHorizontal(vent):
    x1, y1, x2, y2 = coords(vent)
    return y1 == y2


def isVertical(vent):
    x1, y1, x2, y2 = coords(vent)
    return x1 == x2


def getCoords(vent):
    x1, y1, x2, y2 = coords(vent)
    if isHorizontal(vent):
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    elif isVertical(vent):
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    else:  # Handle the diagonals
        x_range = range(min(x1, x2), max(x1, x2) + 1)
        y_range = range(min(y1, y2), max(y1, y2) + 1)
        if (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
            y_range = reversed(y_range)
        return list(zip(x_range, y_range))


def findOverlaps(vents):
    dict = {}
    for vent in vents:
        for coord in getCoords(vent):
            if coord in dict:
                dict[coord] += 1
            else:
                dict[coord] = 1
    return [k for k, v in dict.items() if v > 1]


straightVents = [v for v in all_vent_coords if isHorizontal(v) or isVertical(v)]

dropstar(9, len(findOverlaps(straightVents)), t)

# Part 2

dropstar(10, len(findOverlaps(all_vent_coords)), t)
