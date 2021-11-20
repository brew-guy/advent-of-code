import time, re
from helpers import *

t = time.time()

input = "d5-input.txt"
with open(input) as f:
    strings = f.read().split("\n")


# Part 1
def countVowels(str):
    vowels = "aeiou"
    return len([c for c in str if c in vowels])


def countTwins(str):
    regexp = re.compile(r"(.)\1")
    match = re.findall(regexp, str)
    return len(match)


def hasNaughties(str):
    naughties = ["ab", "cd", "pq", "xy"]
    return any([bad in str for bad in naughties])


nice = 0
for string in strings:
    if (
        countVowels(string) >= 3
        and countTwins(string) >= 1
        and not hasNaughties(string)
    ):
        nice += 1

dropstar(9, nice, t)

# Part 2
def countPairDublets(str):
    return any([str[idx : idx + 2] in str[idx + 2 :] for idx in range(len(str))])


def countTwinsApart(str):
    regexp = re.compile(r"(.).\1")
    match = re.findall(regexp, str)
    return len(match)


nice = 0
for string in strings:
    if countPairDublets(string) and countTwinsApart(string) >= 1:
        nice += 1

dropstar(10, nice, t)

