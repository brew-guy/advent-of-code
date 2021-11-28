import time, re, math
from helpers import *

t = time.time()

# Read document to array split by double-linebreaks
input = mypath + "d16-input.txt"
with open(input) as f:
    document = f.read().split("\n\n")

# Part 1
# Split fields to dictionary of fields and range values {zone: [46, 293, 307, 967] ...}
fields = {}
for field in document[0].splitlines():
    r = re.match("(\w.+): (\d+)-(\d+) or (\d+)-(\d+)", field).groups()
    fields[r[0]] = [int(r[1]), int(r[2]), int(r[3]), int(r[4])]

# Make one big set with all the valid numbers
ranges = set()
for rng in fields.values():
    ranges.update(range(rng[0], rng[1] + 1))
    ranges.update(range(rng[2], rng[3] + 1))

# Split my ticket numbers to an array
my_ticket = document[1].splitlines()[1].split(",")
my_ticket = [int(n) for n in my_ticket]

# Split nearby ticket numbers to array of array of numbers
near_tickets = list(map(lambda ticket: ticket.split(","), document[2].splitlines()[1:]))
near_tickets = [[int(t) for t in tick] for tick in near_tickets]

# Check all nearby ticket values against the set of all numbers
error_rate = 0
for ticket in near_tickets:
    for value in ticket:
        if value not in ranges:
            error_rate += value

dropstar(31, error_rate, t)

# Part 2
# Check all nearby ticket values against the set of all numbers
# Make array of valid tickets
valid_tickets = []
for ticket in near_tickets:
    if all([value in ranges for value in ticket]):
        valid_tickets.append(ticket)


def column_match_fields(tickets_column):
    matching_fields = []
    for field in fields:
        l1 = fields[field][0]
        u1 = fields[field][1]
        l2 = fields[field][2]
        u2 = fields[field][3]
        matching = [l1 <= val <= u1 or l2 <= val <= u2 for val in tickets_column]
        if all(matching):
            matching_fields.append(field)
    return matching_fields


# Iterate over fields and pluck them out if they are the only field that matches a ticket column of numbers
field_order = {}
while len(fields) > 0:
    for idx in range(0, len(valid_tickets[0])):
        tickets_column = [ticket[idx] for ticket in valid_tickets]
        matching_fields = column_match_fields(tickets_column)
        if len(matching_fields) == 1:
            field_order[matching_fields[0]] = idx
            fields.pop(matching_fields[0])

# print(len(field_order), field_order)

my_six_fields = [field_order[f] for f in field_order if "departure" in f]
my_six_values = [my_ticket[val] for val in my_six_fields]
my_product = math.prod(my_six_values)

dropstar(32, my_product, t)
