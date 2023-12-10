import time
from helpers import *

t = time.time()

input = mypath + "d9-input.txt"
with open(input) as f:
    motions = [
        (motion.split(" ")[0], int(motion.split(" ")[1]))
        for motion in f.read().split("\n")
    ]

# Part 1
# Read input to instruction tuples = (direction, moves)
# Lookup dict for U/D/L/R head movement
# Function that determines tail move based on last head coordinate
# Loop over every instruction
# Step one move at a time
#   update head coordinate
#   call function to move tail based on head coordinate
#  aAppend every coordinate set the tail moves to a list
# Tail list to set to count all occupied positions


def moveTail(head_pos, tail_pos):
    diff = tupleDiff(head_pos, tail_pos)
    if diff[0] == 0 or diff[1] == 0:  # on same row or column
        return (int(diff[0] / 2), int(diff[1] / 2))  # move 1 in direction of head
    elif tupleAbsSum(diff) > 2:  # head is getting away in new row/column
        return (
            get1Signed(diff[0]),
            get1Signed(diff[1]),
        )  # move diagonally towards head
    return (0, 0)  # stay


def get1Signed(number):
    if number < 0:
        return -1
    return 1


def tuplesSum(*tuples):
    return tuple(map(sum, zip(*tuples)))


def tupleSub(tuple):
    num1, num2 = tuple
    return num1 - num2


def tupleAbsSum(tuple):
    return sum(map(abs, tuple))


def tupleDiff(*tuples):
    return tuple(map(tupleSub, zip(*tuples)))


head_pos, tail_pos = (0, 0), (0, 0)
tail_trace = [tail_pos]
dx = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

for motion in motions:
    direction, moves = motion
    for move in range(moves):
        head_pos = tuplesSum(head_pos, dx[direction])
        tail_pos = tuplesSum(tail_pos, moveTail(head_pos, tail_pos))
        tail_trace.append(tail_pos)
        # print(f"Head: {head_pos} | Tail: {tail_pos}")

dropstar(17, len(set(tail_trace)), t)

# Part 2
# Create array of tuples (0,0) for knots 1-9
# Insert the head position into 0-index knots array
# Process each knot move as a head/tail pair in each step of the same loop as before
# The new calculated "tail" positions is the "head" of the next pair
# Output should be array of 9 tuples to use as input for next loops
# Trace the last knot as the real tail after each step
t = time.time()

head_pos = (0, 0)
knots_pos = [(0, 0)] * 9
tail_trace = [knots_pos[-1]]

for motion in motions:
    direction, moves = motion
    for move in range(moves):
        head_pos = tuplesSum(head_pos, dx[direction])
        knots_pos.insert(0, head_pos)  # insert real rope head as first knot

        for idx in range(0, 9):  # process the 9 knots with the real head
            head = knots_pos[idx]
            tail = knots_pos[idx + 1]
            tail_pos = tuplesSum(tail, moveTail(head, tail))
            knots_pos[idx + 1] = tail_pos  # update "tail" knot with new position

        knots_pos.pop(0)  # remove the real head again
        tail_trace.append(knots_pos[-1])
        # print(f"Head: {head_pos} | Tail: {knots_pos}")


dropstar(18, len(set(tail_trace)), t)
