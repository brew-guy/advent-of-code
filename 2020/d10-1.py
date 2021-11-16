# Day 10 - Part 1

import time
startTime = time.time()

# Read adapter joltages to a sorted array
input = "d10-input.txt"
with open(input) as f:
	adapter_joltages = sorted([int(line) for line in f])

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

print('The adapter chain had {0} 1-jolt and {1} 3-jolt differences. Multiplied = {2}'.format(jolt_differences[1], jolt_differences[3], jolt_differences[1]*jolt_differences[3]))
print('Execution time in seconds: {0}'.format(time.time() - startTime))