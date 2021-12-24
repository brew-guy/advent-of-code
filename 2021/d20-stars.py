import time
from helpers import *

t = time.time()

input = mypath + "d20-input.txt"
with open(input) as f:
    image = [d for d in f.read().split("\n\n")]

enhancer = image[0]
map = [row for row in image[1].split("\n")]

# Part 1
def addPadding(map, width):
    char = "."
    map_width = len(map[0])
    padding_rows = [char * (2 * width + map_width)] * width
    map = [char * width + row + char * width for row in map]
    map = padding_rows + map + padding_rows
    return map


def enhancePixel(matrix, row, col):
    block = "".join([matrix[r][col - 1 : col + 2] for r in range(row - 1, row + 2)])
    value = int(block.replace(".", "0").replace("#", "1"), 2)
    return enhancer[value]


def enhanceImage(map):
    h, w = len(map), len(map[0])
    map = [[enhancePixel(map, r, c) for c in range(1, w - 1)] for r in range(1, h - 1)]
    map = ["".join(row) for row in map]
    return map


countPixels = lambda map: sum([c == "#" for r in map for c in r])
pprint = lambda map: print("\n".join(map), "\n")

map = addPadding(map, 4)
for i in range(2):
    map = enhanceImage(map)

dropstar(39, countPixels(map), t)

# Part 2

map = addPadding(map, 100)
for i in range(50):
    map = enhanceImage(map)

dropstar(40, countPixels(map), t)
