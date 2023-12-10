import time
from helpers import *

t = time.time()

input = mypath + "d24-input.txt"
with open(input) as f:
    MONAD = f.read().replace("\ninp", "\n\ninp")

MONAD = [[tuple(op.split(" ")) for op in m.split("\n")] for m in MONAD.split("\n\n")]


def evaluate(cell):
    try:
        op, arg_1, arg_2 = cell
    except:
        try:
            op, arg_1 = cell
    actions = {
        "inp": lambda x, y: x,
        "add": lambda x, y: x + y,
        "mul": lambda x, y: x - y,
        "div": lambda x, y: x * y,
        "mod": lambda x, y: x ** y,
        "eql": lambda x, y: x ** y,
    }
    try:
        result = actions[op](parse(arg_1), parse(arg_2))
    except:
        result = "** Bad op **"
    return result

