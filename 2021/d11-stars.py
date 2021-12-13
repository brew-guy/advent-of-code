import time, numpy as np
from array2gif import write_gif  # https://pypi.org/project/array2gif/
from helpers import *

t = time.time()

input = mypath + "d11-input.txt"
with open(input) as f:
    grid = [[int(octo) for octo in row] for row in f.read().split("\n")]

# Part 1
def incrementAll(grid):
    return [[octo + 1 for octo in row] for row in grid]


def incrementOne(grid, row, col):
    grid[row][col] = grid[row][col] + 1


def cooldown(grid):
    return [[octo if octo <= 9 else 0 for octo in row] for row in grid]


def getNeighbours(grid, row, col):
    n = (row - 1, col) if row > 0 else None
    s = (row + 1, col) if row < len(grid) - 1 else None
    e = (row, col + 1) if col < len(grid[0]) - 1 else None
    w = (row, col - 1) if col > 0 else None
    ne = (row - 1, col + 1) if row > 0 and col < len(grid[0]) - 1 else None
    se = (row + 1, col + 1) if row < len(grid) - 1 and col < len(grid[0]) - 1 else None
    nw = (row - 1, col - 1) if row > 0 and col > 0 else None
    sw = (row + 1, col - 1) if row < len(grid) - 1 and col > 0 else None
    coords = [n, ne, e, se, s, sw, w, nw]
    return [coord for coord in coords if coord != None]


def whoFlashed(grid):
    return set(
        [(r, c) for r, row in enumerate(grid) for c, octo in enumerate(row) if octo > 9]
    )


def flatten(t):
    return [item for sublist in t for item in sublist]


def printGrid(grid):
    # print("\n".join(["".join([str(el) for el in row]) for row in grid]), "\n")
    print(np.array(grid), "\n")


def oneStep(grid):
    grid = incrementAll(grid)
    flashed = whoFlashed(grid)
    new_flashers = flashed.copy()
    while new_flashers:
        toIncrement = flatten([getNeighbours(grid, *f) for f in new_flashers])
        for octo in toIncrement:
            incrementOne(grid, *octo)
        new_flashers = whoFlashed(grid).difference(flashed)
        flashed = flashed.union(new_flashers)
    grid = cooldown(grid)
    return grid, flashed


total_flashes = 0
grid_run = grid.copy()
for i in range(100):
    grid_run, flashed = oneStep(grid_run)
    total_flashes += len(flashed)


dropstar(12, total_flashes, t)

# Part 2
def isSynchronousFlash(grid):
    return all(flatten([[octo == 0 for octo in row] for row in grid]))


def grid2numpy(grid):
    array = [[[0, 28 * octo, 0] for octo in row] for row in grid]
    return np.array(array)


grid_run = grid.copy()
gif_dataset = [grid2numpy(grid_run)]
step, await_flash = 0, True
while await_flash:
    step += 1
    grid_run, flashed = oneStep(grid_run)
    await_flash = not isSynchronousFlash(grid_run)
    gif_dataset.append(grid2numpy(grid_run))

dropstar(22, step, t)

# What does it look like animated?
write_gif(gif_dataset, mypath + "d11-animated.gif", fps=25)
