import time, re
from helpers import *

t = time.time()

input = "d12-input.txt"
with open(input) as f:
    json = f.read()

# Part 1
numbers = re.findall("-?[0-9]+", json)
numbers = list(map(int, numbers))

dropstar(23, sum(numbers), t)

# Part 2

# dropstar(24, , t)
