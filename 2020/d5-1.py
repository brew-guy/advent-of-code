# Day 5 - Part 1
import time
startTime = time.time()

# Read seat sequences to array
input = "d5-input.txt"
with open(input) as f:
	seats = f.read().strip().split('\n')

print("Scanned {0} boarding passes.".format(len(seats)))

def findrow(sequence):
  low = 0
  high = 127
  for char in sequence[:len(sequence)-1]:
    if char == 'F':
      high =  int(high - (high - low)/2)
    if char == 'B':
      low = round(low + (high - low)/2)
  if sequence[-1] == 'F':
    return low
  else:
    return high

def findcol(sequence):
  low = 0
  high = 7
  for char in sequence[:len(sequence)-1]:
    if char == 'L':
      high =  int(high - (high - low)/2)
    if char == 'R':
      low = round(low + (high - low)/2)
  if sequence[-1] == 'L':
    return low
  else:
    return high

def findseatID(sequence):
  return (findrow(sequence[:8]) * 8 + findcol(sequence[7:]))

seatIDs = []
for seat in seats:
  seatIDs.append(findseatID(seat))
  
print("The highest seat ID is {0}.".format(max(seatIDs)))
print('Execution time in seconds: {0}'.format(time.time() - startTime))