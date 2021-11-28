# Day 13 - Part 2

import time

startTime = time.time()

# Read notes to array
input = mypath + "d13-input.txt"
with open(input) as f:
    notes = f.read().splitlines()
bus_table = notes[1].split(",")

bus_ids = [int(bus) for bus in bus_table if bus != "x"]
bus_dept = [int(bus_table.index(bus)) for bus in bus_table if bus != "x"]
highest_bus_id = max(bus_ids)

t = 100000000000000

# Find a t-value for each bus
bus_t_offset = []
for bus in bus_ids:
    departure_delay = bus_dept[bus_ids.index(bus)]
    aligned = False
    while not aligned:
        aligned = (t + departure_delay) % bus == 0
        t += 1
    bus_t_offset.append(t - 1)

print(bus_t_offset)

# Find where all align
keep_on_trucking = True
while keep_on_trucking:
    aligned = [(t + bus_dept[idx]) % bus == 0 for idx, bus in enumerate(bus_ids)]
    if sum(aligned) == len(aligned):
        keep_on_trucking = False
        print(t, aligned)
    # if sum(aligned) > 4:
    # 	print(t, aligned)
    t += highest_bus_id


print("t = {0} is the sweet spot".format(t))
print("Execution time in seconds: {0}".format(time.time() - startTime))

