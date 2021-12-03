import time, re
from helpers import *

t = time.time()

input = mypath + "d23-input.txt"
with open(input) as f:
    instructions = f.read().split("\n")

# Part 1
print(instructions)
opcode = "jie a, +4"
regexp = r"(\w*) (\w*)(, (.*))?"
match = re.match(regexp, opcode)
match.groups()

# dropstar(45, , t)

# Part 2

# dropstar(46, , t)
