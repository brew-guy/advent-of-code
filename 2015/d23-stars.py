import time
from helpers import *

t = time.time()

input = mypath + "d23-input.txt"
with open(input) as f:
    program = [op.replace(",", "").split() for op in f.read().split("\n")]

logging = False
log = lambda line: print(line) if logging else None

# Part 1
def parse(arg):
    # arg conversion/testing
    if "+" in arg:
        return int(arg[1:])
    if "-" in arg:
        return -int(arg[1:])
    if arg.isnumeric():
        return int(arg)
    return arg


def evaluate(cell):
    operation, arg_1 = cell[:2]
    arg_2 = cell[2] if len(cell) > 2 else None
    actions = {
        "hlf": lambda x: f"{x} /= 2",
        "tpl": lambda x: f"{x} = {x} * 3",
        "inc": lambda x: f"{x} += 1",
        "jmp": lambda x: f"op += {x} - 1",
        "jie": lambda x, y: f"op += {y} - 1 if {x} % 2 == 0 else 0",
        "jio": lambda x, y: f"op += {y} - 1 if {x} == 1 else 0",
    }
    try:
        result = actions[operation](parse(arg_1), parse(arg_2))
        log(f"{operation, result}")
    except:
        try:
            result = actions[operation](parse(arg_1))
            log(f"{operation, result}")
        except:
            result = "** Bad operation **"
    return result


i, a, b, op = 1, 0, 0, 0
while op < len(program):
    oper = program[op]
    log(f"Step {i} | a: {a} | b: {b} | op: {op}")
    exec(evaluate(oper))
    op += 1
    i += 1
    log(f"Step {i} | a: {a} | b: {b} | op: {op}" + "\n")

dropstar(45, b, t)

# Part 2
i, a, b, op = 1, 1, 0, 0
while op < len(program):
    oper = program[op]
    log(f"Step {i} | a: {a} | b: {b} | op: {op}")
    exec(evaluate(oper))
    op += 1
    i += 1
    log(f"Step {i} | a: {a} | b: {b} | op: {op}" + "\n")

dropstar(46, b, t)
