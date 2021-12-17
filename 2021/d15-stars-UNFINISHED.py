import time
import numpy as np
from helpers import *

t = time.time()

input = mypath + "d15-input.txt"
with open(input) as f:
    map = np.array([[int(c) for c in row] for row in f.read().split("\n")])

# Part 1
# From: https://levelup.gitconnected.com/dijkstras-shortest-path-algorithm-in-a-grid-eb505eb3a290
def walk(map):
    max_val = len(map)
    # Initialize auxiliary arrays
    distmap = np.ones((max_val, max_val), dtype=int) * np.Infinity
    distmap[0, 0] = 0
    originmap = np.ones((max_val, max_val), dtype=int) * np.nan
    visited = np.zeros((max_val, max_val), dtype=bool)
    finished = False
    x, y = 0, 0
    count = 0

    # Loop Dijkstra until reaching the target cell
    while not finished:
        # move to x+1,y
        if x < max_val - 1:
            if (
                distmap[x + 1, y] > map[x + 1, y] + distmap[x, y]
                and not visited[x + 1, y]
            ):
                distmap[x + 1, y] = map[x + 1, y] + distmap[x, y]
                originmap[x + 1, y] = np.ravel_multi_index([x, y], (max_val, max_val))
        # move to x-1,y
        if x > 0:
            if (
                distmap[x - 1, y] > map[x - 1, y] + distmap[x, y]
                and not visited[x - 1, y]
            ):
                distmap[x - 1, y] = map[x - 1, y] + distmap[x, y]
                originmap[x - 1, y] = np.ravel_multi_index([x, y], (max_val, max_val))
        # move to x,y+1
        if y < max_val - 1:
            if (
                distmap[x, y + 1] > map[x, y + 1] + distmap[x, y]
                and not visited[x, y + 1]
            ):
                distmap[x, y + 1] = map[x, y + 1] + distmap[x, y]
                originmap[x, y + 1] = np.ravel_multi_index([x, y], (max_val, max_val))
        # move to x,y-1
        if y > 0:
            if (
                distmap[x, y - 1] > map[x, y - 1] + distmap[x, y]
                and not visited[x, y - 1]
            ):
                distmap[x, y - 1] = map[x, y - 1] + distmap[x, y]
                originmap[x, y - 1] = np.ravel_multi_index([x, y], (max_val, max_val))

        visited[x, y] = True
        dismaptemp = distmap
        dismaptemp[np.where(visited)] = np.Infinity
        # now we find the shortest path so far
        minpost = np.unravel_index(np.argmin(dismaptemp), np.shape(dismaptemp))
        x, y = minpost[0], minpost[1]
        if x == max_val - 1 and y == max_val - 1:
            finished = True
        count = count + 1

    # Start backtracking to plot the path
    mattemp = map.astype(float)
    x, y = max_val - 1, max_val - 1
    path = []
    mattemp[int(x), int(y)] = np.nan

    while x > 0.0 or y > 0.0:
        path.append([int(x), int(y)])
        xxyy = np.unravel_index(int(originmap[int(x), int(y)]), (max_val, max_val))
        x, y = xxyy[0], xxyy[1]
        mattemp[int(x), int(y)] = np.nan
    path.append([int(x), int(y)])
    return str(distmap[max_val - 1, max_val - 1])


# print("The path length is: " + str(distmap[max_val - 1, max_val - 1]))
best_path = walk(map)

dropstar(29, best_path, t)

# Part 2
def growMap(map, step):
    return np.array([[1 + ((val + step - 1) % 9) for val in row] for row in map])


# Expand the base map to 5 times size of increasing values
map_matrix = [[growMap(map, row + col) for col in range(5)] for row in range(5)]
map_rows = [np.concatenate(map_row, axis=1) for map_row in map_matrix]
big_map = np.concatenate(map_rows)

np.savetxt(mypath + "d15-big-map.txt", big_map, delimiter="", fmt="%d")
# best_path = walk(big_map)

# dropstar(30, best_path, t)
