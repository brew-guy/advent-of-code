import time, itertools
from helpers import *

t = time.time()

# Read XMAS data numbers to array
input = "d9-input.txt"
with open(input) as f:
    XMASdata = [int(line) for line in f]

# Part 1
preamble = XMASdata[:25]
available_numbers = preamble.copy()

for i in range(25, len(XMASdata)):
    combinations = list(itertools.combinations(available_numbers, 2))
    combination_sums = map(lambda x: sum(x), combinations)
    if XMASdata[i] not in combination_sums:
        no_sum = XMASdata[i]
        break
    available_numbers = available_numbers[1:]
    available_numbers.append(XMASdata[i])

dropstar(17, no_sum, t)

# Part 2
available_numbers = preamble.copy()

for i in range(25, len(XMASdata)):
    combinations = list(itertools.combinations(available_numbers, 2))
    combination_sums = map(lambda x: sum(x), combinations)
    current_number = XMASdata[i]
    if current_number not in combination_sums:
        # print("No sum possible in 2 of prior 25 numbers for {0}".format(current_number))
        n = 3
        keep_looking = True
        while keep_looking:
            for j in range(0, len(XMASdata)):
                next_group = XMASdata[j : j + n]
                if current_number == sum(next_group):
                    weakness = min(next_group) + max(next_group)
                    keep_looking = False
            n += 1
    available_numbers = available_numbers[1:]
    available_numbers.append(XMASdata[i])

dropstar(18, weakness, t)
