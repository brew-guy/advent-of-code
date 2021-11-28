import time, re, itertools
from helpers import *

t = time.time()

input = mypath + "d9-input.txt"
with open(input) as f:
    routes = f.read().split("\n")

# Part 1
def getCities(route):
    regexp = r"^([A-Za-z]*) to ([A-Za-z]*) = ([0-9]*)$"
    match = re.match(regexp, route)
    return match[1], match[2], match[3]


# Unique cities list
def getUniqueCityList(routes):
    c_list = []
    for route in routes:
        city1, city2, distance = getCities(route)
        if not city1 in c_list:
            c_list.append(city1)
        if not city2 in c_list:
            c_list.append(city2)
    return c_list


# Convert city distances to distance matrix
def getDistanceMatrix(routes, city_list):
    matrix = [[0 for i in range(len(city_list))] for j in range(len(city_list))]
    for route in routes:
        city1, city2, distance = getCities(route)
        matrix[city_list.index(city1)][city_list.index(city2)] = int(distance)
        matrix[city_list.index(city2)][city_list.index(city1)] = int(distance)
    return matrix


def getDistance(route):
    dist = 0
    for r in range(len(route) - 1):
        c1, c2 = route[r], route[r + 1]
        c1_idx, c2_idx = city_list.index(c1), city_list.index(c2)
        dist += graph[c1_idx][c2_idx]
    return dist


# TSP algorithm from https://www.geeksforgeeks.org/travelling-salesman-problem-implementation-using-backtracking/
# def tsp(graph, v, currPos, n, count, cost):
#     # if count == n and graph[currPos][0]:
#     #     answer.append(cost + graph[currPos][0])
#     if count == n:
#         answer.append(cost)
#         return
#     for i in range(n):
#         if v[i] == False and graph[currPos][i]:
#             v[i] = True
#             tsp(graph, v, i, n, count + 1, cost + graph[currPos][i])
#             v[i] = False


# n = len(graph)
# v = [False for i in range(n)]
# v[0] = True
# answer = []
# tsp(graph, v, 0, n, 1, 0)
# print(min(answer))

# Generate all possible routes and calculate distances
city_list = getUniqueCityList(routes)
graph = getDistanceMatrix(routes, city_list)

all_possible_routes = itertools.permutations(city_list, len(city_list))
distances = [getDistance(route) for route in all_possible_routes]

dropstar(17, min(distances), t)

# Part 2

dropstar(18, max(distances), t)
