import re
import time
from helpers import *

t = time.time()

input = mypath + "d15-input-sample.txt"
with open(input) as f:
    readings = [row for row in f.read().split("\n")]

# Part 1
# Break input at linebreaks
# Read sensor and beacon coordinates with regex
# Function to calculate Manhattan distance (dx + dy)
# Calculate Manhattan distances within all sensor/beacon sets
# Locate all sensor/beacon sets that will overlap a given row
#  i.e. it will span (sensor_y +/- manhattan distance) rows
# Function to calculate which x-coordinates in a row will be covered
#  by a given sensor/beacon -> add them to a set
# Get length of set for the row to see how many positions were covered


class SensorBeacon:
    def __init__(self, positions):
        self.sx = positions[0]
        self.sy = positions[1]
        self.bx = positions[2]
        self.by = positions[3]
        self.manhattan = distance(positions)
        self.min_x = self.sx - self.manhattan
        self.max_x = self.sx + self.manhattan
        self.min_y = self.sy - self.manhattan
        self.max_y = self.sy + self.manhattan

    def rowCoverage(self, row):
        # Set of row coordinates covered
        rest = self.manhattan - abs(row - self.sy)
        coverage = set(range(self.sx - rest, self.sx + rest))
        coverage.add(self.sx)
        return coverage

    def __str__(self) -> str:
        pair = f"Sensor: ({self.sx},{self.sy}) | Beacon: ({self.bx},{self.by})"
        span = f"Min y: {self.min_y} | Max y: {self.max_y} | Min x: {self.min_x} | Max x: {self.max_x}"
        manhattan = f"Manhattan distance: {self.manhattan}"
        return pair + "\n" + span + "\n" + manhattan + "\n"


def distance(positions):
    sx, sy, bx, by = positions
    return abs(sx - bx) + abs(sy - by)


def getPositions(reading):
    regex = "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    search = re.search(regex, reading)
    sx, sy, bx, by = map(int, search.groups())
    return sx, sy, bx, by


def getAllPairs(readings):
    return [SensorBeacon(getPositions(r)) for r in readings]


pairs = getAllPairs(readings)
row = 2000000
covers = set()
for pair in pairs:
    if pair.min_y <= row and pair.max_y >= row:
        covers.update(pair.rowCoverage(row))

dropstar(29, len(covers), t)

# Part 2
# Intersection of all the diamond shapes given by their 4 corner coordinates?
t = time.time()

from shapely.geometry import Polygon, box

polys = Polygon()
for pair in pairs:
    coords = [
        (pair.min_x, pair.sy),
        (pair.sx, pair.min_y),
        (pair.max_x, pair.sy),
        (pair.sx, pair.max_y),
    ]
    polys = polys.union(Polygon(coords))

area = Polygon([(0, 0), (0, 20), (20, 20), (20, 0)])
print(polys.difference(area))
dropstar(30, False, t)
