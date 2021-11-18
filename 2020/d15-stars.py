import time
from helpers import *

t = time.time()

# Initialization program
input = [16, 11, 15, 0, 1, 7]
numbers_spoken = input

# Part 1
while len(numbers_spoken) < 2020:
    next_up = numbers_spoken[-1]
    if numbers_spoken.count(next_up) <= 1:
        new_number = 0
    else:
        last_found = list(
            reversed([idx for idx, num in enumerate(numbers_spoken) if num == next_up])
        )
        new_number = last_found[0] - last_found[1]
    numbers_spoken.append(new_number)

# print(numbers_spoken, len(numbers_spoken))

dropstar(29, numbers_spoken[-1], t)

# Part 2
numbers_spoken = {}
# Initialization program to dictionary
for idx, number in enumerate(input):
    numbers_spoken[number] = idx

# print(numbers_spoken)

last_spoken = input[-1]
for idx in range(len(input) - 1, 30000000):
    if last_spoken in numbers_spoken and numbers_spoken[last_spoken] < idx:
        next_number = idx - numbers_spoken[last_spoken]
    else:
        next_number = 0
    numbers_spoken[last_spoken] = idx
    last_spoken = next_number

last = max(numbers_spoken, key=lambda key: numbers_spoken[key])

dropstar(30, last, t)
