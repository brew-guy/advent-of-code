import time
from helpers import *

t = time.time()

# Read bag rules to dictionary
input = "d7-input.txt"
with open(input) as f:
    rules = f.read().splitlines()

# Part 1
master = {}

# Create dictionary of rule sets {bag : {bag : n, bag : n, bag : n...}}
for rule in rules:
    has_bags = {}
    wordlist = rule.split(" ")
    bag = " ".join(wordlist[:2])
    if wordlist[4] == "no":
        has_bags["None"] = 1
    else:
        has_bags[" ".join(wordlist[5:7])] = int(wordlist[4])
    for i in range(8, len(wordlist), 4):
        has_bags[" ".join(wordlist[i + 1 : i + 3])] = int(wordlist[i])
    master[bag] = has_bags

print(master)

# FINDBAG = 'shiny gold'
# can_hold_shiny = set()
# for bag in master:
#   if FINDBAG in master[bag]:
#     can_hold_shiny.add(bag)
# print(can_hold_shiny)

# for bag in can_hold_shiny:
#   if FINDBAG in master[bag]:
#     can_hold_shiny.add(bag)
# print(can_hold_shiny)

# Replace bags in bags
replaced = master.copy()
keep_replacing = True
iterations = 0

while keep_replacing:
    for bag in master:
        before_replace = replaced[bag].copy()
        for content in before_replace:
            if content in master:
                bag_amount = replaced[bag][content]
                # new_content.pop(content)
                for b in master[content]:
                    print(new_content[b], bag_amount)
                    # new_content[b] = master[content][b] * bag_amount
                    # new_content = {**new_content, **master[content]}
                print(
                    "{0} bag had {1} {2} => {3}".format(
                        bag, replaced[bag][content], content, new_content
                    )
                )
            t = [
                master[content]
                if content in master and master[content] != "None"
                else content
                for content in replaced[bag]
            ]
            replaced[bag] = [item for sublist in t for item in sublist]
        if before_replace == replaced[bag]:
            keep_replacing = False
            print(
                "{0} changed from {1} to {2}".format(bag, before_replace, replaced[bag])
            )
        else:
            keep_replacing = True
    iterations += 1

print(replaced)
# dropstar(13, , t)

# print('{0} iterations required to replace bags in all levels.'.format(iterations))
print("Execution time in seconds: {0}".format(time.time() - startTime))

# Part 2

# dropstar(14, , t)
