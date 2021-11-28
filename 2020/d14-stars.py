import time, re
from itertools import product
from helpers import *

t = time.time()

# Read initialization program to array
input = mypath + "d14-input.txt"
with open(input) as f:
    initialization_program = f.read().splitlines()

# Part 1
memory = {}
for command in initialization_program:
    if "mask = " in command:
        mask_OR = int(command[7:].replace("X", "0"), 2)  # Turn on bits with mask
        mask_AND = int(command[7:].replace("X", "1"), 2)  # Turn off bits with mask
    else:
        matches = re.match("mem\[(\d+)\] = (\d+)", command)
        address = int(matches.groups()[0])
        value = int(matches.groups()[1]) & mask_AND | mask_OR
        memory[address] = value

# Sum up the values in the mamory addresses
memory_sum = sum([memory[key] for key in memory])

dropstar(27, memory_sum, t)

# Part 2
memory = {}
for command in initialization_program:
    if "mask = " in command:
        mask = command[7:]
        mask_OR = int(mask.replace("X", "0"), 2)
        float_indices = [idx for idx, bit in enumerate(mask) if bit == "X"]
        float_combinations = list(product("01", repeat=len(float_indices)))
    else:
        matches = re.match("mem\[(\d+)\] = (\d+)", command)
        address = int(matches.groups()[0]) | mask_OR
        value = int(matches.groups()[1])
        addr_bit = str(bin(address))[2:]
        addr_36bit = "0" * (36 - len(addr_bit)) + addr_bit
        addr_list = list(addr_36bit)
        for combination in float_combinations:
            # Replace mask floats with next combination of bits
            for i, float_index in enumerate(float_indices):
                addr_list[float_index] = combination[i]
            addr_joind = "".join(addr_list)
            memory[addr_joind] = value

# Sum up the values in the memory addresses
memory_sum = sum([memory[key] for key in memory])

dropstar(28, memory_sum, t)
