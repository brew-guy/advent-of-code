import time
from helpers import *

t = time.time()

input = mypath + "d14-input.txt"
with open(input) as f:
    recipe = f.read().split("\n\n")

template = recipe[0]
rules = {k: v for k, v in [rule.split(" -> ") for rule in recipe[1].split("\n")]}

# Part 1
def polymerize(primer):
    polymer = []
    for idx, p in enumerate(primer):
        elements = primer[idx : idx + 2]
        polymer.append(p + rules[elements]) if elements in rules else polymer.append(p)
    return "".join(polymer)


def letterCount(string):
    letters = "".join(set(string))
    return {letter: string.count(letter) for letter in letters}


polymer = template
for i in range(10):
    polymer = polymerize(polymer)

letter_counts = letterCount(polymer).values()

dropstar(27, max(letter_counts) - min(letter_counts), t)

# Part 2
polymer = template
for i in range(40):
    polymer = polymerize(polymer)

letter_counts = letterCount(polymer).values()

dropstar(28, max(letter_counts) - min(letter_counts), t)
