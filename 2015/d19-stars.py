import time, re
from helpers import *

t = time.time()

input = mypath + "d19-input.txt"
with open(input) as f:
    calibrations = f.read().split("\n\n")

replacements = calibrations[0].split("\n")
molecule = calibrations[1]

replacer_pairs = [(r.split(" => ")[0], r.split(" => ")[1]) for r in replacements]

# Search and replace one pair at a time and add new molecules to set
molecule_variations = set()
for pair in replacer_pairs:
    search, replace = pair
    match = re.finditer(search, molecule)
    for m in match:
        molecule_variations.add(molecule[: m.start()] + replace + molecule[m.end() :])

dropstar(37, len(molecule_variations), t)

# Part 2

# dropstar(38, , t)
