import time, re
from helpers import *

t = time.time()

input = mypath + "d7-input.txt"
with open(input) as f:
    connections = f.read().split("\n")

# Part 1
def connectionParts(connection):
    regexp = r"^(.*) -> ([a-z]*)$"
    match = re.match(re.compile(regexp), connection)
    parts = match[1]
    wire = match[2]
    return (parts, wire)


circuit = {}
gates = (("NOT", "~"), ("AND", "&"), ("OR", "|"), ("RSHIFT", ">>"), ("LSHIFT", "<<"))

for connection in connections:
    parts, wire = connectionParts(connection)
    for r in gates:
        parts = parts.replace(*r)
    circuit[wire] = parts


print(circuit)


# dropstar(13, , t)


# Part 2

# dropstar(14, , t)

