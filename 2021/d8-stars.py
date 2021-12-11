import time
from helpers import *

t = time.time()

input = mypath + "d8-input.txt"
with open(input) as f:
    entries = [[p.split() for p in entry.split("|")] for entry in f.read().split("\n")]

# Part 1
easy = [1 for output in entries for digit in output[1] if len(digit) in [2, 3, 4, 7]]

dropstar(15, sum(easy), t)

# Part 2
def getOfLen(length, entry):
    return [digit for digit in entry if len(digit) == length]


def getSegWires(entry):
    one = getOfLen(2, entry)[0]
    four = getOfLen(4, entry)[0]
    two = [d for d in getOfLen(5, entry) if len(set(d).union(set(four))) == 7][0]
    six = [d for d in getOfLen(6, entry) if len(set(d).union(set(one))) == 7][0]
    seven = getOfLen(3, entry)[0]
    eight = getOfLen(7, entry)[0]
    nine = [d for d in getOfLen(6, entry) if len(set(d).union(set(four))) == 6][0]
    zero = [
        d for d in getOfLen(6, entry) if len(set(d).union(set(four) - set(one))) == 7
    ][0]

    seg_a = set(seven).difference(set(one)).pop()
    seg_b = set(eight).difference(set(two + one)).pop()
    seg_c = set(eight).difference(set(six)).pop()
    seg_d = set(eight).difference(set(zero)).pop()
    seg_e = set(eight).difference(set(nine)).pop()
    seg_f = set(eight).difference(set(two + seg_b)).pop()
    seg_g = (set("abcdefg") - set(seg_a + seg_b + seg_c + seg_d + seg_e + seg_f)).pop()
    seg = {
        "a": seg_a,
        "b": seg_b,
        "c": seg_c,
        "d": seg_d,
        "e": seg_e,
        "f": seg_f,
        "g": seg_g,
    }
    return dict((v, k) for k, v in seg.items())


def rewire(digit, wires):
    return "".join([wires[d] for d in digit])


display_dict = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

out_values = []
for entry in entries:
    patterns, outputs = entry[0], entry[1]
    wires = getSegWires(patterns)
    num = ""

    for output in outputs:
        rewired = rewire(output, wires)
        num += str([v for k, v in display_dict.items() if set(k) == set(rewired)][0])

    out_values.append(int(num))

dropstar(16, sum(out_values), t)
