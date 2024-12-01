import time
from helpers import *

t = time.time()

input = mypath + "d16-example.txt"
# input = mypath + "d16-input.txt"
with open(input) as f:
    cave = [list(c) for c in f.read().split("\n")]

print(cave[0])
# Part 1
    
class Node:
    def __init__(self, x, y, cave):
        self.x = x
        self.y = y
        self.cave = cave
        self.tile = self.cave[x][y]
        self.parent = None

class Path:
    def __init__(self, start):
        self.start = start
        self.open = [start]
        self.path = []
        self.current = None
        self.nodes = []
            

# dropstar(31, hash_sum, t)


# Part 2

# dropstar(32, focal_strength, t)

