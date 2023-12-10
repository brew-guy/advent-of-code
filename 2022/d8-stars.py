import math
import time
from helpers import *

t = time.time()

input = mypath + "d8-input.txt"
with open(input) as f:
    grid = [[int(digit) for digit in row] for row in f.read().split("\n")]

# Part 1
# Split input to 2D array of digits
# Function that returns the 4 "rays" of digits in all 4 directions from a coordinate
# Find max in each "ray", if digit at coordinate is larger in any -> visible tree


def getRays(coord, grid):
    row, col = coord
    right = grid[row][:col]
    left = grid[row][col + 1 :]
    up = list(map(lambda x: x[col], grid[:row]))
    down = list(map(lambda x: x[col], grid[row + 1 :]))
    return right, left, up, down


def isVisible(coord, grid):
    row, col = coord
    tree = grid[row][col]
    rays = getRays(coord, grid)
    visibility = [max(ray) < tree for ray in rays]
    return any(visibility)


height, width = len(grid), len(grid[0])
visible_counts = []
for row in range(1, height - 1):
    for col in range(1, width - 1):
        coord = (row, col)
        visible = isVisible(coord, grid)
        visible_counts.append(visible)

total = sum(visible_counts) + 2 * height + 2 * width - 4

dropstar(15, total, t)

# Part 2
# Function that counts visible trees in all 4 directions from coordinate until tree of same height
# Function that counts numbers smaller or equal from begginning of array
t = time.time()


def countUp(array, number):
    count = 0
    if array is None or len(array) < 1:
        return 0
    for val in array:
        count += 1
        if val >= number:
            return count
    return count


def getVisibleTreeCounts(coord, grid):
    row, col = coord
    tree = grid[row][col]

    left = grid[row][:col]
    left = countUp(list(reversed(left)), tree)

    right = countUp(grid[row][col + 1 :], tree)

    up = list(map(lambda x: x[col], grid[:row]))
    up = countUp(list(reversed(up)), tree)

    down = countUp(list(map(lambda x: x[col], grid[row + 1 :])), tree)
    return left, right, up, down


height, width = len(grid), len(grid[0])
visible_scores = []
for row in range(height):
    for col in range(width):
        coord = (row, col)
        visible = getVisibleTreeCounts(coord, grid)
        visible_scores.append(math.prod(visible))

dropstar(16, max(visible_scores), t)
