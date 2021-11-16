# Day 6 - Part 2
# Kan også laves mere elegant med intersection() på lists...

import re
import time
startTime = time.time()

# Read each person's response in group to array of arrays
input = "d6-input.txt"
with open(input) as f:
	forms = f.read()[:-1].split('\n\n')
responses = list(map(lambda group: group.split('\n'), forms))

# Check all letters in first array against rest of arrays
def findsame(array):
  found = {}
  for letter in array[0]:
    if all(letter in sequence for sequence in array):
     found[letter] = True
  return len(found)

all_yes_responders = map(findsame, responses)

print("Received {0} group forms with a total of {1} responses.".format(len(responses), len([item for sublist in responses for item in sublist])))

print("Sum of all the unique group form responses were {0}.".format(sum(list(all_yes_responders))))
print('Execution time in seconds: {0}'.format(time.time() - startTime))