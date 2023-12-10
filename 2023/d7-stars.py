import time, itertools
from helpers import *

t = time.time()

# input = mypath + "d7-example.txt"
input = mypath + "d7-input.txt"
with open(input) as f:
    hands = f.read().splitlines()

# Part 1
# It appears that all hands are unique so hands and bets can be split into two lists.
# Bets can later be looked up by index in the original hands list.
# Write functions to groups hands according to their type.
# Write function to sort groups of same type according to their card values.
# Guess 1: 356311561 - too high

hands, bets = zip(*[hand.split() for hand in hands])

# card ranks
card_rank = "23456789TJQKA"

# Function that makes a dict from a hand
def handDict(hand: str):
    h = {c: hand.count(c) for c in hand}
    return h

# Function that checks for five of a kind in a hand
def fiveOfAKind(hand):
    h = handDict(hand)
    return any(filter(lambda x: x[1] == 5, h.items()))

# Function that checks for four of a kind in a hand
def fourOfAKind(hand):
    h = handDict(hand)
    return any(filter(lambda x: x[1] == 4, h.items()))

# Function that checks for a full house in a hand
def fullHouse(hand):
    h = handDict(hand)
    return any(filter(lambda x: x[1] == 3, h.items())) and any(filter(lambda x: x[1] == 2, h.items()))

# Function that checks for three of a kind in a hand
def threeOfAKind(hand):
    h = handDict(hand)
    return any(filter(lambda x: x[1] == 3, h.items())) and not any(filter(lambda x: x[1] == 2, h.items()))

# Function that checks for two pairs in a hand
def twoPairs(hand):
    h = handDict(hand)
    return len(list(filter(lambda x: x[1] == 2, h.items()))) == 2

# Function that checks for one pair in a hand
def onePair(hand):
    h = handDict(hand)
    return len(list(filter(lambda x: x[1] == 2, h.items()))) == 1 and not any(filter(lambda x: x[1] == 3, h.items()))

# A function that checks if all cards in hand are different
def highCard(hand):
    h = handDict(hand)
    return all([x[1] == 1 for x in h.items()])

# Function that returns a list of hands grouped by hand type, one hand can only appear in one group
def groupHands(hands):
    firstOrder = [highCard, onePair, twoPairs, threeOfAKind, fullHouse, fourOfAKind, fiveOfAKind]
    g = [list(filter(f, hands)) for f in firstOrder]
    return g

# Function to sort a list of hands according to their card values
def sortHands(hands):
    return sorted(hands, key=lambda x: [card_rank.index(c) for c in x])

# Function that flattens a list of lists
def flatten(l):
    return [item for sublist in l for item in sublist]

# Group hands by type, sort groups by card values, flatten list of groups, calculate winnings
grouped = groupHands(hands)
sorted_groups = [sortHands(group) for group in grouped]
flattened_groups = flatten(sorted_groups)
winnings = [(i + 1) * int(bets[hands.index(hand)]) for i, hand in enumerate(flattened_groups)]

dropstar(13, sum(winnings), t)

# Part 2
# Generate all combinations of a hand with joker cards (J)
# where joker cards can be replaced by any card rank (2-9, T, J, Q, K, A)
# Run groupHands function on all possible hands to find the most valuable group
# that a hand with joker cards can be a part of

# Updated card ranks
card_rank = "J23456789TQKA"

# Function that generates all combinations of a hand with joker cards
def generateHands(hand, chars=card_rank):
    for p in map(iter, itertools.product(chars, repeat=hand.count('J'))):
        yield ''.join(c if c != 'J' else next(p) for c in hand)

# Remove hands with jokers from hand group, determine optimal joker replacement,
# add hands with jokers to optimal group, sort groups by card values, flatten list of groups,
# calculate winnings

no_jokers = [list(filter(lambda x: 'J' not in x, group)) for group in grouped]
jokers = flatten([list(filter(lambda x: 'J' in x, group)) for group in grouped])

for j in jokers:
    joker_replacements = list(generateHands(j))
    joker_groups = groupHands(joker_replacements)
    # Last group in joker_groups with length > 0 is the optimal group
    optimal_group_index = len(joker_groups) - 1 - joker_groups[::-1].index(list(filter(lambda x: len(x) > 0, joker_groups))[-1])
    # Add original joker hand to optimal group at index optimal_group_index in no_jokers
    no_jokers[optimal_group_index].append(j)

sorted_groups = [sortHands(group) for group in no_jokers]
flattened_groups = flatten(sorted_groups)
winnings = [(i + 1) * int(bets[hands.index(hand)]) for i, hand in enumerate(flattened_groups)]

dropstar(14, sum(winnings), t)

