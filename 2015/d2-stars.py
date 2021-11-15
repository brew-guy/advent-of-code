import os, sys

path = os.path.join(sys.path[0], "d2-input-1.txt")
with open(path, mode="r") as f:
    lines = f.readlines()

dimensions = [sorted(list(map(int, l.strip().split("x")))) for l in lines]

# Part 1
paper = 0
for dims in dimensions:
    l, w, h = dims
    paper += 2 * l * w + 2 * w * h + 2 * h * l + l * w

print(f"Star 3: {paper}")

# Part 2
ribbon = 0
for dims in dimensions:
    l, w, h = dims
    ribbon += 2 * l + 2 * w + l * w * h

print(f"Star 4: {ribbon}")
