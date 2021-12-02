import time
from helpers import *

t = time.time()

input = mypath + "d2-input.txt"
with open(input) as f:
    commands = f.read().split("\n")

# Part 1
route = [(c.split()[0], int(c.split()[1])) for c in commands]

up = [int(_[1]) for _ in route if _[0] == "up"]
down = [int(_[1]) for _ in route if _[0] == "down"]
forward = [int(_[1]) for _ in route if _[0] == "forward"]

prod = (sum(down) - sum(up)) * sum(forward)

dropstar(3, prod, t)

# Part 2
aim, hpos, depth = 0, 0, 0
for d in route:
    aim += d[1] if d[0] == "down" else 0
    aim -= d[1] if d[0] == "up" else 0
    hpos += d[1] if d[0] == "forward" else 0
    depth += d[1] * aim if d[0] == "forward" else 0

prod = hpos * depth

dropstar(4, prod, t)
