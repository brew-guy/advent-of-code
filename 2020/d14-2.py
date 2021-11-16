# Day 14 - Part 2

import time
import re
from itertools import product
startTime = time.time()

# Read initialization program to array
input = "G:/My Drive/My Files/Code/Advent of Code/AoC 2020/d14-input.txt"
with open(input) as f:
	init_program = f.read().splitlines()

memory = {}
for command in init_program:
	if 'mask = ' in command:
		mask = command[7:]
		mask_OR = int(mask.replace('X', '0'), 2)
		float_indices = [idx for idx, bit in enumerate(mask) if bit == 'X']
		float_combinations = list(product('01',repeat = len(float_indices)))
	else:
		matches = re.match('mem\[(\d.+)\] = (\d.+)', command)
		address = int(matches.groups()[0]) | mask_OR
		value = int(matches.groups()[1])
		addr_bit = str(bin(address))[2:]
		addr_36bit = '0' * (36 - len(addr_bit)) + addr_bit
		addr_list = list(addr_36bit)
		for combination in float_combinations:
			# Replace mask floats with next combination of bits
			for i, float_index in enumerate(float_indices):
				addr_list[float_index] = combination[i]
			addr_joind = ''.join(addr_list)
			memory[addr_joind] = value

# Sum up the values in the memory addresses
memory_sum = sum([memory[key] for key in memory])

print("The sum of all values left in memory = {0}".format(memory_sum))
print('Execution time in seconds: {0}'.format(time.time() - startTime))