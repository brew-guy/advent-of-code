import time, math
from helpers import *

t = time.time()

input = mypath + "d9-input.txt"
with open(input) as f:
    heightmap = [_ for _ in f.read().split("\n")]

# Part 1
def getHeight(row, col):
    return int(heightmap[row][col])


def getNeighbours(row, col, coords=False):
    # Coordinates
    n_cor = (row - 1, col) if row > 0 else None
    s_cor = (row + 1, col) if row < len(heightmap) - 1 else None
    e_cor = (row, col + 1) if col < len(heightmap[0]) - 1 else None
    w_cor = (row, col - 1) if col > 0 else None
    coordinates = [n_cor, s_cor, e_cor, w_cor]
    # Values
    values = [getHeight(*c) if c != None else 99 for c in coordinates]
    if coords:
        return coordinates
    return values


def isLowPoint(row, col):
    height = getHeight(row, col)
    nbs = getNeighbours(row, col)
    isLower = lambda val: all([val < _ for _ in nbs])
    return isLower(height)


lows = [
    (r, c)
    for r, row in enumerate(heightmap)
    for c, val in enumerate(row)
    if isLowPoint(r, c)
]

risk_levels = [int(heightmap[r][c]) + 1 for r, c in lows]

dropstar(17, sum(risk_levels), t)

# Part 2
# Taking a walk with sample algorithm, https://en.wikipedia.org/wiki/Pathfinding
def findBasin(low):
    queue, idx = [low], 0
    while idx < len(queue):
        nbs = getNeighbours(*queue[idx], coords=True)
        queue += [n for n in nbs if n != None and n not in queue and getHeight(*n) < 9]
        idx += 1
    return queue


basins = [findBasin(low) for low in lows]
basins.sort(key=len)
three_largest = [len(b) for b in basins[-3:]]

dropstar(18, math.prod(three_largest), t)
