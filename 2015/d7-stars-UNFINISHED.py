import time, re
from helpers import *

t = time.time()

input = mypath + "d7-input.txt"
with open(input) as f:
    connections = f.read().split("\n")

# Part 1
class Circuit:
    # Logic Circuits have names and an evaluation function defined in child
    # classes. They will also contain a set of inputs and outputs.
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        return


class Connector:
    def __init__(self, owner, name, activates=0, monitor=0):
        self.value = None
        self.owner = owner
        self.name = name
        self.monitor = monitor
        self.connects = []
        self.activates = activates

    def connect(self, inputs):
        if not isinstance(inputs, list):
            inputs = [inputs]
        for input in inputs:
            self.connects.append(input)

    def set(self, value):
        if self.value == value:
            return  # Ignore if no change
        self.value = value
        if self.activates:
            self.owner.evaluate()
        if self.monitor:
            print(
                "Connector {0}-{1} set to {2}".format(
                    self.owner.name, self.name, self.value
                )
            )
        for con in self.connects:
            con.set(value)


class Gate2(Circuit):  # two input gates. Inputs A and B. Output C.
    def __init__(self, name):
        Circuit.__init__(self, name)
        self.A = Connector(self, "A", activates=1)
        self.B = Connector(self, "B", activates=1)
        self.C = Connector(self, "C")


class Not(Circuit):  # Inverter. Input A. Output B.
    def __init__(self, name):
        Circuit.__init__(self, name)
        self.A = Connector(self, "A", activates=1)
        self.B = Connector(self, "B")

    def evaluate(self):
        self.B.set(not self.A.value)


class And(Gate2):  # two input AND Gate
    def __init__(self, name):
        Gate2.__init__(self, name)

    def evaluate(self):
        self.C.set(self.A.value and self.B.value)


class Or(Gate2):  # two input OR gate.
    def __init__(self, name):
        Gate2.__init__(self, name)

    def evaluate(self):
        self.C.set(self.A.value or self.B.value)


a = And("And1")
a.C.monitor = 1
n = Not("Not1")
a.C.connect(n.A)
n.B.monitor = 1
a.A.set(1)
a.B.set(0)


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

# print(circuit)

# dropstar(13, , t)


# Part 2

# dropstar(14, , t)

