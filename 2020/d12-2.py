# Day 12 - Part 2

import time
from collections import deque
startTime = time.time()

# Read navigation instructions to array
input = "d12-input.txt"
with open(input) as f:
	nav_codes = f.read().splitlines()

# Rotate dict from https://stackoverflow.com/questions/58366635/rotate-values-of-a-dictionary
def rotate(d, n=1):
    """
    @param d: input python dictionary
    @param n: number of times to rotate it; default:1

    @return do: output dict rotated n times
    ex: d = {34: 'apple', 65: 'ball', 32: 'cat', 78: 'dog'}
        rotate(d, 1) -> {34: 'dog', 65: 'apple', 32: 'ball', 78: 'cat'}
    """

    # Get the values of the dict and put them into a deque collection that contains a rotate method
    do = deque(d.values())
    do.rotate(n)  # rotate the values by n
    do = dict(zip(d.keys(), do))  # recombine the keys and values

    return do

position = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
course = 'E'

for instruction in nav_codes:
  action = instruction[0]
  value = int(instruction[1:])
  if action == 'R':
    waypoint = rotate(waypoint, int(value / 90))
  elif action == 'L':
    waypoint = rotate(waypoint, -int(value / 90))
  elif action == 'F':
    position['N'] += waypoint['N'] * value
    position['E'] += waypoint['E'] * value
    position['S'] += waypoint['S'] * value
    position['W'] += waypoint['W'] * value
  else:
    waypoint[action] += value

print(position)
position_ew = abs(position['E'] - position['W'])
position_ns = abs(position['N'] - position['S'])

print("East/west position: {0} + north/south position: {1} = {2} ".format(position_ew, position_ns, position_ew + position_ns))
print('Execution time in seconds: {0}'.format(time.time() - startTime))