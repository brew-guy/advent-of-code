import time
from queue import PriorityQueue
import numpy as np
from helpers import *

t = time.time()

input = mypath + "d15-input.txt"
with open(input) as f:
    map = np.array([[int(c) for c in row] for row in f.read().split("\n")])

# Part 1
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


def path_sum(map, path):
    return sum(map[p[0]][p[1]] for p in path)


# My heuristics are broken... but whyyy?
def h(matrix, node, goal):
    # Manhattan distance heuristic
    # dx, dy = abs(node[0] - goal[0]), abs(node[1] - goal[1])
    # min_x, min_y = min(node[0], goal[0]), min(node[1], goal[1])
    # vertical = [(x, min_y) for x in range(min_x + 1, min_x + dx + 1)]
    # horizontal = [(min_x + dx, y) for y in range(min_y + 1, min_y + dy + 1)]
    # values = [matrix[x][y] for (x, y) in vertical + horizontal]
    # return sum(values)
    return 0


def adjacent(matrix, row, col):
    dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]  # N S E W
    adjacents = []
    for i in range(len(dx)):
        ax, ay = row + dy[i], col + dx[i]
        if min(ax, ay) >= 0 and ax < len(matrix) and ay < len(matrix[0]):
            adjacents.append((ax, ay))
    return adjacents


# https://en.wikipedia.org/wiki/A*_search_algorithm
def aStar(map, start, goal):
    open_set = PriorityQueue()
    open_set.put((1, start))
    came_from = {}
    # map with default value of infinity
    g_score = {(x, y): float("inf") for x, r in enumerate(map) for y, c in enumerate(r)}
    g_score[start] = 0

    f_score = g_score.copy()
    f_score[start] = h(map, start, goal)

    while not open_set.empty():
        current = open_set.get()[1]
        if current == goal:
            return reconstruct_path(came_from, current)
        neighbours = adjacent(map, *current)
        for nb in neighbours:
            tentative_g_score = g_score[current] + map[nb[0]][nb[1]]
            if tentative_g_score < g_score[nb]:
                came_from[nb] = current
                g_score[nb] = tentative_g_score
                f_score[nb] = tentative_g_score + h(map, nb, goal)
                if nb not in (x[1] for x in open_set.queue):
                    open_set.put((f_score[nb], nb))
    return "Problem: No path found!"


best_path = aStar(map, (0, 0), (99, 99))
best_path_sum = path_sum(map, best_path) - map[0][0]  # don't count start node

dropstar(29, best_path_sum, t)

# Part 2
def growMap(map, step):
    return np.array([[1 + ((val + step - 1) % 9) for val in row] for row in map])


# Expand the base map to 5 times size of increasing values
map_matrix = [[growMap(map, row + col) for col in range(5)] for row in range(5)]
map_rows = [np.concatenate(map_row, axis=1) for map_row in map_matrix]
big_map = np.concatenate(map_rows)

np.savetxt(mypath + "d15-big-map.txt", big_map, delimiter="", fmt="%d")

best_path = aStar(big_map, (0, 0), (499, 499))
best_path_sum = path_sum(big_map, best_path) - map[0][0]  # don't count start node

dropstar(30, best_path_sum, t)
