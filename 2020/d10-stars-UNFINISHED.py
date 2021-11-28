import time
from helpers import *

t = time.time()

# Read adapter joltages to a sorted array
input = mypath + "d10-input.txt"
with open(input) as f:
    adapter_joltages = sorted([int(line) for line in f])

# Part 1
adapter_rating = max(adapter_joltages) + 3
adapter_joltages.append(adapter_rating)

jolt_differences = {}
jolt_differences[min(adapter_joltages)] = 1

for i in range(1, len(adapter_joltages)):
    difference = adapter_joltages[i] - adapter_joltages[i - 1]
    if not difference in jolt_differences:
        jolt_differences[difference] = 1
    else:
        jolt_differences[difference] += 1

multiplied = jolt_differences[1] * jolt_differences[3]

dropstar(19, multiplied, t)

# Part 2
jolt = min(adapter_joltages)

# while jolt < max(adapter_joltages):
#     adapters = len([i for i in adapter_joltages if jolt < i <= jolt + 3])

# print('The adapter chain had {0} 1-jolt and {1} 3-jolt differences. Multiplied = {2}'.format(jolt_differences[1], jolt_differences[3], jolt_differences[1]*jolt_differences[3]))
# dropstar(20, , t)
