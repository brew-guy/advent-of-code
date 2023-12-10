import re
import time
from helpers import *

t = time.time()

input = mypath + "d13-input-sample.txt"
with open(input) as f:
    pairs = [pair.split("\n") for pair in f.read().split("\n\n")]

# Part 1
def testPair(pair):
    left_lists, right_lists = pair[0].count("["), pair[1].count("[")
    left = re.sub("[\[\]]", "", pair[0]).split(",")
    right = re.sub("[\[\]]", "", pair[1]).split(",")
    print(f"{left} <<-->> {right}")
    if len(left) == 0 and len(right) == 0:
        return left_lists < right_lists
    for i in range(min(len(left), len(right))):
        pass


for i, pair in enumerate(pairs):
    print(testPair(pair))


dropstar(25, False, t)

# Part 2


dropstar(26, False, t)
