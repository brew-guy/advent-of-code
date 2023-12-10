import time
from helpers import *

t = time.time()

# input = mypath + "d5-example.txt"
input = mypath + "d5-input.txt"
with open(input) as f:
    almanac = f.read().split("\n\n")

almanac_copy = almanac.copy()

# Generate list of seed dicts
seed_data = almanac.pop(0)
seed_data = seed_data.split(':')[1].split()
seeds = [{"seed": int(s)} for s in seed_data]

# Parse map data
def parse_map(map):
  map = map.split('\n')
  map_type = map.pop(0)
  map_type_from, map_type_to = map_type.split()[0].split('-to-')
  map_table = [v.split() for v in map]
  return map_type_from, map_type_to, map_table

# Parse seed source value to destination value
def parse_seed_data(source, table):
  for row in table:
    dst_start, src_start, length = [int(v) for v in row]
    if source >= src_start and source < src_start + length:
      return dst_start + source - src_start
  return source

# Loop over map data in almanac, pop off each map and process map data
while len(almanac) > 0:
  map = almanac.pop(0)
  map_type_from, map_type_to, map_table = parse_map(map)
  # print(f"map_type_from: {map_type_from}")
  # print(f"map_type_to: {map_type_to}")
  # print(f"map_table: {map_table}")
  for seed in seeds:
    if map_type_from in seed:
      seed[map_type_to] = parse_seed_data(seed[map_type_from], map_table)

min_location = min([s['location'] for s in seeds])

dropstar(9, min_location, t)

# Part 2
# Generate new dict of seeds from ranges

almanac = almanac_copy.copy()
almanac.pop(0)

new_seed_data = []
new_seed_data = []
for i in range(0, len(seed_data) - 1, 2):
  s = int(seed_data[i])
  l = int(seed_data[i + 1])
  r = range(s, s + l)
  new_seed_data.append(r)
  # print % done status
  print(f"{(i+1) / len(seed_data) * 100:.0f}% done")


