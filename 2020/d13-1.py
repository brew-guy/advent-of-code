# Day 13 - Part 1

import time
import math
startTime = time.time()

# Read notes to array
input = "d13-input.txt"
with open(input) as f:
	notes = f.read().splitlines()

my_arrival = int(notes[0])
bus_table = notes[1].split(',')
bus_ids = [int(bus) for bus in bus_table if bus != 'x']

next_bus_after_arrival = [math.ceil((my_arrival / bus)) * bus for bus in bus_ids]
earliest_bus = min(next_bus_after_arrival)
earliest_bus_id = bus_ids[next_bus_after_arrival.index(earliest_bus)]

earliest_timestamp = earliest_bus_id * (earliest_bus - my_arrival)

print("Bus with ID {0} departs {1} minutes after my arrival. Multiplied = {2} ".format(earliest_bus_id, earliest_bus - my_arrival, earliest_timestamp))
print('Execution time in seconds: {0}'.format(time.time() - startTime))