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
# Turns out overlapping spelled digits are allowed so I need to scan
# and keep a list of digits separately

# map of spelled digits to their corresponding int
spelled_digits = {"one": 1, "two": 2, "three": 3, "four": 4,
                "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

# search string from first letter for first occurrence of spelled digit
# and replace it with its corresponding int
def replace_by_scan(string):
    new_string = ""
    for i,l in enumerate(string):
        if l.isdigit():
            new_string += l
            continue
        for key in spelled_digits.keys():
            if string[i:].startswith(key):
                new_string += str(spelled_digits[key])
                continue
    return new_string

# Replace first and last occurrence of spelled digit in each line
replaced_lines = [replace_by_scan(l) for l in lines]

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
