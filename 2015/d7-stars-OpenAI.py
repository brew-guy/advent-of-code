import time, re
from helpers import *

t = time.time()

input = mypath + "d7-input.txt"
with open(input) as f:
    connections = f.read().split("\n")

# Part 1
# ChatGPT prompt: can you help with object-oriented python code to simulate any circuit of logic gates and connectors?

# Define the LogicGate class
class LogicGate:
    # Constructor to initialize the gates
    def __init__(self):
        self.input1 = None
        self.input2 = None
        self.output = None
        self.id = None

    # Define the logic gates
    def AND(self):
        self.output = self.input1 and self.input2

    def OR(self):
        self.output = self.input1 or self.input2

    def NOT(self):
        self.output = not self.input1

    # Method to set the input values
    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    # Method to get the output of the gate
    def getOutput(self):
        return self.output


# Define the Connector class
class Connector:
    # Constructor to initialize the connectors
    def __init__(self, gate1, gate2, input):
        self.gate1 = gate1
        self.gate2 = gate2

    # Method to set the output of the first gate as the input of the second gate
    def setNextInput(self):
        self.gate2.setInputs(self.gate1.getOutput(), self.gate2.input1)


# Create instances of the LogicGate and Connector classes
gate1 = LogicGate()
gate2 = LogicGate()
gate3 = LogicGate()
conn1 = Connector(gate1, gate2)
conn2 = Connector(gate2, gate3)

# Set the input values
gate1.setInputs(1, 0)

# Compute the output of the circuit
gate1.XOR()
conn1.setNextInput()
gate2.NOT()
conn2.setNextInput()
gate3.OR()

# Print the output of the circuit
print(gate3.getOutput())


# dropstar(13, , t)


# Part 2

# dropstar(14, , t)

