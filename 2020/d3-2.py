# Day 3 - Part 2
import time
startTime = time.time()

input = "d3-input.txt"
with open(input) as f:
	lines = f.read()[:-1] # read and get rid of the pestering last linebreak

area = lines.split("\n")
area_height = len(area)
area_width = len(area[0])
print("Looking at {0} rows of toboggan mayhem in the input scenario.".format(area_height))

def slope(deltaCol, deltaRow):
  row = col = 0
  trees = 0
  while row < area_height:
    position = area[row][col]
    if position == '#':
      trees += 1
    # print('{0} ({1},{2}) = {3} trees so far'.format(position, row, col, trees))
    col = col + deltaCol
    if col > area_width - 1:
      col = col - area_width
    row = row + deltaRow
  print('Trees encountered on route going {0} right followed by {1} down: {2}'.format(deltaCol, deltaRow, trees))
  return trees

print('Trees encountered on all routes, multiplied: {0}'.format(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2)))
print('Execution time in seconds: {0}'.format(time.time() - startTime))