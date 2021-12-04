import time
from helpers import *

t = time.time()

input = mypath + "d3-input.txt"
with open(input) as f:
    report = [[int(bit) for bit in binary] for binary in f.read().split("\n")]

# Part 1
def mostCommon(bit_list):  # most common bit per bit index
    count_ones = [sum(bit) for bit in zip(*bit_list)]
    most_common = [int(d / len(bit_list) >= 0.5) for d in count_ones]
    return most_common


def bitString(bit_list):
    return "".join([str(b) for b in bit_list])


bin_len = len(report[0])
most_common = mostCommon(report)

gamma = bitString(most_common)
epsilon = bitString([1 - b for b in most_common])
power = int(gamma, 2) * int(epsilon, 2)

dropstar(1, power, t)

# Part 2
def filterBits(invert_compare=False):
    bit_2d_list = report.copy()
    for bit in range(bin_len):
        common = mostCommon(bit_2d_list)
        bit_2d_list = list(
            filter(lambda x: x[bit] == abs(invert_compare - common[bit]), bit_2d_list)
        )
        if len(bit_2d_list) == 1:
            return bit_2d_list[0]


oxy = bitString(filterBits())
co2 = bitString(filterBits(invert_compare=True))
life = int(oxy, 2) * int(co2, 2)

dropstar(2, life, t)
