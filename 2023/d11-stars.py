import time
from helpers import *

t = time.time()

# input = mypath + "d11-example.txt"
input = mypath + "d11-input.txt"
with open(input) as f:
    sky = f.read().split("\n")

# Part 1

# Transpose a 2D array of strings
def transpose(array):
    return ["".join([row[i] for row in array]) for i in range(len(array[0]))]

def find_galaxies(sky):
    galaxies = []
    for r, row in enumerate(sky):
        for c, char in enumerate(row):
            if char == "#":
                galaxies.append((r, c))
    return galaxies

# # Function to calculate distance between two points in grid
# # when moving only vertically or horizontally, ie. Manhattan distance
def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def galaxy_distances(galaxies):
    distances = []
    for i, g in enumerate(galaxies[:-1]):
        for j in range(i+1, len(galaxies)):
            distances.append(distance(g, galaxies[j]))
    return distances

# Identify rows and columns in sky that are completely empty ie. only has dots
empty_rows_in_sky = [r for r, row in enumerate(sky) if row == "." * len(row)]
empty_cols_in_sky = [c for c, col in enumerate(transpose(sky)) if col == "." * len(col)]

# Adapt each galaxy coordinate to the new sky
# Ie. add 2 to row and 2 to column for each blank space before it
expansion = 2
galaxies = find_galaxies(sky)

def expand_galaxies(galaxies, expansion):
    new_galaxies = []
    for g in galaxies:
        empty_rows_before = sum([1 for r in empty_rows_in_sky if r < g[0]])
        empty_cols_before = sum([1 for c in empty_cols_in_sky if c < g[1]])
        new_row = g[0] + empty_rows_before * expansion - empty_rows_before if empty_rows_before > 0 else g[0]
        new_col = g[1] + empty_cols_before * expansion - empty_cols_before if empty_cols_before > 0 else g[1]
        new_galaxies.append((new_row, new_col))
    return new_galaxies

new_galaxies = expand_galaxies(galaxies, expansion)

dropstar(21, sum(galaxy_distances(new_galaxies)), t)


# Part 2

# Adapt each galaxy coordinate to the new sky
# Ie. add 1000000 to row and 100000 to column for each blank space before it

expansion = 1000000
new_galaxies = expand_galaxies(galaxies, expansion)

dropstar(22, sum(galaxy_distances(new_galaxies)), t)


