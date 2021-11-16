# Day 15 - Part 1

import time
startTime = time.time()

# Read initialization program to array
input = [16,11,15,0,1,7]
numbers_spoken = {}
for idx, number in enumerate(input):
	numbers_spoken[number] = idx

print(numbers_spoken)

last_spoken = input[-1]
for idx in range(len(input) - 1, 30000000):
  if last_spoken in numbers_spoken and numbers_spoken[last_spoken] < idx:
    next_number = idx - numbers_spoken[last_spoken]
  else:
    next_number = 0
  numbers_spoken[last_spoken] = idx
  last_spoken = next_number

last = max(numbers_spoken, key=lambda key: numbers_spoken[key])

print("The 30.000.000th number spoken is {0}".format(last))
print('Execution time in seconds: {0}'.format(time.time() - startTime))