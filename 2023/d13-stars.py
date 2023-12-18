import time
from helpers import *

t = time.time()

# input = mypath + "d13-example.txt"
input = mypath + "d13-input.txt"
with open(input) as f:
    patterns = [p.split("\n") for p in f.read().split("\n\n")]

# Part 1

# Check a string for symmetry across any vertical line between characters
# Return a list of indices where symmetry occurs
def v_sym(string: str) -> list[int]:
    return [i for i in range(0, len(string)//2) if string[:i*2+2] == string[:i*2+2][::-1]]

# Check string for symmetry from boths ends
# Return a set of indices where symmetry occurs
def row_v_sym(string: str) -> set[int]:
    forward = v_sym(string)
    reverse = [len(string) - i - 2 for i in v_sym(string[::-1])]
    return set(forward) | set(reverse)

# Check a block of strings for vertical symmetry
def block_v_sym(block: list[str]) -> set[int]:
    return set.intersection(*[row_v_sym(row) for row in block])

# Transpose a 2D array counter
def transpose(block: list[str]) -> list[str]:
    return ["".join([row[i] for row in block]) for i in range(len(block[0]))]

# Loop over blocks and check for vertical and horizontal symmetry
symmetries = []
for block in patterns:
    v_syms = block_v_sym(block)
    h_syms = block_v_sym(transpose(block))
    symmetries.append((v_syms, h_syms))

# symmetries = [(block_v_sym(block), block_v_sym(transpose(block))) for block in patterns]

v_sums = sum([sum(v) + 1 if v else 0 for v, h in symmetries])
h_sums = sum([sum(h) + 1 if h else 0 for v, h in symmetries])

# print(symmetries)
dropstar(25, 100 * h_sums + v_sums, t)


# Part 2

# Invert a character in a block and return the 'fixed' block
def invert_block_char(block: list[str], char: int) -> list[str]:
    x = char // len(block[0])
    y = char % len(block[0])
    # replace char at x, y with inverse character
    inv = "#" if block[x][y] == "." else "."
    return [row[:y] + inv + row[y+1:] if i == x else row for i, row in enumerate(block)]

# Expect more symmetries per dimension, so collect all
new_symmetries = []
for block in patterns:
    fixed_v_syms, fixed_h_syms = set(), set()
    for i in range(len(block[0]) * len(block)):
        fixed_block = invert_block_char(block, i)
        v_syms, h_syms = block_v_sym(fixed_block), block_v_sym(transpose(fixed_block))
        fixed_v_syms, fixed_h_syms = fixed_v_syms.union(v_syms), fixed_h_syms.union(h_syms)
    new_symmetries.append((fixed_v_syms, fixed_h_syms))

# print(new_symmetries)

# Calculate the number of fixed symmetries and subtract the original numbers from part 1
fixed_v_sums = sum([sum(v) + len(v) if v else 0 for v, h in new_symmetries]) - v_sums
fixed_h_sums = sum([sum(h) + len(h) if h else 0 for v, h in new_symmetries]) - h_sums


dropstar(26, 100 * fixed_h_sums + fixed_v_sums, t)

