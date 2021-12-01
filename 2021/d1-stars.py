import time
from helpers import *

t = time.time()

input = mypath + "d1-input.txt"
with open(input) as f:
    sonar = [int(d) for d in f.read().split("\n")]

# Part 1
def nextIncreases(lst):
    return sum([True for idx, s in enumerate(lst[:-1]) if s < lst[idx + 1]])


dropstar(1, nextIncreases(sonar), t)

# Part 2
slice = 3
windows = [sum(sonar[i : i + slice]) for i, _ in enumerate(sonar[: -slice + 1])]

dropstar(2, nextIncreases(windows), t)
