import time
from helpers import *

t = time.time()

input = mypath + "d8-input.txt"
with open(input) as f:
    program = f.read().splitlines()

# Part 1
acc = 0
line = 1
linesrun = {line}
run = True

# Run program
while run:
    instr = program[line - 1].split()
    op = instr[0]
    arg = int(instr[1])
    if op == "acc":
        acc += arg
        line += 1
    elif op == "jmp":
        line += arg
    elif op == "nop":
        line += 1
    if line in linesrun:
        run = False
    else:
        linesrun.add(line)

dropstar(15, acc, t)

# Part 2
backup = program.copy()

# Compiler(ish) function
def pressplay(program):
    acc = 0
    line = 1
    linesrun = {line}
    trail = []
    while True:
        instr = program[line - 1].split()
        op = instr[0]
        arg = int(instr[1])
        trail.append(["line:{0} op:{1} arg:{2} acc:{3}".format(line, op, arg, acc)])
        if op == "acc":
            acc += arg
            line += 1
        elif op == "jmp":
            line += arg
        elif op == "nop":
            line += 1
        if line in linesrun:
            # print('Break: Instruction {0} caused code to repeat on line {1}.'.format(trail[-1], line))
            return [acc, line, linesrun, trail, "looped"]
        else:
            linesrun.add(line)
        if line > len(program):
            # print('*** Program terminated normally ***')
            return [acc, line, linesrun, trail, "completed"]


# Run program with changes, one possible line changed per run
for i in range(0, len(program)):
    program = backup.copy()
    if "jmp" in program[i]:
        program[i] = program[i].replace("jmp", "nop")
    elif "nop" in program[i]:
        program[i] = program[i].replace("nop", "jmp")
    output = pressplay(program)
    if output[4] == "completed":
        acc = output[0]

dropstar(16, acc, t)

