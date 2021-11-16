# Day 14 - Part 1

import time
import re
startTime = time.time()

# Read initialization program to array
input = "d14-input.txt"
with open(input) as f:
	initialization_program = f.read().splitlines()

memory = {}
for command in initialization_program:
	if 'mask = ' in command:
		mask_OR = int(command[7:].replace('X', '0'), 2) # Turn on bits with mask
		mask_AND = int(command[7:].replace('X', '1'), 2) # Turn off bits with mask
	else:
		matches = re.match('mem\[(\d.+)\] = (\d.+)', command)
		address = int(matches.groups()[0])
		value = int(matches.groups()[1]) & mask_AND | mask_OR
		memory[address] = value

# Sum up the values in the mamory addresses
memory_sum = sum([memory[key] for key in memory])

print("The sum of all values left in memory = {0}".format(memory_sum))
print('Execution time in seconds: {0}'.format(time.time() - startTime))