import time, re, itertools
from helpers import *

t = time.time()

input = "target area: x=57..116, y=-198..-148"

# Part 1
regexp = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"
target = [int(m) for m in re.match(regexp, input).groups()]


def hitsTarget(vx, vy):
    px, py = 0, 0
    max_y = 0
    x1, x2, y1, y2 = target
    while px <= x2 and py >= y1:
        if px >= x1 and py <= y2:
            return True, max_y
        px += vx
        py += vy
        vx -= vx / abs(vx) if vx != 0 else 0
        vy -= 1
        max_y = max(max_y, py)
    return False, 0


x = range(-250, 400)
velocities = [p for p in itertools.product(x, repeat=2)]

hits = []
for v in velocities:
    x, max_y = hitsTarget(*v)
    hits.append((max_y, v)) if x else None

dropstar(33, sorted(hits, reverse=True)[0][0], t)

# Part 2
t = time.time()

dropstar(34, len(hits), t)
