import time
from helpers import *

t = time.time()

input = mypath + "d6-input.txt"
with open(input) as f:
    fishes = [int(fish) for fish in f.read().split(",")]

# Part 1
def nextGen(shoal):
    new_shoal, new_born = [], []
    if isinstance(shoal, int):
        shoal = [shoal]
    for fish in shoal:
        if fish == 0:
            new_shoal.append(6)
            new_born.append(8)
        else:
            new_shoal.append(fish - 1)
    new_shoal += new_born
    return new_shoal


# shoal = fishes.copy()
shoal = [8]
for i in range(45):
    print(i, shoal)
    shoal = nextGen(shoal)

print(i + 1, shoal)

dropstar(11, len(shoal), t)

# Part 2
# shoal = 0

# for i in range(80):
#     shoal = nextGen(shoal)
#     print(i, len(shoal))


# dropstar(12, len(shoal), t)
