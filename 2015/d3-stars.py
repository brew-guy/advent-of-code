import os, sys

path = os.path.join(sys.path[0], "d3-input-1.txt")
with open(path, mode="r") as f:
    lines = f.readlines()

directions = [pointer for pointer in lines[0]]
course = {
    "<": (-1, 0),
    ">": (1, 0),
    "v": (0, -1),
    "^": (0, 1),
}

current_pos = (0, 0)
houses = {current_pos: 1}


def dropoff(current_pos, houses):
    if current_pos in houses:
        houses[current_pos] += 1
    else:
        houses[current_pos] = 1


# Part 1
for next in directions:
    change_pos = course[next]
    current_pos = tuple(
        sum(current_pos) for current_pos in zip(current_pos, change_pos)
    )
    dropoff(current_pos, houses)

print(f"Star 5: {len(houses)}")

# Part 2
santa_current_pos = (0, 0)
robo_current_pos = (0, 0)
houses = {santa_current_pos: 1}


def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)


for next in pairwise(directions):
    santa_change_pos, robo_change_pos = course[next[0]], course[next[1]]
    santa_current_pos = tuple(
        sum(santa_current_pos)
        for santa_current_pos in zip(santa_current_pos, santa_change_pos)
    )
    robo_current_pos = tuple(
        sum(robo_current_pos)
        for robo_current_pos in zip(robo_current_pos, robo_change_pos)
    )
    dropoff(santa_current_pos, houses)
    dropoff(robo_current_pos, houses)

print(f"Star 6: {len(houses)}")
