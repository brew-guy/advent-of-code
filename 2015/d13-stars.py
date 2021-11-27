import time, re, itertools
from helpers import *

t = time.time()

input = "d13-input.txt"
with open(input) as f:
    seating = f.readlines()

# Part 1
def getGuests(seat):
    regexp = r"([a-zA-Z]*) would (lose|gain) ([0-9]*) happiness units by sitting next to ([a-zA-Z]*)."
    match = re.match(regexp, seat)
    a, b, c, d = match.groups()
    return a, d, int(c) if b == "gain" else -int(c)


# Unique guests list
def getUniqueGuestList(seating):
    g_list = []
    for seat in seating:
        g1, g2, happiness = getGuests(seat)
        if not g1 in g_list:
            g_list.append(g1)
        if not g2 in g_list:
            g_list.append(g2)
    return g_list


# A happiness dictionary of gain/loss for Guest1 from Guest2
def getHappinessDict(seating):
    guest_dict = {}
    for seat in seating:
        g1, g2, happiness = getGuests(seat)
        guest_dict[g1 + g2] = happiness
    return guest_dict


# Calculate total happiness for one party
def getHappiness(party):
    total_joy = 0
    for seat in range(-1, len(party) - 1):
        g1, g2 = party[seat], party[seat + 1]
        h1, h2 = happy_dict[g1 + g2], happy_dict[g2 + g1]
        total_joy += h1 + h2
        # print(g1, h1, g2, h2)
    return total_joy


# Generate all possible seatings and calculate happiness
happy_dict = getHappinessDict(seating)
guest_list = getUniqueGuestList(seating)
all_possible_parties = itertools.permutations(guest_list, len(guest_list))

joy = [getHappiness(party) for party in all_possible_parties]

dropstar(25, max(joy), t)

# Part 2
input = "d13-input-2.txt"
with open(input) as f:
    seating = f.readlines()

happy_dict = getHappinessDict(seating)
guest_list = getUniqueGuestList(seating)
all_possible_parties = itertools.permutations(guest_list, len(guest_list))

joy = [getHappiness(party) for party in all_possible_parties]

dropstar(26, max(joy), t)
