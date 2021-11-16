# Day 4 - Part 1
import time
startTime = time.time()

# Read input file to array of strings, one string per line of input file
input = "d4-input.txt"
with open(input) as f:
	lines = f.readlines()
if lines[-1] != '\n': lines.append('\n') # Last line must be blank to include last passport  in array

# Collect passports in a dictionary
passports = []
passport = {}

for line in lines:
  if line != '\n':
    field_pairs = line.strip('\n').split(' ')
    for pair in field_pairs:
      passport[pair.split(':')[0]] = pair.split(':')[1]
  else:
    passports.append(passport)
    passport = {}

print('Passports found: {0}'.format(len(passports)))

# Count valid passports
mandatory_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid = invalid = 0

for pp in passports:
  if all (key in pp for key in mandatory_keys):
    valid += 1
  else:
    invalid += 1

print("{0} of the given passports were valid, {1} were invalid.".format(valid, invalid))
print('Execution time in seconds: {0}'.format(time.time() - startTime))