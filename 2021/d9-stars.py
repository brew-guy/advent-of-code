import time
from helpers import *

t = time.time()

input = mypath + "d9-sample.txt"
with open(input) as f:
    heightmap = [_ for _ in f.read().split("\n")]

# Part 1
def getHeight(row, col):
    return int(heightmap[row][col])


def getNeighbours(row, col, coords=False):
    # Values
    n_val = getHeight(row - 1, col) if row > 0 else 99
    s_val = getHeight(row + 1, col) if row < len(heightmap) - 1 else 99
    e_val = getHeight(row, col + 1) if col < len(heightmap[0]) - 1 else 99
    w_val = getHeight(row, col - 1) if col > 0 else 99
    # Coordinates
    n_cor = (row - 1, col) if n_val != 99 else None
    s_cor = (row + 1, col) if s_val != 99 else None
    e_cor = (row, col + 1) if e_val != 99 else None
    w_cor = (row, col - 1) if w_val != 99 else None
    if coords:
        return n_cor, s_cor, e_cor, w_cor
    return n_val, s_val, e_val, w_val


def isLowPoint(row, col):
    height = getHeight(row, col)
    n, s, e, w = getNeighbours(row, col)
    isLower = lambda val: all([val < _ for _ in [n, s, e, w]])
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
def recursiveSearch(low, basin=set()):
    basin.add(low)
    row, col = low
    # Neighbour values and coordinates
    nb_vals = getNeighbours(row, col)
    nb_coords = getNeighbours(row, col, coords=True)
    for i, coord in enumerate(nb_coords):
        if coord != None and nb_vals[i] != 9 and coord not in basin:
            return recursiveSearch(coord, basin)
        else:
            return basin


# for low in lows:
r = recursiveSearch(lows[0])
print(r)

# dropstar(18, , t)
