# Day 8 - Part 2

import time
startTime = time.time()

# Read instruction lines to array
input = "d8-input.txt"
with open(input) as f:
	program = f.read().splitlines()
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
    trail.append(['line:{0} op:{1} arg:{2} acc:{3}'.format(line, op, arg, acc)])
    if op == 'acc':
      acc += arg
      line += 1
    elif op == 'jmp':
      line += arg
    elif op == 'nop':
      line += 1
    if line in linesrun:
      # print('Break: Instruction {0} caused code to repeat on line {1}.'.format(trail[-1], line))
      return [acc, line, linesrun, trail, 'looped']
    else:
      linesrun.add(line)
    if line > len(program):
      # print('*** Program terminated normally ***')
      return [acc, line, linesrun, trail, 'completed']

# Run program with changes, one possible line changed per run
for i in range(0, len(program)):
  program = backup.copy()
  if 'jmp' in program[i]:
    program[i] = program[i].replace('jmp', 'nop')
  elif 'nop' in program[i]:
    program[i] = program[i].replace('nop', 'jmp')
  output = pressplay(program)
  if output[4] == 'completed':
    print('Acc was {0} when program {1} on line {2} after {3} instructions. Last instruction was {4}'.format(output[0], output[4], output[1], len(output[2]), output[3][-1]))
    print('Op replaced on line {0} = {1}'.format(i+1, program[i]))

# print("Accumulator was {0} when program terminated on line {1} after running {2} lines of code.".format(output[0], output[1], len(output[2])))
print('Execution time in seconds: {0}'.format(time.time() - startTime))