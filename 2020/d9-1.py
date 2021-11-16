# Day 9 - Part 1

import itertools
import time
startTime = time.time()

# Read XMAS data numbers to array
input = "d9-input.txt"
with open(input) as f:
	XMASdata = [int(line) for line in f]

preamble = XMASdata[:25]
available_numbers = preamble.copy()

for i in range(25, len(XMASdata)):
  combinations = list(itertools.combinations(available_numbers, 2))
  combination_sums = (map(lambda x: sum(x), combinations))
  if XMASdata[i] not in combination_sums:
    print('No sum possible in 2 of prior 25 numbers for {0}'.format(XMASdata[i]))
    print(available_numbers)
  available_numbers = available_numbers[1:]
  available_numbers.append(XMASdata[i])

print('Execution time in seconds: {0}'.format(time.time() - startTime))