import time
from helpers import *

t = time.time()

input = mypath + "d24-input.txt"
with open(input) as f:
    MONAD = f.read().replace("\ninp", "\n\ninp")

MONAD = [[tuple(op.split(" ")) for op in m.split("\n")] for m in MONAD.split("\n\n")]

# Part 1
vars = {"w": 0, "x": 0, "y": 0, "z": 0}
num = 9
for instr in MONAD[0]:
    op = instr[0]
    if op == "inp":
        vars[instr[1]] = num
    if op == "add": 
    # print(instr)

# dropstar(47, , t)

# Part 2

# dropstar(48, , t)
