import re
import time
from helpers import *

t = time.time()

input = mypath + "d4-input.txt"
with open(input) as f:
    pairs = [pair for pair in f.read().split("\n")]

# Part 1
# Input to arrays of tuples with integers for section ids. Use regex to split.
# Function to determine if pairs overlap fully (boolean result)
# Array if boolean results for overlaps
# Guess 1: 505 - too high


def getSections(string):
    sections = re.search(r"(\d*)-(\d*),(\d*)-(\d*)", string)
    return [int(s) for s in sections.groups()]


def hasFullOverlap(sections):
    s1, s2, t1, t2 = sections
    return (s1 >= t1 and s2 <= t2) or (t1 >= s1 and t2 <= s2)


sections = [getSections(section) for section in pairs]
overlapped = [hasFullOverlap(section) for section in sections]

dropstar(7, sum(overlapped), t)

# Part 2
# Function that identifies part overlap


def hasOverlap(sections):
    s1, s2, t1, t2 = sections
    return (s2 >= t1 and s2 <= t2) or (t2 >= s1 and t2 <= s2)


overlapped = [hasOverlap(section) for section in sections]

dropstar(8, sum(overlapped), t)
