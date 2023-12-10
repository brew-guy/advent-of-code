import time
from helpers import *

t = time.time()

input = mypath + "d6-input.txt"
with open(input) as f:
    datastream = list(f.read())

# Part 1
# Read data to list of characters
# Loop over blocks of 4 characters, transform to set, check if length = 4


def findMarker(data, packetLen):
    for i in range(0, len(data) - packetLen - 1):
        block = data[i : i + packetLen]
        if len(set(block)) == packetLen:
            return i + packetLen


dropstar(11, findMarker(datastream, 4), t)

# Part 2
# Refactor loop to function to allow varying serach for varying packet lengths
t = time.time()

dropstar(12, findMarker(datastream, 14), t)
