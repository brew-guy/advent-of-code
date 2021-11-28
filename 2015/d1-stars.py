import time
from helpers import *

t = time.time()


input = mypath + "d1-input.txt"
with open(input) as f:
    lines = f.readlines()

# Part 1
directions = lines[0]
floor = directions.count("(") - directions.count(")")

dropstar(1, floor, t)

# Part 2
dirs = {"(": 1, ")": -1}
floor = 0
for index, direction in enumerate(directions):
    floor += dirs[direction]
    if floor == -1:
        break

dropstar(2, index + 1, t)
