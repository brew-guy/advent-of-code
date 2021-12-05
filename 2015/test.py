import itertools, math
from helpers import *

input = mypath + "d24-input.txt"
with open(input) as f:
    weights = [int(w) for w in f.read().split("\n")]


def canPartition(arr):
    n = len(arr)
    Sum = 0
    for i in range(n):
        Sum += arr[i]
    if Sum % 2 != 0:
        return 0
    part = [0] * ((Sum // 2) + 1)
    for i in range((Sum // 2) + 1):
        part[i] = 0
    for i in range(n):
        for j in range(Sum // 2, arr[i] - 1, -1):
            if part[j - arr[i]] == 1 or j == arr[i]:
                part[j] = 1
    return part[Sum // 2]


def findSequences(numbers, target):
    result = []
    for i in range(len(numbers), 0, -1):
        for seq in itertools.combinations(numbers, i):
            if sum(seq) == target:
                result.append(seq)
    return result


target = sum(weights) // 4
print(f"Packages: {len(weights)} | weight: {sum(weights)} | 1/4 weight = {target}")

seqs = findSequences(weights, target)
print(f"Found {len(seqs)} sequences of weight {target}.")

# validated = []
# for seq in seqs:
#     remains = list(set(weights).difference(seq))
#     if canPartition(remains):
#         validated.append(seq)


def quantumEntanglement(partition):
    return math.prod(partition)


fewest_packages = min([len(g) for g in seqs])
first_group = [g for g in seqs if len(g) == fewest_packages]
if len(first_group) > 1:
    quantum = sorted([(quantumEntanglement(g), g) for g in first_group])

print(quantum[0][0])

