import time
from helpers import *

t = time.time()


input = "d2-input.txt"
with open(input) as f:
    lines = f.read()

# Part 1
policies = lines.split("\n")

valid = invalid = 0

for policy in policies:
    min = int(policy[0 : policy.find("-")])
    max = int(policy[policy.find("-") + 1 : policy.find(" ")])
    letter = policy[policy.find(" ") + 1 : policy.find(" ") + 2]
    password = policy[policy.find(": ") + 2 :]
    if password.count(letter) >= min and password.count(letter) <= max:
        valid = valid + 1
    else:
        invalid = invalid + 1

dropstar(3, valid, t)

# Part 2
valid = invalid = 0

for policy in policies:
    first_pos = int(policy[0 : policy.find("-")])
    second_pos = int(policy[policy.find("-") + 1 : policy.find(" ")])
    letter = policy[policy.find(" ") + 1 : policy.find(" ") + 2]
    password = policy[policy.find(": ") + 2 :]
    if (
        password[first_pos - 1] == letter and not password[second_pos - 1] == letter
    ) or (not password[first_pos - 1] == letter and password[second_pos - 1] == letter):
        valid = valid + 1
    else:
        invalid = invalid + 1

dropstar(4, valid, t)
