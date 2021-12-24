import time
import networkx as nx
from networkx.classes.function import to_undirected
from helpers import *

t = time.time()

input = mypath + "d12-sample.txt"
with open(input) as f:
    connections = [path.split("-") for path in f.read().split("\n")]

# Part 1
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


# Unique cave names
caves = set(cave for connection in connections for cave in connection)
# Build graph of cave connections
graph = {cave: set() for cave in caves}
for connection in connections:
    graph[connection[0]].add(connection[1])
    graph[connection[1]].add(connection[0])

# paths = find_all_paths(graph, "start", "end")
# print("\n".join([",".join(p) for p in paths]))

# With networkx
G = nx.Graph()
G.add_nodes_from(caves)
G.add_edges_from(connections)
p = nx.recursive_simple_cycles(G)
# print(p)
for pth in p:
    print(pth)

# for part in cave_parts:


# dropstar(23, , t)

# Part 2

# dropstar(24, , t)
