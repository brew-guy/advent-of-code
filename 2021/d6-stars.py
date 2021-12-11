import time
from helpers import *

t = time.time()

input = mypath + "d6-input.txt"
with open(input) as f:
    fishes = [int(fish) for fish in f.read().split(",")]

# Part 1
# Baaad solution! Go away! Shoo!
def recursiveBreeding(shoal, generations):
    new_shoal, new_born = [], []
    if generations < 1:
        return len(shoal)
    for fish in shoal:
        if fish == 0:
            new_shoal.append(6)
            new_born.append(8)
        else:
            new_shoal.append(fish - 1)
    new_shoal += new_born
    generations -= 1
    return recursiveBreeding(new_shoal, generations)


dropstar(11, recursiveBreeding(fishes, 80), t)

# Part 2
def fastGrowth(shoal, generations):
    count = [shoal.count(f) for f in range(9)]  # Fish count per index
    for g in range(generations):
        new_fish = count[:1]
        count = count[1:] + new_fish  # Left rotate list
        count[6] += new_fish[0]
    return sum(count)


dropstar(12, fastGrowth(fishes, 256), t)
