# Day 2 - Part 1
import time
startTime = time.time()

input = "d2-input.txt"
with open(input) as f:
	lines = f.read()[:-1] # read and get rid of the pestering last linebreak

policies = lines.split("\n")

print("Found {0} policies in input string.".format(len(policies)))
valid = invalid = 0

for policy in policies:
  min = int(policy[0:policy.find("-")])
  max = int(policy[policy.find("-") + 1:policy.find(" ")])
  letter = policy[policy.find(" ") + 1: policy.find(" ") + 2]
  password = policy[policy.find(": ") + 2:]
  if password.count(letter) >= min and password.count(letter) <= max:
    valid = valid + 1
  else:
    invalid = invalid + 1

print("{0} of the found passwords were valid, {1} were invalid.".format(valid, invalid))

print('Execution time in seconds: {0}'.format(time.time() - startTime))