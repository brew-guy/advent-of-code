import os, sys

path = os.path.join(sys.path[0], "d1-input-1.txt")
with open(path, mode="r") as f:
    lines = f.readlines()

# Part 1
directions = lines[0]
floor = directions.count("(") - directions.count(")")

print(f"Star 1: {floor}")

# Part 2
dirs = {"(": 1, ")": -1}
floor = 0
for index, direction in enumerate(directions):
    floor += dirs[direction]
    if floor == -1:
        break

print(f"Star 2: {index + 1}")
