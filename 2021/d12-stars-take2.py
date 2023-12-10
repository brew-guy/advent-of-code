import time
from helpers import *

import networkx as nx
from networkx.algorithms.cycles import cycle_basis
from networkx.classes.function import to_undirected

t = time.time()

input = mypath + "d12-sample2.txt"
with open(input) as f:
    connections = [path.split("-") for path in f.read().split("\n")]

G = nx.Graph()
G.add_edges_from(connections)

simple_paths = nx.all_simple_paths(G, "start", "end")
cycles = nx.cycle_basis(G)
traversal = nx.all_pairs_shortest_path_length(G)

J = nx.all_shortest_paths(G, "start", "end")
print(list(J))
print(list(simple_paths))
print(list(cycles))

# Find leaf nodes (degree = 1)
leafs = [n for n, d in G.degree if d == 1]
# Leaf nodes with small cave predecessor - i.e. cannot be visits / can be removed
dead_ends = [
    leaf
    for leaf in leafs
    for pred in G.adj[leaf]
    if pred.islower() and not pred in ["start", "end"]
]

print(dead_ends)

