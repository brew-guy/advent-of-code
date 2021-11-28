import numpy as np
from itertools import combinations
import time
from helpers import *

t = time.time()

input = mypath + "d1-input.txt"
with open(input) as f:
    lines = f.read()

# Part 1
expense_report = list(map(int, lines.split("\n")))

FIND_NUMBERS = 2
FIND_SUM = 2020

combs = combinations(expense_report, FIND_NUMBERS)

for comb in combs:
    if sum(comb) == FIND_SUM:
        # print("Found: ", comb)
        break

dropstar(1, np.prod(comb), t)

# Part 2
FIND_NUMBERS = 3
FIND_SUM = 2020

combs = combinations(expense_report, FIND_NUMBERS)

for comb in combs:
    if sum(comb) == FIND_SUM:
        # print("Found: ", comb)
        break

dropstar(2, np.prod(comb), t)
