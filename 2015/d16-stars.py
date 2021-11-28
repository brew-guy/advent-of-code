import time, re
from helpers import *

t = time.time()

input = mypath + "d16-input.txt"
with open(input) as f:
    aunts = f.readlines()

ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

# Part 1
def getAunt(aunt):
    regexp = r"Sue ([0-9]*): ([A-Za-z]*): ([0-9]*), ([A-Za-z]*): ([0-9]*), ([A-Za-z]*): ([0-9]*)"
    match = re.match(regexp, aunt)
    sue, i1, a1, i2, a2, i3, a3 = match.groups()
    return int(sue), i1, int(a1), i2, int(a2), i3, int(a3)


potential_aunts = []
for aunt in aunts:
    sue, i1, a1, i2, a2, i3, a3 = getAunt(aunt)
    if ticker_tape[i1] == a1 and ticker_tape[i2] == a2 and ticker_tape[i3] == a3:
        potential_aunts.append(sue)

dropstar(31, potential_aunts, t)

# Part 2
def isMatch(item, amount):
    if (item in ["cats", "trees"]) and amount > ticker_tape[item]:
        return True
    elif (item in ["pomeranians", "goldfish"]) and amount < ticker_tape[item]:
        return True
    elif (
        item in ["children", "samoyeds", "akitas", "vizslas", "cars", "perfumes"]
    ) and amount == ticker_tape[item]:
        return True
    return False


potential_aunts = []
for aunt in aunts:
    sue, i1, a1, i2, a2, i3, a3 = getAunt(aunt)

    if isMatch(i1, a1) and isMatch(i2, a2) and isMatch(i3, a3):
        potential_aunts.append(sue)

dropstar(32, potential_aunts, t)
