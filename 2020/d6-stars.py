import time, re
from helpers import *

t = time.time()

input = mypath + "d6-input.txt"
with open(input) as f:
    forms = f.read()

# Read merged group responses to array
forms = re.sub(r"(\w)\n", r"\1 ", forms).replace(" ", "").split("\n")

# Part 1
any_yes_responders = map(lambda form: len({letter: True for letter in form}), forms)

dropstar(11, sum(list(any_yes_responders)), t)

# Part 2
# Kan nok også laves mere elegant med intersection() på lists...
with open(input) as f:
    forms = f.read()[:-1].split("\n\n")

# Read each person's response in group to array of arrays
responses = list(map(lambda group: group.split("\n"), forms))

# Check all letters in first array against rest of arrays
def findsame(array):
    found = {}
    for letter in array[0]:
        if all(letter in sequence for sequence in array):
            found[letter] = True
    return len(found)


all_yes_responders = map(findsame, responses)

dropstar(12, sum(list(all_yes_responders)), t)
