# Day 10 - Part 1

import time
startTime = time.time()

# Read adapter joltages to a sorted array
input = "d10-input.txt"
with open(input) as f:
	adapter_joltages = sorted([int(line) for line in f])

jolt = min(adapter_joltages)

while jolt < max(adapter_joltages):
  adapters = len([i for i in adapter_joltages if jolt < i <= jolt + 3])
  

# print('The adapter chain had {0} 1-jolt and {1} 3-jolt differences. Multiplied = {2}'.format(jolt_differences[1], jolt_differences[3], jolt_differences[1]*jolt_differences[3]))
print('Execution time in seconds: {0}'.format(time.time() - startTime))