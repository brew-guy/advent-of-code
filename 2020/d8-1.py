# Day 8 - Part 1

import time
startTime = time.time()

# Read instruction lines to array
input = "d8-input.txt"
with open(input) as f:
	program = f.read()[:-1].splitlines()

acc = 0
line = 1
linesrun = {line}
run = True

# Run program
while run:
  instr = program[line - 1].split()
  op = instr[0]
  arg = int(instr[1])
  if op == 'acc':
    acc += arg
    line += 1
  elif op == 'jmp':
    line += arg
  elif op == 'nop':
    line += 1
  if line in linesrun:
    run = False
  else:
    linesrun.add(line)

print("Accumulator was {0} when program looped back on line {1} after running {2} lines of code.".format(acc, line, len(linesrun)))
print('Execution time in seconds: {0}'.format(time.time() - startTime))