import time, re
from bitarray import bitarray
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from helpers import *

t = time.time()

input = mypath + "d6-input.txt"
with open(input) as f:
    instructions = f.read().split("\n")

# Part 1
def getInstruction(instr):
    regexp = re.compile(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)")
    match = re.match(regexp, instr).groups()
    action = match[0]
    x1 = int(match[1])
    y1 = int(match[2])
    x2 = int(match[3])
    y2 = int(match[4])
    return (action, (x1, y1, x2, y2))


def getBitmask(x1, y1, x2, y2):
    xmask = (
        bitarray("0") * (x1 - 1)
        + bitarray("1") * (x2 - x1 + 1)
        + bitarray("0") * (1000 - x2)
    )
    mask = (
        bitarray("0") * 1000 * (y1 - 1)
        + xmask * (y2 - y1 + 1)
        + bitarray("0") * 1000 * (1000 - y2)
    )
    return mask


grid = bitarray("0") * 1000 * 1000

for instr in instructions:
    action, coordset = getInstruction(instr)
    mask = getBitmask(*coordset)
    if action == "turn on":
        grid = grid | mask
    if action == "turn off":
        grid = grid & ~mask
    if action == "toggle":
        grid = grid ^ mask

dropstar(11, sum(grid), t)

# What it looks like in pixels
data = [int(bit) for bit in grid]
plt.imsave(
    mypath + "d6-lightshow-1.png", np.array(data).reshape(1000, 1000), cmap=cm.gray
)

# Part 2
grid = np.zeros(1000 * 1000)


def getNumericMask(x1, y1, x2, y2):
    xmask = [0] * (x1 - 1) + [1] * (x2 - x1 + 1) + [0] * (1000 - x2)
    mask = [0] * 1000 * (y1 - 1) + xmask * (y2 - y1 + 1) + [0] * 1000 * (1000 - y2)
    return np.array(mask)


for instr in instructions:
    action, coordset = getInstruction(instr)
    mask = getNumericMask(*coordset)
    if action == "turn on":  # Increase 1
        grid = grid + mask
    if action == "turn off":  # Decrease 1, min 0
        grid = grid - mask
        grid = np.where(grid < 0, 0, grid)
    if action == "toggle":  # Increase 2
        grid = grid + (mask * 2)

dropstar(12, int(sum(grid)), t)

# What it looks like in pixels
data = [int(bit) for bit in grid]
plt.imsave(
    mypath + "d6-lightshow-2.png", np.array(data).reshape(1000, 1000), cmap=cm.gray
)
