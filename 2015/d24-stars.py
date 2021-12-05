import time, math, itertools
from helpers import *

t = time.time()

input = mypath + "d24-input.txt"
with open(input) as f:
    weights = [int(w) for w in f.read().split("\n")]

logging = False
log = lambda line: print(line) if logging else None

# Part 1
# From https://www.techiedelight.com/3-partition-problem-extended-print-all-partitions/
# Helper function to 3–partition problem.
# def isSubsetExist(S, n, a, b, c, list):
#     if a == 0 and b == 0 and c == 0:
#         return True
#     if n < 0:
#         return False
#     A = False
#     if a - S[n] >= 0:
#         list[n] = 1  # current element goes to the first subset
#         A = isSubsetExist(S, n - 1, a - S[n], b, c, list)
#     B = False
#     if not A and (b - S[n] >= 0):
#         list[n] = 2  # current element goes to the second subset
#         B = isSubsetExist(S, n - 1, a, b - S[n], c, list)
#     C = False
#     if (not A and not B) and (c - S[n] >= 0):
#         list[n] = 3  # current element goes to the third subset
#         C = isSubsetExist(S, n - 1, a, b, c - S[n], list)
#     return A or B or C


# Function for solving the 3–partition problem. It prints the subset if
# given set `S[0…n-1]` can be divided into three subsets with an equal sum
# def partition(S):
#     total = sum(S)
#     A = [None] * len(S)
#     result = (
#         (len(S) >= 3)
#         and (total % 3) == 0
#         and isSubsetExist(S, len(S) - 1, total / 3, total / 3, total / 3, A)
#     )
#     if not result:
#         return "3-Partition of set is not possible"
#     else:
#         partitions = [[S[j] for j in range(len(S)) if A[j] == i + 1] for i in range(3)]
#         return partitions


# From https://www.geeksforgeeks.org/partition-problem-dp-18/
# def canPartition(arr):
#     n = len(arr)
#     Sum = 0
#     for i in range(n):
#         Sum += arr[i]
#     if Sum % 2 != 0:
#         return 0
#     part = [0] * ((Sum // 2) + 1)
#     for i in range((Sum // 2) + 1):
#         part[i] = 0
#     for i in range(n):
#         for j in range(Sum // 2, arr[i] - 1, -1):
#             if part[j - arr[i]] == 1 or j == arr[i]:
#                 part[j] = 1
#     return part[Sum // 2]


# From https://stackoverflow.com/questions/34517540/find-all-combinations-of-a-list-of-numbers-with-a-given-sum/34519260
def findSequences(numbers, target):
    result = []
    for i in range(len(numbers), 0, -1):
        for seq in itertools.combinations(numbers, i):
            if sum(seq) == target:
                result.append(seq)
    return result


def quantumEntanglement(partition):
    return math.prod(partition)


target = sum(weights) // 3
log(f"Packages: {len(weights)} | weight: {sum(weights)} | 1/3 weight = {target}")

seqs = findSequences(weights, target)
log(f"Found {len(seqs)} sequences of weight {target}.")

# validated = []
# for seq in seqs:
#     remains = list(set(weights).difference(seq))
#     if canPartition(remains):
#         validated.append(seq)

fewest_packages = min([len(g) for g in seqs])
first_group = [g for g in seqs if len(g) == fewest_packages]
if len(first_group) > 1:
    quantum = sorted([(quantumEntanglement(g), g) for g in first_group])

dropstar(47, quantum[0][0], t)

# Part 2
target = sum(weights) // 4
log(f"Packages: {len(weights)} | weight: {sum(weights)} | 1/4 weight = {target}")

seqs = findSequences(weights, target)
log(f"Found {len(seqs)} sequences of weight {target}.")

fewest_packages = min([len(g) for g in seqs])
first_group = [g for g in seqs if len(g) == fewest_packages]
if len(first_group) > 1:
    quantum = sorted([(quantumEntanglement(g), g) for g in first_group])

dropstar(48, quantum[0][0], t)
