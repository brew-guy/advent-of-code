import time
import numpy as np
from array2gif import write_gif
from helpers import *

t = time.time()

input = mypath + "d18-input.txt"
with open(input) as f:
    grid = [row.strip() for row in f.readlines()]
    # grid = [[light for light in "." + row.strip() + "."] for row in f.readlines()]

# Part 1
padding = 1


def addPadding(grid, char):
    grid_width = len(grid[0])
    padding_rows = [char * (2 * padding + grid_width)] * padding
    grid = [char * padding + row + char * padding for row in grid]
    grid = padding_rows + grid + padding_rows
    return grid


def trimPadding(grid):
    grid = grid[padding:-padding]
    grid = [row[padding:-padding] for row in grid]
    return grid


def isLit(x, y, grid):
    return grid[x][y] == "#"


def getLitNeighbours(x, y, grid):
    neighbours = [row[y - 1 : y + 2] for row in grid[x - 1 : x + 2]]
    lit = sum([light == "#" for row in neighbours for light in row]) - isLit(x, y, grid)
    return lit


def newState(x, y, grid):
    if isLit(x, y, grid) and (2 <= getLitNeighbours(x, y, grid) <= 3):
        return "#"
    elif not isLit(x, y, grid) and getLitNeighbours(x, y, grid) == 3:
        return "#"
    return "."


def grid2numpy(grid):
    array = [[[255, 0, 0] if c == "#" else [0, 0, 0] for c in r] for r in grid]
    return np.array(array)


grid = addPadding(grid, ".")
current_frame = grid
gif_dataset = []

for i in range(100):
    next_frame = []
    for row in range(padding, 100 + padding):
        new_row = "".join(
            [newState(row, col, current_frame) for col in range(padding, 100 + padding)]
        )
        next_frame.append(new_row)
    gif_dataset.append(grid2numpy(next_frame))
    next_frame = addPadding(next_frame, ".")
    current_frame = next_frame.copy()

current_frame = trimPadding(current_frame)
lights_on = sum([row.count("#") for row in current_frame])

# What does it look like animated?
write_gif(gif_dataset, mypath + "d18-animated-1.gif", fps=5)

dropstar(35, lights_on, t)

# Part 2
def lightCorners(grid):
    first_row = list(grid[0])
    first_row[0] = "#"
    first_row[-1] = "#"
    last_row = list(grid[-1])
    last_row[0] = "#"
    last_row[-1] = "#"
    grid[0] = "".join(first_row)
    grid[-1] = "".join(last_row)
    return grid


current_frame = grid
gif_dataset = []

for i in range(100):
    next_frame = []
    for row in range(padding, 100 + padding):
        new_row = "".join(
            [newState(row, col, current_frame) for col in range(padding, 100 + padding)]
        )
        next_frame.append(new_row)
    next_frame = lightCorners(next_frame)
    gif_dataset.append(grid2numpy(next_frame))
    next_frame = addPadding(next_frame, ".")
    current_frame = next_frame.copy()

current_frame = trimPadding(current_frame)
lights_on = sum([row.count("#") for row in current_frame])

# What does it look like animated?
write_gif(gif_dataset, mypath + "d18-animated-2.gif", fps=5)

dropstar(36, lights_on, t)
