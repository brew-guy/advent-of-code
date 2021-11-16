# Day 16 - Part 1

import time
import re
startTime = time.time()

# Read document to array split by double-linebreaks
input = "d16-input.txt"
with open(input) as f:
	document = f.read().split('\n\n')

# Split fields to dictionary of fields and range values {zone: [46, 293, 307, 967] ...}
fields = {}
for field in document[0].splitlines():
	r = re.match('(\w.+): (\d.+)-(\d.+) or (\d.+)-(\d.+)', field).groups()
	fields[r[0]] = [int(r[1]), int(r[2]), int(r[3]), int(r[4])]

# MAke one big set with all the valid numbers
ranges = set()
for rng in fields.values():
	ranges.update(range(rng[0], rng[1] + 1))
	ranges.update(range(rng[2], rng[3] + 1))

# Split my ticket numbers to an array
my_ticket = document[1].splitlines()[1].split(',')
my_ticket = [int(n) for n in my_ticket]

# Split nearby ticket numbers to array of array of numbers
near_tickets = list(map(lambda ticket: ticket.split(','), document[2].splitlines()[1:]))
near_tickets = [[int(t) for t in tick] for tick in near_tickets]

# Check all nearby ticket values against the set of all numbers
error_rate = 0
for ticket in near_tickets:
	for value in ticket:
		if value not in ranges:
			error_rate += value

print("The ticket scanning error rate is {0}".format(error_rate))
print('Execution time in seconds: {0}'.format(time.time() - startTime))