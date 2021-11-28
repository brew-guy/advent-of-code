import time, re
from helpers import *

t = time.time()

input = "d7-input.txt"
with mypath + open(input) as f:
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

# regex_not = r"^([A-Z]*) ([a-z]*) -> ([a-z]*)$"
# regex_gate = r"^([a-z\d]*) ([A-Z]*) ([a-z\d]*) -> ([a-z]*)$"
# regex_direct = r"^([a-z\d]*) -> ([a-z]*)$"

# match_not = re.match(re.compile(regex_not), connection)
# match_gate = re.match(re.compile(regex_gate), connection)
# match_direct = re.match(re.compile(regex_direct), connection)

# if match_not:
#     circuit[match_not[3]] = gates[match_not[1]] + match_not[2]
# elif match_gate:
#     circuit[match_gate[4]] = match_gate[1] + gates[match_gate[2]] + match_gate[3]
# elif match_direct:
#     circuit[match_direct[2]] = match_direct[1]

print(circuit)

# dropstar(13, , t)


# Part 2

# dropstar(14, , t)

