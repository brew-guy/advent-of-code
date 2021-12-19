import time
from helpers import *

t = time.time()

input = mypath + "d14-input.txt"
with open(input) as f:
    recipe = f.read().split("\n\n")

template = recipe[0]
rules = {k: v for k, v in [rule.split(" -> ") for rule in recipe[1].split("\n")]}

# Part 1
def addToDict(dict, value, amount):
    dict[value] = dict[value] + amount if value in dict else amount
    return dict


def splitToAdjacentPairs(string):
    pair_dict = {}
    for idx, atom in enumerate(string[:-1]):
        pair = atom + string[idx + 1]
        pair_dict = addToDict(pair_dict, pair, 1)
    return pair_dict


def iterate(pair_dict):
    nextgen_dict = {}
    for pair in pair_dict.keys():
        if pair in rules:
            new_pairs = [pair[0] + rules[pair], rules[pair] + pair[1]]
            for np in new_pairs:
                nextgen_dict = addToDict(nextgen_dict, np, pair_dict[pair])
        else:
            nextgen_dict = addToDict(nextgen_dict, pair, pair_dict[pair])
    return nextgen_dict


# Count only first letters in pairs
def letterCount(dict):
    last_atom = [template[-1]][0]
    letters = {}
    for k, v in dict.items():
        addToDict(letters, k[0], v)
    addToDict(letters, last_atom, 1)  # Count that last letter in the molecule
    return letters


# Split primer molecule to adjacent pairs
pair_dict = splitToAdjacentPairs(template)

for i in range(10):
    pair_dict = iterate(pair_dict)

count = letterCount(pair_dict).values()

dropstar(27, max(count) - min(count), t)

# Part 2
pair_dict = splitToAdjacentPairs(template)

for i in range(40):
    pair_dict = iterate(pair_dict)

count = letterCount(pair_dict).values()

dropstar(28, max(count) - min(count), t)
