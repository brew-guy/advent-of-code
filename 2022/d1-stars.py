import time
from helpers import *

t = time.time()

input = mypath + "d1-input.txt"
with open(input) as f:
    inventory = [
        [int(cals) for cals in ration.split("\n")] for ration in f.read().split("\n\n")
    ]

# Part 1
# Split input on double new-line -> array of strings
# Split each string on new-line -> array of arrays of integer
# Generate array of sums
# Sort array descending and select first element as result

calories_sorted = sorted([sum(cals) for cals in inventory], reverse=True)

dropstar(1, calories_sorted[0], t)

# Part 2
# Select 3 first elements and sum them as result
t = time.time()

dropstar(2, sum(calories_sorted[0:3]), t)
