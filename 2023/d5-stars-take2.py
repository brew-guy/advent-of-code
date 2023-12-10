import time
from tqdm import tqdm
from helpers import *

t = time.time()

# input = mypath + "d5-example.txt"
input = mypath + "d5-input.txt"
with open(input) as f:
    almanac = f.read().split("\n\n")

# Part 1
# Maps appear in order of application, so we can pop off the first map and apply
#  it to all seeds, then pop off the next map and apply it to all seeds, etc.

# Generate array with seed data
seeds_data = almanac.pop(0)
maps_data = almanac.copy()
seeds_part = seeds_data.split(':')[1].split()
seeds = [int(s) for s in seeds_part]

# Parse map data
def parse_map(map):
  map = map.split('\n')
  map_table = [[int(v) for v in row.split()] for row in map[1:]]
  return map_table

# Parse seed source value to destination value
def parse_seed_data(source, map_table):
  for row in map_table:
    dst_start, src_start, length = row
    if source >= src_start and source < src_start + length:
      return dst_start + source - src_start
  return source

# Loop over maps from almanac, pop off each map and process seed data with map
processed = seeds
while len(maps_data) > 0:
  map = maps_data.pop(0)
  map_table = parse_map(map)
  processed = [parse_seed_data(s, map_table) for s in processed]

dropstar(9, min(processed), t)


# Part 2
# Generate new list of seeds by ranges
# Figure out how long it takes. If it's too long, we'll need to optimize.
# Some ranges are millions of numbers long, so maybe we can't just generate a list

seeds_data_ranges = []
for i in tqdm(range(0, len(seeds) - 1, 2)):
  start, length = seeds[i], seeds[i + 1]
  r = range(start, start + length)
  seeds_data_ranges.append(r)

# Loop over maps from almanac, pop off each map and process seed data ranges with map

lowest = max([s.stop for s in seeds_data_ranges])

maps_data = almanac.copy()
map = maps_data.pop(0)
map_table = parse_map(map)

# while len(maps_data) > 0:
#   map = maps_data.pop(0)
#   map_table = parse_map(map)
#   for s in tqdm(seeds_data_ranges[1]):
#     output = parse_seed_data(s, map_table)
#     lowest = min(lowest, output)
#   print(f"Processing 1 map done")

print(lowest)

# dropstar(10, min(processed), t)



