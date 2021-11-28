import time
from helpers import *

t = time.time()

input = mypath + "d2-input.txt"
with open(input) as f:
    lines = f.readlines()

dimensions = [sorted(list(map(int, l.strip().split("x")))) for l in lines]

# Part 1
paper = 0
for dims in dimensions:
    l, w, h = dims
    paper += 2 * l * w + 2 * w * h + 2 * h * l + l * w

dropstar(3, paper, t)

# Part 2
ribbon = 0
for dims in dimensions:
    l, w, h = dims
    ribbon += 2 * l + 2 * w + l * w * h

dropstar(4, ribbon, t)
