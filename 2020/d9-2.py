# Day 9 - Part 2

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
  current_number = XMASdata[i]
  if current_number not in combination_sums:
    print('No sum possible in 2 of prior 25 numbers for {0}'.format(current_number))
    n = 3
    keep_looking = True
    while keep_looking:
      for j in range(0, len(XMASdata)):
        next_group = XMASdata[j:j + n]
        if current_number == sum(next_group):
          print('Sum of {0} is possible in a range of {1} contiguous numbers: {2}'.format(current_number, n, next_group))
          print('Sum of smallest and largest number in group being {0} + {1} = {2}'.format(min(next_group), max(next_group), min(next_group) + max(next_group)))
          keep_looking = False
      n += 1
      
  available_numbers = available_numbers[1:]
  available_numbers.append(XMASdata[i])

print('Execution time in seconds: {0}'.format(time.time() - startTime))