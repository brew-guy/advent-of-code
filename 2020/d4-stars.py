import time, re
from helpers import *

t = time.time()

input = mypath + "d4-input.txt"
with open(input) as f:
    lines = f.readlines()
if lines[-1] != "\n":
    lines.append("\n")  # Last line must be blank to include last passport in array

# Part 1
passports = []
passport = {}

# Collect passports in a dictionary
for line in lines:
    if line != "\n":
        field_pairs = line.strip("\n").split(" ")
        for pair in field_pairs:
            passport[pair.split(":")[0]] = pair.split(":")[1]
    else:
        passports.append(passport)
        passport = {}

mandatory_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
valid = invalid = 0

# Count valid passports
for pp in passports:
    if all(key in pp for key in mandatory_keys):
        valid += 1
    else:
        invalid += 1

dropstar(7, valid, t)

# Part 2
mandatory_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
key_validation = {
    "byr": "^(19[2-9][0-9]|200[0-2])$",
    "iyr": "^(201[0-9]|2020)$",
    "eyr": "^(202[0-9]|2030)$",
    "hgt": "^((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)$",
    "hcl": "^#([0-9]|[a-f]){6}$",
    "ecl": "^(amb|blu|brn|gry|grn|hzl|oth)$",
    "pid": "^[0-9]{9}$",
}

valid = invalid = 0

# Count valid passports
for pp in passports:
    # Verify the passport has all mandatory fields
    if all(key in pp for key in mandatory_keys):
        # Validate data in each field of the passport
        bad_field = False
        for vkey in key_validation:
            pattern = key_validation[vkey]
            if re.match(pattern, pp[vkey]) == None:
                invalid += 1
                bad_field = True
                break
        if bad_field == False:
            valid += 1
    else:
        invalid += 1

dropstar(8, valid, t)
