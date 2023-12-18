import time, re, itertools
from helpers import *

t = time.time()

# input = mypath + "d12-example.txt"
input = mypath + "d12-input.txt"
with open(input) as f:
    records = f.read().split("\n")

# Split records at a space to a string and a tuple of ints
records = [[r.split()[0], tuple(int(s) for s in r.split()[1].split(","))] for r in records]

# Part 1
# Solution is slow (50 secs), but acceptable for part 1

# Count size of hash groups in a record string and return as a tuple of ints
def springs_tuple(record):
    groups = (len(g) for g in re.sub(r'\.+', '.', record).split('.'))
    return tuple(ele for ele in groups if ele != 0)

# Generate all possible combinations of '.' and '#' for the unknowns in a record string
def combinations(record):
    unknowns = record.count('?')
    return itertools.product(['.', '#'], repeat=unknowns)

# Generate all possible record strings where ? is replaced by '.' or '#'
def arrangements(record):
    for c in combinations(record):
        yield record.replace('?', '{}').format(*c)

# Find the record string arrangements that matches the tuple of ints in a record
# count = 0
# for record in records:
#     for a in arrangements(record[0]):
#         if springs_tuple(a) == record[1]:
#             count += 1

# dropstar(23, count, t)


# Part 2
# Optimized solution
# Leading,  trailing and multiple '.' can be removed from the record string
# If record string length equals the sum of the tuple of ints plus amount of groups minus 1, then there's 1 match 
# Can strings be analyzed in chunks separated by '.'?

# Remove excess '.'
def trim(record):
    return re.sub(r'\.+', '.', record.strip('.'))

# Quintuple the record string and remove excess '.'
def quintuple(record):
    return trim(record * 5)

# Quintuple the tuple of ints
def quintuple_tuple(tup):
    return tup * 5

for record in records:
    print(f'{record[0]} => {quintuple(record[0])}')
    print(f'{record[1]} => {quintuple_tuple(record[1])}')

# dropstar(24, , t)

