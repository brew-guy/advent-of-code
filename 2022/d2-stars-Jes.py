import time
from helpers import *

t = time.time()

input = mypath + "d2-input.txt"
with open(input) as f:
    matches = [tuple(hands for hands in row.split(" ")) for row in f.read().split("\n")]

# Part 1
# Read input to array of tuples
# Use a match matrix to look up match points
# Use a function to return single match points for Player 1 and 2
# Loop matches to generate array with all match points for p2
# Player 1 (ABC) against Player 2 (XYZ) point matrix:
#     | X Y Z
#   --+------
#   A | 3 6 0
#   B | 0 3 6
#   C | 6 0 3

playIndex = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
pointsMatrix = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]


def getMatchPoints(matchtuple):
    p1, p2 = (playIndex[m] for m in matchtuple)
    p1Points = pointsMatrix[p2][p1] + p1 + 1
    p2Points = pointsMatrix[p1][p2] + p2 + 1
    return {"p1_points": p1Points, "p2_points": p2Points}


matchOutcomes = [getMatchPoints(match)["p2_points"] for match in matches]
dropstar(3, sum(matchOutcomes), t)

# Part 2
# Use lookup table to transform Player 2 choice
# Redo match outcome calculations
# Attempt 1: 15522 - too high
# Player 2 (XYZ) choice transform matrix:
#     | X Y Z
#   --+------
#   A | Z X Y
#   B | X Y Z
#   C | Y Z X

newHandMatrix = [["Z", "X", "Y"], ["X", "Y", "Z"], ["Y", "Z", "X"]]
newHandMatches = [
    (p1, newHandMatrix[playIndex[p1]][playIndex[p2]]) for p1, p2 in matches
]
matchOutcomes = [getMatchPoints(match)["p2_points"] for match in newHandMatches]

dropstar(4, sum(matchOutcomes), t)
