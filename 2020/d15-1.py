# Day 15 - Part 1

import time
startTime = time.time()

# Read initialization program to array
input = [16,11,15,0,1,7]
numbers_spoken = input

while len(numbers_spoken) < 2020:
	next_up = numbers_spoken[-1]
	if numbers_spoken.count(next_up) <= 1:
		new_number = 0
	else:
		last_found = list(reversed([idx for idx, num in enumerate(numbers_spoken) if num == next_up]))
		new_number = last_found[0] - last_found[1]
	numbers_spoken.append(new_number)

# print(numbers_spoken, len(numbers_spoken))

print("The 2020th number spoken is {0}".format(numbers_spoken[-1]))
print('Execution time in seconds: {0}'.format(time.time() - startTime))