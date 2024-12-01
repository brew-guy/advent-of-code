import time
import re
from helpers import mypath, dropstar

t = time.time()

input = mypath + "d7-input.txt"
with open(input) as f:
    connections = f.read().split("\n")

# Part 1

# Process circuit string to return operation and components
def splitParts(parts):
    parts, wire = parts.split(" -> ")
    parts = parts.split(" ")
    if len(parts) == 1:
        operation, inputs = "ASSIGN", parts
    elif len(parts) == 2:
        operation, inputs = parts[0], parts[1]
    elif len(parts) == 3:
        operation, inputs = parts[1], [parts[0], parts[2]]
    return wire, operation, inputs

# Create circuit dictionary with wire as key and operation and inputs as values
circuit = {}
for connection in connections:
    wire, operation, inputs = splitParts(connection)
    circuit[wire] = {
        'operation': operation,
        'inputs': inputs,
        'value': None
    }

print(circuit)

# Evaluate the circuit
def evaluate(wire):
    if circuit[wire]['value'] is not None:
        return circuit[wire]['value']
    if circuit[wire]['operation'] == "ASSIGN":
        circuit[wire]['value'] = evaluate(circuit[wire]['inputs'][0])
    elif circuit[wire]['operation'] == "NOT":
        circuit[wire]['value'] = ~evaluate(circuit[wire]['inputs'][0])
    elif circuit[wire]['operation'] == "AND":
        circuit[wire]['value'] = evaluate(circuit[wire]['inputs'][0]) & evaluate(circuit[wire]['inputs'][1])
    elif circuit[wire]['operation'] == "OR":
        circuit[wire]['value'] = evaluate(circuit[wire]['inputs'][0]) | evaluate(circuit[wire]['inputs'][1])
    elif circuit[wire]['operation'] == "RSHIFT":
        circuit[wire]['value'] = evaluate(circuit[wire]['inputs'][0]) >> evaluate(circuit[wire]['inputs'][1])
    elif circuit[wire]['operation'] == "LSHIFT":
        circuit[wire]['value'] = evaluate(circuit[wire]['inputs'][0]) << evaluate(circuit[wire]['inputs'][1])
    else:
        circuit[wire]['value'] = int(circuit[wire]['inputs'][0])
    return circuit[wire]['value']

# Evaluate the circuit
a = evaluate('a')
print(a)



# def connectionParts(connection):
#     regexp = r"^(.*) -> ([a-z]*)$"
#     match = re.match(re.compile(regexp), connection)
#     parts = match[1]
#     wire = match[2]
#     return (parts, wire)

# gates = (("NOT", "~"), ("AND", "&"), ("OR", "|"), ("RSHIFT", ">>"), ("LSHIFT", "<<"))

# for connection in connections:
#     parts, wire = connectionParts(connection)
#     for r in gates:
#         parts = parts.replace(*r)
#     circuit[wire] = parts


# dropstar(13, , t)


# Part 2

# dropstar(14, , t)

