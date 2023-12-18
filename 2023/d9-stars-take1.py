import time
import numpy as np
from helpers import *

t = time.time()

input = mypath + "d9-example.txt"
# input = mypath + "d9-input.txt"
with open(input) as f:
    history = [[int(v) for v in l.split()] for l in f.readlines()]

# Part 1
# This could be about finding polynomials of unknown degree for each row of the input
# Rows are numerical values in the form of a list
# https://www.math.cmu.edu/~bkell/21110-2010s/formula.html
# Find out how to solve polynomials of linear, quadratic, cubic, etc. degree
# Guess 1: 1955513201 - too high
# Guess 2: 1955513089 - too low
# Guess 3: 1955513199 - too high
# Guess 4: 1955513110 - not right
# Guess 5: 
# Seems like a dead end due to inaccuracies from the polynomial approximation

# Function that takes an input row and returns the degree of the polynomial
def find_differences(row):
    differences = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    print(differences)
    return differences

def find_degree(row):
    degree = 0
    diffs = find_differences(row)
    while sum(diffs) != 0:
        diffs = find_differences(diffs)
        degree += 1
    return degree

# Horner’s method can be used to evaluate polynomial in O(n) time.
def horner(coeff, x):
    result, n = coeff[0], len(coeff)
    for i in range(1, n):
        result = result*x + coeff[i]
    return result

extrapolated = []
for row in history:
    degree = find_degree(row)
    x = np.array(range(1, len(row) + 1))
    y = np.array(row)
    coeff = np.polyfit(x, y, degree)
    # Calculate polynomial result for next x value
    val = (horner(coeff, len(row) + 1))
    extrapolated.append(val)
    

dropstar(17, sum(extrapolated), t)


# Part 2

# dropstar(18, math.lcm(*s), t)

