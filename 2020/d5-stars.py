import time
from helpers import *

t = time.time()

# Read seat sequences to array
input = mypath + "d5-input.txt"
with open(input) as f:
    seats = f.read().strip().split("\n")

# Part 1
def findrow(sequence):
    low = 0
    high = 127
    for char in sequence[: len(sequence) - 1]:
        if char == "F":
            high = int(high - (high - low) / 2)
        if char == "B":
            low = round(low + (high - low) / 2)
    if sequence[-1] == "F":
        return low
    else:
        return high


def findcol(sequence):
    low = 0
    high = 7
    for char in sequence[: len(sequence) - 1]:
        if char == "L":
            high = int(high - (high - low) / 2)
        if char == "R":
            low = round(low + (high - low) / 2)
    if sequence[-1] == "L":
        return low
    else:
        return high


def findseatID(sequence):
    return findrow(sequence[:8]) * 8 + findcol(sequence[7:])


seatIDs = []
for seat in seats:
    seatIDs.append(findseatID(seat))

dropstar(9, max(seatIDs), t)

# Part 2
seatIDs = []
for seat in seats:
    seatIDs.append(findseatID(seat))

seatIDs = sorted(seatIDs)
seat_status = {seat: (seat - 1 in seatIDs and seat + 1 in seatIDs) for seat in seatIDs}
has_empty_neighbour = [key for (key, value) in seat_status.items() if value == False]
your_seat = has_empty_neighbour[1] + 1

dropstar(10, your_seat, t)

