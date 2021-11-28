import itertools


import itertools

weapon_options = ["w1", "w2", "w3", "w4", "w5"]
w = itertools.combinations(weapon_options, 1)

armor_options = ["a0", "a1", "a2", "a3", "a4", "a5"]
a = itertools.combinations(armor_options, 1)

ring_options = ["r0", "r1", "r2", "r3", "r4", "r5", "r6"]
r = [("r0", "r0")] + list(itertools.combinations(ring_options, 2))

i = list(itertools.product(w, a, r))
print(i)
print(len(i))

