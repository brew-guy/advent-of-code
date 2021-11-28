import time, math
from helpers import *

t = time.time()

input = 29000000

# Part 1
# Faster than naive from https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/?ref=lbp
def factors(n):
    i = 1
    divisors = []
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors += [i, int(n / i)]
        i += 1
    return divisors


presents = lambda house: sum(factors(house)) * 10

house, delivered = int(input / 50), 0
while delivered < input:
    house += 1
    delivered = presents(house)

dropstar(39, house, t)

# Part 2
# Guess 1: 637560 - too low
# Guess 2: 2636364 - too high
# Guess 3: 276255 - too low
house, delivered = 0, 0
elf = 1
while delivered < input:
    for i in range(50):
        house += elf
        delivered = elf * 11
        if delivered > input:
            break
        # print(house, elf, delivered)
    elf += 1

print(house, elf, delivered)

dropstar(40, house, t)
