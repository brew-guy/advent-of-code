import time, re
from helpers import *

t = time.time()

# input = mypath + "d18-example.txt"
input = mypath + "d18-input.txt"
with open(input) as f:
    plan = f.read().splitlines()

# Sum of tuples
def tuplesum(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

edges = [(0, 0)]
node = (0, 0)
# Part 1
for line in plan:
    d, l, c = line.split(" ")
    for i in range(int(l)):
        node = tuplesum(node, directions[d])
        edges.append(node)

# Normalize
min_x = min([x for x, y in edges])
min_y = min([y for x, y in edges])
edges = [(x - min_x, y - min_y) for x, y in edges]

# flood fill algorithm
def flood_fill(edges, node, visited):
    visited.add(node)
    for d in directions.values():
        new_node = tuplesum(node, d)
        if new_node in edges and new_node not in visited:
            flood_fill(edges, new_node, visited)
    return visited

filled = flood_fill(edges, (1, 1), set())

print(len(filled))

# dropstar(35, hash_sum, t)


# Part 2

# dropstar(36, focal_strength, t)

