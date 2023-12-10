import time, re
from helpers import *

t = time.time()

# input = mypath + "d4-example.txt"
input = mypath + "d4-input.txt"
with open(input) as f:
    cards = f.read().split("\n")

# Part 1
# Split cards into two arrays of win/scratch numbers
# Generate a lookup dict of wins and points for each card

lookup = {i+1:{"wins":[], "points":0} for i,_ in enumerate(cards)}
for i, card in enumerate(cards):
    win, scratch = card.split(":")[1].split("|")
    win = [int(x) for x in win.split()]
    scratch = [int(x) for x in scratch.split()]
    matches = [c for c in win if c in scratch]
    if len(matches) > 0:
        lookup[i+1]["wins"] = matches
        lookup[i+1]["points"] = 2 ** (len(matches) - 1)

points = [card["points"] for card in lookup.values()]

dropstar(7, sum(points), t)

# Part 2
# Recursive function to calculate amount of new cards won with each card
# If slow, use memoization to store the results of each card?
# ...slow without memoization (~3 seconds), but works

def calc_cards(card_number, card_pile):
    card = lookup[card_number]
    w = len(card["wins"])
    card_pile += 1
    if w == 0:
        return card_pile

    for i in range(w):
        card_copy = card_number + i + 1
        card_pile = calc_cards(card_copy, card_pile)

    return card_pile


total = sum([calc_cards(i + 1, 0) for i, c in enumerate(cards)])

dropstar(8, total, t)
