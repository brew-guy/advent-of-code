import time
from helpers import *

t = time.time()

input = mypath + "d3-input.txt"
with open(input) as f:
    lines = f.read()

# Part 1
area = lines.split("\n")
area_height = len(area)
area_width = len(area[0])

row = col = 0
deltaCol = 3
deltaRow = 1
trees = 0

while row < area_height:
    position = area[row][col]
    if position == "#":
        trees += 1
    # print('{0} ({1},{2}) = {3} trees so far'.format(position, row, col, trees))
    col = col + deltaCol
    if col > area_width - 1:
        col = col - area_width
    row = row + deltaRow

dropstar(5, trees, t)

# Part 2
def slope(deltaCol, deltaRow):
    row = col = 0
    trees = 0
    while row < area_height:
        position = area[row][col]
        if position == "#":
            trees += 1
        # print('{0} ({1},{2}) = {3} trees so far'.format(position, row, col, trees))
        col = col + deltaCol
        if col > area_width - 1:
            col = col - area_width
        row = row + deltaRow
    return trees


multiplied = slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2)
dropstar(6, multiplied, t)
