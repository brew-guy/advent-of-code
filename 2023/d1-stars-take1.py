import time, re
from helpers import *

t = time.time()

input = mypath + "d1-input.txt"
with open(input) as f:
    lines = f.read().split("\n")

# Part 1
# Extract digits from each line and take first and last digit
digits = [[d for d in l if d.isdigit()] for l in lines]
two_digits = [int(d[0]+d[-1]) for d in digits]

dropstar(1, sum(two_digits), t)

# Part 2
# Careful only to replace first and last occurrence of spelled digit
# E.g. "eightwothree" is dangerous as eight and two overlap
# Order of replacement is important; from start, then end
# First try: 54419 (too high)
# Second try: 54251 (too high)
# Third try: 54204 (too low)
# Fourth try: 54169 (too low)
# Fifth try: 54235
# Revelation:
# Turns out overlapping spelled digits are allowed so I need to scan
# and keep a list of digits separately

# map of spelled digits to their corresponding int
spelled_digits = {"one": 1, "two": 2, "three": 3, "four": 4,
                "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

# search string from first letter for first occurrence of spelled digit
# and replace it with its corresponding int
def replace_first(string):
    for i,l in enumerate(string):
        for key in spelled_digits.keys():
            if string[i:].startswith(key):
                string = string.replace(key, str(spelled_digits[key]), 1)
                return string
    return string

# search string from last letter for first occurrence of spelled digit
# and replace it with its corresponding int
def replace_last(string):
    for i,l in enumerate(string):
        for key in spelled_digits.keys():
            if string[:len(string)-i].endswith(key):
                string = string[::-1].replace(key[::-1], str(spelled_digits[key]), 1)[::-1]
                return string
    return string

# Replace first and last occurrence of spelled digit in each line
replaced_lines = [replace_last(replace_first(l)) for l in lines]

# Extract digits from each line and take first and last digit
digits = [[d for d in l if d.isdigit()] for l in replaced_lines]
two_digits = [int(d[0]+d[-1]) for d in digits]

zipped = list(zip(lines, replaced_lines, two_digits))
printable = "\n".join([str(z) for z in zipped]
    + ["\n\nSum of digits: " + str(sum(two_digits))])
                      
output = mypath + "d1-output.txt"
with open(output, "w") as f:
    f.write(printable)

dropstar(2, sum(two_digits), t)
