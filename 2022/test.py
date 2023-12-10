import time
from helpers import *
import itertools

t = time.time()


def stringOverlap(str1, str2, second_pass=False):
    merged = []
    for i in range(1, len(str1)):
        piece = str1[-i:]
        if str2.startswith(piece):
            merged.append(str1[:-i] + str2)

    if str2.find(str1) > -1:
        merged.append(str2)

    if not merged:
        merged.append(str1 + str2)

    if not second_pass:
        merged += stringOverlap(str2, str1, True)

    return merged


def getShortest(str_list):
    base = str_list[0]
    for str in str_list[1:]:
        results = stringOverlap(base, str)
        base = sorted(results, key=len)[0]

    return base


genes = ["AGATTA", "GATTACA", "TACAGA"]
genes = ["TT", "AA", "ACT"]
permuts = list(itertools.permutations(genes))

shortest = 9999
for p in permuts:
    s = getShortest(p)
    shortest = len(s) if len(s) < shortest else shortest

print(shortest)

dropstar(1, False, t)
