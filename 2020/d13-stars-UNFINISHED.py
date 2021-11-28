import time, math
from helpers import *

t = time.time()

# Read notes to array
input = mypath + "d13-input.txt"
with open(input) as f:
    notes = f.read().splitlines()

# Part 1
my_arrival = int(notes[0])
bus_table = notes[1].split(",")
bus_ids = [int(bus) for bus in bus_table if bus != "x"]

next_bus_after_arrival = [math.ceil((my_arrival / bus)) * bus for bus in bus_ids]
earliest_bus = min(next_bus_after_arrival)
earliest_bus_id = bus_ids[next_bus_after_arrival.index(earliest_bus)]

earliest_timestamp = earliest_bus_id * (earliest_bus - my_arrival)

dropstar(25, earliest_timestamp, t)

# Part 2 - UNSOLVED OR BRUTEFORCED?
bus_dept = [int(bus_table.index(bus)) for bus in bus_table if bus != "x"]

t_time = 100000000000000

# Find a t-value for each bus
bus_t_offset = []
for bus in bus_ids:
    departure_delay = bus_dept[bus_ids.index(bus)]
    aligned = False
    while not aligned:
        aligned = (t + departure_delay) % bus == 0
        t_time += 1
    bus_t_offset.append(t - 1)

# print(bus_t_offset)

# Find where all align
keep_on_trucking = True
while keep_on_trucking:
    aligned = [(t + bus_dept[idx]) % bus == 0 for idx, bus in enumerate(bus_ids)]
    if sum(aligned) == len(aligned):
        keep_on_trucking = False
        print(t, aligned)
    # if sum(aligned) > 4:
    # 	print(t_time, aligned)
    t_time += largest_bus_id

dropstar(26, t_time, t)
