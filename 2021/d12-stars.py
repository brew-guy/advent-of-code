import time
from helpers import *

t = time.time()

input = mypath + "d12-input.txt"
with open(input) as f:
    caveparts = [path.split("-") for path in f.read().split("\n")]

# Part 1
print(caveparts)

# dropstar(23, , t)

# Part 2

# dropstar(24, , t)
