import time
from helpers import *

t = time.time()

input = mypath + "d10-input.txt"
with open(input) as f:
    signals = f.read().split("\n")

# Part 1
# Read input as array of signals
# Build cycle array with 1 element per cycle, each element a register value during that cycle
#   If noop -> append last value once
#   If addx V -> append last value once and then append increased by V
# Index = after <index> cycle
# Index - 1 = during <index> cycle
# Calculate signal strengths with list comprehension

cycles = [1]
for signal in signals:
    if signal == "noop":
        cycles.append(cycles[-1])
    else:
        val = int(signal.split(" ")[1])
        cycles.append(cycles[-1])
        cycles.append(cycles[-1] + val)

peek = [20, 60, 100, 140, 180, 220]
signal_strengths = [cycles[cycle - 1] * cycle for cycle in peek]

dropstar(19, sum(signal_strengths), t)

# Part 2
# Convert cycles list to CRT output list
#   draw '#' if (register value - 1) <= index <= (register value + 1)
# Every CRT line index restarts at zero
# Break the CRT output in 6 (every 40), join to text and print
t = time.time()


def getPixel(beam_pos, register):
    return u"\u25A0" if (register - 1) <= beam_pos <= (register + 1) else "."


def splitList(list, n):
    return [list[i : i + n] for i in range(0, len(list), n)]


crt_cycles = [getPixel(i % 40, c) for i, c in enumerate(cycles[:-1])]
crt_output = ["".join(l) for l in splitList(crt_cycles, 40)]

print("\n".join(crt_output))

dropstar(20, "PLGFKAZG", t)
