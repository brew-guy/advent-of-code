import time, re
from itertools import groupby
from helpers import *

t = time.time()

input = "1113122113"

# Part 1
def splitSequence(input):
    return [m.group(0) for m in re.finditer(r"(\d)\1*", input)]


def lookAndSay(seq):
    seq = splitSequence(seq)
    say = "".join(map(lambda c: str(len(c)) + c[0], seq))
    return say


for i in range(45):
    input = lookAndSay(input)

dropstar(19, len(input), t)

# Part 2
def lookAndSay2(number):
    return "".join(str(len(list(g))) + k for k, g in groupby(number))


# 1113122113
# 132113
# 3113
# 1113
# 13
# 3

input = "3"
for i in range(55):
    input = lookAndSay2(input)

dropstar(20, len(input), t)
