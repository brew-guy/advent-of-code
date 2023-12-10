import time, re, math
from helpers import *

t = time.time()

# input = mypath + "d8-example3.txt"
input = mypath + "d8-input.txt"
with open(input) as f:
    instructions = f.read()

# Part 1

def parse_instruction(instruction: str) -> tuple:
    return re.match(r"(\w+) = \((\w+), (\w+)\)", instruction).groups()

# Based on step integer, return the next direction from the directions string
# repeat endlessly from beginning of string
def next_direction(step: int, directions: str) -> str:
    return directions[step % len(directions)]

# Split input into directions and map
directions, map_block = instructions.split("\n\n")
map_rows = map_block.split("\n")
# Create dict for map of node: (left, right)
map = {node: (left, right) for node, left, right in [parse_instruction(instruction) for instruction in map_rows]}

step, node = 0, 'AAA'
while node != 'ZZZ':
    dir = next_direction(step, directions)
    dir_index = 0 if dir == "L" else 1
    navigation = map[node]
    node = navigation[dir_index]
    # print(f"Step {step}: {dir} -> {node}")
    step += 1

dropstar(15, step, t)


# Part 2
# Tried running the above code simultaneously for all nodes that end with A but it took too long
# Tried running individual nodes that start with A and look for patterns in the steps when they
# arrive at nodes that end with Z
# Found that each node keeps returning to the same node that ends with Z in an endlessloop
# The solution must be to find a common denominator for step counts as that should bring them all
# to a Z node at the same point in time
# 
# Guess 1: 153341838310440 - too high

nodes_end_with_A = [node for node, navigation in map.items() if node[2] == 'A']

z_steps = []
nodes = nodes_end_with_A
for i, node in enumerate(nodes):
    step = 0
    z_hits, z_step_list = 0, []
    while node[2] != 'Z' or z_hits < 2:
        dir = next_direction(step, directions)
        dir_index = 0 if dir == "L" else 1
        navigation = map[node]
        node = navigation[dir_index]
        step += 1
        if node[2] == 'Z':
            z_hits += 1
            z_step_list.append(step)
    z_steps.append(z_step_list)

# Find the lowest common denominator for all step counts

s = [z[1]-z[0] for z in z_steps]

dropstar(16, math.lcm(*s), t)

