import time, statistics
from helpers import *

t = time.time()

input = mypath + "d10-input.txt"
with open(input) as f:
    subsystem = [sys for sys in f.read().split("\n")]

# Part 1
lefts = ["(", "[", "{", "<"]
rights = [")", "]", "}", ">"]
primitives = ["".join(brackets) for brackets in zip(lefts, rights)]
syntax_points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def trimPrimitives(line):
    do_trim = True
    while do_trim:
        l = len(line)
        for p in primitives:
            line = line.replace(p, "")
        do_trim = len(line) != l
    return line


def countBrackets(line):
    lcount = sum([l in lefts for l in line])
    rcount = sum([r in rights for r in line])
    return lcount, rcount


syntax_score = 0
for line in subsystem:
    trimmed = trimPrimitives(line)
    lcount, rcount = countBrackets(trimmed)
    if lcount != 0 and rcount != 0 and lcount != rcount:  # skip incomplete
        bad_bracket = [r for r in trimmed if r in rights][0]
        syntax_score += syntax_points[bad_bracket]

dropstar(19, syntax_score, t)

# Part 2
def invertBrackets(line):
    return "".join([rights[lefts.index(b)] for b in line[::-1]])


ac_points = {")": 1, "]": 2, "}": 3, ">": 4}
ac_scoreboard = []
for line in subsystem:
    ac_score = 0
    trimmed = trimPrimitives(line)
    lcount, rcount = countBrackets(trimmed)
    if lcount == 0 or rcount == 0:  # skip corrupted
        missing = invertBrackets(trimmed)
        for bracket in missing:
            ac_score = ac_score * 5 + ac_points[bracket]
        ac_scoreboard.append(ac_score)

middle = statistics.median(ac_scoreboard)

dropstar(20, middle, t)
