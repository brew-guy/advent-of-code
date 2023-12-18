import time, re
from helpers import *

t = time.time()

# input = mypath + "d15-example.txt"
input = mypath + "d15-input.txt"
with open(input) as f:
    init_seq = f.read().split(",")

# Part 1

def hash(seq_string: str) -> int:
    hash = 0
    for c in seq_string:
        hash = (hash + ord(c)) * 17 % 256
    return hash

hash_sum = sum([hash(i) for i in init_seq])

dropstar(29, hash_sum, t)


# Part 2
# 256 boxes (0-255)
# Lenses of strength 1-9 (1-9)
# Boxes can hold 0-any number of lenses
# Strings = lens labels
# Strings hash = box number

# Parses string to tuple of lens label, operator, focal length
def parse_string(seq_string: str) -> tuple:
    return re.match(r"(\w+)([=-])(\d*)", seq_string).groups()

# Function that checks if list has any tuple where first element equeals value, return index
def check_list(list: list, value: str) -> int:
    for i in list:
        if i[0] == value:
            return list.index(i)

# Create a list of empty boxes
boxes = [[] for i in range(256)]

# Loop through init_seq and add or remove lenses from boxes
for i in init_seq:
    lens_label, op, focal_length = parse_string(i)
    box = hash(lens_label)
    lens_index = check_list(boxes[box], lens_label)
    match op:
        case "=":
            if lens_index != None:
                boxes[box][lens_index] = (lens_label, focal_length)
            else:
                boxes[box].append((lens_label, focal_length))
        case "-":
            if lens_index != None:
                boxes[box].pop(lens_index)

# Calculate focal strength
focal_strength = 0
for b, box in enumerate(boxes):
    for l, lens in enumerate(box):
        focal_strength += (b + 1) * (l + 1) * int(lens[1])

dropstar(30, focal_strength, t)

