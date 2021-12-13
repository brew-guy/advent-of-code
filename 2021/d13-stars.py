import time, re
from helpers import *

t = time.time()

input = mypath + "d13-input.txt"
with open(input) as f:
    manual = f.read().split("\n\n")
paper = [[int(coord) for coord in line.split(",")] for line in manual[0].split("\n")]
foldings = manual[1].split("\n")

# Part 1
def getFolding(folding):
    regexp = r"fold along ([x|y])=([\d+]*)"
    axis, index = re.match(regexp, folding).groups()
    return axis, int(index)


def foldPaper(paper, axis, idx):
    if axis == "x":
        paper = [(2 * idx - x, y) if x > idx else (x, y) for (x, y) in paper]
    if axis == "y":
        paper = [(x, 2 * idx - y) if y > idx else (x, y) for (x, y) in paper]
    return sorted(set(paper))


fold = getFolding(foldings[0])
folded_paper = foldPaper(paper, *fold)

dropstar(25, len(folded_paper), t)

# Part 2
def makeGrid(paper):
    dim_x = max([x for (x, y) in paper]) + 1
    dim_y = max([y for (x, y) in paper]) + 1
    grid = [[" " for i in range(dim_x)] for j in range(dim_y)]
    for (x, y) in paper:
        grid[y][x] = chr(9632)
    return "\n".join(["".join(row) for row in grid])


folded_paper = paper.copy()
for folding in foldings:
    fold = getFolding(folding)
    folded_paper = foldPaper(folded_paper, *fold)

grid = makeGrid(folded_paper)
print(grid)

dropstar(26, "🎄🎄 Read the ASCII above 🎄🎄", t)
