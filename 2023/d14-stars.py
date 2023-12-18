import time
from tqdm import tqdm
from helpers import *

t = time.time()

# input = mypath + "d14-example.txt"
input = mypath + "d14-input.txt"
with open(input) as f:
    platform = [list(r) for r in f.read().split("\n")]

pfcopy = platform.copy()

# Part 1

# Join a 2D array
def printable(arr: list) -> str:
    return "\n".join(["".join(row) for row in arr])
    
# Get column from a 2D array
def get_col(arr: list, col: int) -> list:
    return [row[col] for row in arr]

# Find the first index to left of a given index in a list that is not a dot
def stop_at(arr: list, idx: int) -> int:
    for i in range(idx - 1, -1, -1):
        if arr[i] != ".":
            return i + 1
    return 0

# Calculate the value of 'O' rocks on a given row
def calc_row(arr: list, row: int) -> int:
    rocks = arr[row].count("O")
    return rocks * (len(arr) - row)

# Move all O's up in the array
def tilt_platform(platfm: list) -> list:
    for i, row in enumerate(platfm):
        for j, rock in enumerate(row):
            if rock == "O":
                row[j] = "."
                roll_to = stop_at(get_col(platfm, j), i)
                platfm[roll_to][j] = "O"
    return platfm

platform = tilt_platform(platform)
# print(printable(platform), "\n")
rock_sum = sum([calc_row(platform, r) for r in range(len(platform))])

dropstar(27, rock_sum, t)


# Part 2
# After a while (177 tilt cycles), the pattern repeats every 14 cycles
# 
# Guess #1: 66694 - too low
# Guess #2: 103878 - too high
# Guess #3: 103861 - correct

# Transpose a 2D array clockwise
def transpose(arr: list) -> list:
    return [list(row) for row in zip(*arr[::-1])]

def tilt_cycle(arr: list) -> list:
    arr = tilt_platform(arr)
    for i in range(3):
        arr = tilt_platform(transpose(arr))
    return transpose(arr)

# Examine first few hundred numbers in the series to find the repeating pattern
series = []
for r in tqdm(range(200)):
    platform = tilt_cycle(platform)
    # print(printable(platform), "\n")
    rock_sum = sum([calc_row(platform, r) for r in range(len(platform))])
    series.append(rock_sum)

# print(series)

# Numbers up until index 176 are chaotic. Following 14 numbers are then repeating endlessly in a cycle of 14.
# Function that returns a number in the series at a given index
def get_number(index: int, series: list) -> int:
    if index < 176:
        return series[index]
    else:
        return series[176 + (index - 176) % 14 - 1]


dropstar(28, get_number(1000000000, series), t)

