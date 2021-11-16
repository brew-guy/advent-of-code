# Day 11 - Part 1

import time
startTime = time.time()

# Read seat layout as array of arrays of characters
input = "d11-input.txt"
with open(input) as f:
	layout = [list(i) for i in f.read().splitlines()]

def isEmptyChair(row, col):
  if 0 <= row < len(layout) and 0 <= col < len(layout[0]):
    return layout[row][col] == 'L'
  else:
    return False

def isOccupiedChair(row, col):
    if 0 <= row < len(layout) and 0 <= col < len(layout[0]):
      return layout[row][col] == '#'
    else:
      return False

def occupiedNeighbours(row, col):
  freeNeighbours = [
    isOccupiedChair(row-1, col),
    isOccupiedChair(row+1, col),
    isOccupiedChair(row, col-1),
    isOccupiedChair(row, col+1),
    isOccupiedChair(row-1, col-1),
    isOccupiedChair(row-1, col+1),
    isOccupiedChair(row+1, col-1),
    isOccupiedChair(row+1, col+1)
  ]
  return sum(freeNeighbours)

go_get_them = True
rounds = 0

while go_get_them:
  layout_after = [inner_list.copy() for inner_list in layout]
  for row in range(0, len(layout)):
    for col in range(0, len(layout[0])):
      if isEmptyChair(row, col) and occupiedNeighbours(row, col) == 0:
        layout_after[row][col] = '#'
      elif isOccupiedChair(row, col) and occupiedNeighbours(row, col) >= 4:
        layout_after[row][col] = 'L'
  if layout_after == layout:
    go_get_them = False
  layout = [inner_list.copy() for inner_list in layout_after]
  rounds += 1

occupied = sum([chair == '#' for row in layout_after for chair in row])

output = list(map(lambda row: ''.join(row), layout))
with open("outfile.txt", "w") as outfile:
    outfile.write("\n".join(output))

print("After {0} rounds, {1} chairs were occupied.".format(rounds, occupied))
print('Execution time in seconds: {0}'.format(time.time() - startTime))