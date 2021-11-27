import time, re
from helpers import *

t = time.time()

input = "d14-input.txt"
with open(input) as f:
    troopers = f.readlines()

# Part 1
def getReindeerStats(trooper):
    regexp = r"([A-Z-a-z]*) can fly ([0-9]*) km/s for ([0-9]*) seconds, but then must rest for ([0-9]*) seconds."
    match = re.match(regexp, trooper)
    r, s, t, p = match.groups()
    return r, int(s), int(t), int(p)


def getDistance(seconds, stats):
    r, s, t, p = stats
    full_cycles = int(seconds / (t + p))

    part_cycle_time = seconds - full_cycles * (t + p)
    part_travel_time = min(t, part_cycle_time)

    distance = full_cycles * t * s + part_travel_time * s
    return distance


secs = 2503
distances = [getDistance(secs, getReindeerStats(trooper)) for trooper in troopers]

dropstar(27, max(distances), t)

# Part 2
scores = [0 for _ in range(len(troopers))]

# Move one sec at a time, find lead(s) and zip lead list with score list
for s in range(1, secs + 1):
    distances = [getDistance(s, getReindeerStats(trooper)) for trooper in troopers]
    leads = [1 if i == max(distances) else 0 for i in distances]
    scores = [x + y for x, y in zip(scores, leads)]

dropstar(28, max(scores), t)
