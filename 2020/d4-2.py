# Day 4 - Part 2
import re
import time
startTime = time.time()

# Read input file to array of strings, one string per line of input file
input = "d4-input.txt"
with open(input) as f:
	lines = f.readlines()
if lines[-1] != '\n': lines.append('\n') # Last line must be blank to include last passport  in array

# Find a way to clip it up in two lines with join/split and a map
# with open(input) as f:
# 	lines = f.read()
# passdata = re.sub(r'(\w)\n', r'\1 ', lines)

# Collect all passports in dictionaries inside an array
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
key_validation = {
  'byr':'^(19[2-9][0-9]|200[0-2])$',
  'iyr':'^(201[0-9]|2020)$',
  'eyr':'^(202[0-9]|2030)$',
  'hgt':'^((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)$',
  'hcl':'^#([0-9]|[a-f]){6}$',
  'ecl':'^(amb|blu|brn|gry|grn|hzl|oth)$',
  'pid':'^[0-9]{9}$'
  }

valid = invalid = 0

for pp in passports:
  # Verify the passport has all mandatory fields
  if all (key in pp for key in mandatory_keys):
    # Validate data in each field of the passport
    bad_field = False
    for vkey in key_validation:
      pattern = key_validation[vkey]
      if re.match(pattern, pp[vkey]) == None:
        invalid += 1
        bad_field = True
        break
    if bad_field == False: valid += 1
  else:
    invalid += 1

print("{0} of the given passports were valid, {1} were invalid.".format(valid, invalid))
print('Execution time in seconds: {0}'.format(time.time() - startTime))