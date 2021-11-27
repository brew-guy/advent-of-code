import time, itertools
from helpers import *

t = time.time()

input = "d17-input.txt"
with open(input) as f:
    containers = [int(_) for _ in f.readlines()]

# Part 1
target = 150

combinations = [
    seq
    for i in range(len(containers), 0, -1)
    for seq in itertools.combinations(containers, i)
    if sum(seq) == target
]

dropstar(33, len(combinations), t)

# Part 2
combinations_lengths = [len(l) for l in combinations]
min_length_count = combinations_lengths.count(min(combinations_lengths))

dropstar(34, min_length_count, t)
