import time
startTime = time.time()

# Read notes to array
input = "d13-input.txt"
with open(input) as f:
	notes = f.read().splitlines()
bus_table = notes[1].split(',')

bus_ids = [int(bus) for bus in bus_table if bus !='x']
bus_dept = [int(bus_table.index(bus)) for bus in bus_table if bus !='x']

t = 100000000000000

# Find best offset and step value using the largest bus ID
highest_bus_id = max(bus_ids)
departure_delay = bus_dept[bus_ids.index(highest_bus_id)]
keep_on_trucking = True
while keep_on_trucking:
	aligned = (t + departure_delay) % highest_bus_id == 0
	if aligned:
		keep_on_trucking = False
		print(t, aligned)
	else:
		t += 1

# Brute force to the first possible line-up of the bus times
keep_on_trucking = True
while keep_on_trucking:
	aligned = [(t + bus_dept[idx]) % bus == 0 for idx, bus in enumerate(bus_ids)]
	if sum(aligned) == len(aligned):
		keep_on_trucking = False
		print(t, aligned)
	if sum(aligned) > 5:
		print(t, aligned)
	t += highest_bus_id

Print(t)

# print("Bus with ID {0} departs {1} minutes after my arrival. Multiplied = {2} ".format(earliest_bus_id, earliest_bus - my_arrival, earliest_timestamp))
print('Execution time in seconds: {0}'.format(time.time() - startTime))