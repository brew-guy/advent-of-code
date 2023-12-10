import time
from helpers import *

t = time.time()

input = mypath + "d14-input.txt"
with open(input) as f:
    scan = [[coord for coord in row.split(" -> ")] for row in f.read().split("\n")]
scan = [[tuple(map(int, c.split(","))) for c in row] for row in scan]

# Part 1
# Split input at linebreaks, then split lines into coord set tuples
# Find min/max values to define list dimensions
# Function that takes pairs of tuples and plot the lines they represent in a 2D list
# Set sand entry coord from list dimensions
# Function that drops sand grain and follows it until it comes to rest
#  or can only trickle out of the list boundaries
# Function to analyse the 3 possible coords below a sand grain

scan_x = [c[0] for r in scan for c in r]
scan_y = [c[1] for r in scan for c in r]
min_x, max_x, min_y, max_y = min(scan_x), max(scan_x), min(scan_y), max(scan_y)
cave = [["." for col in range(max_x - min_x + 1)] for row in range(max_y + 1)]


def draw_cave(cave_arr, stdout=True):
    output = "\n".join(["".join(row) for row in cave_arr])
    if stdout:
        print(output)
    else:
        return output


def plot_wall(tuple1, tuple2, cave_arr):
    [t1_x, t1_y], [t2_x, t2_y] = tuple1, tuple2
    for y in range(min(t1_y, t2_y), max(t1_y, t2_y) + 1):
        cave_arr[y][t1_x - min_x] = "#"
    for x in range(min(t1_x, t2_x) - min_x, max(t1_x, t2_x) - min_x + 1):
        cave_arr[t1_y][x] = "#"
    return cave_arr


def plot_rock(tuples_arr, cave_arr):
    for idx, tup in enumerate(tuples_arr[:-1]):
        plot_wall(tup, tuples_arr[idx + 1], cave_arr)
    return cave_arr


def grain_move(pos, cave_arr):
    x, y = pos
    if x < 0 or x > (max_x - min_x) or y >= max_y:
        return "Abyss", cave_arr

    try:
        if cave_arr[y + 1][x] == ".":
            return (x, y + 1), cave_arr
        if cave_arr[y + 1][x - 1] == ".":
            return (x - 1, y + 1), cave_arr
        if cave_arr[y + 1][x + 1] == ".":
            return (x + 1, y + 1), cave_arr
        return "Landed", cave_arr
    except:
        return "Abyss", cave_arr


def add_grain(cave_arr):
    sand_pos = (500 - min_x, 0)
    while True:
        next_pos, cave_arr = grain_move(sand_pos, cave_arr)
        if not next_pos in ["Abyss", "Landed"]:
            sand_pos = next_pos
        else:
            cave_arr[sand_pos[1]][sand_pos[0]] = "o"
            return next_pos, cave_arr


# Add rock walls to cave
for line in scan:
    plot_rock(line, cave)

# Simulate grains of sand dropping
cave_copy = [row[:] for row in cave]

step = 0
while True:
    status, cave_copy = add_grain(cave_copy)
    if status == "Abyss":
        break
    step += 1

draw_cave(cave_copy)

dropstar(27, step, t)

# Part 2
# Make a new copy of the cave array, extend with x 'air' cells to left + rigth
# Add a row of 'air' to bottom + a horizontal wall full length
# Adjust min/max values with the adjusted cave size
# Simulate grains until the map has a grain of landed sand in the init location
# Attempt: 23609 - too low
t = time.time()


def growCave(size, cave_arr):
    new = map(
        lambda row: ["." for _ in range(size)] + row + ["." for _ in range(size)],
        cave_arr,
    )
    return list(new)


def addCaveFloor(cave_arr):
    cave_arr.append(["." for _ in range(len(cave_arr[-1]))])
    cave_arr.append(["#" for _ in range(len(cave_arr[-1]))])
    return cave_arr


# Start new cave, expand it and add rock floor
cave_copy = [row[:] for row in cave]

expand_size = 170
cave_copy = growCave(expand_size, cave_copy)
cave_copy = addCaveFloor(cave_copy)

# Adjust the cave boundaries for the script
min_x -= expand_size
max_x += expand_size
max_y += 2

step = 0
while True:
    status, cave_copy = add_grain(cave_copy)
    if status == "Landed" and cave_copy[0][500 - min_x] == "o":
        break
    step += 1


cave_txt = draw_cave(cave_copy, False)
with open(mypath + "d14-part2-cave.txt", "w") as f:
    f.write(cave_txt)

dropstar(28, step + 1, t)
