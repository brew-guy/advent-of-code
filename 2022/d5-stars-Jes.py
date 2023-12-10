import re, copy
import time
from helpers import *

t = time.time()

input = mypath + "d5-input.txt"
with open(input) as f:
    data = f.read().split("\n")

# Part 1
# Read initial stacks:
#  Read first x lines to list and stop when line starts with " 1"
#  Split each stack string to list in 4 letters
#  Remove [] and whitespace from each element in array
#  Transpose 2D list (confirm orientation is as expected)
#  Remove empty places in stacks
#  Store stacks in dict keys 1-9
# Read crane instructions:
#  Following lines from idx+2 to end
# Function to make instruction string to tuple
# Function to move cargo between stacks

idx, stacks = 0, []
while data[idx][:2] != " 1":
    stacks.append(data[idx])
    idx += 1

stacks = [[row[idx : idx + 4] for idx in range(0, len(row), 4)] for row in stacks]
stacks = [[re.sub("[\[\] ]", "", el) for el in row] for row in stacks]
stacks = [list(x) for x in zip(*stacks)]
stacks = {idx + 1: [el for el in stack if el != ""] for idx, stack in enumerate(stacks)}
stacks_copy = copy.deepcopy(stacks)

instructions = data[idx + 2 :]


def getCraneMove(moveString):
    moves = re.search("move (\d+) from (\d+) to (\d+)", moveString).groups()
    return (int(move) for move in moves)


def moveCargo(craneMoves):
    n, a, b = craneMoves
    for i in range(n):
        stacks[b].insert(0, stacks[a].pop(0))


for move in instructions:
    moveCargo(getCraneMove(move))

topCrates = "".join([stacks[i][0] for i in range(1, 10)])

dropstar(9, topCrates, t)

# Part 2
# Reset stacks
# New function to move elements in blocks between stacks


def moveCargo9001(craneMoves):
    n, a, b = craneMoves
    crates = stacks[a][:n]
    stacks[a] = stacks[a][n:]
    stacks[b] = crates + stacks[b]


stacks = copy.deepcopy(stacks_copy)

for move in instructions:
    moveCargo9001(getCraneMove(move))

topCrates = "".join([stacks[i][0] for i in range(1, 10)])

dropstar(10, topCrates, t)
