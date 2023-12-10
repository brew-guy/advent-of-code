import time, re
from helpers import *

t = time.time()

input = mypath + "d3-input.txt"
with open(input) as f:
    engine = f.read().split("\n")

example = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

# Part 1
# Use regex to scan the example grid for multi digit numbers and their start coordinates
# and store numbers and coordinates in a list of tuples
# Repeat for symbols
# Guess 1: 549927 (too high)

numbers, symbols = [], []
for i, line in enumerate(engine):
    for match in re.finditer(r'\d+', line):
        numbers.append((int(match.group()), i, match.start()))
    for match in re.finditer(r'[^0-9.]', line):
        symbols.append((match.group(), i, match.start()))

# Determine numbers adjacent to symbols by comparing coordinates
# Use while loop to move found numbers to a new list
# Repeat until no more numbers left to check

numbers_copy = numbers.copy()

adjacent = []
while len(numbers) > 0:
    for n in numbers:
        for s in symbols:
            if abs(n[1] - s[1]) <= 1 and s[2] - n[2] >= -1 and s[2] - n[2] - len(str(n[0])) + 1 <= 1:
                adjacent.append(n)
                numbers.remove(n)
                break
        if n in numbers:
            numbers.remove(n)
            break

engine_parts = [x[0] for x in adjacent]

dropstar(5, sum(engine_parts), t)

# Part 2
# Make a gear array from symbols that only keeps asterisk symbols
# Repeat finding adjacent numbers to gears and build a new dict with gears as keys
# and numbers as values

gears = [g for g in symbols if g[0] == '*']
numbers = numbers_copy.copy()

adjacent = {g:[] for g in gears}

while len(numbers) > 0:
    for n in numbers:
        for s in gears:
            if abs(n[1] - s[1]) <= 1 and s[2] - n[2] >= -1 and s[2] - n[2] - len(str(n[0])) + 1 <= 1:
                adjacent[s].append(n)                
                numbers.remove(n)
                break
        if n in numbers:
            numbers.remove(n)
            break

# Filter adjacent dict for only gears with 2 adjacent numbers

real_gears = {k:v for k,v in adjacent.items() if len(v) == 2}
gear_ratios = [v[0][0] * v[1][0] for k,v in real_gears.items()]

dropstar(6, sum(gear_ratios), t)
