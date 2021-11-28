import time, re
from helpers import *

t = time.time()

input = mypath + "d19-input.txt"
with open(input) as f:
    chemistry = f.readlines()

molecule = chemistry.pop()
chemistry.pop()

# Part 1
def getReplacement(compound):
    regexp = r"([A-Za-z]*) => ([A-Za-z]*)"
    match = re.match(regexp, compound)
    return match.groups()


def replaceFiesta(molecule, processed="", replaced=[], variations=[]):
    if len(molecule) < 1:
        return replaced, variations
    elif molecule[:1] in replace_dict:
        processed += molecule[:1]
        replacers = replace_dict[molecule[:1]]
        replaced.append(replacers)
        variations += [processed + r + molecule[1:] for r in replacers]
        return replaceFiesta(molecule[1:], processed, replaced, variations)
    elif molecule[:2] in replace_dict:
        processed += molecule[:2]
        replacers = replace_dict[molecule[:2]]
        replaced.append(replacers)
        variations += [processed + r + molecule[2:] for r in replacers]
        return replaceFiesta(molecule[2:], processed, replaced, variations)
    else:
        replaced.append(molecule[:1])
        processed += molecule[:1]
        return replaceFiesta(molecule[1:], processed, replaced, variations)


replace_dict = {}
for comp in chemistry:
    compound, replacement = getReplacement(comp)
    if compound in replace_dict:
        replace_dict[compound].append(replacement)
    else:
        replace_dict[compound] = [replacement]


replace_options, replace_variations = replaceFiesta(molecule)
replace_lengths = [len(r) for r in replace_options if len(r) > 1]
print(len(set(replace_variations)))
print(len(replace_variations))

# print(replace_options)

distinct = sum(replace_lengths)

dropstar(37, distinct, t)

# Part 2

# dropstar(38, , t)
