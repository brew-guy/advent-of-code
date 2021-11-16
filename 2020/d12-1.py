# Day 12 - Part 1

import time
startTime = time.time()

# Read navigation instructions to array
input = "d12-input.txt"
with open(input) as f:
	nav_codes = f.read().splitlines()

def get_course(course, angle):
  directions = ['N', 'E', 'S', 'W']
  turn = int(int(angle[1:]) / 90)
  if angle[0] == 'R':
    new_course = directions.index(course) + turn
    if new_course > 3:
      new_course = abs(4 - new_course)
    return directions[new_course]
  if angle[0] == 'L':
    new_course = directions.index(course) - turn
    if new_course < 0:
      new_course = abs(4 + new_course)
    return directions[new_course]

position = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
course = 'E'

for instruction in nav_codes:
  action = instruction[0]
  if action == 'R' or action == 'L':
    course = get_course(course, instruction)
  elif action == 'F':
    position[course] += int(instruction[1:])
  else:
    position[action] += int(instruction[1:])

print(position)
position_ew = abs(position['E'] - position['W'])
position_ns = abs(position['N'] - position['S'])

print("East/west position: {0} + north/south position: {1} = {2} ".format(position_ew, position_ns, position_ew + position_ns))
print('Execution time in seconds: {0}'.format(time.time() - startTime))