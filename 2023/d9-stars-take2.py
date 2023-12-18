import time, functools
from helpers import *

t = time.time()

# input = mypath + "d9-example.txt"
input = mypath + "d9-input.txt"
with open(input) as f:
    history = [[int(v) for v in l.split()] for l in f.readlines()]

# Part 1
# Calculate the extrapolated values step by step

# Function that takes an input list and returns a list of differences
def find_differences(row):
    differences = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    return differences

# Check if all values in list are zero
def all_zero(row):
    return all([v == 0 for v in row])

# Store all differences in a list
def extrapolate(row):
    all_diffs = []
    diffs = find_differences(row)
    while not all_zero(diffs):
        all_diffs.append(diffs)
        diffs = find_differences(diffs)
    return all_diffs

extrapolated = []
for row in history:
    diffs = extrapolate(row)
    last_diffs = [d[-1] for d in diffs]
    next_value = sum(last_diffs) + row[-1]
    extrapolated.append(next_value)

dropstar(17, sum(extrapolated), t)


# Part 2
# Guess 1: 38681 - too high
# Guess 2: 20379 - too high
# Guess 3: -16225 - incorrect
# Guess 4: 16225 - incorrect

extrapolated = []
for row in history:
    diffs = extrapolate(row)
    first_diffs = [d[0] for d in diffs[::-1]]
    first_reduced = functools.reduce(lambda a, c: c-a, first_diffs)
    next_value = row[0] - first_reduced
    extrapolated.append(next_value)

dropstar(18, sum(extrapolated), t)

