import time
from helpers import *

t = time.time()

input = mypath + "d7-input.txt"
with open(input) as f:
    crabs = [int(d) for d in f.read().split(",")]

# Part 1
def scootToPos(x):
    return sum([abs(c - x) for c in crabs])


# https://www.youtube.com/watch?v=wJqOwyA9iqY&t=192s
sliddle = [scootToPos(i) for i in range(min(crabs), max(crabs) + 1)]

dropstar(13, min(sliddle), t)

# Part 2
def sumOfIntegers(first, last):
    n = last - first + 1
    return n * (first + last) / 2


def increasedScootToPos(x):
    return sum([sumOfIntegers(1, abs(c - x)) for c in crabs])


sliddle = [increasedScootToPos(i) for i in range(min(crabs), max(crabs) + 1)]

dropstar(14, min(sliddle), t)
