import time, re
from helpers import *

t = time.time()

input = "d9-input.txt"
with open(input) as f:
    routes = f.read().split("\n")

# Part 1
def getDistance(route):
    regexp = r"^([A-Za-z]*) to ([A-Za-z]*) = ([0-9]*)$"
    match = re.match(re.compile(regexp), route)
    return match[1], match[2], match[3]


# Unique cities list
city_list = []
for route in routes:
    city1, city2, distance = getDistance(route)
    if not city1 in city_list:
        city_list.append(city1)
    if not city2 in city_list:
        city_list.append(city2)

# Convert city distances to distance matrix
graph = [[0 for i in range(len(city_list))] for j in range(len(city_list))]
for route in routes:
    city1, city2, distance = getDistance(route)
    graph[city_list.index(city1)][city_list.index(city2)] = int(distance)
    graph[city_list.index(city2)][city_list.index(city1)] = int(distance)


# TSP algorithm from https://www.geeksforgeeks.org/travelling-salesman-problem-implementation-using-backtracking/
def tsp(graph, v, currPos, n, count, cost, trace=[]):
    # if count == n and graph[currPos][0]:
    #     answer.append(cost + graph[currPos][0])
    if count == n:
        answer.append(cost)
        traces.append(trace)
        trace = []
        return
    for i in range(n):
        if v[i] == False and graph[currPos][i]:
            v[i] = True
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i], trace)
            v[i] = False


n = len(graph)
v = [False for i in range(n)]
v[0] = True
answer = []
traces = []
tsp(graph, v, 0, n, 1, 0)
print(len(answer))
print(len(traces[0]))
dropstar(17, min(answer), t)

# Part 2
# 1st guess: 860 - too low
# 2nd guess: 985 - too high

v = [False for i in range(n)]
v[0] = True
answer = []
tsp(graph, v, 0, n, 1, 0)

dropstar(18, max(answer), t)
