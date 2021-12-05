import time, re
from helpers import *

t = time.time()

input = mypath + "d25-input.txt"
with open(input) as f:
    message = f.read()

row, col = map(int, re.findall(r"([0-9]+)", message))
multiplier, divisor = 252533, 33554393

# Part 1
def nextCode(current_code):
    return current_code * multiplier % divisor


def sumInts(first, last):
    n = last - first + 1
    return n * (first + last) / 2


def sumIters(first, n):
    return n * (n + 2 * first - 1) / 2


index = int(sumInts(1, col) + sumIters(col, row - 1))

code = 20151125
for i in range(index - 1):
    code = nextCode(code)

dropstar(49, code, t)

# Part 2

# dropstar(50, , t)
