import time
from helpers import *

t = time.time()

input = mypath + "d3-input.txt"
with open(input) as f:
    rucksacks = [sack for sack in f.read().split("\n")]

# Part 1
# Input to array of strings (rucksack items)
# Function that splits a string in to two equal length halves
# Function that finds common character in strings (output one letter)
# Function that calculates priority from letter


def splitString(string):
    half = len(string) // 2
    return string[:half], string[half:]


def findCommon(*strings):
    sets = [set(list(string)) for string in strings]
    return "".join(set.intersection(*sets))


def getPriority(character):
    if character.islower():
        return ord(character) - 96
    return ord(character) - 38


compartments = [splitString(sack) for sack in rucksacks]
commonItems = [findCommon(*items) for items in compartments]
priorities = [getPriority(item) for item in commonItems]

dropstar(5, sum(priorities), t)

# Part 2
# Input to array of 3-group arrays
# Function that finds common character in strings (output one letter)
# Function that calculates priority from letter

groups = [rucksacks[idx : idx + 3] for idx in range(0, len(rucksacks), 3)]
commonItems = [findCommon(*items) for items in groups]
priorities = [getPriority(item) for item in commonItems]

dropstar(6, sum(priorities), t)
