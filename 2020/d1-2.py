# Day 1 - Part 2
import numpy as np
from itertools import combinations 
import time
startTime = time.time()

input = "d1-input.txt"
with open(input) as f:
	lines = f.read()[:-1]

expense_report = list(map(int, lines.split("\n")))

FIND_NUMBERS = 3
FIND_SUM = 2020

combs = combinations(expense_report, FIND_NUMBERS)

for comb in combs:
  if sum(comb) == FIND_SUM:
    print("Found: ", comb)
    print("Multiplied: ", np.prod(comb))
    break

print('Execution time in seconds: {0}'.format(time.time() - startTime))