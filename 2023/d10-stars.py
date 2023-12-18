import time
from helpers import *

t = time.time()

# input = mypath + "d10-example1.txt"
input = mypath + "d10-input.txt"
with open(input) as f:
    maze = f.readlines()

# Part 1
# Find S in the maze and get its coordinates
# S only connects to 2 other points
# Pick one of the points and follow the path, never going back
# Count number of steps until back at S

for r, line in enumerate(maze):
    for c, char in enumerate(line):
        if char == "S":
            start = (r, c)
            break

# Empty array same size as maze
clean_maze = [["." for c in range(len(maze[0]))] for r in range(len(maze))]

# Define the pipe types and their exits
pipes = {
    "|": [(1,0), (-1,0)],
    "-": [(0,1), (0,-1)],
    "L": [(-1,0), (0,1)],
    "J": [(-1,0), (0,-1)],
    "7": [(1,0), (0,-1)],
    "F": [(1,0), (0,1)],
    }

replace = {
    "|": "│",
    "-": "─",
    "L": "└",
    "J": "┘",
    "7": "┐",
    "F": "┌",
    "S": "S",
    " ": " ",
    "\n": "",
    ".": ".",
    }

pretty_maze = "\n".join(["".join([replace[c] for c in r]) for r in maze])

# Output a prettified maze to a file
with open(mypath + "d10-output1.txt", "w", encoding="utf-8") as f:
    f.write(pretty_maze)

# Set the underlying pipe type on the start position
start_pipe = "|"
maze[start[0]] = maze[start[0]][:start[1]] + start_pipe + maze[start[0]][start[1]+1:]

def neg(t):
    return tuple(-i for i in t)

def add_tuples(t1, t2):
    return tuple(sum(i) for i in zip(t1, t2))

def get_exits(position, pipe):
    way1, way2 = pipes[pipe]
    exit1 = add_tuples(position, way1)
    exit2 = add_tuples(position, way2)
    return exit1, exit2

position = start
path = [start]
while True:
    r, c = position
    pipe = maze[r][c]
    # clean_maze[r][c] = " "
    clean_maze[r][c] = replace[pipe]
    exits = get_exits(position, pipe)
    if len(path) == 1:
        position = exits[0]
    else:
        position = exits[0] if exits[1] == path[-2] else exits[1]
    if position == start:
        break
    path.append(position)

trimmed_maze = "\n".join(["".join(r) for r in clean_maze])

# Output trimmed_maze to a file
with open(mypath + "d10-output2.txt", "w", encoding="utf-8") as f:
    f.write(trimmed_maze)

dropstar(19, len(path)/2, t)

# Part 2
# Flood fill the maze from (0,0) to find all points that are connected




    

# dropstar(20, sum(extrapolated), t)

